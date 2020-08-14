import pytest
import time
import sys
from os.path import dirname, abspath
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_acl import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "40151"


def test_c40151(browser):

	try:
		login_web(browser, url="10.2.2.86")

		# 添加10个acl组
		for gn in range(0, 10):
			groupname = 'test' + str(gn)
			add_ipv4_aclgroup(browser, groupname)

		# 添加完最后一个组，点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		# 获得目前有多少个acl组
		groupnum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)

		# 循环给每个acl组，添加10个acl规则
		for addgn in range(1, groupnum+1):
			for addnum in range(1, 11):
				add_ipv4_acl(browser, addgn)

		try:

			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		# reload(hostip="10.2.2.81")
		# print(err)
		# rail_fail(test_run_id, test_id)
		# time.sleep(70)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_test50.py"])