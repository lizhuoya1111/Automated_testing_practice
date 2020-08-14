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

test_id = 141694


def test_c141694(browser):

	try:
		login_web(browser, url=dev1)
		inter_sum = get_physical_interface_sum(browser)
		for x in range(0, inter_sum):
			browser.refresh()

			into_fun(browser, 物理接口)
			n = 2+x
			# 如果不是透明接口，再点击编辑
			if browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[4]/span').text != "透明":
				# 点击编辑
				browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[9]/a/img').click()
				time.sleep(0.5)
				# 点击静态
				browser.find_element_by_xpath('//*[@id="address_mode_0"]').click()

				# 添加ip
				browser.find_element_by_xpath('//*[@id="ipaddress_tex"]').send_keys("10.2.2.22")
				browser.find_element_by_xpath('//*[@id="mask_tex"]').clear()
				browser.find_element_by_xpath('//*[@id="mask_tex"]').send_keys("24")
				# 保存
				browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()
				# 获得操作结束的信息，并返回
				info = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
				try:
					assert "IP地址与本系统其他IP地址冲突" in info
					rail_pass(test_run_id, test_id)
				except:
					rail_fail(test_run_id, test_id)
					assert "IP地址与本系统其他IP地址冲突" in info
					break


	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])