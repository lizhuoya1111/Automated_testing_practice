import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_dev import *
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "144128"
# 在一条addr obj中删除多个range,查看log


def test_c144128(browser):

	try:
		login_web(browser, url=dev1)

		# 先添加再删除
		add_obj_address_range_wxw(browser, name='obj_add_range_353', desc='zhe是yi个描述1',
								  fromip='12.12.12.1', toip='12.12.12.250')

		one_obj_more_range_wxw(browser, name='obj_add_range_353', num=3, fromip='12.12.', toip='12.12.')

		del_one_obj_more_range_wxw(browser, name='obj_add_range_353', num=3)

		loginfo = get_log_info(browser, 管理日志)
		# print(loginfo)

		del_obj_range_wxw(browser, name='obj_add_range_353')

		try:
			assert "配置地址范围对象成功，修改内部对象 [obj_add_range_353]" in loginfo
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "配置地址范围对象成功，修改内部对象 [obj_add_range_353]" in loginfo

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])