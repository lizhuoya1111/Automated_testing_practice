import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 40499
# 对象名称包含"#@"等特殊字符


def test_add_obj_wxw(browser):

	try:
		login_web(browser, url="10.2.2.85")

		# 切换到默认frame
		browser.switch_to.default_content()
		# 切换到左侧frame
		browser.switch_to.frame("lefttree")
		# 点击对象
		browser.find_element_by_xpath(对象).click()
		# 点击ipv4
		browser.find_element_by_xpath(IPv4).click()
		# 点击地址
		browser.find_element_by_xpath(IPv4地址).click()

		# 定位到默认frame
		browser.switch_to.default_content()
		# 定位到内容frame
		browser.switch_to.frame("content")

		# 点击增加
		browser.find_element_by_xpath('//*[@id="button_area"]/div/input[2]').click()

		# 输入地址名称
		browser.find_element_by_xpath('//*[@id="name"]').send_keys('#@')
		# 输入描述
		browser.find_element_by_xpath('//*[@id="comment"]').send_keys("miaoshu")
		# 输入子网列表ip
		browser.find_element_by_xpath('//*[@id="subnetip0"]').send_keys('2.2.2.3')
		# 输入子网列表mask
		browser.find_element_by_xpath('//*[@id="subnetmask0"]').send_keys(24)

		# 保存
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()

		alert = browser.switch_to_alert()
		# print(alert.text)
		time.sleep(1)

		try:
			assert "对象名输入错误"in alert.text
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "对象名输入错误" in alert.text

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip="10.2.2.81")
		print(err)
		rail_fail(test_run_id, test_id)
		time.sleep(70)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c40499.py"])