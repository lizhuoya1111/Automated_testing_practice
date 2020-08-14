
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

test_id = 141661

def test_c141661(browser):

	try:
		login_web(browser, url=dev1)
		get_into_physical_interface(browser, interface=interface_name_6)
		# 点击取消
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()
		n = 2
		get_interface = []						# //*[@id="table"]/tbody/tr[11]/td[1]
		getnum1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[11]/td[1]').text
		print(getnum1)
		while int(n) <= int(int(getnum1)+1):
			get_interface_num = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ ' + str(n) + ' ]/td[2]/a').text
			n = n + 1
			get_interface.append(get_interface_num)
		print(get_interface)
		try:
			assert interface_name_1+"这写的什么？？？要修改" and interface_name_2 and interface_name_3 and interface_name_4 and interface_name_5 \
			       and interface_name_6 and interface_name_7 and interface_name_8 and interface_name_9 and \
			       interface_name_10 in get_interface
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert interface_name_1 and interface_name_2 and interface_name_3 and interface_name_4 and interface_name_5 \
			       and interface_name_6 and interface_name_7 and interface_name_8 and interface_name_9 and \
			       interface_name_10 in get_interface
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])