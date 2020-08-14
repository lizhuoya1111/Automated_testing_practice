
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

test_id = 141662

def test_c141662(browser):

	try:
		login_web(browser, url=dev1)
		get_into_physical_interface(browser, interface=interface_name_6)
		# 点击取消
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()
		n = 2
		get_infor = []						# //*[@id="table"]/tbody/tr[11]/td[1]
		getnum1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[11]/td[1]').text
		print(getnum1)
		while int(n) <= int(int(getnum1)+1):
			get_interface_num = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ ' + str(n) + ' ]/td[4]/span').text
			n = n + 1
			get_infor.append(get_interface_num)
		# print(get_infor)
		try:
			assert "路由" or "透明" in get_infor
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "路由" or "透明" in get_infor
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])