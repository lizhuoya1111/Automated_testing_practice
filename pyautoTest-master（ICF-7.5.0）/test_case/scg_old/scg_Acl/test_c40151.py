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
		login_web(browser, url="10.2.2.81")

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
			for addnum in range(0, 1):
				add_ipv4_acl(browser, addgn)

		# 切换到默认frame
		browser.switch_to.default_content()
		# 切换到左侧frame
		browser.switch_to.frame("lefttree")
		browser.find_element_by_xpath(防火墙).click()
		browser.find_element_by_xpath(IPv4访问控制列表).click()
		browser.switch_to.default_content()
		# 切换到内容frame
		browser.switch_to.frame("content")

		# 获得原始最后一个组的名称
		bottom_groupname_old = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[11]/li[1]/span[1]/a').text

		for addgn in range(groupnum, 1, -1):
			time.sleep(1)
			browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul['+str(addgn)+']/li[3]/a/img').click()
			browser.find_element_by_xpath('//*[@id="link_but"]').click()

		# 获得当前第一个组的名称
		bottom_groupname_new = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[1]/li[1]/span[1]/a').text

		get_log(browser, 管理日志)

		browser.switch_to.default_content()
		# 切换到左侧frame
		browser.switch_to.frame("content")
		log_pool = []

		for logid in range(0, 10):
			log_pool.append(browser.find_element_by_xpath('//*[@id="namearea' + str(logid) + '"]').text)

		del_all_acl_group_wxw(browser)

		try:
			assert bottom_groupname_new == bottom_groupname_old
			assert "的规则从 [2]到 [1]" in log_pool[0]
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip="10.2.2.81")
		print(err)
		rail_fail(test_run_id, test_id)
		time.sleep(70)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])

