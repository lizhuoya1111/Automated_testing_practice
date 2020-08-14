
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

test_id = 140761

def test_c140761(browser):
	try:
		login_web(browser, url=dev1)
		antiddos_settings_wxw(browser, function_enable='yes', function_disable='no',
							  syn_cookie='yes', allways_on='no', intelligent_defense='yes',
							  log_enable='yes', log_messages='100',
							  other_dos_attack='no',
							  land_attack='yes/no', ping_of_death='yes/no', winnuke='yes/no',
							  replay_attack='yes/no', smurf='yes/no', ip_fragment_attack='yes/no')

		add_antiddos_profile_wxw(browser, name='$#&?>', desc='1', schdule='请选择',
								 sn_perrule='0', sn_perip='0', sn_sche_perrule='0', sn_sche_perip='0',
								 ss_perrule='1000', ss_perip='100', ss_sche_perrule='0', ss_sche_perip='0',
								 ps_perrule='1000', ps_perip='100', ps_sche_perrule='0', ps_sche_perip='0',
								 synlow='0', synhigh='0', save='yes', cancel='yes/no')

		alert = browser.switch_to_alert()
		# print(alert.text)
		web_info = alert.text
		# 接受告警
		browser.switch_to_alert().accept()

		antiddos_settings_wxw(browser, function_enable="no", function_disable='yes',
							  syn_cookie='no', allways_on='no', intelligent_defense='yes',
							  log_enable='no', log_messages='1',
							  other_dos_attack='no',
							  land_attack='yes/no', ping_of_death='yes/no', winnuke='yes/no',
							  replay_attack='yes/no', smurf='yes/no', ip_fragment_attack='yes/no')
		try:
			assert "名称输入错误，请重新输入" in web_info
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "名称输入错误，请重新输入" in web_info
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])