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
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *

test_id = 139449
def test_c139449(browser):
	try:
		# 登录函数
		login_web(browser, url=dev5)
		add_admin_profile(browser, profile_name='aaa', desc='描述1', cfg="读写", report="读写")
		add_admin(browser, admin_name="bob", auth_database="local", temp="aaa",
				  https="yes", telent="yes", ssh="yes", console="yes",
				  password="admin@139", confirm_password="admin@139",
				  status="enable", interface=interface_name_1, online_num="32", ip1="0.0.0.0/0")
		add_admin_profile(browser, profile_name='aaa', desc='miaoshu', cfg="只读", report="只读")
		web_info1 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text.rstrip()
		delete_all_admin_list_jyl(browser)
		time.sleep(1)
		delete_all_admin_profile_jyl(browser)
		try:
			assert "修改" in web_info1
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "修改" in web_info1
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev5)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])