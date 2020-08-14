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

test_id = 38909
# 添加一个maplist对象， 填写非法的地址形式，如1.1.2.256


def test_maplist_wxw(browser):

	try:
		login_web(browser, url="10.2.2.81")

		add_maplist_part_wxw(browser, name='map909', desc='miaoshu', oriipfrom='1.1.1.25', oriipto='1.1.1.257',
							 transipfrom='2.2.2.25', transipto='2.2.2.255',
							 one_to_one_mapping="no", sticky='yes', portfrom='1', portto='65535')
		time.sleep(1)
		# 点击新增项目
		browser.find_element_by_xpath('//*[@id="btn_additem"]').click()

		# 打印警告框
		alert = browser.switch_to_alert()
		# print(alert.text)

		try:
			assert "IP格式输入错误，请重新输入。"in alert.text
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "IP格式输入错误，请重新输入。"in alert.text

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip="10.2.2.81")
		print(err)
		rail_fail(test_run_id, test_id)
		time.sleep(70)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])