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

test_id = "144149"
# 修改一条service的obj,修改协议,端口,timeout,查看log


def test_c144149(browser):

	try:
		login_web(browser, url=dev1)

		add_obj_service_wxw(browser, name='obj_serv_374', desc='zhe是ge描shu',
								  tcp='', src_port_from='1', src_port_to='2', dest_port_from='3', dest_port_to='4',
								  udp='yes', src_port_from1='1', src_port_to1='2', dst_port_from1='3', dst_port_to1='4',
								  icmp='', item='ping',
								  ip='', number='85')

		change_obj_service_wxw(browser, name='obj_serv_374', desc='zhe是ge描shu22',
							   tcp='', src_port_from='1', src_port_to='2', dest_port_from='3', dest_port_to='4',
							   udp='no', src_port_from1='1', src_port_to1='2', dst_port_from1='3', dst_port_to1='4',
							   icmp='', item='ping',
							   ip='yes', number='85')

		loginfo = get_log(browser, 管理日志)
		# print(loginfo)

		del_obj_service_wxw(browser, name='obj_serv_374')

		try:
			assert "配置服务对象成功，修改内部对象 [obj_serv_374]" in loginfo
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "配置服务对象成功，修改内部对象 [obj_serv_374]" in loginfo

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
