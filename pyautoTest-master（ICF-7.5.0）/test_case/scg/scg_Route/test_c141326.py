import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.scg.scg_def_multi_isp import *
from page_obj.scg.scg_def import *
from page_obj.scg.scg_dev import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141326"
# 输入$ #
# 无法配置成功，系统报错


def test_c141326(browser):

	try:
		login_web(browser, url=dev3)

		add_multi_isp_before_save_wxw(browser, name='isp_516', desc='$ #')

		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()

		time.sleep(1)
		alert = browser.switch_to_alert()
		# print(alert.text)
		alert = alert.text



		try:
			assert "描述格式输入错误，请重新输入。" in alert
			assert "不能输入 | ; #, $" in alert
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "描述格式输入错误，请重新输入。" in alert
			assert "不能输入 | ; #, $" in alert


	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev3)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])