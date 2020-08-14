import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_nat import *
from page_obj.scg.scg_def_bridge import *
from page_obj.scg.scg_def_default_hole import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_physical_interface import  *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.common.ssh import *

test_id = 132467
def test_c132467(browser):
	try:
		login_web(browser, url=dev1)
		get_into_default_hole_jyl(browser)
		time.sleep(1)
		# 点击全选
		browser.find_element_by_xpath('//*[@id="check_button"]').click()
		# 点击启用
		browser.find_element_by_xpath('//*[@id="apply_button"]').click()
		time.sleep(2)
		webinfo1 = browser.find_element_by_xpath('//*[@id="pagecmd"]/ul/li[6]').text.rstrip()


		get_into_default_hole_jyl(browser)
		# 点击全选
		browser.find_element_by_xpath('//*[@id="check_button"]').click()
		# 点击禁用
		browser.find_element_by_xpath('//*[@id="unapply_button"]').click()
		time.sleep(2)
		webinfo2 = browser.find_element_by_xpath('//*[@id="pagecmd"]/ul/li[6]').text.rstrip()

		get_into_default_hole_jyl(browser)
		# 点击启用（单个）
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[5]/input').click()
		get_into_default_hole_jyl(browser)
		time.sleep(3)
		webinfo3 = browser.find_element_by_xpath('//*[@id="pagecmd"]/ul/li[6]').text.rstrip()

		time.sleep(2)
		get_into_default_hole_jyl(browser)
		# 点击启用（单个）关闭启用
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[5]/input').click()
		get_into_default_hole_jyl(browser)
		webinfo4 = browser.find_element_by_xpath('//*[@id="pagecmd"]/ul/li[6]').text.rstrip()

		try:
			assert "启用规则数：3113" in webinfo1
			assert "启用规则数：0" in webinfo2
			assert "启用规则数：1" in webinfo3
			assert "启用规则数：0" in webinfo4
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "启用规则数：3113" in webinfo1
			assert "启用规则数：0" in webinfo2
			assert "启用规则数：1" in webinfo3
			assert "启用规则数：0" in webinfo4
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
