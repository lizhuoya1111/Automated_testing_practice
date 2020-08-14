
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

test_id = 141627

def test_c141627(browser):

	try:
		login_web(browser, url=dev1)
		physics_interface_change_transparent_interface(browser,  interface3=interface_name_3)
		transparent_interface_change_physics_interface_jyl(browser, interface3=interface_name_3)
		add_physical_interface_static_ip_jyl(browser, interface=interface_name_3, ip='192.165.12.3', mask='24')
		loginfo1 = get_log(browser, 管理日志)
		delete_physical_interface_ip_jyl(browser, interface=interface_name_3, ip="192.165.12.3")
		loginfo2 = get_log(browser, 管理日志)

		try:
			assert "成功" in loginfo1
			assert "成功" in loginfo2
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "成功" in loginfo1
			assert "成功" in loginfo2

		switch_physical_interface_snat(browser, interface=interface_name_3, snat="close")

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])