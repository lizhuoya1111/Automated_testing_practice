
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

test_id = "143952"

# 根据源地址、目的地址查找rule
# 仅仅是验证了可以查找，xpath定位总是感觉不够妥当


def test_c143952(browser):
	try:
		login_web(browser, url=dev1)
		# 添加组
		add_ipv4_aclgroup_lzy(browser, group_name='lzy')
		# 添加规则
		add_ipv4acl_lzy(browser, aclgroup_name='lzy', source_custom='yes', fromip='13.1.1.1', fromnetmask='255.255.255.0',
								  source_address_object='no', dest_custom='yes', toip='14.1.1.1', tonetmask='255.255.255.0', dest_address_object='no')
		# 高级搜索
		find_ipv4acl_lzy(browser, source_custom='yes', fromip='13.1.1.1', fromnetmask='255.255.255.0', source_address_object='no',
					  dest_custom='yes', toip='14.1.1.1', tonetmask='255.255.255.0', dest_address_object='no')
		sleep(10)
		# 获取信息
		browser.switch_to.default_content()
		browser.switch_to.frame("content")
		browser.switch_to.frame("iFrame1")
		info1 = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/div[1]/ul/li[2]/a[2]').text
		# print(info1)
		info2 = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/div[1]/ul/li[3]/a[2]').text
		# print(info2)

		# 还原
		del_all_acl_group_lzy(browser)
		sleep(2)

		try:
			assert '13.1.1.1' in info1 and '14.1.1.1' in info2
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert '13.1.1.1' in info1 and '14.1.1.1' in info2

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip=dev1)
		print(err)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])





