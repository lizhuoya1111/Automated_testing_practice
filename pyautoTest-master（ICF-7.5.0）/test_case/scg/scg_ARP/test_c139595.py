import pytest
import time
import sys
from os.path import dirname, abspath
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_def_log import *
from page_obj.scg.scg_def_mac import *
from page_obj.common.rail import *
from page_obj.common.telnet import *
from page_obj.common.ssh import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "139595"
def test_c139595(browser):

	try:
		login_web(browser, url=dev2)
		get_into_static_arp_jyl(browser)
		# 点击增加
		browser.find_element_by_xpath('//*[@id="button_area"]/div/input[5]').click()
		info1 = browser.find_element_by_xpath('//*[@id="for_config_tb_title"]/ul/li').text.rstrip()
		# print(info1)

		try:
			assert "新增静态ARP" in info1
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert "新增静态ARP" in info1


	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev2)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])