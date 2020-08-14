
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

test_id = 141639

def test_c141639(browser):

	try:
		login_web(browser, url=dev3)
		add_physical_interface_static_ip_jyl(browser, interface=interface_name_4, ip='192.165.12.2', mask='24')
		loginfo1 = get_log_info(browser, log_type=管理日志)
		get_into_physical_interface(browser, interface=interface_name_4)
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()
		time.sleep(1)
		webinfo1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[5]/td[3]').text.rstrip()
		# print(webinfo1)
		delete_physical_interface_ip_jyl(browser, interface=interface_name_4, ip="192.165.12.2")
		loginfo2 = get_log_info(browser, log_type=管理日志)

		try:
			assert "成功修改" in loginfo1
			assert "删除IPv4地址成功" in loginfo2
			assert "192.165.12.2/255.255.255.0" in webinfo1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "成功修改" in loginfo1
			assert "删除IPv4地址成功" in loginfo2
			assert "192.165.12.2/255.255.255.0" in webinfo1

		switch_physical_interface_snat(browser, interface=interface_name_3, snat="close")

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev3)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])