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

test_id = "140617"
# 添加limit profile 2
# 设置per rule session rate为300，per ip session rater为100，其他设置为0


def test_c140617(browser):

	try:

		login_web(browser, url=dev1)

		add_antiddos_profile_wxw(browser, name='617', desc='1', schdule='请选择',
								 sn_perrule='0', sn_perip='0', sn_sche_perrule='0', sn_sche_perip='0',
								 ss_perrule='300', ss_perip='100', ss_sche_perrule='300', ss_sche_perip='100',
								 ps_perrule='0', ps_perip='0', ps_sche_perrule='0', ps_sche_perip='0',
								 synlow='0', synhigh='0', save='yes', cancel='yes/no')

		loginfo = get_log_info(browser, 管理日志)
		# print(loginfo)

		del_antiddos_profile_wxw(browser, name='617')

		try:
			assert "添加用户配置[617]成功" in loginfo
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "添加用户配置[617]成功" in loginfo

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])