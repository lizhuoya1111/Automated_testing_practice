import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_interface import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 141766

def test_c141766(browser):

	try:
		login_web(browser, url=dev3)
		for x in range(1, 6):
			a = Shell_SSH()
			a.connect(dev2)
			a.execute("en")
			a.execute("conf t")
			a.execute("interface gigabitethernet "+interface_name_3)
			a.execute("shutdown")
			a.execute("no shutdown")
			a.close()

		web_info1 = get_physical_interface_link_station(browser, interface_id="2")

		for x in range(1, 6):
			a = Shell_SSH()
			a.connect(dev2)
			a.execute("en")
			a.execute("conf t")
			a.execute("interface gigabitethernet "+interface_name_6)
			a.execute("shutdown")
			a.execute("no shutdown")
			a.close()

		web_info2 = get_physical_interface_link_station(browser, interface_id="6")

		try:
			assert "连接" in web_info1
			assert "连接" in web_info2
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "连接" in web_info1
			assert "连接" in web_info2

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=[dev2, dev3])
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])