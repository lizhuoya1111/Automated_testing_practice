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

test_id = "139619"

def test_c139619(browser):

	try:
		login_web(browser, url=dev1)
		for x in range(1, 3):
			add_ipmac_list(browser, ipadd="192.165.12."+str(x), inteface=interface_name_3, mac="02:11:31:f8:52:1"+str(x),
						   host_name="aaa"+str(x))

		get_into_ip_mac_binding_jyl(browser)
		# 点击绑定列表与静态ARP同步
		browser.find_element_by_xpath('//*[@id="status"]').click()
		# 接受告警
		browser.switch_to_alert().accept()
		time.sleep(1)
		# 接受告警
		browser.switch_to_alert().accept()
		loginfo1 = get_log_info(browser, log_type=管理日志)
		del_bindinglist(browser, index_list="all")
		get_into_ip_mac_binding_jyl(browser)
		# 点击绑定列表与静态ARP同步
		browser.find_element_by_xpath('//*[@id="status"]').click()
		# 接受告警
		browser.switch_to_alert().accept()
		time.sleep(1)
		# 接受告警
		browser.switch_to_alert().accept()

		try:
			assert "成功设置IP MAC绑定同步" in loginfo1
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert "成功设置IP MAC绑定同步" in loginfo1

		del_bindinglist(browser)

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])