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

test_id = 142893
# 根据页码查询admin日志
def test_c142893(browser):
	try:
		# 登录admin
		login_web(browser, url=dev1)
		# 获取页数
		get_into_logging(browser, log_type=管理日志)
		info1 = browser.find_element_by_xpath('//*[@id="timearea0"]').text
		# print(info1)
		num1 = browser.find_element_by_xpath('//*[@id="rules_count"]').text
		# print(num1)
		num2 = int(num1)
		s1 = Select(browser.find_element_by_xpath('//*[@id="counter"]'))
		s1.select_by_visible_text('50')
		page1 = num2/50
		page2 = math.ceil(page1)
		# print(page2)
		# 根据页码查询admin日志
		s1 = Select(browser.find_element_by_xpath('//*[@id="Select1"]'))
		s1.select_by_visible_text('2/'+str(page2))
		time.sleep(1.5)
		info2 = browser.find_element_by_xpath('//*[@id="timearea0"]').text
		# print(info2)
		
		try:
			assert info1 != info2
			rail_pass(test_run_id, test_id)
		except:
			# 当日志仅有一页时,该脚本会执行失败,在这里可以添加SSH登陆或者接口downup去产生日志，保证重新执行时可以PASS
			# INTERFACE DOWN UP
			rail_fail(test_run_id, test_id)
			assert info1 != info2
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		# reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
