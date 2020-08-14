import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_acl import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 40143


def test_add_obj_wxw(browser):

	try:
		login_web(browser, url="10.2.2.81")

		for n in range(1, 101):
			add_acl_group_wxw(browser, name='acl_group_'+str(n))
			n = n + 1
			time.sleep(4)

		# 切换到默认frame
		browser.switch_to.default_content()
		get_log(browser, 管理日志)
		browser.switch_to.default_content()
		# 切换到左侧frame
		browser.switch_to.frame("content")

		loginfo = browser.find_element_by_xpath('//*[@id="namearea0"]').text

		try:
			assert "配置过滤规则对象成功，添加内部对象 [100]" in loginfo
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "配置过滤规则对象成功，添加内部对象 [100]" in loginfo

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip="10.2.2.81")
		print(err)
		rail_fail(test_run_id, test_id)
		time.sleep(70)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c40143.py"])