import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_firewall import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_nat import *
from page_obj.common.ssh import *
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "142589"
# 添加3个server load balance对象,删除全部对象
# 都能正确删除,并有日志记录，shell下查看正确


def test_c142589(browser):

	try:
		login_web(browser, url=dev3)

		# 添加三个slb
		for n in range(1, 4):
			add_slb_wxw(browser, name="slb_"+str(n), desc='miaoshu', portfrom='1', portto='2', load_balance_method='轮换',
						monitor_servers="yes/no", monitor_method='Ping', save1='yes', ip='1.1.1.1', weight='1',
					 	save2='yes', cancel='yes/no')

		# 添加三个slb
		for n in range(1, 4):
			del_slb_by_name_wxw(browser, name="slb_"+str(n))

		loginfo = get_log_info(browser, 管理日志)
		# print(loginfo)

		try:
			assert "删除SLB对象成功" in loginfo
			rail_pass(test_run_id, test_id)
		except:
			assert "删除SLB对象成功" in loginfo
			rail_fail(test_run_id, test_id)

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev3)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])