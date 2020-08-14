import pytest
import time
import sys
from os.path import dirname, abspath
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_interface import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.common.telnet import *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_vlan_interface import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "139765"


def test_c139765(browser):

	try:
		login_web(browser, url=dev1)
		add_obj_zone(browser, "t23246", "d", [interface_name_4, interface_name_5])
		loginfo_add = get_log_info(browser, 管理日志)
		# print("日志：" + loginfo_add)
		time.sleep(1)

		edit_zone_simple(browser, "t23246", "wwwwww")
		loginfo_edit = get_log_info(browser, 管理日志)
		# print("日志：" + loginfo_edit)
		time.sleep(1)

		del_obj_zone_byname(browser, "t23246")
		loginfo_del = get_log_info(browser, 管理日志)
		# print("日志：" + loginfo_del)

		try:
			assert "对象成功，添加内部对象 [t23246]" in str(loginfo_add) and \
			       "对象成功，修改内部对象 [t23246]" in str(loginfo_edit) and \
			       "对象成功，删除内部对象 [t23246]" in str(loginfo_del)
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert "对象成功，添加内部对象 [t23246]" in str(loginfo_add) and \
			       "对象成功，修改内部对象 [t23246]" in str(loginfo_edit) and \
			       "对象成功，删除内部对象 [t23246]" in str(loginfo_del)



	except Exception as err:
		# 如果上面的步骤有报错，重启设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(dev1)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])