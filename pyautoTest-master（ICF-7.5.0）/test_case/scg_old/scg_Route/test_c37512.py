import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.scg.scg_def_multi_isp import *
from page_obj.scg.scg_def import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 37512
# 输入$#&?>


def test_route_wxw(browser):

	try:
		login_web(browser, url="10.2.2.83")

		add_multi_isp_before_save_wxw(browser, name='$#&?>', desc='')

		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()

		time.sleep(1)
		alert = browser.switch_to_alert()
		# print(alert.text)
		alert = alert.text


		try:
			assert "对象名输入错误，请重新输入。" in alert
			rail_pass(test_run_id, test_id)
		except:
			rail_pass(test_run_id, test_id)
			assert "对象名输入错误，请重新输入。" in alert



	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip="10.2.2.83")
		time.sleep(70)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])