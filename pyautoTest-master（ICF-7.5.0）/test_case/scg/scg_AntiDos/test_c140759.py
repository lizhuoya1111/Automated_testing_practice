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

test_id = "140759"
# 输入非法的参数 2
# 在Anti Dos rule中输入非法的ip掩码，例如1.1.1.0/32这种


def test_c140759(browser):

	try:

		login_web(browser, url=dev1)

		add_antiddos_profile_wxw(browser, name='profile_759', desc='1', schdule='请选择',
								 sn_perrule='0', sn_perip='0', sn_sche_perrule='0', sn_sche_perip='0',
								 ss_perrule='0', ss_perip='0', ss_sche_perrule='0', ss_sche_perip='0',
								 ps_perrule='0', ps_perip='0', ps_sche_perrule='0', ps_sche_perip='0',
								 synlow='0', synhigh='0', save='yes', cancel='yes/no')

		add_antiddos_rule_wxw(browser, name='rule_759', desc='中文', zone="Z:any",
							  s_any='yes/no', s_single_ip='yes/no', saddress_sip='',
							  s_ip='yes', saddress_custom='1.1.1.0', saddress_mask='32',
							  d_any='yes/no', d_single_ip='yes/no', daddress_sip='',
							  d_ip='yes', daddress_custom='12.12.12.0', daddress_mask='32',
							  serv='P:any', profile='profile_759', monitor='yes', defense='yes/no',
							  save='yes', cancel='yes/no')

		loginfo = get_log_info(browser, 管理日志)
		# print(loginfo)

		del_antiddos_profile_wxw(browser, name='profile_759')

		del_antiddos_rule_wxw(browser, name='rule_759')

		try:
			assert "添加规则[rule_759]成功" in loginfo
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "添加规则[rule_759]成功" in loginfo

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])