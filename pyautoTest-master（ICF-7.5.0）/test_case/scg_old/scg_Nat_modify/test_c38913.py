import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_nat import *
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 38913
# 在maplist名中 ，添加中文、中线、 ◎％……等非法字符


def test_maplist_wxw(browser):

	try:
		login_web(browser, url="10.2.2.81")

		add_maplist_desc_wxw(browser, name='中文|%', desc='miaoshu')

		time.sleep(1)
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()

		# 打印警告框
		alert = browser.switch_to_alert()
		# print(alert.text)

		try:
			assert "对象名输入错误，请重新输入。"in alert.text
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "对象名输入错误，请重新输入。"in alert.text

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip="10.2.2.81")
		print(err)
		rail_fail(test_run_id, test_id)
		time.sleep(70)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])