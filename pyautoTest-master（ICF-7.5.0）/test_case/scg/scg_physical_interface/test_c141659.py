
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

test_id = 141659

def test_c141659(browser):

	try:
		login_web(browser, url=dev1)
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_6)
		a.execute("work-mode route")
		a.close()
		loginfo1 = get_log(browser, 管理日志)
		add_physical_interface_static_ip_jyl(browser, interface=interface_name_6, ip='192.165.12.3', mask='24')
		loginfo2 = get_log(browser, 管理日志)
		delete_physical_interface_ip_jyl(browser, interface=interface_name_6, ip="192.165.12.3")
		loginfo3 = get_log(browser, 管理日志)
		physics_interface_change_transparent_interface(browser, interface6=interface_name_6)
		loginfo4 = get_log(browser, 管理日志)


		try:
			assert "成功" in loginfo1
			assert "成功" in loginfo2
			assert "成功" in loginfo3
			assert "成功" in loginfo4
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "成功" in loginfo1
			assert "成功" in loginfo2
			assert "成功" in loginfo3
			assert "成功" in loginfo4
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])