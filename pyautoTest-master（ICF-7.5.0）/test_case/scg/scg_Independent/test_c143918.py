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

test_id = "143918"

# 使用脚本添加100个分组，每个分组的名称都是32个字符
# 貌似只能添加99个 加上默认的 最多100个


def test_c143918(browser):
	try:
		login_web(browser, url=dev1)
		for x in range(1, 100):
			add_ipv4_aclgroup_lzy(browser, group_name='lzy'+str(x))
		sleep(2)
		info1 = browser.find_element_by_xpath('//*[@id="rules_count"]').text
		print(info1)

		# 还原
		del_all_acl_group_lzy(browser)
		sleep(2)

		try:
			assert "100" in info1
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "100" in info1

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip=dev1)
		print(err)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])