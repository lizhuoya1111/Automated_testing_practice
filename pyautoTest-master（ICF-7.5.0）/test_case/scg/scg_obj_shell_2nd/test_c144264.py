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

test_id = "144264"
# 添加每Address对象包含子网10+1个


def test_c144264(browser):

	try:
		login_web(browser, url=dev1)

		# 先添加地址对象
		add_obj_address_wxw(browser, name='obj_add_489', desc='zhe是yi个描述1', subnetip='11.11.10.1', subnetmask='32')

		one_obj_add_more_ip_s_wxw(browser, name='obj_add_489', num=9, subnetip='11.11.11.', subnetmask='32')

		one_obj_add_more_ip_s_half_wxw(browser, name='obj_add_489', num=1)

		# 点击增加
		browser.find_element_by_xpath('//*[@id="add_subnet_link"]').click()
		# time.sleep(3)

		alert = browser.find_element_by_xpath('//*[@id="layui-layer1"]/div[2]').text
		# print(alert)
		browser.find_element_by_xpath('//*[@id="layui-layer1"]/div[3]/a').click()
		time.sleep(1)

		del_obj_address_wxw(browser, name='obj_add_489')

		try:
			assert alert == "超出最大限制"
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert alert == "超出最大限制"

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])