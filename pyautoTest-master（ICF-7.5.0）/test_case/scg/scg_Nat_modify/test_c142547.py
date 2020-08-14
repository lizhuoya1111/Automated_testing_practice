

import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_nat import *
from page_obj.scg.scg_def_bridge import *
from page_obj.scg.scg_def_nat_modify import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_physical_interface import  *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.common.ssh import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def import *

test_id = 142547
def test_c142547(browser):
	try:
		login_web(browser, url=dev3)
		add_maplist_wxw(browser, name='maplist_jia_1', desc='描述', save1='yes', cancel='no',
						oriipfrom='192.168.0.1', oriipto='192.168.0.1', transipfrom='218.104.98.254', transipto='218.104.98.254',
						one_to_one_mapping="no", sticky='yes', portfrom='80', portto='80', save2="yes")

		loginfo1 = get_log(browser, 管理日志)

		# 删除10.2.2.83maplist
		del_maplist_by_name_jyl(browser, name="maplist_jia_1")


		try:
			assert "添加MAPLIST项成功" in loginfo1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "添加MAPLIST项成功" in loginfo1

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev3)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
