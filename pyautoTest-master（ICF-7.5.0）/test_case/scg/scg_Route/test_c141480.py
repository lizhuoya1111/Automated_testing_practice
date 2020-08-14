import pytest
import time
import sys
from os.path import dirname, abspath
from page_obj.common.ssh import *
from page_obj.scg.scg_def_multi_isp import *
from page_obj.scg.scg_def import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_policy_route import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141480"
# ADRT_IMPORT_ISP_IP_SUCCESS


def test_c141480(browser):

	try:
		login_web(browser, url=dev3)

		add_multi_isp_save_wxw(browser, name='isp_670', desc='miaoshu')

		import_ip_config_file_wxw(browser, name='isp_670', save='yes', cancel='no', file='isp.txt')

		loginfo1 = get_log_info(browser, 管理日志)
		# print(loginfo1)

		del_multi_isp_byname(browser, name='isp_670')

		try:
			assert "成功导入归属IP文件"in loginfo1
			rail_pass(test_run_id, test_id)
		except:
			rail_pass(test_run_id, test_id)
			assert "成功导入归属IP文件" in loginfo1

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev3)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])