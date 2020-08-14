import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_dev import *
from os.path import dirname, abspath
from page_obj.scg.scg_def_multi_isp import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141379"
# ISP导入目的ip file中含有本地直连路由的
# 无法配置成功，系统报错

# 可以保存成功 本用例按照可以保存成功写


def test_c141379(browser):
	try:

		login_web(browser, url=dev1)
		# 添加ISP
		add_multi_isp_save_wxw(browser, name='lzy')

		# 导入IP
		import_ip_config_file_wxw(browser, name='lzy', save='yes', cancel='no', file='12.1.1.0.txt')

		# 添加路由 单网关
		add_isp_route_lzy(browser, name='lzy', single_gateway='yes', device=interface_name_2, gateway='12.1.1.2',
						  multi_gateway='no', gateway_group='1(GROUP_1)', grp_mem=['主用', '备份1'],
						  enable='yes', disable='no')

		# 获取日志
		log1 = get_log(browser, 管理日志)
		print(log1)

		# 删除ISP路由
		del_all_multi_isp_wxw(browser)

		try:
			assert "成功" in log1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "成功" in log1

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s",  "test_c"+str(test_id)+".py"])