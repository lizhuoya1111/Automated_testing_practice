import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_interface import *
from page_obj.scg.scg_def_reporter import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
from selenium.webdriver import ActionChains
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 139853


def test_c139852(browser):

	try:
		login_web(browser, url=dev1)
		into_fun(browser, 接口统计报表)
		time.sleep(5)
		print('sssssssssss')
		browser.find_element_by_xpath('//*[@id="ge0/1"]/div[1]/canvas').click()
		e = browser.find_element_by_xpath('//*[@id="ge0/1"]')
		# 将鼠标悬停在家用电器上，暂停0.1s
		# ActionChains(browser).move_to_element_with_offset(e, 200, 0).perform()
		# ActionChains(browser).move_to_element(e).move_by_offset(85, 27).pause(2).click().perform()
		# ActionChains(browser).move_to_element(e).move_by_offset(15, 27).pause(2).click().perform()
		# ActionChains(browser).move_to_element(e).move_by_offset(85, 127).pause(2).click().perform()
		# x = 0
		for x in range(1, 100, 4):
			# ActionChains(browser).move_to_element(e).move_by_offset(-220+x, 127).pause(0.1).click().perform()
			ActionChains(browser).move_to_element(e).move_by_offset(-220 + x, 127).click().perform()
			ActionChains(browser).move_to_element(e).move_by_offset(-220 + x, 200).click().perform()
			# x = x+10
			# print(x)
			# www = browser.find_element_by_xpath('//*[@id="ge0/1"]/div[2]/..').get_attribute('id')
			# print(www)
		ActionChains(browser).move_to_element(e).pause(1).perform()
		ActionChains(browser).click(e).perform()
		ActionChains(browser).move_to_element(e).pause(2).perform()
		# time.sleep(1)
		# s = browser.find_element_by_xpath('//*[@id="ge0/1"]/div[2]').text //*[@id="ge0/1"]/div[1]/canvas
		# aa = browser.find_element_by_xpath('//*[@id="ge0/1"]/div[2]').is_displayed()
		# print(aa)
		# print(type(s))
		# print(s)
		# for x in s:
		# 	print(x)

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置  //*[@id="ge0/1"]/div[2]/text()[1]
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])