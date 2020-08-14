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

test_id = "140630"
# 删除/批量删除黑/白名单 1
# 1.添加10条黑/白名单，选择第5条，删除


def test_c140630(browser):

	try:

		login_web(browser, url=dev1)

		for n in range(1, 11):
			add_black_or_white_list_wxw(browser, name='list_630_'+str(n), desc='miaoshu', any='yes',
							   		single_ip='yes/no', sip='',
							   		ip='yes/no', custom='', mask='',
							   		address='yes/no', srange='',
							   		white='yes/no', black='yes', never='yes',
							   		date='yes/no', expire_date='2019-04-15', expire_time='02:00:00',
							   		save='yes', cancel='yes/no')

		del_black_or_white_list_wxw(browser, name='list_630_5')

		loginfo = get_log_info(browser, 管理日志)
		# print(loginfo)

		for n in range(1, 11):
			if n == 5:
				continue
			del_black_or_white_list_wxw(browser, name='list_630_'+str(n))


		try:
			assert "删除黑白名单[name=list_630_5]" in loginfo
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "删除黑白名单[name=list_630_5]" in loginfo

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])