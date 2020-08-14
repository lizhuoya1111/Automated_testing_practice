
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

test_id = 142542
def test_c142542(browser):
	try:
		login_web(browser, url=dev3)
		add_maplist_wxw(browser, name='Maplist_jia_1', desc='', save1='yes', cancel='no')

		# 编辑描述
		edit_maplist_by_name_jyl(browser, name="Maplist_jia_1", maplist_del="no", desc="zxcvbnmlkjhgfdsaqwertyuiopzxcv"
								"zxcvbnmlkjhgfdsaqwertyuiopzxcvzxcvbnmlkjhgfdsaqwertyuiopzxcvzxcvbnmlkjhgfdsaqwertyuio"
								"zxcvbnmlkjhgfdsaqwertyuiopzxcvpzxcv")
		loginfo1 = get_log(browser, 管理日志)

		# 编辑勾选sticky
		edit_maplist_by_name_jyl(browser, name="Maplist_jia_1", maplist_del="no", desc="zxcvbnmlkjhgfdsaqwertyuiopzxcv"
								"zxcvbnmlkjhgfdsaqwertyuiopzxcvzxcvbnmlkjhgfdsaqwertyuiopzxcvzxcvbnmlkjhgfdsaqwertyuio"
								"zxcvbnmlkjhgfdsaqwertyuiopzxcvpzxcv",
								 oriipfrom="30.1.1.0", oriipto="30.1.1.255", one_to_one_mapping="no",
								 transipfrom="40.1.1.0", transipto="40.1.1.255", sticky="yes", portfrom="1",
								 portto="65535", new_item="yes", save="yes", cancel="no")
		loginfo2 = get_log(browser, 管理日志)

		# 编辑不选sticky
		edit_maplist_by_name_jyl(browser, name="Maplist_jia_1", maplist_del="no", desc="zxcvbnmlkjhgfdsaqwertyuiopzxcv"
								"zxcvbnmlkjhgfdsaqwertyuiopzxcvzxcvbnmlkjhgfdsaqwertyuiopzxcvzxcvbnmlkjhgfdsaqwertyuio"
								"zxcvbnmlkjhgfdsaqwertyuiopzxcvpzxcv",
								 oriipfrom="31.1.1.0", oriipto="31.1.1.255", one_to_one_mapping="no",
								 transipfrom="41.1.1.0", transipto="41.1.1.255", sticky="no", portfrom="1",
								 portto="65535", new_item="yes", save="yes", cancel="no")
		loginfo3 = get_log(browser, 管理日志)

		# 编辑选一对一映射
		edit_maplist_by_name_jyl(browser, name="Maplist_jia_1", maplist_del="no", desc="zxcvbnmlkjhgfdsaqwertyuiopzxcv"
								"zxcvbnmlkjhgfdsaqwertyuiopzxcvzxcvbnmlkjhgfdsaqwertyuiopzxcvzxcvbnmlkjhgfdsaqwertyuio"
								"zxcvbnmlkjhgfdsaqwertyuiopzxcvpzxcv",
								 oriipfrom="32.1.1.0", oriipto="32.1.1.255", one_to_one_mapping="yes",
								 transipfrom="42.1.1.0", sticky="no", portfrom="1",
								 portto="65535", new_item="yes", save="yes", cancel="no")
		loginfo4 = get_log(browser, 管理日志)

		edit_maplist_by_name_jyl(browser, name="Maplist_jia_1", maplist_del="no", desc="zxcvbnmlkjhgfdsaqwertyuiopzxcv"
								"zxcvbnmlkjhgfdsaqwertyuiopzxcvzxcvbnmlkjhgfdsaqwertyuiopzxcvzxcvbnmlkjhgfdsaqwertyuio"
								"zxcvbnmlkjhgfdsaqwertyuiopzxcvpzxcv",
								 oriipfrom="33.1.1.0", oriipto="33.1.1.255", one_to_one_mapping="yes",
								 transipfrom="43.1.1.0", sticky="no", portfrom="1",
								 portto="65535", new_item="yes", save="yes", cancel="no")
		for x in range(1, 4):
			edit_maplist_del_maplist_jyl(browser, name="Maplist_jia_1", maplist_del="yes")

		# 删除10.2.2.83maplist
		del_maplist_by_name_jyl(browser, name="Maplist_jia_1")


		try:
			assert "添加MAPLIST对象成功" in loginfo1
			assert "添加MAPLIST项成功" in loginfo2
			assert "添加MAPLIST项成功" in loginfo3
			assert "添加MAPLIST项成功" in loginfo4
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "添加MAPLIST对象成功" in loginfo1
			assert "添加MAPLIST项成功" in loginfo2
			assert "添加MAPLIST项成功" in loginfo3
			assert "添加MAPLIST项成功" in loginfo4

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev3)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
