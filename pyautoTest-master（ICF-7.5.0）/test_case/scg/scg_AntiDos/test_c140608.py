
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

test_id = 140608

def test_c140608(browser):
	try:
		login_web(browser, url=dev1)
		antiddos_settings_wxw(browser, function_enable='yes', function_disable='no',
							  syn_cookie='yes', allways_on='no', intelligent_defense='yes',
							  log_enable='yes', log_messages='100',
							  other_dos_attack='no',
							  land_attack='yes/no', ping_of_death='yes/no', winnuke='yes/no',
							  replay_attack='yes/no', smurf='yes/no', ip_fragment_attack='yes/no')

		add_antiddos_profile_wxw(browser, name='anti_pro_jia_1', desc='1', schdule='请选择',
								 sn_perrule='0', sn_perip='0', sn_sche_perrule='0', sn_sche_perip='0',
								 ss_perrule='0', ss_perip='0', ss_sche_perrule='0', ss_sche_perip='0',
								 ps_perrule='0', ps_perip='0', ps_sche_perrule='0', ps_sche_perip='0',
								 synlow='0', synhigh='0', save='yes', cancel='yes/no')

		add_antiddos_rule_wxw(browser, name='antiddos_profile_jia_1', desc='描述', zone=interface_name_4,
							  s_any='yes', s_single_ip='yes/no', saddress_sip='',
							  s_ip='yes/no', saddress_custom='', saddress_mask='',
							  d_any='yes', d_single_ip='yes/no', daddress_sip='',
							  d_ip='yes/no', daddress_custom='', daddress_mask='',
							  serv='P:any', profile='anti_pro_jia_1', monitor='yes', defense='yes/no',
							  save='yes', cancel='yes/no')

		edit_antiddos_rule_wxw(browser, name='antiddos_profile_jia_1', desc='miaoshu', zone=interface_name_2,
							   s_any='yes/no', s_single_ip='yes/no', saddress_sip='',
							   s_ip='yes', saddress_custom='192.168.24.0', saddress_mask='24',
							   d_any='yes/no', d_single_ip='yes/no', daddress_sip='',
							   d_ip='yes', daddress_custom='12.12.12.0', daddress_mask='24',
							   serv='P:FTP', profile='anti_pro_jia_1', monitor='yes', defense='yes/no',
							   save='yes', cancel='yes/no')


		loginfo = get_log_info(browser, 管理日志)

		del_antiddos_rule_wxw(browser, name='antiddos_profile_jia_1')

		del_antiddos_profile_wxw(browser, name='anti_pro_jia_1')

		antiddos_settings_wxw(browser, function_enable="no", function_disable='yes',
							  syn_cookie='no', allways_on='no', intelligent_defense='yes',
							  log_enable='no', log_messages='1',
							  other_dos_attack='no',
							  land_attack='yes/no', ping_of_death='yes/no', winnuke='yes/no',
							  replay_attack='yes/no', smurf='yes/no', ip_fragment_attack='yes/no')

		try:
			assert "修改规则" in loginfo
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "修改规则" in loginfo

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])