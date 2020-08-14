import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.scg.scg_def_multi_isp import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 37569
# ISP导入目的ip file中含有本地直连路由的
# 用例有问题


def test_route_wxw(browser):

	try:
		rail_fail(test_run_id, test_id)

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		# reload(hostip="10.2.2.82")
		# print(err)
		# rail_fail(test_run_id, test_id)
		# time.sleep(70)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s",  "test_c"+str(test_id)+".py"])