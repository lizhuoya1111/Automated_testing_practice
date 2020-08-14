import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.scg.scg_def_multi_isp import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141321"
# 输入中文字符(ISP Name输入异常检测 1)


def test_c141321(browser):

	try:
		login_web(browser, url=dev3)

		add_multi_isp_save_wxw(browser, name='中文', desc='')

		exist = is_multi_isp_exist_wxw(browser, name='中文')
		# print(exist)

		del_multi_isp_wxw(browser, name='中文')

		try:
			assert exist is True
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert exist is True


	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev3)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])