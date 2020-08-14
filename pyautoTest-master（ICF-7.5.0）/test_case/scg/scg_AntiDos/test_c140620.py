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

test_id = "140620"
# 删除/批量删除limit profile 1
# 添加10条limit profile，点击删除按钮，删除第五条


def test_c140620(browser):

	try:

		login_web(browser, url=dev1)

		for n in range(1, 11):
			add_antiddos_profile_wxw(browser, name='620_'+str(n), desc='1', schdule='请选择',
								 sn_perrule='0', sn_perip='0', sn_sche_perrule='0', sn_sche_perip='0',
								 ss_perrule='300', ss_perip='100', ss_sche_perrule='300', ss_sche_perip='100',
								 ps_perrule='0', ps_perip='0', ps_sche_perrule='0', ps_sche_perip='0',
								 synlow='0', synhigh='0', save='yes', cancel='yes/no')
		del_antiddos_profile_wxw(browser, name='620_5')

		loginfo = get_log_info(browser, 管理日志)
		# print(loginfo)

		for n in range(1, 5):
			del_antiddos_profile_wxw(browser, name='620_'+str(n))
		for n in range(6, 11):
			del_antiddos_profile_wxw(browser, name='620_' + str(n))

		try:
			assert "删除用户配置[name=620_5]成功" in loginfo
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "删除用户配置[name=620_5]成功" in loginfo

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])