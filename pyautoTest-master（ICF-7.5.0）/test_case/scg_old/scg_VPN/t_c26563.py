import pytest
import time
import sys
import random
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_ipsec import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *

test_id = "26563"


def test_c26563(browser):

	login_web(browser)

	p1en_list = ["des", "3des", "aes128", "aes192", "aes256"]

	p1au_list = ["md5", "sha1", "sha256", "sha384", "sha512"]

	sn = 0

	for x in p1en_list:

		for y in p1au_list:

			sn = sn + 1
			randomsn = random.randint(10000, 99999)
			info1 = add_ipsec_gw(browser, "tt_"+str(randomsn)+"_" +str(sn), "ipsec_to_test!", "ge0/1", "3.3.3.5", "123456", "3.1.1.0/24",
			                     "13.1.1.0/24",
			                     adv='yes',
			                     encry_p1=x, auth_p1=y
			                     )

			if "隧道已经存在" in info1:

				continue

			if info1 == "操作成功":

				# 在web右上角 获取远程网关总数
				ipsecgw_num_text = browser.find_element_by_xpath('//*[@id="rules_count"]').text

				page_num_sum = int(ipsecgw_num_text) // 15

				if page_num_sum > 0:

					ipsecgw_num_text = int(ipsecgw_num_text) % 15

				for clicknum in range(0,page_num_sum):

					browser.find_element_by_xpath('//*[@id="pagecmd"]/ul/li[2]/a').click()

					time.sleep(1)

				ipsecgw_num = int(ipsecgw_num_text) + 1

				time.sleep(2)

				# 找到最后一个远程网关规则，即刚刚添加的网关规则，对它点击编辑
				browser.find_element_by_xpath('//*[@id="vpn_remote_tunnel_table"]/tbody/tr['+str(ipsecgw_num) +']/td[8]/a[1]').click()

				time.sleep(2)

				# 点击高级，进入高级设置界面
				browser.find_element_by_xpath('//*[@id="conftr_31"]/td[1]/a').click()

				# 获取当前下拉框的值
				selectp1encry = Select(browser.find_element_by_xpath('//*[@id="encry_alg"]')).first_selected_option

				cu_p1en = selectp1encry.text

				print(cu_p1en)

				selectp1auth = Select(browser.find_element_by_xpath('//*[@id="auth_alg"]')).first_selected_option

				cu_p1au = selectp1auth.text

				print(cu_p1au)


				if (cu_p1en != x) or (cu_p1au != y):
					global testflag
					testflag = False
				else:
					testflag = True

	try:
		assert testflag
		rail_pass(test_run_id, test_id)

	except:
		rail_fail(test_run_id, test_id)
		assert testflag




if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+ test_id +".py"])