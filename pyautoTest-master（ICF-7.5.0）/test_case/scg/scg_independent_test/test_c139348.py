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

test_id = 139348

# 1.添加一个管理员帐号
# 2.该管理员帐号的登录密码含有特殊字符，如#￥%……&
# 3.用该管理员登录设备
# 符号$#为非法

def test_c139348(browser):
	try:
		login_web(browser, url=dev2)
		# 添加管理员lzy
		add_admin(browser, admin_name='lzy', password='admin&139', confirm_password='admin&139')
		# 退出当前账号
		sign_out_jyl(browser)
		# 用新账号登录
		login_web(browser, url=dev2, username='lzy', password='admin&139')
		# 系统日志
		log1 = get_log(browser, 系统日志)
		# 还原
		sign_out_jyl(browser)
		login_web(browser, url=dev2)
		delete_all_admin_list_jyl(browser)


		try:
			assert "管理员登录成功(虚拟系统=[0];帐户名=[lzy]" in log1
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "管理员登录成功(虚拟系统=[0];帐户名=[lzy]" in log1
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev2)
		rail_fail(test_run_id, test_id)
		assert False




if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])