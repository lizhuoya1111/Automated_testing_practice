import pytest
import pytest
import time
import sys
import math
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_physical_interface import *
from page_obj.scg.scg_def_vlan_interface import *
from page_obj.scg.scg_def_bridge import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_log import *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def_sys import *
from page_obj.scg.scg_def import *

test_id = 142900
# 根据时间日期查询system日志
# 1.设置为同一天查询日志
# 2.起始日期小于终止日期查询
def test_c142900(browser):
	try:
		# 登录admin
		login_web(browser, url=dev1)
		# 获取当前时间（年月日）
		time2 = get_time(browser)
		# print(time2)
		date1 = time2.split()[0]
		# print(date1)
		# time1 = time.strftime('%Y-%m-%d', time.localtime(time.time()))
		# print(time1)
		# 设置为同一天查询日志
		get_into_logging(browser, log_type=系统日志)
		browser.find_element_by_xpath('//*[@id="datefrom"]').send_keys(date1)
		browser.find_element_by_xpath('//*[@id="dateto"]').send_keys(date1)
		sleep(1)
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/div[1]/div[2]/div/form/table/tbody/tr[2]/td[5]/input[1]').click()
		info1 = browser.find_element_by_xpath('//*[@id="timearea0"]').text
		# print(info1)
		sleep(1)
		# 起始日期小于终止日期查询
		browser.find_element_by_xpath('//*[@id="datefrom"]').clear()
		browser.find_element_by_xpath('//*[@id="datefrom"]').send_keys('2019-01-01')
		browser.find_element_by_xpath('//*[@id="dateto"]').clear()
		browser.find_element_by_xpath('//*[@id="dateto"]').send_keys(date1)
		sleep(1)
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/div[1]/div[2]/div/form/table/tbody/tr[2]/td[5]/input[1]').click()
		info2 = browser.find_element_by_xpath('//*[@id="timearea0"]').text
		# print(info2)
		# 还原
		# browser.find_element_by_xpath('//*[@id="datefrom"]').clear()
		# browser.find_element_by_xpath('//*[@id="dateto"]').clear()

		try:
			assert date1 in info1 and date1 in info2
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert date1 in info1 and date1 in info2
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		# reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
