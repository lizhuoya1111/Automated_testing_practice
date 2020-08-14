import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.common.ssh import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_antiddos import *
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "140603"
# 添加AntiDos rule 2
# 1.添加一条AntiDos rule，name为数字，description包含中文、英文、数字和逗号，source interface/zone为子接口ge0/2.100，其他为默认配置
# 2.点击save


def test_c140603(browser):

	try:

		login_web(browser, url=dev1)

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("inter gig "+interface_name_2)
		a.execute("vlan 100")
		a.execute("exit")
		a.execute("exit")

		add_antiddos_profile_wxw(browser, name='profile_603', desc='1', schdule='请选择',
								 sn_perrule='0', sn_perip='0', sn_sche_perrule='0', sn_sche_perip='0',
								 ss_perrule='0', ss_perip='0', ss_sche_perrule='0', ss_sche_perip='0',
								 ps_perrule='0', ps_perip='0', ps_sche_perrule='0', ps_sche_perip='0',
								 synlow='0', synhigh='0', save='yes', cancel='yes/no')

		add_antiddos_rule_wxw(browser, name='603', desc='中文', zone=interface_name_2+".100",
							  s_any='yes', s_single_ip='yes/no', saddress_sip='',
							  s_ip='yes/no', saddress_custom='', saddress_mask='',
							  d_any='yes', d_single_ip='yes/no', daddress_sip='',
							  d_ip='yes/no', daddress_custom='', daddress_mask='',
							  serv='P:any', profile='profile_603', monitor='yes', defense='no',
							  save='yes', cancel='yes/no')

		loginfo = get_log_info(browser, 管理日志)
		# print(loginfo)

		del_antiddos_rule_wxw(browser, name='603')

		del_antiddos_profile_wxw(browser, name='profile_603')

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("no inter vlan " + interface_name_2 + ".100")
		a.execute("exit")

		try:
			assert "添加规则[603]成功" in loginfo
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "添加规则[603]成功" in loginfo

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])