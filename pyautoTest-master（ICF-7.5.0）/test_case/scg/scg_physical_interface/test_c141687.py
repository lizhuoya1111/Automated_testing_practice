
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

test_id = 141687

def test_c141687(browser):

	try:
		login_web(browser, url=dev1)
		web_info1 = add_physical_interface_static_ip_jyl(browser, interface=interface_name_3, ip='192.165.12.2', mask='24')
		# print(web_info)
		web_info2 = add_physical_interface_static_ip_jyl(browser, interface=interface_name_3, ip='192.166.255.255',
													mask='24')
		print(web_info2)
		delete_physical_interface_ip_jyl(browser, interface=interface_name_3, ip="192.165.12.2")
		try:
			assert "操作成功" in web_info1
			assert "不能使用广播地址" in web_info2
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "操作成功" in web_info1
			assert "不能使用广播地址" in web_info2
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])