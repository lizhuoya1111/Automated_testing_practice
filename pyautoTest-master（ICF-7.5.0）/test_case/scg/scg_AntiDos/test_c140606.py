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

test_id = "140606"
# 编辑AntiDos rule 1
# 1.添加一条AntiDos rule，源为zone1，custom 192.168.24.0/24，目的custom为12.12.12.0/24，服务为ftp，点击save
# 2.点击编辑按钮，修改源为子接口ge0/2.100，点击save


def test_c140606(browser):

	try:

		login_web(browser, url=dev1)

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("object zone zone1 ")
		a.execute("exit")
		a.execute("inter gig " + interface_name_2)
		a.execute("vlan 100")
		a.execute("exit")
		a.execute("exit")

		add_antiddos_profile_wxw(browser, name='profile_606', desc='1', schdule='请选择',
								 sn_perrule='0', sn_perip='0', sn_sche_perrule='0', sn_sche_perip='0',
								 ss_perrule='0', ss_perip='0', ss_sche_perrule='0', ss_sche_perip='0',
								 ps_perrule='0', ps_perip='0', ps_sche_perrule='0', ps_sche_perip='0',
								 synlow='0', synhigh='0', save='yes', cancel='yes/no')

		add_antiddos_rule_wxw(browser, name='606', desc='中文', zone="Z:zone1",
							  s_any='yes/no', s_single_ip='yes/no', saddress_sip='',
							  s_ip='yes', saddress_custom='192.168.24.0', saddress_mask='24',
							  d_any='yes/no', d_single_ip='yes/no', daddress_sip='',
							  d_ip='yes', daddress_custom='12.12.12.0', daddress_mask='24',
							  serv='P:FTP', profile='profile_606', monitor='yes', defense='yes/no',
							  save='yes', cancel='yes/no')

		edit_antiddos_rule_wxw(browser, name='606', desc='miaoshu', zone=interface_name_2+".100",
							   s_any='yes/no', s_single_ip='yes/no', saddress_sip='',
							   s_ip='yes', saddress_custom='192.168.24.0', saddress_mask='24',
							   d_any='yes/no', d_single_ip='yes/no', daddress_sip='',
							   d_ip='yes', daddress_custom='12.12.12.0', daddress_mask='24',
							   serv='P:FTP', profile='profile_606', monitor='yes', defense='yes/no',
							   save='yes', cancel='yes/no')

		loginfo = get_log_info(browser, 管理日志)
		# print(loginfo)

		del_antiddos_rule_wxw(browser, name='606')

		del_antiddos_profile_wxw(browser, name='profile_606')

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("no object zone zone1")
		a.execute("no inter vlan " + interface_name_2 + ".100")
		a.execute("exit")
		a.execute("exit")

		try:
			assert "修改规则[606]成功" in loginfo
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "修改规则[606]成功" in loginfo

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])