import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.scg.scg_def_multi_isp import *
from page_obj.scg.scg_def import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 37515
# 输入中文字符（描述）
# 可以添加


def test_route_wxw(browser):

	try:
		login_web(browser, url="10.2.2.83")

		add_multi_isp_save_wxw(browser, name='isp_515', desc='中文')

		log = get_log_info(browser, 管理日志)
		# print(log)

		exist = is_multi_isp_exist_wxw(browser, name='isp_515')
		# print(exist)

		del_multi_isp_byname(browser, name='isp_515')


		try:
			assert "添加ISP对象成功" in log
			assert "描述 [中文]" in log
			assert exist is True
			rail_pass(test_run_id, test_id)
		except:
			rail_pass(test_run_id, test_id)
			assert "添加ISP对象成功" in log
			assert "描述 [中文]" in log
			assert exist is True


	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip="10.2.2.83")
		print(err)
		rail_fail(test_run_id, test_id)
		time.sleep(70)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])