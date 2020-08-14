
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

test_id = 141638

def test_c141638(browser):

	try:
		login_web(browser, url=dev1)
		get_into_physical_interface(browser, interface=interface_name_1)
		webinfo1 = browser.find_element_by_xpath('//*[@id="for_config_tb_title"]/ul/li').text.rstrip()

		try:

			assert "接口设置" in webinfo1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "接口设置" in webinfo1

		switch_physical_interface_snat(browser, interface=interface_name_3, snat="close")

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])