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

test_id = "144097"
# 输入非法参数 1
# 添加一个分组，在名称中使用一些非法字符，如￥……


def test_c144097(browser):

	try:
		login_web(browser, url=dev1)

		add_acl_group_before_save(browser, name='￥', enable='yes', sour='Z:any', dest='Z:any', desc='miaoshu')

		time.sleep(1)
		# 保存
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[4]').click()

		alert = browser.find_element_by_xpath('//*[@id="layui-layer1"]/div[2]').text
		# print(alert)

		try:
			assert "名称输入错误，请重新输入" in alert
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "名称输入错误，请重新输入" in alert

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip=dev1)
		print(err)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])