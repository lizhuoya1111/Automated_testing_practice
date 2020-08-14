import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_vlan_interface import *
from page_obj.scg.scg_def_bridge import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_physical_interface import  *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *

test_id = 141838
def test_c141838(browser):
	try:
		login_web(browser, url=dev3)
		language_switch(browser, language="繁体")
		time.sleep(2)
		language_switch(browser, language="China")
		time.sleep(0.5)
		loginfo1 = get_log_info(browser, 管理日志)

		language_switch(browser, language="English")
		time.sleep(1)
		language_switch(browser, language="China")
		time.sleep(0.5)
		loginfo2 = get_log_info(browser, 管理日志)

		try:
			assert "成功修改" in loginfo1
			assert "成功修改" in loginfo2
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "成功修改" in loginfo1
			assert "成功修改" in loginfo2
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev3)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
