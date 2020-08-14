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

test_id = "144135"



def test_c144135(browser):

	try:
		login_web(browser, url=dev1)

		add_obj_address_wxw(browser, name='obj_add_359', desc='zhe是yi个描述1', subnetip='11.11.11.0', subnetmask='24')
		add_obj_address_wxw(browser, name='obj_add_351', desc='zhe是yi个描述1', subnetip='11.11.12.0', subnetmask='24')

		add_obj_group_use_more_addr_obj_wxw(browser, name='obj_grp_359', desc='zhe是yi个描述1', addr_obj=['A:obj_add_359', 'A:obj_add_351'])
		loginfo = get_log(browser, 管理日志)
		print('\n')
		print(loginfo)

		del_obj_grp_wxw(browser, name='obj_grp_359')

		del_obj_address_wxw(browser, name='obj_add_359')
		del_obj_address_wxw(browser, name='obj_add_351')

		try:
			assert "添加内部对象 [obj_grp_359]，具体属性 : 所选地址为 [obj_add_359,obj_add_351," in loginfo
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "添加内部对象 [obj_grp_359]，具体属性 : 所选地址为 [obj_add_359,obj_add_351," in loginfo

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])