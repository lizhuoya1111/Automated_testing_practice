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

test_id = "139608"


def test_c139608(browser):

	try:
		login_web(browser, url=dev2)
		into_fun(browser, 绑定列表)
		# browser.find_element_by_xpath('//*[@id="tabs"]/li[1]/a').click()
		# time.sleep(1)
		# 获得规则数量
		ip_mac_rules_count = browser.find_element_by_xpath('//*[@id="rules_count"]').text
		# print(ip_mac_rules_count)
		# 找到对应名字的接口的编辑按钮，并点击进入编辑界面
		get_title = "null"
		for x in range(2, 2 + int(ip_mac_rules_count)):
			# print(browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[2]').text.rstrip())
			if browser.find_element_by_xpath(
					'//*[@id="table"]/tbody/tr[' + str(x) + ']/td[2]').text.rstrip() == interface_name_1:
				browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[5]/a').click()
				get_title = browser.find_element_by_xpath('//*[@id="for_config_tb_title"]/ul/li').text
				break

		try:
			assert "IP-MAC绑定规则设定" in get_title
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert "IP-MAC绑定规则设定" in get_title

		delete_bridge_byname(browser)

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev2)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])