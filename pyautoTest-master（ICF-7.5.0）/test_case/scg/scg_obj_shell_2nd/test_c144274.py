import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_dev import *
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "144274"
# 对象名称包含"#@"等特殊字符


def test_c144274(browser):

	try:
		login_web(browser, url=dev1)

		# 切换到默认frame
		# browser.switch_to.default_content()
		# # 切换到左侧frame
		# browser.switch_to.frame("lefttree")
		# # 点击对象
		# browser.find_element_by_xpath(对象).click()
		# # 点击ipv4
		# browser.find_element_by_xpath(IPv4).click()
		# # 点击地址
		# browser.find_element_by_xpath(IPv4地址).click()
		#
		# # 定位到默认frame
		# browser.switch_to.default_content()
		# # 定位到内容frame
		# browser.switch_to.frame("content")
		into_fun(browser, IPv4地址)
		# 点击增加
		time.sleep(0.5)
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

		alert = browser.find_element_by_xpath('//*[@id="layui-layer1"]/div[2]').text
		# print(alert)


		try:
			assert "名称输入错误"in alert
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "名称名输入错误" in alert

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])