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

test_id = "142727"
# 描述中有非法字符
# 在snat、dnat、maplist、slb的描述中输入$ #这两个字符
# 不能输入，有错误提示


def test_c142727(browser):

	try:
		login_web(browser, url=dev3)

		# 添加一个slb
		add_slb_wxw(browser, name="$ #", desc='miaoshu', portfrom='1', portto='2', load_balance_method='轮换',
					monitor_servers="yes/no", monitor_method='Ping', save1='no', ip='1.1.1.1', weight='1',
					save2='yes', cancel='yes/no')
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
		alert1 = browser.find_element_by_xpath('//*[@id="layui-layer1"]/div[2]').text
		# print(alert1)

		add_maplist_wxw(browser, name="$ #", desc='maioshu', save1='no', cancel='yes/no', oriipfrom='',
						oriipto='', transipfrom='', transipto='', one_to_one_mapping="no", sticky='yes',
						portfrom='1', portto='65535', save2="yes/no", cance2='yes/no')
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
		time.sleep(2)
		alert2 = browser.find_element_by_xpath('//*[@id="layui-layer1"]/div[2]').text
		# print(alert2)

		# 添加snat
		add_snat(browser, name='$ #', desc="", src_inter_zone="Z:any", des_inter_zone="Z:any", other_match_switch="no",
				 src_ipadd_switch="预定义", srcaddress_predefine="A:any", srcip_custom="", srcmask_custom="",
				 des_ipadd_switch="预定义", desaddress_predefine="A:any", desip_custom="", desmask_custom="",
				 server='P:any', trans_local_ip="yes", single_ip='no', ip_range_start='no', ip_range_end='no',
				 other_action_nomap='no', other_action_maplist='no', save='no', cancel='no')
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[2]').click()
		time.sleep(2)
		alert3 = browser.find_element_by_xpath('//*[@id="layui-layer1"]/div[2]').text
		# print(alert3)

		add_dnat(browser, name='$ #', desc="", src_inter_zone="Z:any", src_ipadd_switch="预定义", srcaddress_predefine="A:any",
				 srcip_custom="", srcmask_custom="", des_ipadd_switch="预定义", desaddress_predefine="A:any",
				 desip_custom="", desmask_custom="", arp_proxy="no", server='P:any', trans_ip='', trans_port='no',
				 other_action_nomap='no', other_action_load='no', save="no", cancel='no')
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[2]').click()
		time.sleep(2)
		alert4 = browser.find_element_by_xpath('//*[@id="layui-layer1"]/div[2]').text
		# print(alert4)
		try:
			assert "名称输入错误，请重新输入。 范围1-32个字符，不能输入 空格 $ < > \ ' '' | ; , ? & # ￥" in alert1
			assert "名称输入错误，请重新输入。 范围1-32个字符，不能输入 空格 $ < > \ ' '' | ; , ? & # ￥" in alert2
			assert "名称输入错误，请重新输入。 范围1-32个字符，不能输入 空格 $ < > \ ' '' | ; , ? & # ￥" in alert3
			assert "名称输入错误，请重新输入。 范围1-32个字符，不能输入 空格 $ < > \ ' '' | ; , ? & # ￥" in alert4
			rail_pass(test_run_id, test_id)
		except:
			assert "名称输入错误，请重新输入。 范围1-32个字符，不能输入 空格 $ < > \ ' '' | ; , ? & # ￥" in alert1
			assert "名称输入错误，请重新输入。 范围1-32个字符，不能输入 空格 $ < > \ ' '' | ; , ? & # ￥" in alert2
			assert "名称输入错误，请重新输入。 范围1-32个字符，不能输入 空格 $ < > \ ' '' | ; , ? & # ￥" in alert3
			assert "名称输入错误，请重新输入。 范围1-32个字符，不能输入 空格 $ < > \ ' '' | ; , ? & # ￥" in alert4
			rail_fail(test_run_id, test_id)

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev3)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])