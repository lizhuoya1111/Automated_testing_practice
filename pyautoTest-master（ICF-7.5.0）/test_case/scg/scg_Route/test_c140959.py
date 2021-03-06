import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_dev import *
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "140959"
# 点击static route里的“Add single Gateway”


def test_c140959(browser):

	try:
		login_web(browser, url=dev1)

		into_fun(browser, 静态路由)

		# 点击单网关
		browser.find_element_by_xpath('//*[@id="button_area"]/div/input[2]').click()

		time.sleep(1)
		gettext = browser.find_element_by_xpath('//*[@id="for_config_tb_title"]/ul/li').text
		# print(gettext)

		try:
			assert "增加单路由" in gettext
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "增加单路由" in gettext

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])