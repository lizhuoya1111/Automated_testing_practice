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

test_id = 139452

# 新建用户的用户名为root
# 新建不成功
def test_c139452(browser):
	try:
		# 登录
		login_web(browser, url=dev1)
		s = get_admin_list_look_online_admin(browser)
		while s < 5:
			a2 = Shell_SSH()
			a2.connect(dev1)
			s = get_admin_list_look_online_admin(browser)
		# login_web(browser, url=dev1, new="yes")
		# 添加admin user，输入name为root
		edit_admin_jyl(browser, edit_admin_name="admin", interface="any", online_num="5")
		a4 = Shell_SSH()
		a4.connect(dev1)
		online_num = get_admin_list_look_online_admin(browser)
		info1 = ""
		if online_num == 5:
			info1 = get_admin_list_look_online_admin(browser)
			# print(info1)

		try:
			assert info1 == 5
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert info1 == 5
		edit_admin_jyl(browser, edit_admin_name="admin", interface="any", online_num="32")

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])