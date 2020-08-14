
import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

from page_obj.scg.scg_def import *
from page_obj.scg.scg_button import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *

from page_obj.scg.scg_def_acl import *
from page_obj.scg.scg_def_firewall import *
from page_obj.scg.scg_def_ipv4acl import *

test_id = "143946"

# 添加20条acl后，点击reboot重启DUT，查看acl是否还存在

def test_c143946(browser):
	try:
		login_web(browser, url=dev1)
		# 添加组
		add_ipv4_aclgroup_lzy(browser, group_name='lzy')
		# 添加20条规则
		for x in range(1, 21):
			add_acl_rule_complete_wxw(browser, aclgroup_name='lzy', source_zone_interface=interface_name_2, dest_zone_interface=interface_name_2)
			sleep(1)
		# 保存配置
		save_configer(browser)
		# 获取ACL条目数
		get_into_ipv4acl_lzy(browser)
		num1 = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[2]/li[1]/span[2]').text
		print(num1)
		# 点击重启
		reload(hostip=dev1, switch="重启")
		login_web(browser, url=dev1)
		# 获取ACL条目数
		get_into_ipv4acl_lzy(browser)
		num2 = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[2]/li[1]/span[2]').text
		print(num2)

		# 还原
		del_all_acl_group_lzy(browser)
		# 保存配置
		save_configer(browser)
		sleep(2)

		try:
			assert num1 == num2
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert num1 == num2

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip=dev1)
		print(err)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])







