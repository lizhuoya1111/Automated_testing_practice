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

test_id = "140626"
# 添加黑/白名单 3
# 添加一条白名单，name为英文，过期时间为never，查看能否正常添加


def test_c140626(browser):

	try:

		login_web(browser, url=dev1)

		add_black_or_white_list_wxw(browser, name='whitelist', desc='miaoshu', any='yes',
							   		single_ip='yes/no', sip='',
							   		ip='yes/no', custom='', mask='',
							   		address='yes/no', srange='',
							   		white='yes', black='yes/no', never='yes',
							   		date='yes/no', expire_date='2019-04-15', expire_time='02:00:00',
							   		save='yes', cancel='yes/no')

		loginfo = get_log_info(browser, 管理日志)
		# print(loginfo)

		# 删除黑白名单
		del_black_or_white_list_wxw(browser, name='whitelist')


		try:
			assert "添加黑白名单[whitelist]成功" in loginfo
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "添加黑白名单[whitelist]成功" in loginfo

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])