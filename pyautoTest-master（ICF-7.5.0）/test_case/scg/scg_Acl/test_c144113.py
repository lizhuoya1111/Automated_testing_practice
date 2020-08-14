import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_firewall import *
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "144113"
# 名称是否区分大小写
# 1.添加一个aclgroup，名称为abc
# 2.再添加一个ipv6 acl group，名称为ABC
# 此版本无ipv6ACL  2改为添加ipv4


def test_c144113(browser):

	try:
		login_web(browser, url=dev1)
		# 添加ACL   abc
		add_acl_group_complete(browser, name='abc')
		# 添加ACL   ABC
		add_acl_group_complete(browser, name='ABC')

		info1 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
		print(info1)
		browser.find_element_by_xpath('//*[@id="link_but"]').click()

		del_acl_group_wxw(browser, name='abc')


		try:
			assert "ABC已经存在" in info1
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "ABC已经存在" in info1

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip=dev1)
		print(err)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])