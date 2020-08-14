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

test_id = "144134"
# 添加一个grp,这个grp中包含一个addr obj,查看log


def test_c144134(browser):

	try:
		login_web(browser, url=dev1)

		add_obj_address_wxw(browser, name='obj_add_359', desc='zhe是yi个描述1', subnetip='11.11.11.0', subnetmask='24')


		add_obj_group_use_addr_obj_wxw(browser, name='obj_grp_359', desc='zhe是yi个描述1', addr_obj='A:obj_add_359')

		loginfo = get_log(browser, 管理日志)
		# print(loginfo)

		del_obj_grp_wxw(browser, name='obj_grp_359')

		del_obj_address_wxw(browser, name='obj_add_359')

		try:
			assert "配置地址组对象成功，添加内部对象 [obj_grp_359]" in loginfo
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "配置地址组对象成功，添加内部对象 [obj_grp_359]" in loginfo

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])