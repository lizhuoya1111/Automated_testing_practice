import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.scg.scg_def_ipsec import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_ipsec import *
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
test_id = " "
"""
测试一、二阶段不同算法组合运行远程网关
p1en: 阶段1加密算法
p1au: 阶段1认证算法
p2en: 阶段2加密算法
p2au: 阶段2认证算法
"""


def test_main(browser):
	try:
		p1en = ["aes256", "sm1", "sm4"]
		p1au = ["md5", "sha1", "sha256", "sha384", "sha512", "sm3"]

		p2en = ["des", "3des", "aes128", "aes192", "aes256", "sm1", "sm4"]
		p2au = ["md5", "sha1", "sha256", "sha384", "sha512", "sm3"]

		for i in p1en:
			for j in p1au:
				login_web(browser, url="10.2.2.87")

				add_ipsecremotegw(browser, ipsecrgmname='', ipsecrgminterseq='', ipsecrgmgateway='', preshared_key='', localsubnet='',
								  remotesubnet='')

				edit_ipsecRemoteGW_inhand("/html/body/div[1]/div[2]/form/div/table/tbody/tr[2]/td[8]/a[1]/img",
										  i, j, i, j)

				login_web("10.2.2.35", "admin", "admin@139", "0613")

				edit_ipsecRemoteGW_inhand("/html/body/div[1]/div[2]/form/div/table/tbody/tr[2]/td[8]/a[1]/img",
										  i, j, i, j)
				print(i + "+" + j)

				time.sleep(15)



		try:

			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		# reload(hostip="10.2.2.87")
		# print(err)
		# rail_fail(test_run_id, test_id)
		# time.sleep(70)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])



