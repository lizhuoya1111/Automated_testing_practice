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

test_id = "139584"


def test_c139584(browser):

	try:
		login_web(browser, url=dev1)
		# 定位到默认frame
		# browser.switch_to.default_content()
		# # 定位到左侧frame
		# browser.switch_to.frame("lefttree")
		# # 点击网络
		# browser.find_element_by_xpath(网络).click()
		# if not browser.find_element_by_xpath(display_MAC).is_displayed():
		# 	# 如果不可见，点击加号，展开元素
		# 	browser.find_element_by_xpath(MAC).click()
		# browser.find_element_by_xpath(ARP列表).click()
		# browser.switch_to.default_content()
		# # 定位到内容frame
		# browser.switch_to.frame("content")
		into_fun(browser, ARP列表)
		info = browser.find_element_by_xpath('//*[@id="current"]/a/span').text
		try:
			assert "动态ARP" in info
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert "动态ARP" in info


	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(dev1)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])