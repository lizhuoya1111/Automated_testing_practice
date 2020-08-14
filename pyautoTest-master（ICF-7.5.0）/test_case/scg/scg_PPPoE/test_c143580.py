import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_interface import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 143580


def test_c143580(browser):

	try:
		login_web(browser, url=dev1)
		connect_pc2 = Shell_SSH()
		connect_pc2.connect(hostip="10.1.1.202", name="root", passwd="root")
		connect_pc2.execute('pppoe-server -I eth5 -L 20.1.1.2 -R 20.1.1.100 -N 10')
		connect_pc2.close()
		delete_physical_interface_ip_jyl(browser, interface=interface_name_4, ip="20.1.1.1")
		physics_interface_pppoe_set(browser, physical_interface=interface_name_4, pppoe_uesr="test", pppoe_passwd="test")
		loginfo = get_log(browser, 管理日志)
		try:

			assert " 成功修改 interface模块,参数: [address mode : PPPoE" in loginfo
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert " 成功修改 interface模块,参数: [address mode : PPPoE" in loginfo

		add_physical_interface_ip_wxw(browser, interface=interface_name_4, ip='20.1.1.1', mask='24')

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])