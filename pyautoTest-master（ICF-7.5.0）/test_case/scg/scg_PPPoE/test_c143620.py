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

test_id = 143620


def test_c143620(browser):

	try:
		login_web(browser, url=dev1)
		connect_pc2 = Shell_SSH()
		connect_pc2.connect(hostip="10.1.1.202", name="root", passwd="root")
		connect_pc2.execute('pppoe-server -I eth5 -L 20.1.1.2 -R 20.1.1.100 -N 10')
		delete_physical_interface_ip_jyl(browser, interface=interface_name_4, ip="20.1.1.1")
		physics_interface_pppoe_set(browser, physical_interface=interface_name_4, pppoe_uesr="test", pppoe_passwd="test", idle_time="60")
		time.sleep(75)
		ppp_info = get_physics_interface_pppoe_station(browser, physical_interface=interface_name_4)
		# print(ppp_info[0], ppp_info[1])
		connect_pc2.execute('ping '+ppp_info[1]+' -c 5 -i 0.2')
		ppp_info1 = get_physics_interface_pppoe_station(browser, physical_interface=interface_name_4)
		# print(ppp_info1[0], ppp_info1[1])
		connect_pc2.close()
		loginfo = get_log_info(browser, log_type=管理日志, num=3)
		# print(loginfo)
		try:
			# assert True
			assert 'Idle' in ppp_info[0] and 'Connecting' in ppp_info1[0] and '启动PPPoE链接成功' in loginfo
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			# assert True
			assert 'Idle' in ppp_info[0] and 'Connecting' in ppp_info1[0] and '启动PPPoE链接成功' in loginfo

		add_physical_interface_ip_wxw(browser, interface=interface_name_4, ip='20.1.1.1', mask='24')

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])