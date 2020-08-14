import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_acl import *
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 40382
# 添加一个serv grp,包含一个serv obj,查看log


def test_obj_wxw(browser):

	try:
		login_web(browser, url="10.2.2.81")

		# 切换到默认frame
		browser.switch_to.default_content()
		# 切换到左侧frame
		browser.switch_to.frame("lefttree")
		# 点击对象
		browser.find_element_by_xpath(对象).click()
		# 点击ipv4
		browser.find_element_by_xpath(IPv4).click()
		# 点击服务
		browser.find_element_by_xpath(服务).click()
		# 点击服务组
		browser.find_element_by_xpath(服务组).click()

		add_obj_serv_grp_wxw(browser, name='serv_grp_382', desc='zhe是ge描shu', serv_obj='P:any')
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()

		time.sleep(2)

		# 切换到默认frame
		browser.switch_to.default_content()

		get_log(browser, 管理日志)

		browser.switch_to.default_content()

		# 切换到左侧frame
		browser.switch_to.frame("content")

		loginfo = browser.find_element_by_xpath('//*[@id="namearea0"]').text
		# print(loginfo)

		try:
			assert "配置服务组对象成功，添加内部对象 [serv_grp_382]" in loginfo
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "配置服务组对象成功，添加内部对象 [serv_grp_382]" in loginfo

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip="10.2.2.81")
		print(err)
		rail_fail(test_run_id, test_id)
		time.sleep(70)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c40382.py"])