import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
# from page_obj.scg.scg_def_physical_interface import *
# from page_obj.scg.scg_def_vlan_interface import *
# from page_obj.scg.scg_def_bridge import *
# from page_obj.common.rail import *
# from page_obj.scg.scg_def_log import *
# from page_obj.common.ssh import *
# from page_obj.scg.scg_def_dhcp import *
# from page_obj.scg.scg_dev import *
# from page_obj.scg.scg_def_ifname_OEM import *
# from page_obj.scg.scg_def_sys import *
from page_obj.scg.scg_def import *

test_id = 142892
# 根据关键字查询admin日志
def test_c142892(browser):
	try:
		# 登录admin 添加lzy
		login_web(browser, url=dev1)
		# add_admin(browser, admin_name='lzy')
		# # 获取随机ID号
		# get_into_adminlist(browser)
		# browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[10]/a').click()
		#
		# IDnum = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[2]').text.rstrip()
		# print(IDnum)
		# 根据关键字查询admin日志 /
		get_into_logging(browser, log_type=管理日志)
		browser.find_element_by_xpath('//*[@id="included_clause"]').send_keys('登录')
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/div[1]/div[2]/div/form/table/tbody/tr[2]/td[5]/input[1]').click()
		time.sleep(1)
		info1 = browser.find_element_by_xpath('//*[@id="namearea0"]').text
		# print(info1)
		# 还原
		# delete_all_admin_list_jyl(browser)
		try:
			assert "登录" in info1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "登录" in info1
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		# reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
