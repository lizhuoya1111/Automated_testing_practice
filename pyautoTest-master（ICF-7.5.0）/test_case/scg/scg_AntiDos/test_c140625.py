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

test_id = "140625"
# 添加黑/白名单 2
# 添加一条黑名单，name为包含英文、数字和下划线的32个字符，
# description为包含中文，英文，数字，逗号，单引号，双引号的256个字符，
# 过期时间为date，输入2009-04-15，点击save


def test_c140625(browser):

	try:

		login_web(browser, url=dev1)
		add_black_or_white_list_wxw(browser, name='aaaaaaaaaaaaaaaaaaaaaaaaaaaaa_12', desc='aaaaaaaaaaaaaaaaaaaaaaaaaa'
									'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
									'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
									'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa’”中12', any='yes/no',
							   		single_ip='yes/no', sip='',
							   		ip='yes/no', custom='', mask='',
							   		address='yes/no', srange='',
							   		white='no', black='yes', never='yes/no',
							   		date='yes', expire_date='2009-04-15', expire_time='02:00:00',
							   		save='yes', cancel='yes/no')

		loginfo = get_log_info(browser, 管理日志)
		# print(loginfo)

		# 删除黑白名单
		del_black_or_white_list_wxw(browser, name='aaaaaaaaaaaaaaaaaaaaaaaaaaaaa_12')


		try:
			assert "添加黑白名单[aaaaaaaaaaaaaaaaaaaaaaaaaaaaa_12]成功" in loginfo
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "添加黑白名单[aaaaaaaaaaaaaaaaaaaaaaaaaaaaa_12]成功" in loginfo

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])