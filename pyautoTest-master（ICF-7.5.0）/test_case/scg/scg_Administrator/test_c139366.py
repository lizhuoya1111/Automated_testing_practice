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
from page_obj.common.telnet import *

test_id = 139366

# 1.添加一个admin profile aaa，conf system为write-read，report system为read-write
# 2.添加一个admin user，name为31个英文字符，auth database为local，profile 引用aaa，login type选择telnet，permit ip 1.1.1.0/24,interface zone1，inline number是3，status是enable，点击save
# 3.从1.1.1.0/24网段使用该用户通过telnet方式登录设备
# 可以登录


def test_c139366(browser):
	try:
		# 登录函数
		login_web(browser, url=dev2)
		add_admin(browser, admin_name="lzy", auth_database="local", temp="max_profile", https="yes", telent="yes",
		          ssh="yes", console="yes", password="admin@138", confirm_password="admin@138", status="enable",
		          interface=interface_name_1, online_num="3", ip1="192.168.188.0/24", ip2="10.1.1.0/24",)
		sys_set_jyl(browser, telent_port="33")
		to_telnet = TelnetClient()
		telnet_info = to_telnet.login_host("10.2.2.82", "lzy", "admin@138", port=33)
		to_telnet.execute_some_command("en")
		telnet_info1 = to_telnet.execute_some_command("show ip add")
		# print("正在匹配telnet信息..." + telnet_info1)
		# to_telnet.logout_host()

		# cmd = Shell_SSH()
		# cmd.connect(hostip=dev4)
		# cmd.execute("en")
		# cmd.execute("telnet "+dev1)
		# time.sleep(1.5)
		# cmd.execute("lzy")
		# time.sleep(0.5)
		# cmd.execute("admin@138")
		# time.sleep(0.5)
		# cmd.execute("en")
		# cmd.execute("show ip address")
		# cmd_out = cmd.output()
		# print(cmd_out)

		try:
			assert 'interface         ip address        net mask          address mode' in telnet_info1
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert 'interface         ip address        net mask          address mode' in telnet_info1

		# sign_out_jyl(browser)
		login_web(browser, url=dev2)
		delete_all_admin_list_jyl(browser)
		sys_set_jyl(browser, telent_port="23")
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev2)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])