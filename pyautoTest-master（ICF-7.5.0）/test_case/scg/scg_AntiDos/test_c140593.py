import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_antiddos import *
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "140593"
# 开启AntiDos模块 2
# 将AntiDos mode设置为on,将AntiDos rule设置为Monitor mode，点击save


def test_c140593(browser):

	try:

		login_web(browser, url=dev1)

		antiddos_settings_wxw(browser, function_enable='yes', function_disable='no',
							  syn_cookie='yes', allways_on='no', intelligent_defense='yes',
							  log_enable='no', log_messages='1',
							  other_dos_attack='no',
							  land_attack='yes/no', ping_of_death='yes/no', winnuke='yes/no',
							  replay_attack='yes/no', smurf='yes/no', ip_fragment_attack='yes/no')
		add_antiddos_profile_wxw(browser, name='profile_593', desc='1', schdule='请选择',
								 sn_perrule='0', sn_perip='0', sn_sche_perrule='0', sn_sche_perip='0',
								 ss_perrule='0', ss_perip='0', ss_sche_perrule='0', ss_sche_perip='0',
								 ps_perrule='0', ps_perip='0', ps_sche_perrule='0', ps_sche_perip='0',
								 synlow='0', synhigh='0', save='yes', cancel='yes/no')

		add_antiddos_rule_wxw(browser, name='rule', desc='中文', zone=interface_name_4,
							  s_any='yes', s_single_ip='yes/no', saddress_sip='',
							  s_ip='yes/no', saddress_custom='', saddress_mask='',
							  d_any='yes', d_single_ip='yes/no', daddress_sip='',
							  d_ip='yes/no', daddress_custom='', daddress_mask='',
							  serv='P:any', profile='profile_593', monitor='yes', defense='yes/no',
							  save='yes', cancel='yes/no')

		loginfo = get_log_info(browser, 管理日志)
		# print(loginfo)

		del_antiddos_rule_wxw(browser, name='rule')

		del_antiddos_profile_wxw(browser, name='profile_593')

		try:
			assert "添加规则[rule]成功" in loginfo
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "添加规则[rule]成功" in loginfo

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])