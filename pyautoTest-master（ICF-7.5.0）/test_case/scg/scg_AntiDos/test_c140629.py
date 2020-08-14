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

test_id = "140629"
# 修改黑/白名单
# 1.添加一条黑名单，点击save
# 2.将此黑名单修改为白名单，点击save


def test_c140629(browser):

	try:

		login_web(browser, url=dev1)

		add_black_or_white_list_wxw(browser, name='blacklist', desc='miaoshu', any='yes',
							   		single_ip='yes/no', sip='',
							   		ip='yes/no', custom='', mask='',
							   		address='yes/no', srange='',
							   		white='yes/no', black='yes', never='yes',
							   		date='yes/no', expire_date='2019-04-15', expire_time='02:00:00',
							   		save='yes', cancel='yes/no')

		edit_black_or_white_list_wxw(browser, name='blacklist', desc='miaoshu1', any='yes',
									 single_ip='yes/no', sip='',
									 ip='yes/no', custom='', mask='',
									 address='yes/no', srange='',
									 white='yes', black='no', never='yes',
									 date='yes/no', expire_date='2019-03-06', expire_time='02:00:00',
									 save='yes', cancel='yes/no')

		loginfo = get_log_info(browser, 管理日志)
		# print(loginfo)

		# 删除黑白名单
		del_black_or_white_list_wxw(browser, name='blacklist')


		try:
			assert "修改黑白名单[blacklist]成功" in loginfo
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "修改黑白名单[blacklist]成功" in loginfo

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])