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

test_id = 142970
# 在System Log中配置查询时间大于结束时间
def test_c142970(browser):
	try:
		# 登录admin
		login_web(browser, url=dev1)
		# 获取当前时间（年月日）
		time1 = time.strftime('%Y-%m-%d', time.localtime(time.time()))
		# print(time1)
		# 在System Log中配置查询时间大于结束时间
		get_into_logging(browser, log_type=系统日志)
		browser.find_element_by_xpath('//*[@id="datefrom"]').send_keys(time1)
		browser.find_element_by_xpath('//*[@id="dateto"]').send_keys('2019-01-01')
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/div[1]/div[2]/div/form/table/tbody/tr[2]/td[5]/input[1]').click()
		info1 = browser.switch_to_alert().text
		# print(info1)
		time.sleep(0.5)
		browser.switch_to_alert().accept()

		try:
			assert '截止日期不能早于开始日期' in info1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert '截止日期不能早于开始日期' in info1
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		# reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
