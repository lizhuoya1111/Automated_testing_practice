
import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_interface import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 141660

def test_c141660(browser):

	try:
		login_web(browser, url=dev1)
		get_into_physical_interface(browser, interface=interface_name_6)
		browser.find_element_by_xpath('//*[@id="work_mode_0"]').click()
		# 接受告警
		browser.switch_to_alert().dismiss()
		time.sleep(1)
		# 点击取消
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_6)
		a.execute("work-mode route")
		a.close()
		get_into_physical_interface(browser, interface=interface_name_6)
		# 点击取消
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()
		get_into_physical_interface(browser, interface=interface_name_6)
		browser.find_element_by_xpath('//*[@id="ipaddress_tex"]').send_keys("192.165.12.3")
		browser.find_element_by_xpath('//*[@id="mask_tex"]').send_keys("24")
		# 点击取消
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()
		physics_interface_change_transparent_interface(browser, interface6=interface_name_6)
		try:
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])