import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_acl import *
from page_obj.scg.scg_dev import *
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "144157"
# 添加一个serv grp,包含一个serv obj,查看log


def test_c144157(browser):

	try:
		login_web(browser, url=dev1)

		add_obj_serv_grp_wxw(browser, name='serv_grp_382', desc='zhe是ge描shu', serv_obj='P:any')

		loginfo = get_log(browser, 管理日志)
		# print(loginfo)

		del_obj_serv_grp_wxw(browser, name='serv_grp_382')

		try:
			assert "配置服务组对象成功，添加内部对象 [serv_grp_382]" in loginfo
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "配置服务组对象成功，添加内部对象 [serv_grp_382]" in loginfo

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])