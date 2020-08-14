import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_antiddos import *
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 140615


def test_c140615(browser):

	try:

		login_web(browser, url=dev1)

		add_antiddos_profile_wxw(browser, name='profile_602', desc='1', schdule='请选择',
								 sn_perrule='0', sn_perip='0', sn_sche_perrule='0', sn_sche_perip='0',
								 ss_perrule='0', ss_perip='0', ss_sche_perrule='0', ss_sche_perip='0',
								 ps_perrule='0', ps_perip='0', ps_sche_perrule='0', ps_sche_perip='0',
								 synlow='0', synhigh='0', save='yes', cancel='yes/no')
		for x in range(0, 10):
			add_antiddos_rule_wxw(browser, name='rule'+str(x), desc='中文', zone=interface_name_4,
								  s_any='yes', s_single_ip='yes/no', saddress_sip='',
								  s_ip='yes/no', saddress_custom='', saddress_mask='',
								  d_any='yes', d_single_ip='yes/no', daddress_sip='',
								  d_ip='yes/no', daddress_custom='', daddress_mask='',
								  serv='P:any', profile='profile_602', monitor='yes', defense='yes/no',
								  save='yes', cancel='yes/no')

		move_ddos_rule_list(browser, fromindex='10', toindex='1')
		loginfo = get_log_info(browser, 管理日志)
		# print(loginfo)

		try:
			assert "移动规则[name=rule9]从index=[2]到index=[1]成功." in loginfo
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "移动规则[name=rule0]从index=[9]到index=[10]成功." in loginfo

		for x in range(0, 10):
			del_antiddos_rule_wxw(browser, name='rule'+str(x))

		del_antiddos_profile_wxw(browser, name='profile_602')
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])