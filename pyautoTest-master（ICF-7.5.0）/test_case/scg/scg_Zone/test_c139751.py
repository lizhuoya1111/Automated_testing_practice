import pytest
import time
import sys
from os.path import dirname, abspath
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_interface import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.common.telnet import *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_vlan_interface import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "139751"


def test_c139751(browser):

	try:
		login_web(browser,  url=dev1)
		into_fun(browser, Zone)
		# 点击增加
		time.sleep(1)
		browser.find_element_by_xpath('//*[@id="button_area"]/div/input[1]').click()
		# 输入名称
		browser.find_element_by_xpath('//*[@id="name"]').send_keys("test1")
		# 输入描述
		browser.find_element_by_xpath('//*[@id="comment"]').send_keys("test1")

		# 取消
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()

		result1 = find_zone_byname(browser, "test1")
		# print(result1)
		try:
			assert result1 is None
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert result1 is None


	except Exception as err:
		# 如果上面的步骤有报错，重启设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(dev1)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])