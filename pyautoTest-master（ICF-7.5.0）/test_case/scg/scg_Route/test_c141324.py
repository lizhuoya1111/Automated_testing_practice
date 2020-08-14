import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.scg.scg_def_multi_isp import *
from page_obj.scg.scg_def import *
from page_obj.scg.scg_dev import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141324"
# 输入字符串长度超过 32（中文字符一个占三个字符位
# 无法配置成功,最多输入32个字符
# 可以配置成功  输入最大长度为32
# ISP Name输入异常检测 4


def test_c141324(browser):

	try:
		login_web(browser, url=dev3)
		# 添加ISP Name 长度超过32字符
		add_multi_isp_save_wxw(browser, name='aaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeee', desc='aaaa')
		# 获取日志
		log1 = get_log(browser, 管理日志)
		# 还原
		del_all_multi_isp_wxw(browser)


		try:
			assert "e" not in log1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "e" not in log1



	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev3)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])