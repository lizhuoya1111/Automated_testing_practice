import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.scg.scg_def_multi_isp import *
from page_obj.scg.scg_def import *
from page_obj.scg.scg_dev import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141323"
# 检查大小写敏感
# 大小写不敏感，输入Abc之后，不允许输入abc，但显示必需显示成Abc


def test_c141323(browser):

	try:
		login_web(browser, url=dev3)

		add_multi_isp_save_wxw(browser, name='Abc', desc='')

		add_multi_isp_before_save_wxw(browser, name='abc', desc='')

		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()

		time.sleep(1)
		alert = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
		# print(alert)
		del_multi_isp_byname(browser, name='Abc')


		try:
			assert "ISP名称已存在" in alert
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "ISP名称已存在" in alert



	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev3)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])