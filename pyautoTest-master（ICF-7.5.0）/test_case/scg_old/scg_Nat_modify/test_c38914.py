import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_nat import *
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 38914
# 添加一个one-to-one mapping的规则，Original IP from 192.168.0.1 to 192.168.0.255 Translated IP from 192.168.1.2


def test_maplist_wxw(browser):

	try:
		login_web(browser, url="10.2.2.81")

		add_maplist_wxw(browser, name='map914', desc='miaoshu', oriipfrom='192.168.0.1', oriipto='192.168.0.255',
						transipfrom='192.168.1.2', transipto='', one_to_one_mapping="yes", sticky='yes', portfrom='1', portto='65535')
		time.sleep(1)
		# 切换到默认frame
		browser.switch_to.default_content()
		get_log(browser, 管理日志)
		browser.switch_to.default_content()

		# 切换到左侧frame
		browser.switch_to.frame("content")
		loginfo = browser.find_element_by_xpath('//*[@id="namearea0"]').text
		# print(loginfo)

		try:
			assert "添加MAPLIST项成功" in loginfo
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "添加MAPLIST项成功" in loginfo

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip="10.2.2.81")
		print(err)
		rail_fail(test_run_id, test_id)
		time.sleep(70)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])