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

test_id = "140607"
# 编辑AntiDos rule 2
# 1.添加一条AntiDos rule，引用自定义的service
# 2.修改自定义的service


def test_c140607(browser):

	try:

		login_web(browser, url=dev1)

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("object service 607 ip 11 timeout 11")
		a.execute("exit")
		a.execute("exit")

		add_antiddos_profile_wxw(browser, name='profile_607', desc='1', schdule='请选择',
								 sn_perrule='0', sn_perip='0', sn_sche_perrule='0', sn_sche_perip='0',
								 ss_perrule='0', ss_perip='0', ss_sche_perrule='0', ss_sche_perip='0',
								 ps_perrule='0', ps_perip='0', ps_sche_perrule='0', ps_sche_perip='0',
								 synlow='0', synhigh='0', save='yes', cancel='yes/no')

		add_antiddos_rule_wxw(browser, name='607', desc='中文', zone="Z:any",
							  s_any='yes/no', s_single_ip='yes/no', saddress_sip='',
							  s_ip='yes', saddress_custom='192.168.24.0', saddress_mask='24',
							  d_any='yes/no', d_single_ip='yes/no', daddress_sip='',
							  d_ip='yes', daddress_custom='12.12.12.0', daddress_mask='24',
							  serv='C:607', profile='profile_607', monitor='yes', defense='yes/no',
							  save='yes', cancel='yes/no')

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("object service 607 ip 22 timeout 11")
		a.execute("exit")
		a.execute("exit")


		loginfo = get_log_info(browser, 管理日志)
		# print(loginfo)

		del_antiddos_rule_wxw(browser, name='607')

		del_antiddos_profile_wxw(browser, name='profile_607')

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("no object service 607")
		a.execute("exit")
		a.execute("exit")

		try:
			assert "配置服务对象成功，修改内部对象 [607]" in loginfo
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "配置服务对象成功，修改内部对象 [607]" in loginfo

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])