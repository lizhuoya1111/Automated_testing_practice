import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_sys import *
from page_obj.scg.scg_def import *
from page_obj.scg.scg_button import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *

test_id = 139322

def test_c139322(browser):
	try:
		login_web(browser, url=dev1)
		for x in range(1, 30):
			add_admin_profile(browser, profile_name='bob'+str(x), desc="bob权限"+str(x), cfg="只读", report="无权限")
		# 获取web页面最大profile数目
		time.sleep(1)
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		time.sleep(1)
		web_inrfo = browser.find_element_by_xpath('//*[@id="rules_count"]').text
		# print(web_inrfo)
		time.sleep(1)
		loginfo = get_log(browser, 管理日志)
		# print(loginfo)
		delete_all_admin_list_jyl(browser)
		time.sleep(1)
		delete_all_admin_profile_jyl(browser)
		try:
			assert "添加管理员视图成功" in loginfo
			assert web_inrfo == "32"
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "添加管理员视图失败" in loginfo
			assert web_inrfo == "32"
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip=dev1)
		print(err)
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])