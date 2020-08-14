# coding=utf-8
import time
from selenium.webdriver.support.ui import Select
from page_obj.scg.scg_button import *
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_ifname_OEM import *


# 废除
def add_ipsec_gw(browser, ipsecRGWname, ipsecdesc, ipsecRGWinterSeq, ipsecRGWgateway, preshared_key, localsubnet,
				 remotesubnet, ike_id="no", localidtype="Email Address", localid="test@test.com",
				 remoteidtype="Accept Any Remote ID", remoteid=" ",
				 adv="no", mode="主模式", encry_p1="3des", auth_p1="sha1", dh_group="2", p1_timeout="86400",
				 esp_protocol='ESP',
				 ah_auth="md5", encry_p2='aes128', auth_p2='sha1', ip_compression='no', pfs='no', pfs_group=" ",
				 p2_timeout_type='时间',
				 p2_timeout_time="86400", p2_timeout_data=" ", redundant="no", redundant_tunnel=" ",
				 start_negotiation='yes', return_switch_adv="no"
				 ):
	"""

	:param browser:
	:param ipsecRGWname:
	:param ipsecdesc:
	:param ipsecRGWinterSeq:
	:param ipsecRGWgateway:
	:param preshared_key:
	:param localsubnet:
	:param remotesubnet:
	:return: 操作完成后提示信息
	"""

	# browser.switch_to.default_content()
	# # 定位到默认frame
	#
	# browser.switch_to.frame("lefttree")
	# # 登入后，定位到左侧frame
	#
	# browser.find_element_by_xpath(虚拟专网).click()
	# # 点击”虚拟专网“
	#
	# browser.find_element_by_xpath(远程网关).click()
	# # 点击”远程网关“
	#
	# browser.switch_to.default_content()
	# # 定位到默认frame
	#
	# browser.switch_to.frame("content")
	# # 定位到内容frame
	into_fun(browser, 远程网关)
	time.sleep(1)
	browser.find_element_by_xpath("/html/body/div[1]/div[3]/div/input").click()
	# 点击”增加远程网关“

	time.sleep(1)

	browser.find_element_by_xpath('//*[@id="name"]').send_keys(ipsecRGWname)
	# 输入name

	time.sleep(1)

	browser.find_element_by_xpath('//*[@id="description"]').send_keys(ipsecdesc)
	# 输入name

	time.sleep(1)

	localif = Select(browser.find_element_by_xpath('//*[@id="localif"]'))

	# 选择本地接口 ge0/1 ge0/2....
	localif.select_by_visible_text(ipsecRGWinterSeq)

	time.sleep(1)

	browser.find_element_by_xpath('//*[@id="gateway"]').send_keys(ipsecRGWgateway)
	# 输入remote IP add

	time.sleep(1)

	browser.find_element_by_xpath('//*[@id="preshared_key"]').send_keys(preshared_key)
	# input republicKey

	time.sleep(1)

	if ike_id == "yes":

		# 展开IKE ID
		browser.find_element_by_xpath('//*[@id="ikeid_toggle"]').click()

		select_local_id = Select(browser.find_element_by_xpath('//*[@id="local_id_sel"]'))

		select_remote_id = Select(browser.find_element_by_xpath('//*[@id="remote_id_sel"]'))

		select_local_id.select_by_visible_text(localidtype)

		browser.find_element_by_xpath('//*[@id="local_text"]').send_keys(localid)

		select_remote_id.select_by_visible_text(remoteidtype)

		# 判断远端ID选择的是什么，来确定远端ID的值填什么
		if remoteidtype != "Accept Any Remote ID":

			if remoteidtype == "Distinguished Name":

				browser.find_element_by_xpath('//*[@id="remote_id_email"]').send_keys(remoteid)
				browser.find_element_by_xpath('//*[@id="remote_id_cn"]').send_keys("w")
				browser.find_element_by_xpath('//*[@id="remote_id_ou"]').send_keys("w")
				browser.find_element_by_xpath('//*[@id="remote_id_organization"]').send_keys("w")
				browser.find_element_by_xpath('//*[@id="remote_id_location"]').send_keys("w")
				browser.find_element_by_xpath('//*[@id="remote_id_state"]').send_keys("w")
				browser.find_element_by_xpath('//*[@id="remote_id_country"]').send_keys("w")
			else:

				browser.find_element_by_xpath('//*[@id="remote_id_text"]').send_keys(remoteid)

	browser.find_element_by_xpath('//*[@id="localsubnet"]').clear()
	# clear loacl subnet text

	time.sleep(1)

	browser.find_element_by_xpath('//*[@id="localsubnet"]').send_keys(localsubnet)
	# input local subnet

	time.sleep(1)

	browser.find_element_by_xpath('//*[@id="remotesubnet"]').send_keys(remotesubnet)
	# input remote subnet

	time.sleep(1)

	# 当输入参数adv是yes时，进入高级界面
	if adv == "yes":

		browser.find_element_by_xpath('//*[@id="conftr_31"]/td[1]/a').click()

		global title_adv

		title_adv = browser.find_element_by_xpath('//*[@id="container_inner"]/div/div/ul/li').text

		if mode == "主模式":
			browser.find_element_by_xpath('//*[@id="mode_0"]').click()

		if mode == "野蛮模式":
			browser.find_element_by_xpath('//*[@id="mode_1"]').ckick()

		select_p1_encry = Select(browser.find_element_by_xpath('//*[@id="encry_alg"]'))
		select_p1_auth = Select(browser.find_element_by_xpath('//*[@id="auth_alg"]'))
		select_dh_group = Select(browser.find_element_by_xpath('//*[@id="dh_group"]'))

		select_p1_encry.select_by_visible_text(encry_p1)
		select_p1_auth.select_by_visible_text(auth_p1)
		select_dh_group.select_by_visible_text(dh_group)

		# IKE SA有效时间
		if p1_timeout != "86400":
			browser.find_element_by_xpath('//*[@id="ike_sa_lifetime"]').clear()
			browser.find_element_by_xpath('//*[@id="ike_sa_lifetime"]').send_keys(p1_timeout)

		# 选择阶段二的封装协议,有"AH"、"ESP"、"AH+ESP"三种选型
		if esp_protocol == "ESP":

			if not (browser.find_element_by_xpath('//*[@id="using_esp_protocol"]').is_selected()):
				browser.find_element_by_xpath('//*[@id="using_esp_protocol"]').click()

			select_p2_encry = Select(browser.find_element_by_xpath('//*[@id="esp_encry_alg"]'))
			select_p2_auth = Select(browser.find_element_by_xpath('//*[@id="esp_auth_alg"]'))

			select_p2_encry.select_by_visible_text(encry_p2)
			select_p2_auth.select_by_visible_text(auth_p2)

		elif esp_protocol == "AH":

			if not (browser.find_element_by_xpath('//*[@id="using_ah_protocol"]').is_selected()):
				browser.find_element_by_xpath('//*[@id="using_ah_protocol"]').click()

			select_ah_auth = Select(browser.find_element_by_xpath('//*[@id="ah_auth_alg"]'))
			select_ah_auth.select_by_visible_text(ah_auth)


		elif esp_protocol == "AH+ESP" or esp_protocol == "ESP+AH":

			if not (browser.find_element_by_xpath('//*[@id="using_esp_protocol"]').is_selected()):
				browser.find_element_by_xpath('//*[@id="using_esp_protocol"]').click()

			select_p2_encry = Select(browser.find_element_by_xpath('//*[@id="esp_encry_alg"]'))
			select_p2_auth = Select(browser.find_element_by_xpath('//*[@id="esp_auth_alg"]'))

			select_p2_encry.select_by_visible_text(encry_p2)
			select_p2_auth.select_by_visible_text(auth_p2)

			if not (browser.find_element_by_xpath('//*[@id="using_ah_protocol"]').is_selected()):
				browser.find_element_by_xpath('//*[@id="using_ah_protocol"]').click()

			select_ah_auth = Select(browser.find_element_by_xpath('//*[@id="ah_auth_alg"]'))
			select_ah_auth.select_by_visible_text(ah_auth)

		if ip_compression == "yes":

			if not (browser.find_element_by_xpath('//*[@id="enable_ip_compression"]').is_selected()):
				browser.find_element_by_xpath('//*[@id="enable_ip_compression"]').click()

		if pfs == "yes":
			browser.find_element_by_xpath('//*[@id="enable_pfs"]').click()

			select_pfd = Select(browser.find_element_by_xpath('//*[@id="pfs_group"]'))

			select_pfd.select_by_visible_text(pfs_group)

		if p2_timeout_type == "时间":

			browser.find_element_by_xpath('//*[@id="ipsec_sa_lifetime_0"]').click()

			if p2_timeout_time != "86400":
				browser.find_element_by_xpath('//*[@id="time"]').clear()
				browser.find_element_by_xpath('//*[@id="time"]').send_keys(p2_timeout_time)

		if p2_timeout_type == "数据":
			browser.find_element_by_xpath('//*[@id="ipsec_sa_lifetime_1"]').click()

			browser.find_element_by_xpath('//*[@id="bytes"]').clear()
			browser.find_element_by_xpath('//*[@id="bytes"]').send_keys(p2_timeout_data)

		if redundant == "yes":
			browser.find_element_by_xpath('//*[@id="redundant_tunnel"]').click()

			select_redundant = Select(browser.find_element_by_xpath('//*[@id="redundant_tunnel_pl"]'))

			select_redundant.select_by_visible_text(redundant_tunnel)

		if start_negotiation == "yes":

			if not (browser.find_element_by_xpath('//*[@id="start_negotiation_immediately"]').is_selected()):
				browser.find_element_by_xpath('//*[@id="start_negotiation_immediately"]').click()

		if start_negotiation == "no":

			if browser.find_element_by_xpath('//*[@id="start_negotiation_immediately"]').is_selected():
				browser.find_element_by_xpath('//*[@id="start_negotiation_immediately"]').click()

		# 点击返回，退出高级界面
		browser.find_element_by_xpath('//*[@id="container_inner"]/div/div[2]/div[2]/div/input').click()

	browser.find_element_by_xpath('//*[@id="btn_save"]').click()
	# 点击”保存“

	time.sleep(2)

	op_result = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text

	# 点击”return“
	browser.find_element_by_xpath('//*[@id="link_but"]').click()

	# 如果这项选yes,则返回高级设置界面的标题
	if return_switch_adv == "yes":

		return title_adv

	else:

		return op_result


# 添加ipsec网关
def add_ipsec_gw_cer(browser,
					 ipsecRGWname,
					 ipsecdesc,
					 ipsecRGWinterSeq,
					 ipsecRGWgateway,
					 cert_local_name,
					 cert_remote_name,
					 localsubnet,
					 remotesubnet):
	"""

	 证书版ipsec远程网关添加
	:param browser:
	:param ipsecRGWname:
	:param ipsecdesc:
	:param ipsecRGWinterSeq:
	:param ipsecRGWgateway:
	:param cert_local_name:
	:param cert_remote_name:
	:param localsubnet:
	:param remotesubnet:
	:return:
	"""

	# browser.switch_to.default_content()
	# # 定位到默认frame
	#
	# browser.switch_to.frame("lefttree")
	# # 登入后，定位到左侧frame
	#
	# browser.find_element_by_xpath(虚拟专网).click()
	# # 点击”虚拟专网“
	#
	# browser.find_element_by_xpath(远程网关).click()
	# # 点击”远程网关“
	#
	# browser.switch_to.default_content()
	# # 定位到默认frame
	#
	# browser.switch_to.frame("content")
	# 定位到内容frame
	into_fun(browser, 远程网关)
	time.sleep(1)
	browser.find_element_by_xpath("/html/body/div[1]/div[3]/div/input").click()
	# 点击”增加远程网关“

	time.sleep(1)

	browser.find_element_by_xpath('//*[@id="name"]').send_keys(ipsecRGWname)
	# 输入name

	time.sleep(1)

	browser.find_element_by_xpath('//*[@id="description"]').send_keys(ipsecdesc)
	# 输入name

	time.sleep(1)

	localif = Select(browser.find_element_by_xpath('//*[@id="localif"]'))

	# 选择本地接口 ge0/1 ge0/2....
	localif.select_by_visible_text(ipsecRGWinterSeq)

	time.sleep(1)

	browser.find_element_by_xpath('//*[@id="gateway"]').send_keys(ipsecRGWgateway)
	# 输入remote IP add

	time.sleep(1)

	# 选择使用证书认证
	auth_type = Select(browser.find_element_by_xpath('//*[@id="auth_method"]'))
	auth_type.select_by_visible_text("证书")

	local_cert = Select(browser.find_element_by_xpath('//*[@id="local_cert"]'))
	remote_cert = Select(browser.find_element_by_xpath('//*[@id="remote_cert"]'))

	local_cert.select_by_visible_text(cert_local_name)

	time.sleep(1)

	remote_cert.select_by_visible_text(cert_remote_name)

	time.sleep(1)

	browser.find_element_by_xpath('//*[@id="localsubnet"]').clear()
	# clear loacl subnet text

	time.sleep(1)

	browser.find_element_by_xpath('//*[@id="localsubnet"]').send_keys(localsubnet)
	# input local subnet

	time.sleep(1)

	browser.find_element_by_xpath('//*[@id="remotesubnet"]').send_keys(remotesubnet)
	# input remote subnet

	time.sleep(1)

	browser.find_element_by_xpath('//*[@id="btn_save"]').click()
	# 点击”保存“

	time.sleep(2)

	op_result = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text

	# 点击”return“
	browser.find_element_by_xpath('//*[@id="link_but"]').click()

	return op_result


# 添加ca证书
def add_ca(browser, ca_name="ca", ca_desc="desc", ca_path=r"C:\Users\Administrator\Desktop\证书处理\证书处理\证书2份\ca.crt"):
	# browser.switch_to.default_content()
	#
	# # 登入后，定位到左侧frame
	# browser.switch_to.frame("lefttree")
	#
	# # 点击”虚拟专网“
	# browser.find_element_by_xpath(虚拟专网).click()
	#
	# browser.find_element_by_xpath(CA证书).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	#
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, CA证书)
	# 点击导入
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()

	browser.find_element_by_xpath('//*[@id="name"]').send_keys(ca_name)

	browser.find_element_by_xpath('//*[@id="description"]').send_keys(ca_desc)

	browser.find_element_by_xpath('//*[@id="local_file"]').send_keys(ca_path)

	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()

	op_result = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text

	return op_result


def add_cer_local(browser,
				  cer_name="t_cerlocal1",
				  cer_desc="desc",
				  cer_path=r"C:\Users\Administrator\Desktop\证书处理\证书处理\证书2份\server.crt",
				  cer_key_path=r"C:\Users\Administrator\Desktop\证书处理\证书处理\证书2份\server.key",
				  password="123456"):
	# browser.switch_to.default_content()
	#
	# # 登入后，定位到左侧frame
	# browser.switch_to.frame("lefttree")
	#
	# # 点击”虚拟专网“
	# browser.find_element_by_xpath(虚拟专网).click()
	#
	# browser.find_element_by_xpath(CA证书).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	#
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, CA证书)

	# 进入本地证书页  //*[@id="current"]/a  //*[@id="tabs"]/li[2]/a //*[@id="current"]   //*[@id="tabs"]/li[2]/a
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a').click()

	time.sleep(1)
	# 点击导入
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()

	browser.find_element_by_xpath('//*[@id="name"]').send_keys(cer_name)

	browser.find_element_by_xpath('//*[@id="description"]').send_keys(cer_desc)

	# 点击上传PEM/DER格式证书
	browser.find_element_by_xpath('//*[@id="mode_0"]').click()

	browser.find_element_by_xpath('//*[@id="pem_cert_file"]').send_keys(cer_path)

	browser.find_element_by_xpath('//*[@id="pem_key_file"]').send_keys(cer_key_path)

	browser.find_element_by_xpath('//*[@id="pem_passphrase"]').send_keys(password)

	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()

	op_result = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text

	return op_result


def add_cer_remote(browser,
				   cer_name="t_cerremote2",
				   cer_desc="desc",
				   cer_path=r"C:\Users\Administrator\Desktop\证书处理\证书处理\证书2份\ca.crt", ):
	# browser.switch_to.default_content()
	#
	# # 登入后，定位到左侧frame
	# browser.switch_to.frame("lefttree")
	#
	# # 点击”虚拟专网“
	# browser.find_element_by_xpath(虚拟专网).click()
	#
	# browser.find_element_by_xpath(CA证书).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	#
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, CA证书)
	time.sleep(1)

	# 进入远程证书页
	browser.find_element_by_xpath('//*[@id="tabs"]/li[3]/a').click()

	time.sleep(1)

	# 点击导入
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()

	browser.find_element_by_xpath('//*[@id="name"]').send_keys(cer_name)

	browser.find_element_by_xpath('//*[@id="description"]').send_keys(cer_desc)

	browser.find_element_by_xpath('//*[@id="local_file"]').send_keys(cer_path)

	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()

	op_result = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text

	return op_result


# 添加ipsec远程网关（映翰通）
def add_ipsecRemoteGW_inhand(browser, ipsecRGWname, ipsecRGWinterSeq, ipsecRGWgateway, AuthenticationMethod,
							 PresharedKey, localid, remoteid, localsubnet, remotesubnet):
	# browser.switch_to.default_content()
	# # 定位到默认frame
	#
	# browser.switch_to.frame("lefttree")
	# # 登入后，定位到左侧frame
	#
	# browser.find_element_by_xpath("/html/body/div[1]/div[6]/header/a").click()
	# # 点击”虚拟专网“
	#
	# if not browser.find_element_by_xpath('//*[@id="menu"]/div[6]/div/ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath('//*[@id="menu"]/div[6]/div/div').click()
	# browser.find_element_by_xpath('//*[@id="menu"]/div[6]/div/ul/li[4]/span/a').click()
	# # 点击”远程网关“
	#
	# browser.switch_to.default_content()
	# # 定位到默认frame
	#
	# browser.switch_to.frame("content")
	# 定位到内容frame
	into_fun(browser, 远程网关)
	browser.find_element_by_xpath("/html/body/div[1]/div[3]/div/input").click()
	# 点击”增加远程网关“

	time.sleep(1)

	browser.find_element_by_xpath('//*[@id="name"]').send_keys(ipsecRGWname)
	# 输入name

	time.sleep(1)

	localif = Select(browser.find_element_by_xpath('//*[@id="localif"]'))

	localif.select_by_visible_text(ipsecRGWinterSeq)

	time.sleep(1)

	browser.find_element_by_xpath('//*[@id="gateway"]').send_keys(ipsecRGWgateway)
	# 输入remote IP add

	time.sleep(1)

	localif = Select(browser.find_element_by_xpath('//*[@id="auth_method"]'))

	localif.select_by_visible_text(AuthenticationMethod)

	browser.find_element_by_xpath('//*[@id="preshared_key"]').send_keys(PresharedKey)
	# 输入密钥

	# browser.find_element_by_xpath('//*[@id="localid"]').send_keys(localid)
	# # input local ID
	# # browser.find_element_by_xpath('//*[@id="preshared_key"]').send_keys(preshared_key)
	# # input republicKey
	# time.sleep(1)
	# browser.find_element_by_xpath('//*[@id="remoteid"]').send_keys(remoteid)
	# # input remote ID

	time.sleep(1)

	browser.find_element_by_xpath('//*[@id="localsubnet"]').clear()
	# clear loacl subnet text

	time.sleep(1)

	browser.find_element_by_xpath('//*[@id="localsubnet"]').send_keys(localsubnet)
	# input local subnet

	time.sleep(1)

	browser.find_element_by_xpath('//*[@id="remotesubnet"]').send_keys(remotesubnet)
	# input remote subnet

	time.sleep(1)

	browser.find_element_by_xpath('//*[@id="conftr_31"]/td[1]/a').click()
	# 点击”高级“

	p1en = ["aes256", "ses192", "aes128", "3des", "des"]
	p1au = ["md5", "sha1", "sha256", "sha384", "sha512"]

	p2en = ["des", "3des", "aes128", "aes192", "aes256", "sm1", "sm4", "b91"]
	p2au = ["md5", "sha1", "sha256", "sha384", "sha512", "sm3"]

	for i in p1en:
		for j in p1au:
			localif = Select(browser.find_element_by_xpath('//*[@id="encry_alg"]'))
			localif.select_by_visible_text(i)

			localif = Select(browser.find_element_by_xpath('//*[@id="auth_alg"]'))
			localif.select_by_visible_text(j)

			for m in p2en:
				for n in p2au:
					localif = Select(browser.find_element_by_xpath('//*[@id="esp_encry_alg"]'))
					localif.select_by_visible_text(m)

					localif = Select(browser.find_element_by_xpath('//*[@id="esp_auth_alg"]'))
					localif.select_by_visible_text(n)

					print(i, j, m, n)

					browser.find_element_by_xpath('/html/body/form/div[2]/div/div[2]/div[2]/div/input').click()
					# 点击”return“
					browser.find_element_by_xpath('//*[@id="btn_save"]').click()
					# 点击”保存“
					browser.find_element_by_xpath('//*[@id="link_but"]').click()
					# 点击”return“
					browser.find_element_by_xpath(
						'//*[@id="vpn_remote_tunnel_table"]/tbody/tr[2]/td[8]/a[1]/img').click()
					# 点击”编辑“
					time.sleep(1)
					browser.find_element_by_xpath('//*[@id="conftr_31"]/td[1]/a').click()
					# 点击”高级“
					time.sleep(1)

				# ssh = SSH("10.1.1.202", 'root', 'root', 22)
				# ssh.connect()
				# time.sleep(1)
				# result1 = ssh.execute('ping 13.1.1.3 -c 3')
				# # print(result1)
				# ssh.close()
				# if "ttl" not in result1:
				# 	print("算法匹配不成功", i, j, m, n)


# 废除
# def edit_ipsecRemoteGW(browser):
# 	# browser.switch_to.default_content()
# 	# # 定位到默认frame
# 	#
# 	# browser.switch_to.frame("lefttree")
# 	# # 登入后，定位到左侧frame
# 	#
# 	# browser.find_element_by_xpath("/html/body/div[1]/div[6]/header/a").click()
# 	# # 点击”虚拟专网“
# 	#
# 	# if not browser.find_element_by_xpath('//*[@id="menu"]/div[6]/div/ul').is_displayed():
# 	# 	# 如果不可见，点击加号，展开元素
# 	# 	browser.find_element_by_xpath('//*[@id="menu"]/div[6]/div/div').click()
# 	# browser.find_element_by_xpath('//*[@id="menu"]/div[6]/div/ul/li[4]/span/a').click()
# 	# # 点击”远程网关“
# 	#
# 	# browser.switch_to.default_content()
# 	# # 定位到默认frame
# 	#
# 	# browser.switch_to.frame("content")
# 	# 定位到内容frame
# 	into_fun(browser, 远程网关)
# 	browser.find_element_by_xpath('//*[@id="vpn_remote_tunnel_table"]/tbody/tr[2]/td[8]/a[1]/img').click()
# 	# 点击”编辑“
# 	time.sleep(2)
# 	browser.find_element_by_xpath('//*[@id="conftr_31"]/td[1]/a').click()
# 	# 点击”高级“
# 	p1en = ["aes256", "ses192", "aes128", "3des", "des"]
# 	p1au = ["md5", "sha1", "sha256", "sha384", "sha512"]
#
# 	p2en = ["des", "3des", "aes128", "aes192", "aes256", "sm1", "sm4", "b91"]
# 	p2au = ["md5", "sha1", "sha256", "sha384", "sha512", "sm3"]
#
# 	for i in p1en:
# 		for j in p1au:
# 			localif = Select(browser.find_element_by_xpath('//*[@id="encry_alg"]'))
# 			localif.select_by_visible_text(i)
#
# 			localif = Select(browser.find_element_by_xpath('//*[@id="auth_alg"]'))
# 			localif.select_by_visible_text(j)
#
# 			for m in p2en:
# 				for n in p2au:
# 					localif = Select(browser.find_element_by_xpath('//*[@id="esp_encry_alg"]'))
# 					localif.select_by_visible_text(m)
#
# 					localif = Select(browser.find_element_by_xpath('//*[@id="esp_auth_alg"]'))
# 					localif.select_by_visible_text(n)
#
# 					print(i, j, m, n)
#
# 					browser.find_element_by_xpath('/html/body/form/div[2]/div/div[2]/div[2]/div/input').click()
# 					# 点击”return“
# 					browser.find_element_by_xpath('//*[@id="btn_save"]').click()
# 					# 点击”保存“
# 					browser.find_element_by_xpath('//*[@id="link_but"]').click()
# 					# 点击”return“
# 					browser.find_element_by_xpath('//*[@id="vpn_remote_tunnel_table"]/tbody/tr[2]/td[8]/a[1]/img').click()
# 					# 点击”编辑“
# 					time.sleep(1)
# 					browser.find_element_by_xpath('//*[@id="conftr_31"]/td[1]/a').click()
# 					# 点击”高级“
# 					time.sleep(1)
#
# 					# ssh = SSH("10.1.1.202", 'root', 'root', 22)
# 					# ssh.connect()
# 					# time.sleep(1)
# 					# result1 = ssh.execute('ping 13.1.1.3 -c 3')
# 					# # print(result1)
# 					# ssh.close()
# 					# if "ttl" not in result1:
# 					# 	print("算法匹配不成功", i, j, m, n)


# 添加ipsec远程网关
def add_ipsec_remote_gateway_wxw(browser, name='ipsec', desc='miaoshu', status='enable', out_interface="",
								 out_ip="default",
								 remote_gateway='static/dynamic_ip', gateway='10.2.2.82', auth_method='预共享密钥/证书',
								 password='123456',
								 local_ca='', remote_ca='',
								 local='local_ip/local_addr_obj', local_ip='30.1.1.0/255.255.255.0',
								 local_addr_obj='any',
								 remote='remote_ip/remote_addr_obj', remote_ip='20.1.1.0/255.255.255.0',
								 remote_addr_obj='any',
								 advanced='no', xauth='server/client/no', user='', user_name='', user_password='',
								 mode='main/aggressive', encry_alg_div='3des', auth_alg='sha1', dh_group='2',
								 ike_sa_lifetime='86400',
								 ah='no', ah_auth_alg='',
								 esp='yes', esp_encry_alg='aes128', esp_auth_alg='sha1',
								 ip_compression='no', pfs='no', pfs_group='',
								 ipsec_sa='time/data', ipsec_sa_lifetime='86400', data='',
								 tunnel='yes/no', tunnel_pl='', start_negotiation='yes', return1='yes',
								 save='yes/no', cancel=''):
	into_fun(browser, menu=远程网关)
	# # 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击虚拟专网
	# browser.find_element_by_xpath(虚拟专网).click()
	# # 点击远程网关
	# browser.find_element_by_xpath(远程网关).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	# 点击增加
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
	# 输入名称
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(name)
	# 输入描述
	browser.find_element_by_xpath('//*[@id="description"]').send_keys(desc)
	if status == "enable":
		pass
	else:
		browser.find_element_by_xpath('//*[@id="status_1"]').click()
	# 选择本地/出接口
	time.sleep(2)
	# print(1111111111)
	s1 = Select(browser.find_element_by_xpath('//*[@id="localif"]'))
	s1.select_by_visible_text(out_interface)
	if out_ip != "default":
		select_out_ip = Select(browser.find_element_by_xpath('//*[@id="localip"]'))
		time.sleep(1)
		select_out_ip.select_by_visible_text(out_ip)
	# print(out_interface)
	if remote_gateway == 'static':
		# time.sleep(1)
		browser.find_element_by_xpath('//*[@id="gateway"]').send_keys(gateway)
	else:
		time.sleep(1)
		browser.find_element_by_xpath('//*[@id="gwtype_1"]').click()
	# print(33333333333)
	# 选择认证方法
	s1 = Select(browser.find_element_by_xpath('//*[@id="auth_method"]'))
	s1.select_by_visible_text(auth_method)
	# time.sleep(10)
	if auth_method == '预共享密钥':
		browser.find_element_by_xpath('//*[@id="preshared_key"]').send_keys(password)
	if auth_method == '证书':
		s1 = Select(browser.find_element_by_xpath('//*[@id="local_cert"]'))
		s1.select_by_visible_text(local_ca)
		s2 = Select(browser.find_element_by_xpath('//*[@id="remote_cert"]'))
		s2.select_by_visible_text(remote_ca)
	# 填入IKE ID
	if local == 'local_ip':  # //*[@id="localid_status_0"]
		browser.find_element_by_xpath('//*[@id="localid_status_0"]').click()
		browser.find_element_by_xpath('//*[@id="localsubnet"]').clear()
		browser.find_element_by_xpath('//*[@id="localsubnet"]').send_keys(local_ip)
	else:
		browser.find_element_by_xpath('//*[@id="localid_status_1"]').click()
		s1 = Select(browser.find_element_by_xpath('//*[@id="localsubnetobj"]'))
		s1.select_by_visible_text(local_addr_obj)
	if remote == 'remote_ip':
		browser.find_element_by_xpath('//*[@id="remoteid_status_0"]').click()
		browser.find_element_by_xpath('//*[@id="remotesubnet"]').send_keys(remote_ip)
	else:
		browser.find_element_by_xpath('//*[@id="remoteid_status_1"]').click()
		s1 = Select(browser.find_element_by_xpath('//*[@id="remotesubnetobj"]'))
		s1.select_by_visible_text(remote_addr_obj)
	# 高级
	if advanced == "yes":
		browser.find_element_by_xpath('//*[@id="conftr_31"]/td[1]/a').click()
		time.sleep(3)
		# 选择xauth模式：
		if xauth == "server":
			browser.find_element_by_xpath('//*[@id="server_mode_0"]').click()
			s1 = Select(browser.find_element_by_xpath('//*[@id="users"]'))
			s1.select_by_visible_text(user)
		if xauth == "client":
			browser.find_element_by_xpath('//*[@id="server_mode_1"]').click()
			browser.find_element_by_xpath('//*[@id="user_name"]').send_keys(user_name)
			browser.find_element_by_xpath('//*[@id="auth_password"]').send_keys(user_password)
		if xauth == "none":
			browser.find_element_by_xpath('//*[@id="server_mode_2"]').click()
		# ike提议
		# 第一阶段提议
		if mode == "main":
			browser.find_element_by_xpath('//*[@id="mode_0"]').click()
		else:
			browser.find_element_by_xpath('//*[@id="mode_1"]').click()
		# 选择加密算法
		s1 = Select(browser.find_element_by_xpath('//*[@id="encry_alg"]'))
		s1.select_by_visible_text(encry_alg_div)
		# 选择认证算法
		s1 = Select(browser.find_element_by_xpath('//*[@id="auth_alg"]'))
		s1.select_by_visible_text(auth_alg)
		# 选择DH组
		s1 = Select(browser.find_element_by_xpath('//*[@id="dh_group"]'))
		s1.select_by_visible_text(dh_group)
		# ike sa有效时间
		browser.find_element_by_xpath('//*[@id="ike_sa_lifetime"]').clear()
		browser.find_element_by_xpath('//*[@id="ike_sa_lifetime"]').send_keys(ike_sa_lifetime)
		# 第二阶段提议
		if ah == "yes":
			if (browser.find_element_by_xpath('//*[@id="using_ah_protocol"]').is_selected()) is True:
				pass
			else:
				browser.find_element_by_xpath('//*[@id="using_ah_protocol"]').click()
			s1 = Select(browser.find_element_by_xpath('//*[@id="ah_auth_alg"]'))
			s1.select_by_visible_text(ah_auth_alg)
		else:
			if (browser.find_element_by_xpath('//*[@id="using_ah_protocol"]').is_selected()) is True:
				browser.find_element_by_xpath('//*[@id="using_ah_protocol"]').click()
		if esp == 'yes':
			if (browser.find_element_by_xpath('//*[@id="using_esp_protocol"]').is_selected()) is True:
				pass
			else:
				browser.find_element_by_xpath('//*[@id="using_esp_protocol"]').click()
			s1 = Select(browser.find_element_by_xpath('//*[@id="esp_encry_alg"]'))
			s1.select_by_visible_text(esp_encry_alg)
			s2 = Select(browser.find_element_by_xpath('//*[@id="esp_auth_alg"]'))
			s2.select_by_visible_text(esp_auth_alg)
		else:
			if (browser.find_element_by_xpath('//*[@id="using_esp_protocol"]').is_selected()) is True:
				browser.find_element_by_xpath('//*[@id="using_esp_protocol"]').click()

		if ip_compression == 'yes':
			if (browser.find_element_by_xpath('//*[@id="enable_ip_compression"]').is_selected()) is True:
				pass
			else:
				browser.find_element_by_xpath('//*[@id="enable_ip_compression"]').click()
		else:
			if (browser.find_element_by_xpath('//*[@id="enable_ip_compression"]').is_selected()) is True:
				browser.find_element_by_xpath('//*[@id="enable_ip_compression"]').click()

		if pfs == "yes":
			if (browser.find_element_by_xpath('//*[@id="enable_pfs"]').is_selected()) is True:
				pass
			else:
				browser.find_element_by_xpath('//*[@id="enable_pfs"]').click()
			s1 = Select(browser.find_element_by_xpath('//*[@id="pfs_group"]'))
			s1.select_by_visible_text(pfs_group)
		else:
			if (browser.find_element_by_xpath('//*[@id="enable_pfs"]').is_selected()) is True:
				browser.find_element_by_xpath('//*[@id="enable_pfs"]').click()
		# ipsec sa有效时间
		if ipsec_sa == 'time':
			browser.find_element_by_xpath('//*[@id="ipsec_sa_lifetime_0"]').click()
			browser.find_element_by_xpath('//*[@id="time"]').clear()
			browser.find_element_by_xpath('//*[@id="time"]').send_keys(ipsec_sa_lifetime)
		if ipsec_sa == 'data':
			browser.find_element_by_xpath('//*[@id="ipsec_sa_lifetime_1"]').clear()
			browser.find_element_by_xpath('//*[@id="ipsec_sa_lifetime_1"]').click()
			browser.find_element_by_xpath('//*[@id="bytes"]').send_keys(data)

		if tunnel == "yes":
			if (browser.find_element_by_xpath('//*[@id="redundant_tunnel"]').is_selected()) is True:
				pass
			else:
				browser.find_element_by_xpath('//*[@id="redundant_tunnel"]').click()
			s1 = Select(browser.find_element_by_xpath('//*[@id="redundant_tunnel_pl"]'))
			s1.select_by_visible_text(tunnel_pl)
		else:
			if (browser.find_element_by_xpath('//*[@id="redundant_tunnel"]').is_selected()) is True:
				browser.find_element_by_xpath('//*[@id="redundant_tunnel"]').click()
		# 是否协商
		if start_negotiation == 'yes':
			if (browser.find_element_by_xpath('//*[@id="start_negotiation_immediately"]').is_selected()) is True:
				pass
			else:
				browser.find_element_by_xpath('//*[@id="start_negotiation_immediately"]').click()
		else:
			if (browser.find_element_by_xpath('//*[@id="start_negotiation_immediately"]').is_selected()) is True:
				browser.find_element_by_xpath('//*[@id="start_negotiation_immediately"]').click()
			browser.find_element_by_xpath('//*[@id="start_negotiation_immediately"]').click()
		if return1 == "yes":
			browser.find_element_by_xpath('//*[@id="container_inner"]/div/div[2]/div[2]/div/input').click()
	if save == "yes":
		browser.find_element_by_xpath('//*[@id="btn_save"]').click()
	if cancel == "yes":
		browser.find_element_by_xpath('//*[@id="btn_cancel"]').click()


# 删除指定的ipsec远程网关
def del_ipsec_remote_gateway_wxw(browser, name='ipsec'):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击虚拟专网
	# browser.find_element_by_xpath(虚拟专网).click()
	# # 点击远程网关
	# browser.find_element_by_xpath(远程网关).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 远程网关)
	# 找到指定的ipsec远程网关并删除//*[@id="vpn_remote_tunnel_table"]/tbody/tr[2]/td[2]
	# //*[@id="vpn_remote_tunnel_table"]/tbody/tr[3]/td[2]
	n = 2
	getname = browser.find_element_by_xpath(
		'//*[@id="vpn_remote_tunnel_table"]/tbody/tr[' + str(n) + ']/td[2]').text.replace(' ', '')
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath(
			'//*[@id="vpn_remote_tunnel_table"]/tbody/tr[' + str(n) + ']/td[2]').text.replace(' ', '')
	# 点击删除
	browser.find_element_by_xpath('//*[@id="vpn_remote_tunnel_table"]/tbody/tr[' + str(n) + ']/td[8]/a[2]/img').click()


# 删除指定的ipsec远程访问
def del_ipsec_remote_access(browser, name='ipsec'):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击虚拟专网
	# browser.find_element_by_xpath(虚拟专网).click()
	# # 点击远程网关
	# browser.find_element_by_xpath(远程网关).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 远程访问)
	# 找到指定的ipsec远程网关并删除
	n = 2
	getname = browser.find_element_by_xpath(
		'//*[@id="vpn_remote_access_table"]/tbody/tr[' + str(n) + ']/td[2]').text.replace(' ', '')
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath(
			'//*[@id="vpn_remote_access_table"]/tbody/tr[' + str(n) + ']/td[2]').text.replace(' ', '')
	# 点击删除
	browser.find_element_by_xpath('//*[@id="vpn_remote_access_table"]/tbody/tr[' + str(n) + ']/td[8]/a[2]/img').click()


# 判断ipsec是否存在，若存在返回True,反之返回False
def is_ipsec_remote_gateway_exist_wxw(browser, name='ipsec'):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击虚拟专网
	# browser.find_element_by_xpath(虚拟专网).click()
	# # 点击远程网关
	# browser.find_element_by_xpath(远程网关).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 远程网关)
	# 获取目前有多少个ipsec
	time.sleep(1)
	route_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	# 根据route数量,遍历一下
	# print(str(destination))
	for x in range(2, 2 + route_sum):
		if str(name) == browser.find_element_by_xpath(
				'//*[@id="vpn_remote_tunnel_table"]/tbody/tr[' + str(x) + ']/td[2]').text.replace(' ', ''):
			return True
	else:
		return False


# 判断ipsec access是否存在，若存在返回True,反之返回False
def is_ipsec_remote_access_exist(browser, name='ipsec'):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击虚拟专网
	# browser.find_element_by_xpath(虚拟专网).click()
	# # 点击远程网关
	# browser.find_element_by_xpath(远程网关).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 远程访问)
	# 获取目前有多少个ipsec
	time.sleep(1)
	route_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	# 根据route数量,遍历一下
	# print(str(destination))
	for x in range(2, 2 + route_sum):
		if str(name) == browser.find_element_by_xpath(
				'//*[@id="vpn_remote_access_table"]/tbody/tr[' + str(x) + ']/td[2]').text.replace(' ', ''):
			return True
	else:
		return False


# 编辑指定的ipsec远程网关
def edit_ipsec_remote_gateway_wxw(browser, name='ipsec', desc='miaoshu/unmodify', status='enable/unmodify',
								  out_interface=interface_name_3+'/unmodify',
								  remote_gateway='static/dynamic_ip/unmodify', gateway='10.2.2.82/unmodify', auth_method='预共享密钥/证书/unmodify',
								  password='123456/unmodify',
								  local_ca='/unmodify', remote_ca='/unmodify',
								  local='local_ip/local_addr_obj/unmodify', local_ip='30.1.1.0/255.255.255.0/unmodify',
								  local_addr_obj='any/unmodify',
								  remote='remote_ip/remote_addr_obj/unmodify', remote_ip='20.1.1.0/255.255.255.0/unmodify',
								  remote_addr_obj='any/unmodify',
								  advanced='no/unmodify', xauth='server/client/no/unmodify', user='/unmodify', user_name='/unmodify', user_password='/unmodify',
								  mode='main/aggressive/unmodify', encry_alg_div='3des/unmodify', auth_alg='sha1/unmodify', dh_group='2/unmodify',
								  ike_sa_lifetime='86400/unmodify',
								  ah='no/unmodify', ah_auth_alg='/unmodify',
								  esp='yes/unmodify', esp_encry_alg='aes128/unmodify', esp_auth_alg='sha1/unmodify',
								  ip_compression='no/unmodify', pfs='no/unmodify', pfs_group='/unmodify',
								  ipsec_sa='time/data/unmodify', ipsec_sa_lifetime='86400/unmodify', data='/unmodify',
								  tunnel='yes/no/unmodify', tunnel_pl='/unmodify', start_negotiation='yes/unmodify', return1='yes/unmodify',
								  save='yes/no', cancel=''):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击虚拟专网
	# browser.find_element_by_xpath(虚拟专网).click()
	# # 点击远程网关
	# browser.find_element_by_xpath(远程网关).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 远程网关)
	# 找到指定的ipsec远程网关并删除
	n = 2
	getname = browser.find_element_by_xpath(
		'//*[@id="vpn_remote_tunnel_table"]/tbody/tr[' + str(n) + ']/td[2]').text.replace(' ', '')
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath(
			'//*[@id="vpn_remote_tunnel_table"]/tbody/tr[' + str(n) + ']/td[2]').text.replace(' ', '')
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="vpn_remote_tunnel_table"]/tbody/tr[' + str(n) + ']/td[8]/a[1]/img').click()
	if "unmodify" not in desc:
		# 编辑描述
		browser.find_element_by_xpath('//*[@id="description"]').clear()
		browser.find_element_by_xpath('//*[@id="description"]').send_keys(desc)

	if "unmodify" not in status:
		if status == "enable":
			pass
		else:
			browser.find_element_by_xpath('//*[@id="status_1"]').click()

	# 选择本地/出接口
	if "unmodify" not in out_interface:
		s1 = Select(browser.find_element_by_xpath('//*[@id="localif"]'))
		s1.select_by_visible_text(out_interface)

	if "unmodify" not in remote_gateway:
		if remote_gateway == 'static':
			browser.find_element_by_xpath('//*[@id="gateway"]').clear()
			browser.find_element_by_xpath('//*[@id="gateway"]').send_keys(gateway)
		else:
			browser.find_element_by_xpath('//*[@id="gwtype_1"]').click()

	if "unmodify" not in auth_method:
		# 选择认证方法
		s1 = Select(browser.find_element_by_xpath('//*[@id="auth_method"]'))
		s1.select_by_visible_text(auth_method)
		if auth_method == '预共享密钥':
			browser.find_element_by_xpath('//*[@id="preshared_key"]').clear()
			browser.find_element_by_xpath('//*[@id="preshared_key"]').send_keys(password)
		if auth_method == '证书':
			s1 = Select(browser.find_element_by_xpath('//*[@id="local_cert"]'))
			s1.select_by_visible_text(local_ca)
			s2 = Select(browser.find_element_by_xpath('//*[@id="remote_cert"]'))
			s2.select_by_visible_text(remote_ca)
	# 填入IKE ID
	if "unmodify" not in local:
		if local == 'local_ip':
			browser.find_element_by_xpath('//*[@id="localid_status_0"]').click()
			browser.find_element_by_xpath('//*[@id="localsubnet"]').clear()
			browser.find_element_by_xpath('//*[@id="localsubnet"]').send_keys(local_ip)
		else:
			browser.find_element_by_xpath('//*[@id="localid_status_1"]').click()
			s1 = Select(browser.find_element_by_xpath('//*[@id="localsubnetobj"]'))
			s1.select_by_visible_text(local_addr_obj)
	if "unmodify" not in remote:
		if remote == 'remote_ip':
			browser.find_element_by_xpath('//*[@id="remoteid_status_0"]').click()
			browser.find_element_by_xpath('//*[@id="remotesubnet"]').clear()
			browser.find_element_by_xpath('//*[@id="remotesubnet"]').send_keys(remote_ip)
		else:
			browser.find_element_by_xpath('//*[@id="remoteid_status_1"]').click()
			s1 = Select(browser.find_element_by_xpath('//*[@id="remotesubnetobj"]'))
			s1.select_by_visible_text(remote_addr_obj)

	# 高级
	if "unmodify" not in advanced:
		if advanced == "yes":
			browser.find_element_by_xpath('//*[@id="conftr_31"]/td[1]/a').click()
			# 选择xauth模式：
			if xauth == "server":
				browser.find_element_by_xpath('//*[@id="server_mode_0"]').click()
				s1 = Select(browser.find_element_by_xpath('//*[@id="users"]'))
				s1.select_by_visible_text(user)
			if xauth == "client":
				browser.find_element_by_xpath('//*[@id="server_mode_1"]').click()
				browser.find_element_by_xpath('//*[@id="user_name"]').clear()
				browser.find_element_by_xpath('//*[@id="user_name"]').send_keys(user_name)
				browser.find_element_by_xpath('//*[@id="auth_password"]').clear()
				browser.find_element_by_xpath('//*[@id="auth_password"]').send_keys(user_password)
			if xauth == "none":
				browser.find_element_by_xpath('//*[@id="server_mode_2"]').click()
			# ike提议
			# 第一阶段提议
			if mode == "main":
				browser.find_element_by_xpath('//*[@id="mode_0"]').click()
			else:
				browser.find_element_by_xpath('//*[@id="mode_1"]').click()
			# 选择加密算法
			s1 = Select(browser.find_element_by_xpath('//*[@id="encry_alg"]'))
			s1.select_by_visible_text(encry_alg_div)
			# 选择认证算法
			s1 = Select(browser.find_element_by_xpath('//*[@id="auth_alg"]'))
			s1.select_by_visible_text(auth_alg)
			# 选择DH组
			s1 = Select(browser.find_element_by_xpath('//*[@id="dh_group"]'))
			s1.select_by_visible_text(dh_group)
			# ike sa有效时间
			browser.find_element_by_xpath('//*[@id="ike_sa_lifetime"]').clear()
			browser.find_element_by_xpath('//*[@id="ike_sa_lifetime"]').send_keys(ike_sa_lifetime)
			# 第二阶段提议
			if ah == "yes":
				if (browser.find_element_by_xpath('//*[@id="using_ah_protocol"]').is_selected()) is True:
					pass
				else:
					browser.find_element_by_xpath('//*[@id="using_ah_protocol"]').click()
				s1 = Select(browser.find_element_by_xpath('//*[@id="ah_auth_alg"]'))
				s1.select_by_visible_text(ah_auth_alg)
			else:
				if (browser.find_element_by_xpath('//*[@id="using_ah_protocol"]').is_selected()) is True:
					browser.find_element_by_xpath('//*[@id="using_ah_protocol"]').click()
			if esp == 'yes':
				if (browser.find_element_by_xpath('//*[@id="using_esp_protocol"]').is_selected()) is True:
					pass
				else:
					browser.find_element_by_xpath('//*[@id="using_esp_protocol"]').click()
				s1 = Select(browser.find_element_by_xpath('//*[@id="esp_encry_alg"]'))
				s1.select_by_visible_text(esp_encry_alg)
				s2 = Select(browser.find_element_by_xpath('//*[@id="esp_auth_alg"]'))
				s2.select_by_visible_text(esp_auth_alg)
			else:
				if (browser.find_element_by_xpath('//*[@id="using_esp_protocol"]').is_selected()) is True:
					browser.find_element_by_xpath('//*[@id="using_esp_protocol"]').click()

			if ip_compression == 'yes':
				if (browser.find_element_by_xpath('//*[@id="enable_ip_compression"]').is_selected()) is True:
					pass
				else:
					browser.find_element_by_xpath('//*[@id="enable_ip_compression"]').click()
			else:
				if (browser.find_element_by_xpath('//*[@id="enable_ip_compression"]').is_selected()) is True:
					browser.find_element_by_xpath('//*[@id="enable_ip_compression"]').click()

			if pfs == "yes":
				if (browser.find_element_by_xpath('//*[@id="enable_pfs"]').is_selected()) is True:
					pass
				else:
					browser.find_element_by_xpath('//*[@id="enable_pfs"]').click()
				s1 = Select(browser.find_element_by_xpath('//*[@id="pfs_group"]'))
				s1.select_by_visible_text(pfs_group)
			else:
				if (browser.find_element_by_xpath('//*[@id="enable_pfs"]').is_selected()) is True:
					browser.find_element_by_xpath('//*[@id="enable_pfs"]').click()
			# ipsec sa有效时间
			if ipsec_sa == 'time':
				browser.find_element_by_xpath('//*[@id="ipsec_sa_lifetime_0"]').click()
				browser.find_element_by_xpath('//*[@id="time"]').clear()
				browser.find_element_by_xpath('//*[@id="time"]').send_keys(ipsec_sa_lifetime)
			if ipsec_sa == 'data':
				browser.find_element_by_xpath('//*[@id="ipsec_sa_lifetime_1"]').clear()
				browser.find_element_by_xpath('//*[@id="ipsec_sa_lifetime_1"]').click()
				browser.find_element_by_xpath('//*[@id="bytes"]').clear()
				browser.find_element_by_xpath('//*[@id="bytes"]').send_keys(data)

			if tunnel == "yes":
				if (browser.find_element_by_xpath('//*[@id="redundant_tunnel"]').is_selected()) is True:
					pass
				else:
					browser.find_element_by_xpath('//*[@id="redundant_tunnel"]').click()
				s1 = Select(browser.find_element_by_xpath('//*[@id="redundant_tunnel_pl"]'))
				s1.select_by_visible_text(tunnel_pl)
			else:
				if (browser.find_element_by_xpath('//*[@id="redundant_tunnel"]').is_selected()) is True:
					browser.find_element_by_xpath('//*[@id="redundant_tunnel"]').click()
			# 是否协商
			if start_negotiation == 'yes':
				if (browser.find_element_by_xpath('//*[@id="start_negotiation_immediately"]').is_selected()) is True:
					pass
				else:
					browser.find_element_by_xpath('//*[@id="start_negotiation_immediately"]').click()
			else:
				if (browser.find_element_by_xpath('//*[@id="start_negotiation_immediately"]').is_selected()) is True:
					browser.find_element_by_xpath('//*[@id="start_negotiation_immediately"]').click()
				browser.find_element_by_xpath('//*[@id="start_negotiation_immediately"]').click()
			if return1 == "yes":
				browser.find_element_by_xpath('//*[@id="container_inner"]/div/div[2]/div[2]/div/input').click()
			if save == "yes":
				browser.find_element_by_xpath('//*[@id="btn_save"]').click()
			if cancel == "yes":
				browser.find_element_by_xpath('//*[@id="btn_cancel"]').click()


# 添加远程访问
def add_ipsec_remote_access(browser, name='ipsec', desc='miaoshu', status='enable', out_interface="",
								 out_ip="default", auth_method='预共享密钥/证书', password='123456',
								 local_ca='', remote_ca='', remote_ike_id_switch='no', ikeid_type="IP Address", remoteid_ipadd="5.5.5.5",
								 pri_dns="", sencond_dns="", pri_win="", sencond_win="",
 								 local='local_ip/local_addr_obj', local_ip='30.1.1.0/255.255.255.0',
								 local_addr_obj='any',
								 advanced='no', mode='main/aggressive', encry_alg_div='3des', auth_alg='sha1', dh_group='2',
								 ike_sa_lifetime='86400',
								 ah='no', ah_auth_alg='',
								 esp='yes', esp_encry_alg='aes128', esp_auth_alg='sha1',
								 ip_compression='no', pfs='no', pfs_group='',
								 ipsec_sa='time/data', ipsec_sa_lifetime='86400', data='',
								  tunnel='yes/no', tunnel_pl='', start_negotiation='yes', return1='yes',
								 save='yes/no', cancel=''):
	into_fun(browser, menu=远程访问)
	# # 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击虚拟专网
	# browser.find_element_by_xpath(虚拟专网).click()
	# # 点击远程网关
	# browser.find_element_by_xpath(远程网关).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	# 点击增加
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
	# 输入名称
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(name)
	# 输入描述
	browser.find_element_by_xpath('//*[@id="description"]').send_keys(desc)
	if status == "enable":
		pass
	else:
		browser.find_element_by_xpath('//*[@id="status_1"]').click()
	# 选择本地/出接口
	time.sleep(2)
	# print(1111111111) //*[@id="local_interface"]
	s1 = Select(browser.find_element_by_xpath('//*[@id="local_interface"]'))
	s1.select_by_visible_text(out_interface)
	if out_ip != "default":
		select_out_ip = Select(browser.find_element_by_xpath('//*[@id="local_ip"]'))
		time.sleep(1)
		select_out_ip.select_by_visible_text(out_ip)
	# print(out_interface)

	# 选择认证方法
	s1 = Select(browser.find_element_by_xpath('//*[@id="auth_method"]'))
	s1.select_by_visible_text(auth_method)
	# time.sleep(10)
	if auth_method == '预共享密钥':
		browser.find_element_by_xpath('//*[@id="preshared_key"]').send_keys(password)
	if auth_method == '证书':
		s1 = Select(browser.find_element_by_xpath('//*[@id="local_cert"]'))
		s1.select_by_visible_text(local_ca)
		s2 = Select(browser.find_element_by_xpath('//*[@id="remote_cert"]'))
		s2.select_by_visible_text(remote_ca)
	# 填入IKE ID
	if remote_ike_id_switch == "yes":
		pass
		if browser.find_element_by_xpath('//*[@id="ikeid_toggle"]').get_attribute('class') == "adv_toggle_show":
			browser.find_element_by_xpath('//*[@id="ikeid_toggle"]').click()
		select_remote_ikeid = Select(browser.find_element_by_xpath('//*[@id="remote_id_sel"]'))
		select_remote_ikeid.select_by_visible_text(ikeid_type)
		browser.find_element_by_xpath('//*[@id="remote_id_text"]').send_keys(remoteid_ipadd)

		# 远端IKE ID功能，暂时不写，占位
	# 远程设置
	if pri_dns != "":
		browser.find_element_by_xpath('//*[@id="pri_dns_ip"]').clear()
		browser.find_element_by_xpath('//*[@id="pri_dns_ip"]').send_keys(pri_dns)
	if sencond_dns != "":
		browser.find_element_by_xpath('//*[@id="sec_dns_ip"]').clear()
		browser.find_element_by_xpath('//*[@id="sec_dns_ip"]').send_keys(sencond_dns)
	if pri_win != "":
		browser.find_element_by_xpath('//*[@id="pri_wins_ip"]').clear()
		browser.find_element_by_xpath('//*[@id="pri_wins_ip"]').send_keys(pri_win)
	if sencond_win != "":
		browser.find_element_by_xpath('//*[@id="sec_wins_ip"]').clear()
		browser.find_element_by_xpath('//*[@id="sec_wins_ip"]').send_keys(sencond_win)
	# 本地受保护网络
	if local == 'local_ip':  # //*[@id="localid_status_0"]
		browser.find_element_by_xpath('//*[@id="localid_status_0"]').click()
		browser.find_element_by_xpath('//*[@id="localsubnet"]').clear()
		browser.find_element_by_xpath('//*[@id="localsubnet"]').send_keys(local_ip)
	else:
		browser.find_element_by_xpath('//*[@id="localid_status_1"]').click()
		s1 = Select(browser.find_element_by_xpath('//*[@id="localsubnetobj"]'))
		s1.select_by_visible_text(local_addr_obj)
	# 高级
	if advanced == "yes":
		browser.find_element_by_xpath('//*[@id="conftr_20"]/td[1]/a').click()
		time.sleep(3)
		# 选择xauth模式：
		# if xauth == "server":
		# 	browser.find_element_by_xpath('//*[@id="server_mode_0"]').click()
		# 	s1 = Select(browser.find_element_by_xpath('//*[@id="users"]'))
		# 	s1.select_by_visible_text(user)
		# if xauth == "client":
		# 	browser.find_element_by_xpath('//*[@id="server_mode_1"]').click()
		# 	browser.find_element_by_xpath('//*[@id="user_name"]').send_keys(user_name)
		# 	browser.find_element_by_xpath('//*[@id="auth_password"]').send_keys(user_password)
		# if xauth == "none":
		# 	browser.find_element_by_xpath('//*[@id="server_mode_2"]').click()
		# ike提议
		# 第一阶段提议
		if mode == "main":
			browser.find_element_by_xpath('//*[@id="mode_0"]').click()
		else:
			browser.find_element_by_xpath('//*[@id="mode_1"]').click()
		# 选择加密算法
		s1 = Select(browser.find_element_by_xpath('//*[@id="encry_alg"]'))
		s1.select_by_visible_text(encry_alg_div)
		# 选择认证算法
		s1 = Select(browser.find_element_by_xpath('//*[@id="auth_alg"]'))
		s1.select_by_visible_text(auth_alg)
		# 选择DH组
		s1 = Select(browser.find_element_by_xpath('//*[@id="dh_group"]'))
		s1.select_by_visible_text(dh_group)
		# ike sa有效时间
		browser.find_element_by_xpath('//*[@id="ike_sa_lifetime"]').clear()
		browser.find_element_by_xpath('//*[@id="ike_sa_lifetime"]').send_keys(ike_sa_lifetime)
		# 第二阶段提议
		if ah == "yes":
			if (browser.find_element_by_xpath('//*[@id="using_ah_protocol"]').is_selected()) is True:
				pass
			else:
				browser.find_element_by_xpath('//*[@id="using_ah_protocol"]').click()
			s1 = Select(browser.find_element_by_xpath('//*[@id="ah_auth_alg"]'))
			s1.select_by_visible_text(ah_auth_alg)
		else:
			if (browser.find_element_by_xpath('//*[@id="using_ah_protocol"]').is_selected()) is True:
				browser.find_element_by_xpath('//*[@id="using_ah_protocol"]').click()
		if esp == 'yes':
			if (browser.find_element_by_xpath('//*[@id="using_esp_protocol"]').is_selected()) is True:
				pass
			else:
				browser.find_element_by_xpath('//*[@id="using_esp_protocol"]').click()
			s1 = Select(browser.find_element_by_xpath('//*[@id="esp_encry_alg"]'))
			s1.select_by_visible_text(esp_encry_alg)
			s2 = Select(browser.find_element_by_xpath('//*[@id="esp_auth_alg"]'))
			s2.select_by_visible_text(esp_auth_alg)
		else:
			if (browser.find_element_by_xpath('//*[@id="using_esp_protocol"]').is_selected()) is True:
				browser.find_element_by_xpath('//*[@id="using_esp_protocol"]').click()

		if ip_compression == 'yes':
			if (browser.find_element_by_xpath('//*[@id="enable_ip_compression"]').is_selected()) is True:
				pass
			else:
				browser.find_element_by_xpath('//*[@id="enable_ip_compression"]').click()
		else:
			if (browser.find_element_by_xpath('//*[@id="enable_ip_compression"]').is_selected()) is True:
				browser.find_element_by_xpath('//*[@id="enable_ip_compression"]').click()

		if pfs == "yes":
			if (browser.find_element_by_xpath('//*[@id="enable_pfs"]').is_selected()) is True:
				pass
			else:
				browser.find_element_by_xpath('//*[@id="enable_pfs"]').click()
			s1 = Select(browser.find_element_by_xpath('//*[@id="pfs_group"]'))
			s1.select_by_visible_text(pfs_group)
		else:
			if (browser.find_element_by_xpath('//*[@id="enable_pfs"]').is_selected()) is True:
				browser.find_element_by_xpath('//*[@id="enable_pfs"]').click()
		# ipsec sa有效时间
		if ipsec_sa == 'time':
			browser.find_element_by_xpath('//*[@id="ipsec_sa_lifetime_0"]').click()
			browser.find_element_by_xpath('//*[@id="time"]').clear()
			browser.find_element_by_xpath('//*[@id="time"]').send_keys(ipsec_sa_lifetime)
		if ipsec_sa == 'data':
			browser.find_element_by_xpath('//*[@id="ipsec_sa_lifetime_1"]').click()
			browser.find_element_by_xpath('//*[@id="bytes"]').clear()
			browser.find_element_by_xpath('//*[@id="bytes"]').send_keys(data)

		# if tunnel == "yes": //*[@id="ipsec_sa_lifetime_1"]
		# 	if (browser.find_element_by_xpath('//*[@id="redundant_tunnel"]').is_selected()) is True:
		# 		pass
		# 	else:
		# 		browser.find_element_by_xpath('//*[@id="redundant_tunnel"]').click()
		# 	s1 = Select(browser.find_element_by_xpath('//*[@id="redundant_tunnel_pl"]'))
		# 	s1.select_by_visible_text(tunnel_pl)
		# else:
		# 	if (browser.find_element_by_xpath('//*[@id="redundant_tunnel"]').is_selected()) is True:
		# 		browser.find_element_by_xpath('//*[@id="redundant_tunnel"]').click()
		# 是否协商
		# if start_negotiation == 'yes':
		# 	if (browser.find_element_by_xpath('//*[@id="start_negotiation_immediately"]').is_selected()) is True:
		# 		pass
		# 	else:
		# 		browser.find_element_by_xpath('//*[@id="start_negotiation_immediately"]').click()
		# else:
		# 	if (browser.find_element_by_xpath('//*[@id="start_negotiation_immediately"]').is_selected()) is True:
		# 		browser.find_element_by_xpath('//*[@id="start_negotiation_immediately"]').click()
		# 	browser.find_element_by_xpath('//*[@id="start_negotiation_immediately"]').click()
		if return1 == "yes":
			browser.find_element_by_xpath('//*[@id="container_inner"]/div/div[2]/div[2]/div/input').click()
	if save == "yes":
		browser.find_element_by_xpath('//*[@id="btn_save"]').click()
	if cancel == "yes":
		browser.find_element_by_xpath('//*[@id="btn_cancel"]').click()


# 编辑远程访问
def edit_ipsec_remote_access(browser, name='ipsec', desc='miaoshu/unmodify', status='enable/unmodify', out_interface="/unmodify",
								 out_ip="default/unmodify", auth_method='预共享密钥/证书/unmodify', password='123456/unmodify',
								 local_ca='/unmodify', remote_ca='/unmodify', remote_ike_id_switch='no/unmodify', ikeid_type="IP Address/unmodify", remoteid_ipadd="5.5.5.5/unmodify",
								 pri_dns="/unmodify", sencond_dns="/unmodify", pri_win="/unmodify", sencond_win="/unmodify",
 								 local='local_ip/local_addr_obj/unmodify', local_ip='30.1.1.0/255.255.255.0/unmodify',
								 local_addr_obj='any/unmodify',
								 advanced='no/unmodify', mode='main/aggressive/unmodify', encry_alg_div='3des/unmodify', auth_alg='sha1/unmodify', dh_group='2/unmodify',
								 ike_sa_lifetime='86400/unmodify',
								 ah='no/unmodify', ah_auth_alg='/unmodify',
								 esp='yes/unmodify', esp_encry_alg='aes128/unmodify', esp_auth_alg='sha1/unmodify',
								 ip_compression='no/unmodify', pfs='no/unmodify', pfs_group='/unmodify',
								 ipsec_sa='time/data/unmodify', ipsec_sa_lifetime='86400/unmodify', data='/unmodify',
								  tunnel='yes/no', tunnel_pl='', start_negotiation='yes', return1='yes',
								 save='yes/no/unmodify', cancel='/unmodify'):
	browser.refresh()
	into_fun(browser, menu=远程访问)
	# # 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击虚拟专网
	# browser.find_element_by_xpath(虚拟专网).click()
	# # 点击远程网关
	# browser.find_element_by_xpath(远程网关).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	# 点击增加 //*[@id="vpn_remote_access_table"]/tbody/tr[2]/td[2] //*[@id="vpn_remote_access_table"]/tbody/tr[2]/td[3]
	n = 2
	getname = browser.find_element_by_xpath(
		'//*[@id="vpn_remote_access_table"]/tbody/tr[' + str(n) + ']/td[2]').text.replace(' ', '')
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath(
			'//*[@id="vpn_remote_access_table"]/tbody/tr[' + str(n) + ']/td[2]').text.replace(' ', '')
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="vpn_remote_access_table"]/tbody/tr[' + str(n) + ']/td[8]/a[1]/img').click()
	# 输入名称
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(name)
	# 输入描述
	if "unmodify" not in desc:
		browser.find_element_by_xpath('//*[@id="description"]').send_keys(desc)

	if "unmodify" not in status:
		if status == "enable":
			pass
		else:
			browser.find_element_by_xpath('//*[@id="status_1"]').click()
	# 选择本地/出接口
	if "unmodify" not in out_interface:
		time.sleep(2)
		# print(1111111111) //*[@id="local_interface"]
		s1 = Select(browser.find_element_by_xpath('//*[@id="local_interface"]'))
		s1.select_by_visible_text(out_interface)
		if out_ip != "default":
			select_out_ip = Select(browser.find_element_by_xpath('//*[@id="local_ip"]'))
			time.sleep(1)
			select_out_ip.select_by_visible_text(out_ip)
		# print(out_interface)

	# 选择认证方法
	if "unmodify" not in auth_method:
		s1 = Select(browser.find_element_by_xpath('//*[@id="auth_method"]'))
		s1.select_by_visible_text(auth_method)
		# time.sleep(10)
		if auth_method == '预共享密钥':
			browser.find_element_by_xpath('//*[@id="preshared_key"]').send_keys(password)
		if auth_method == '证书':
			s1 = Select(browser.find_element_by_xpath('//*[@id="local_cert"]'))
			s1.select_by_visible_text(local_ca)
			s2 = Select(browser.find_element_by_xpath('//*[@id="remote_cert"]'))
			s2.select_by_visible_text(remote_ca)
	# 填入IKE ID
	if "unmodify" not in remote_ike_id_switch:
		if remote_ike_id_switch == "yes":
			pass
			if browser.find_element_by_xpath('//*[@id="ikeid_toggle"]').get_attribute('class') == "adv_toggle_show":
				browser.find_element_by_xpath('//*[@id="ikeid_toggle"]').click()
			select_remote_ikeid = Select(browser.find_element_by_xpath('//*[@id="remote_id_sel"]'))
			select_remote_ikeid.select_by_visible_text(ikeid_type)
			browser.find_element_by_xpath('//*[@id="remote_id_text"]').send_keys(remoteid_ipadd)

		# 远端IKE ID功能，暂时不写，占位
	# 远程设置
	if pri_dns != "" and "unmodify" not in pri_dns:
		browser.find_element_by_xpath('//*[@id="pri_dns_ip"]').clear()
		browser.find_element_by_xpath('//*[@id="pri_dns_ip"]').send_keys(pri_dns)
	if sencond_dns != "" and "unmodify" not in sencond_dns:
		browser.find_element_by_xpath('//*[@id="sec_dns_ip"]').clear()
		browser.find_element_by_xpath('//*[@id="sec_dns_ip"]').send_keys(sencond_dns)
	if pri_win != "" and "unmodify" not in pri_win:
		browser.find_element_by_xpath('//*[@id="pri_wins_ip"]').clear()
		browser.find_element_by_xpath('//*[@id="pri_wins_ip"]').send_keys(pri_win)
	if sencond_win != "" and "unmodify" not in sencond_win:
		browser.find_element_by_xpath('//*[@id="sec_wins_ip"]').clear()
		browser.find_element_by_xpath('//*[@id="sec_wins_ip"]').send_keys(sencond_win)
	# 本地受保护网络
	if "unmodify" not in local:
		if local == 'local_ip' :  # //*[@id="localid_status_0"]
			browser.find_element_by_xpath('//*[@id="localid_status_0"]').click()
			browser.find_element_by_xpath('//*[@id="localsubnet"]').clear()
			browser.find_element_by_xpath('//*[@id="localsubnet"]').send_keys(local_ip)
		else:
			browser.find_element_by_xpath('//*[@id="localid_status_1"]').click()
			s1 = Select(browser.find_element_by_xpath('//*[@id="localsubnetobj"]'))
			s1.select_by_visible_text(local_addr_obj)
	# 高级
	if advanced == "yes":
		browser.find_element_by_xpath('//*[@id="conftr_20"]/td[1]/a').click()
		time.sleep(3)
		# 选择xauth模式：
		# if xauth == "server":
		# 	browser.find_element_by_xpath('//*[@id="server_mode_0"]').click()
		# 	s1 = Select(browser.find_element_by_xpath('//*[@id="users"]'))
		# 	s1.select_by_visible_text(user)
		# if xauth == "client":
		# 	browser.find_element_by_xpath('//*[@id="server_mode_1"]').click()
		# 	browser.find_element_by_xpath('//*[@id="user_name"]').send_keys(user_name)
		# 	browser.find_element_by_xpath('//*[@id="auth_password"]').send_keys(user_password)
		# if xauth == "none":
		# 	browser.find_element_by_xpath('//*[@id="server_mode_2"]').click()
		# ike提议
		# 第一阶段提议
		if mode == "main":
			browser.find_element_by_xpath('//*[@id="mode_0"]').click()
		else:
			browser.find_element_by_xpath('//*[@id="mode_1"]').click()
		# 选择加密算法
		s1 = Select(browser.find_element_by_xpath('//*[@id="encry_alg"]'))
		s1.select_by_visible_text(encry_alg_div)
		# 选择认证算法
		s1 = Select(browser.find_element_by_xpath('//*[@id="auth_alg"]'))
		s1.select_by_visible_text(auth_alg)
		# 选择DH组
		s1 = Select(browser.find_element_by_xpath('//*[@id="dh_group"]'))
		s1.select_by_visible_text(dh_group)
		# ike sa有效时间
		browser.find_element_by_xpath('//*[@id="ike_sa_lifetime"]').clear()
		browser.find_element_by_xpath('//*[@id="ike_sa_lifetime"]').send_keys(ike_sa_lifetime)
		# 第二阶段提议
		if ah == "yes":
			if (browser.find_element_by_xpath('//*[@id="using_ah_protocol"]').is_selected()) is True:
				pass
			else:
				browser.find_element_by_xpath('//*[@id="using_ah_protocol"]').click()
			s1 = Select(browser.find_element_by_xpath('//*[@id="ah_auth_alg"]'))
			s1.select_by_visible_text(ah_auth_alg)
		else:
			if (browser.find_element_by_xpath('//*[@id="using_ah_protocol"]').is_selected()) is True:
				browser.find_element_by_xpath('//*[@id="using_ah_protocol"]').click()
		if esp == 'yes':
			if (browser.find_element_by_xpath('//*[@id="using_esp_protocol"]').is_selected()) is True:
				pass
			else:
				browser.find_element_by_xpath('//*[@id="using_esp_protocol"]').click()
			s1 = Select(browser.find_element_by_xpath('//*[@id="esp_encry_alg"]'))
			s1.select_by_visible_text(esp_encry_alg)
			s2 = Select(browser.find_element_by_xpath('//*[@id="esp_auth_alg"]'))
			s2.select_by_visible_text(esp_auth_alg)
		else:
			if (browser.find_element_by_xpath('//*[@id="using_esp_protocol"]').is_selected()) is True:
				browser.find_element_by_xpath('//*[@id="using_esp_protocol"]').click()

		if ip_compression == 'yes':
			if (browser.find_element_by_xpath('//*[@id="enable_ip_compression"]').is_selected()) is True:
				pass
			else:
				browser.find_element_by_xpath('//*[@id="enable_ip_compression"]').click()
		else:
			if (browser.find_element_by_xpath('//*[@id="enable_ip_compression"]').is_selected()) is True:
				browser.find_element_by_xpath('//*[@id="enable_ip_compression"]').click()

		if pfs == "yes":
			if (browser.find_element_by_xpath('//*[@id="enable_pfs"]').is_selected()) is True:
				pass
			else:
				browser.find_element_by_xpath('//*[@id="enable_pfs"]').click()
			s1 = Select(browser.find_element_by_xpath('//*[@id="pfs_group"]'))
			s1.select_by_visible_text(pfs_group)
		else:
			if (browser.find_element_by_xpath('//*[@id="enable_pfs"]').is_selected()) is True:
				browser.find_element_by_xpath('//*[@id="enable_pfs"]').click()
		# ipsec sa有效时间
		if ipsec_sa == 'time':
			browser.find_element_by_xpath('//*[@id="ipsec_sa_lifetime_0"]').click()
			browser.find_element_by_xpath('//*[@id="time"]').clear()
			browser.find_element_by_xpath('//*[@id="time"]').send_keys(ipsec_sa_lifetime)
		if ipsec_sa == 'data':
			browser.find_element_by_xpath('//*[@id="ipsec_sa_lifetime_1"]').click()
			browser.find_element_by_xpath('//*[@id="bytes"]').clear()
			browser.find_element_by_xpath('//*[@id="bytes"]').send_keys(data)

		# if tunnel == "yes": //*[@id="ipsec_sa_lifetime_1"]
		# 	if (browser.find_element_by_xpath('//*[@id="redundant_tunnel"]').is_selected()) is True:
		# 		pass
		# 	else:
		# 		browser.find_element_by_xpath('//*[@id="redundant_tunnel"]').click()
		# 	s1 = Select(browser.find_element_by_xpath('//*[@id="redundant_tunnel_pl"]'))
		# 	s1.select_by_visible_text(tunnel_pl)
		# else:
		# 	if (browser.find_element_by_xpath('//*[@id="redundant_tunnel"]').is_selected()) is True:
		# 		browser.find_element_by_xpath('//*[@id="redundant_tunnel"]').click()
		# 是否协商
		# if start_negotiation == 'yes':
		# 	if (browser.find_element_by_xpath('//*[@id="start_negotiation_immediately"]').is_selected()) is True:
		# 		pass
		# 	else:
		# 		browser.find_element_by_xpath('//*[@id="start_negotiation_immediately"]').click()
		# else:
		# 	if (browser.find_element_by_xpath('//*[@id="start_negotiation_immediately"]').is_selected()) is True:
		# 		browser.find_element_by_xpath('//*[@id="start_negotiation_immediately"]').click()
		# 	browser.find_element_by_xpath('//*[@id="start_negotiation_immediately"]').click() //*[@id="btn_save"]
		if return1 == "yes":
			browser.find_element_by_xpath('//*[@id="container_inner"]/div/div[2]/div[2]/div/input').click()
		print("2222222222222222")
	if save == "yes":
		time.sleep(1)
		browser.find_element_by_xpath('//*[@id="btn_save"]').click()
	if cancel == "yes":
		browser.find_element_by_xpath('//*[@id="btn_cancel"]').click()

"""
------------------------------------------RSA与国密版本函数分割线--------------------------------------------------------
"""


# 添加ipsec远程网关-国密
def add_ipsec_remote_gateway_gm(browser, name='ipsec', desc='miaoshu', status='enable', out_interface="",
								out_ip="default",
								remote_gateway='static/dynamic_ip', gateway='10.2.2.82', auth_method='证书',
								localid="127.0.0.1", remoteid="127.0.0.1", remote_cert_id_any_switch="yes/no",
								local='local_ip/local_addr_obj', local_ip='30.1.1.0/255.255.255.0',
								local_addr_obj='any',
								remote='remote_ip/remote_addr_obj', remote_ip='20.1.1.0/255.255.255.0',
								remote_addr_obj='any', ipsec_super_net_switch="no",
								advanced='no',
								encry_alg_div='3des', auth_alg='sha1',
								ike_sa_lifetime='86400',
								ah='no', ah_auth_alg='',
								esp='yes', esp_encry_alg='aes128', esp_auth_alg='sha1',
								ipsec_sa='time/data', ipsec_sa_lifetime='86400', data='',
								tunnel='yes/no', tunnel_pl='', start_negotiation='yes', return1='yes',
								save='yes/no', cancel='yes/no'):
	into_fun(browser, menu=远程网关)
	time.sleep(1)
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
	# 输入名称
	time.sleep(0.5)
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(name)
	# 输入描述
	browser.find_element_by_xpath('//*[@id="description"]').send_keys(desc)
	if status == "enable":
		pass
	else:
		browser.find_element_by_xpath('//*[@id="status_1"]').click()
	# 选择本地/出接口
	time.sleep(0.5)
	s1 = Select(browser.find_element_by_xpath('//*[@id="localif"]'))
	time.sleep(1)
	s1.select_by_visible_text(out_interface)
	if out_ip != "default":
		select_out_ip = Select(browser.find_element_by_xpath('//*[@id="localip"]'))
		time.sleep(1)
		select_out_ip.select_by_visible_text(out_ip)
	# print(out_interface)
	if remote_gateway == 'static':
		# time.sleep(1)
		browser.find_element_by_xpath('//*[@id="gateway"]').send_keys(gateway)
	else:
		time.sleep(1)
		browser.find_element_by_xpath('//*[@id="gwtype_1"]').click()
	# 选择认证方法
	s1 = Select(browser.find_element_by_xpath('//*[@id="auth_method"]'))
	s1.select_by_visible_text(auth_method)
	# 输入本地证书ID
	browser.find_element_by_xpath('//*[@id="localid"]').send_keys(localid)
	# 输入对端证书ID
	browser.find_element_by_xpath('//*[@id="remoteid"]').send_keys(remoteid)
	# 对远端ID any操作
	if remote_cert_id_any_switch == "yes":
		if (browser.find_element_by_xpath('//*[@id="ckany"]').is_selected()) is True:
			pass
		else:
			browser.find_element_by_xpath('//*[@id="ckany"]').click()
	else:
		if (browser.find_element_by_xpath('//*[@id="ckany"]').is_selected()) is False:
			pass
		else:
			browser.find_element_by_xpath('//*[@id="ckany"]').click()
	# 输入本地保护地址
	if local == 'local_ip':
		browser.find_element_by_xpath('//*[@id="localid_status_0"]').click()
		browser.find_element_by_xpath('//*[@id="localsubnet"]').send_keys(local_ip)
	else:
		browser.find_element_by_xpath('//*[@id="localid_status_1"]').click()
		s1 = Select(browser.find_element_by_xpath('//*[@id="localsubnetobj"]'))
		s1.select_by_visible_text(local_addr_obj)
	# 输入对端保护地址
	if remote == 'remote_ip':
		browser.find_element_by_xpath('//*[@id="remoteid_status_0"]').click()
		browser.find_element_by_xpath('//*[@id="remotesubnet"]').send_keys(remote_ip)
	else:
		browser.find_element_by_xpath('//*[@id="remoteid_status_1"]').click()
		s1 = Select(browser.find_element_by_xpath('//*[@id="remotesubnetobj"]'))
		s1.select_by_visible_text(remote_addr_obj)
	# 对子网聚合操作
	if ipsec_super_net_switch == "yes":
		if (browser.find_element_by_xpath('//*[@id="clientwithin"]').is_selected()) is True:
			pass
		else:
			browser.find_element_by_xpath('//*[@id="clientwithin"]').click()
	else:
		if (browser.find_element_by_xpath('//*[@id="clientwithin"]').is_selected()) is False:
			pass
		else:
			browser.find_element_by_xpath('//*[@id="clientwithin"]').click()
	# 高级
	if advanced == "yes":
		browser.find_element_by_xpath('//*[@id="conftr_31"]/td[1]/a').click()
		time.sleep(1)
		# ike提议
		# 第一阶段提议
		# 选择加密算法
		s1 = Select(browser.find_element_by_xpath('//*[@id="encry_alg"]'))
		s1.select_by_visible_text(encry_alg_div)
		# 选择认证算法
		s1 = Select(browser.find_element_by_xpath('//*[@id="auth_alg"]'))
		s1.select_by_visible_text(auth_alg)
		# ike sa有效时间
		browser.find_element_by_xpath('//*[@id="ike_sa_lifetime"]').clear()
		browser.find_element_by_xpath('//*[@id="ike_sa_lifetime"]').send_keys(ike_sa_lifetime)
		# 第二阶段提议
		if ah == "yes":
			if (browser.find_element_by_xpath('//*[@id="using_ah_protocol"]').is_selected()) is True:
				pass
			else:
				browser.find_element_by_xpath('//*[@id="using_ah_protocol"]').click()
			s1 = Select(browser.find_element_by_xpath('//*[@id="ah_auth_alg"]'))
			s1.select_by_visible_text(ah_auth_alg)
		else:
			if (browser.find_element_by_xpath('//*[@id="using_ah_protocol"]').is_selected()) is True:
				browser.find_element_by_xpath('//*[@id="using_ah_protocol"]').click()
		if esp == 'yes':
			if (browser.find_element_by_xpath('//*[@id="using_esp_protocol"]').is_selected()) is True:
				pass
			else:
				browser.find_element_by_xpath('//*[@id="using_esp_protocol"]').click()
			s1 = Select(browser.find_element_by_xpath('//*[@id="esp_encry_alg"]'))
			s1.select_by_visible_text(esp_encry_alg)
			s2 = Select(browser.find_element_by_xpath('//*[@id="esp_auth_alg"]'))
			s2.select_by_visible_text(esp_auth_alg)
		else:
			if (browser.find_element_by_xpath('//*[@id="using_esp_protocol"]').is_selected()) is True:
				browser.find_element_by_xpath('//*[@id="using_esp_protocol"]').click()

		# ipsec sa有效时间 //*[@id="ipsec_sa_lifetime_div"]/td[2]/span[1]
		if ipsec_sa == 'time':
			browser.find_element_by_xpath('//*[@id="ipsec_sa_lifetime_0"]').click()
			browser.find_element_by_xpath('//*[@id="time"]').clear()
			browser.find_element_by_xpath('//*[@id="time"]').send_keys(ipsec_sa_lifetime)

		if ipsec_sa == 'data':
			browser.find_element_by_xpath('//*[@id="ipsec_sa_lifetime_1"]').click()
			browser.find_element_by_xpath('//*[@id="ipsec_sa_lifetime_1"]').click()
			browser.find_element_by_xpath('//*[@id="bytes"]').click()
			browser.find_element_by_xpath('//*[@id="bytes"]').clear()
			browser.find_element_by_xpath('//*[@id="bytes"]').click()
			browser.find_element_by_xpath('//*[@id="bytes"]').send_keys(data)
		if tunnel == "yes":
			if (browser.find_element_by_xpath('//*[@id="redundant_tunnel"]').is_selected()) is True:
				pass
			else:
				browser.find_element_by_xpath('//*[@id="redundant_tunnel"]').click()
			s1 = Select(browser.find_element_by_xpath('//*[@id="redundant_tunnel_pl"]'))
			s1.select_by_visible_text(tunnel_pl)
		else:
			if (browser.find_element_by_xpath('//*[@id="redundant_tunnel"]').is_selected()) is True:
				browser.find_element_by_xpath('//*[@id="redundant_tunnel"]').click()
		# 是否协商
		if start_negotiation == 'yes':
			if (browser.find_element_by_xpath('//*[@id="start_negotiation_immediately"]').is_selected()) is True:
				pass
			else:
				browser.find_element_by_xpath('//*[@id="start_negotiation_immediately"]').click()
		else:
			if (browser.find_element_by_xpath('//*[@id="start_negotiation_immediately"]').is_selected()) is True:
				browser.find_element_by_xpath('//*[@id="start_negotiation_immediately"]').click()
			browser.find_element_by_xpath('//*[@id="start_negotiation_immediately"]').click()
		if return1 == "yes":
			browser.find_element_by_xpath('//*[@id="container_inner"]/div/div[2]/div[2]/div/input').click()
	if save == "yes":
		browser.find_element_by_xpath('//*[@id="btn_save"]').click()
	if cancel == "yes":
		browser.find_element_by_xpath('//*[@id="btn_cancel"]').click()


# 编辑ipsec远程网关-国密
def edit_ipsec_remote_gateway_gm(browser, name='ipsec', desc='miaoshu/unmodify', status='enable/unmodify',
								 out_interface="/unmodify", out_ip="default/unmodify",
								 remote_gateway='static/dynamic_ip/unmodify', gateway='10.2.2.82/unmodify',
								 auth_method='证书/unmodify',
								 localid="127.0.0.1/unmodify", remoteid="127.0.0.1/unmodify",
								 remote_cert_id_any_switch="yes/no/unmodify",
								 local='local_ip/local_addr_obj/unmodify', local_ip='30.1.1.0/255.255.255.0/unmodify',
								 local_addr_obj='any/unmodify',
								 remote='remote_ip/remote_addr_obj/unmodify',
								 remote_ip='20.1.1.0/255.255.255.0/unmodify',
								 remote_addr_obj='any/unmodify', ipsec_super_net_switch="no/unmodify",
								 advanced='no/unmodify',
								 encry_alg_div='3des/unmodify', auth_alg='sha1/unmodify',
								 ike_sa_lifetime='86400/unmodify',
								 ah='no/unmodify', ah_auth_alg='/unmodify',
								 esp='yes/unmodify', esp_encry_alg='aes128/unmodify', esp_auth_alg='sha1/unmodify',
								 ipsec_sa='time/data/unmodify', ipsec_sa_lifetime='86400/unmodify', data='/unmodify',
								 tunnel='yes/no/unmodify', tunnel_pl='/unmodify', start_negotiation='yes/unmodify',
								 return1='yes/unmodify',
								 save='yes/no/unmodify', cancel='yes/no/unmodify'):
	into_fun(browser, menu=远程网关)
	time.sleep(1)
	n = 2
	getname = browser.find_element_by_xpath(
		'//*[@id="vpn_remote_tunnel_table"]/tbody/tr[' + str(n) + ']/td[2]').text.replace(' ', '')
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath(
			'//*[@id="vpn_remote_tunnel_table"]/tbody/tr[' + str(n) + ']/td[2]').text.replace(' ', '')
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="vpn_remote_tunnel_table"]/tbody/tr[' + str(n) + ']/td[8]/a[1]/img').click()
	# 输入描述
	if "unmodify" not in desc:
		browser.find_element_by_xpath('//*[@id="description"]').clear()
		browser.find_element_by_xpath('//*[@id="description"]').send_keys(desc)

	if "unmodify" not in status:
		time.sleep(1)
		if status == "enable":
			pass
		else:
			browser.find_element_by_xpath('//*[@id="status_1"]').click()
	# 选择本地/出接口 //*[@id="status_1"]
	if "unmodify" not in out_interface:
		time.sleep(0.5)
		s1 = Select(browser.find_element_by_xpath('//*[@id="localif"]'))
		time.sleep(1)
		s1.select_by_visible_text(out_interface)
	# 选择本地ip
	if out_ip != "default/unmodify":
		select_out_ip = Select(browser.find_element_by_xpath('//*[@id="localip"]'))
		time.sleep(1)
		select_out_ip.select_by_visible_text(out_ip)
	# print(out_interface)
	# 选择远程网关 静态或者动态
	if "unmodify" not in remote_gateway:
		if remote_gateway == 'static':
			# time.sleep(1)
			browser.find_element_by_xpath('//*[@id="gateway"]').clear()
			browser.find_element_by_xpath('//*[@id="gateway"]').send_keys(gateway)
		else:
			time.sleep(1)
			browser.find_element_by_xpath('//*[@id="gwtype_1"]').click()
	# 选择认证方法
	if "unmodify" not in auth_method:
		s1 = Select(browser.find_element_by_xpath('//*[@id="auth_method"]'))
		s1.select_by_visible_text(auth_method)
	# 输入本地证书ID
	if "unmodify" not in localid:
		browser.find_element_by_xpath('//*[@id="local_cert_div"]/td[2]/input').clear()
		browser.find_element_by_xpath('//*[@id="local_cert_div"]/td[2]/input').send_keys(localid)
	# 输入对端证书ID
	if "unmodify" not in remoteid:
		browser.find_element_by_xpath('//*[@id="remoteid"]').clear()
		browser.find_element_by_xpath('//*[@id="remoteid"]').send_keys(remoteid)
	# 对远端ID any操作
	if "unmodify" not in remote_cert_id_any_switch:
		if remote_cert_id_any_switch == "yes":
			if (browser.find_element_by_xpath('//*[@id="ckany"]').is_selected()) is True:
				pass
			else:
				browser.find_element_by_xpath('//*[@id="ckany"]').click()
		else:
			if (browser.find_element_by_xpath('//*[@id="ckany"]').is_selected()) is False:
				pass
			else:
				browser.find_element_by_xpath('//*[@id="ckany"]').click()
	# 输入本地保护地址
	if "unmodify" not in local_ip or "unmodify" not in local_addr_obj:
		if local == 'local_ip':
			browser.find_element_by_xpath('//*[@id="localid_status_0"]').click()
			browser.find_element_by_xpath('//*[@id="localsubnet"]').clear()
			browser.find_element_by_xpath('//*[@id="localsubnet"]').send_keys(local_ip)
		else:
			browser.find_element_by_xpath('//*[@id="localid_status_1"]').click()
			s1 = Select(browser.find_element_by_xpath('//*[@id="localsubnetobj"]'))
			s1.select_by_visible_text(local_addr_obj)
	# 输入对端保护地址
	if "unmodify" not in remote_ip or "unmodify" not in remote_addr_obj:
		if remote == 'remote_ip':
			browser.find_element_by_xpath('//*[@id="remoteid_status_0"]').click()
			browser.find_element_by_xpath('//*[@id="remotesubnet"]').clear()
			browser.find_element_by_xpath('//*[@id="remotesubnet"]').send_keys(remote_ip)
		else:
			browser.find_element_by_xpath('//*[@id="remoteid_status_1"]').click()
			s1 = Select(browser.find_element_by_xpath('//*[@id="remotesubnetobj"]'))
			s1.select_by_visible_text(remote_addr_obj)
	# 对子网聚合操作
	if "unmodify" not in ipsec_super_net_switch:
		if ipsec_super_net_switch == "yes":
			if (browser.find_element_by_xpath('//*[@id="clientwithin"]').is_selected()) is True:
				pass
			else:
				browser.find_element_by_xpath('//*[@id="clientwithin"]').click()
		else:
			if (browser.find_element_by_xpath('//*[@id="clientwithin"]').is_selected()) is False:
				pass
			else:
				browser.find_element_by_xpath('//*[@id="clientwithin"]').click()
	# 高级
	if advanced == "yes":
		time.sleep(2.5)
		browser.find_element_by_xpath('//*[@id="conftr_31"]/td[1]/a').click()
		time.sleep(1)
		# ike提议
		# 第一阶段提议
		# 选择加密算法
		if "unmodify" not in encry_alg_div:
			s1 = Select(browser.find_element_by_xpath('//*[@id="encry_alg"]'))
			s1.select_by_visible_text(encry_alg_div)
		# 选择认证算法
		if "unmodify" not in auth_alg:
			s1 = Select(browser.find_element_by_xpath('//*[@id="auth_alg"]'))
			s1.select_by_visible_text(auth_alg)
		# ike sa有效时间
		if "unmodify" not in ike_sa_lifetime:
			browser.find_element_by_xpath('//*[@id="ike_sa_lifetime"]').clear()
			browser.find_element_by_xpath('//*[@id="ike_sa_lifetime"]').send_keys(ike_sa_lifetime)
		# 第二阶段提议
		if "unmodify" not in ah or "unmodify" not in esp:
			if ah == "yes":
				if (browser.find_element_by_xpath('//*[@id="using_ah_protocol"]').is_selected()) is True:
					pass
				else:
					browser.find_element_by_xpath('//*[@id="using_ah_protocol"]').click()
				s1 = Select(browser.find_element_by_xpath('//*[@id="ah_auth_alg"]'))
				s1.select_by_visible_text(ah_auth_alg)
			else:
				if (browser.find_element_by_xpath('//*[@id="using_ah_protocol"]').is_selected()) is True:
					browser.find_element_by_xpath('//*[@id="using_ah_protocol"]').click()
			if esp == 'yes':
				if (browser.find_element_by_xpath('//*[@id="using_esp_protocol"]').is_selected()) is True:
					pass
				else:
					browser.find_element_by_xpath('//*[@id="using_esp_protocol"]').click()
				s1 = Select(browser.find_element_by_xpath('//*[@id="esp_encry_alg"]'))
				s1.select_by_visible_text(esp_encry_alg)
				s2 = Select(browser.find_element_by_xpath('//*[@id="esp_auth_alg"]'))
				s2.select_by_visible_text(esp_auth_alg)
			else:
				if (browser.find_element_by_xpath('//*[@id="using_esp_protocol"]').is_selected()) is True:
					browser.find_element_by_xpath('//*[@id="using_esp_protocol"]').click()

		# ipsec sa有效时间
		if "unmodify" not in ipsec_sa_lifetime or "unmodify" not in data:
			if ipsec_sa == 'time':
				browser.find_element_by_xpath('//*[@id="ipsec_sa_lifetime_0"]').click()
				browser.find_element_by_xpath('//*[@id="time"]').clear()
				# time.sleep(0.5)
				browser.find_element_by_xpath('//*[@id="time"]').send_keys(ipsec_sa_lifetime)
			if ipsec_sa == 'data':
				browser.find_element_by_xpath('//*[@id="ipsec_sa_lifetime_1"]').clear()
				browser.find_element_by_xpath('//*[@id="ipsec_sa_lifetime_1"]').click()
				browser.find_element_by_xpath('//*[@id="bytes"]').send_keys(data)
		if "unmodify" not in tunnel:
			if tunnel == "yes":
				if (browser.find_element_by_xpath('//*[@id="redundant_tunnel"]').is_selected()) is True:
					pass
				else:
					browser.find_element_by_xpath('//*[@id="redundant_tunnel"]').click()
				s1 = Select(browser.find_element_by_xpath('//*[@id="redundant_tunnel_pl"]'))
				s1.select_by_visible_text(tunnel_pl)
			else:
				if (browser.find_element_by_xpath('//*[@id="redundant_tunnel"]').is_selected()) is True:
					browser.find_element_by_xpath('//*[@id="redundant_tunnel"]').click()
		# 是否协商
		if "unmodify" not in start_negotiation:
			if start_negotiation == 'yes':
				if (browser.find_element_by_xpath('//*[@id="start_negotiation_immediately"]').is_selected()) is True:
					pass
				else:
					browser.find_element_by_xpath('//*[@id="start_negotiation_immediately"]').click()
			else:
				if (browser.find_element_by_xpath('//*[@id="start_negotiation_immediately"]').is_selected()) is True:
					browser.find_element_by_xpath('//*[@id="start_negotiation_immediately"]').click()
				browser.find_element_by_xpath('//*[@id="start_negotiation_immediately"]').click()
		if return1 == "yes":
			browser.find_element_by_xpath('//*[@id="container_inner"]/div/div[2]/div[2]/div/input').click()
	if save == "yes":
		browser.find_element_by_xpath('//*[@id="btn_save"]').click()
	if cancel == "yes":
		browser.find_element_by_xpath('//*[@id="btn_cancel"]').click()


# 通过隧道名，获取隧道高级设置中的阶段1的加密认证算法或者阶段2的加密认证算法
def get_ipesc_remote_gateway_en_au_gm(browser, name='ipsec', switch="阶段1/阶段2", per2_switch="ESP"):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击虚拟专网
	# browser.find_element_by_xpath(虚拟专网).click()
	# # 点击远程网关
	# browser.find_element_by_xpath(远程网关).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 远程网关)
	# 找到指定的ipsec远程网关并删除//*[@id="vpn_remote_tunnel_table"]/tbody/tr[2]/td[2]
	# //*[@id="vpn_remote_tunnel_table"]/tbody/tr[3]/td[2]
	n = 2
	getname = browser.find_element_by_xpath(
		'//*[@id="vpn_remote_tunnel_table"]/tbody/tr[' + str(n) + ']/td[2]').text.replace(' ', '')
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath(
			'//*[@id="vpn_remote_tunnel_table"]/tbody/tr[' + str(n) + ']/td[2]').text.replace(' ', '')
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="vpn_remote_tunnel_table"]/tbody/tr[' + str(n) + ']/td[8]/a[1]/img').click()
	# 点击高级
	time.sleep(2)
	browser.find_element_by_xpath('//*[@id="conftr_31"]/td[1]/a').click()
	if switch == "阶段1" or switch == "阶段一":
		select_en_per1 = Select(
			browser.find_element_by_xpath('//*[@id="encry_alg"]'))
		en_per1 = select_en_per1.all_selected_options

		select_au_per1 = Select(
			browser.find_element_by_xpath('//*[@id="auth_alg"]'))
		au_per1 = select_au_per1.all_selected_options

		return en_per1[0].text, au_per1[0].text

	if switch == "阶段2" or switch == "阶段二":
		if per2_switch == "ESP":
			select_en_per2 = Select(
				browser.find_element_by_xpath('//*[@id="esp_encry_alg"]'))
			en_per2 = select_en_per2.all_selected_options

			select_au_per2 = Select(
				browser.find_element_by_xpath('//*[@id="esp_auth_alg"]'))
			au_per2 = select_au_per2.all_selected_options

			return en_per2[0].text, au_per2[0].text

		elif per2_switch == "AH":
			select_au_per2 = Select(
				browser.find_element_by_xpath('//*[@id="ah_auth_alg"]'))
			au_per2 = select_au_per2.all_selected_options

			return au_per2[0].text

		else:
			return None


# 通过隧道名，返回立即协商是否开启，返回T/F
def get_ipesc_remote_gateway_start_negotiation_gm(browser, name='ipsec'):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击虚拟专网
	# browser.find_element_by_xpath(虚拟专网).click()
	# # 点击远程网关
	# browser.find_element_by_xpath(远程网关).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 远程网关)
	# 找到指定的ipsec远程网关并删除//*[@id="vpn_remote_tunnel_table"]/tbody/tr[2]/td[2]
	# //*[@id="vpn_remote_tunnel_table"]/tbody/tr[3]/td[2]
	n = 2
	getname = browser.find_element_by_xpath(
		'//*[@id="vpn_remote_tunnel_table"]/tbody/tr[' + str(n) + ']/td[2]').text.replace(' ', '')
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath(
			'//*[@id="vpn_remote_tunnel_table"]/tbody/tr[' + str(n) + ']/td[2]').text.replace(' ', '')
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="vpn_remote_tunnel_table"]/tbody/tr[' + str(n) + ']/td[8]/a[1]/img').click()
	# 点击高级
	time.sleep(1)
	if (browser.find_element_by_xpath('//*[@id="start_negotiation_immediately"]').is_selected()) is True:
		return True
	else:
		return False


# 删除指定的ipsec远程网关
def del_ipsec_remote_gateway_gm(browser, name='ipsec'):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击虚拟专网
	# browser.find_element_by_xpath(虚拟专网).click()
	# # 点击远程网关
	# browser.find_element_by_xpath(远程网关).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 远程网关)
	# 找到指定的ipsec远程网关并删除//*[@id="vpn_remote_tunnel_table"]/tbody/tr[2]/td[2]
	# //*[@id="vpn_remote_tunnel_table"]/tbody/tr[3]/td[2]
	n = 2
	getname = browser.find_element_by_xpath(
		'//*[@id="vpn_remote_tunnel_table"]/tbody/tr[' + str(n) + ']/td[2]').text.replace(' ', '')
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath(
			'//*[@id="vpn_remote_tunnel_table"]/tbody/tr[' + str(n) + ']/td[2]').text.replace(' ', '')
	# 点击删除
	browser.find_element_by_xpath('//*[@id="vpn_remote_tunnel_table"]/tbody/tr[' + str(n) + ']/td[8]/a[2]/img').click()


# 删除全部ipsec远程网关
def del_all_ipsec_remote_gateway_gm(browser):
	into_fun(browser, 远程网关)
	ipsec_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	while ipsec_sum > 0:
		browser.find_element_by_xpath(
			'//*[@id="vpn_remote_tunnel_table"]/tbody/tr[2]/td[8]/a[2]/img').click()
		time.sleep(0.5)
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		time.sleep(0.5)
		ipsec_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)


# 导入国密证书 //*[@id="fileid"]

def import_cert_gm(browser, cert_name=""):
	cert_path = "C:\\Users\\swy22\\Desktop\\"
	into_fun(browser, VPN证书)
	browser.find_element_by_xpath('//*[text()="证书导入"]').click()
	browser.find_element_by_xpath('//*[@id="fileid"]').send_keys(cert_path+cert_name)
	browser.find_element_by_xpath('//*[@id="btn_save"]').click()
	time.sleep(5)
	op_result = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
	return op_result


# 证书请求-生成请求,返回生成证书的信息
def certificate_request(browser, nation="国家", provinces="省份", city="城市", org="组织", department="部门", p_name="主体名称",
						save="yes/no"):
	into_fun(browser, VPN证书)
	if nation != "国家":
		select_nation = Select(
			browser.find_element_by_xpath('//*[@id="container"]/div[2]/div/form/table/tbody/tr[1]/td[2]/select'))
		select_nation.select_by_visible_text(nation)
	if provinces != "省份":
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/div/form/table/tbody/tr[2]/td[2]/input').clear()
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/div/form/table/tbody/tr[2]/td[2]/input').send_keys(
			provinces)
	if city != "城市":
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/div/form/table/tbody/tr[3]/td[2]/input').clear()
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/div/form/table/tbody/tr[3]/td[2]/input').send_keys(
			city)
	if org != "组织":
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/div/form/table/tbody/tr[4]/td[2]/input').clear()
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/div/form/table/tbody/tr[4]/td[2]/input').send_keys(
			org)
	if department != "部门":
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/div/form/table/tbody/tr[5]/td[2]/input').clear()
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/div/form/table/tbody/tr[5]/td[2]/input').send_keys(
			department)
	if p_name != "主体名称":
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/div/form/table/tbody/tr[6]/td[2]/input').clear()
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/div/form/table/tbody/tr[6]/td[2]/input').send_keys(
			p_name)

	browser.find_element_by_xpath('//*[@id="btn_save"]').click()
	time.sleep(0.5)
	if save == "yes":
		browser.switch_to_alert().accept()
		time.sleep(0.5)
		out_cert_content = browser.find_element_by_xpath('//*[@id="container"]/div[3]/pre').text
		out_cert_info_nation = browser.find_element_by_xpath(
			'//*[@id="container"]/div[3]/div/table/tbody/tr[1]/td[2]').text
		out_cert_info_provinces = browser.find_element_by_xpath(
			'//*[@id="container"]/div[3]/div/table/tbody/tr[2]/td[2]').text
		out_cert_info_city = browser.find_element_by_xpath(
			'//*[@id="container"]/div[3]/div/table/tbody/tr[3]/td[2]').text
		out_cert_info_org = browser.find_element_by_xpath(
			'//*[@id="container"]/div[3]/div/table/tbody/tr[4]/td[2]').text
		out_cert_info_department = browser.find_element_by_xpath(
			'//*[@id="container"]/div[3]/div/table/tbody/tr[5]/td[2]').text
		out_cert_info_p_name = browser.find_element_by_xpath(
			'//*[@id="container"]/div[3]/div/table/tbody/tr[6]/td[2]').text
		return out_cert_content, out_cert_info_nation, out_cert_info_provinces, out_cert_info_city, out_cert_info_org, out_cert_info_department, out_cert_info_p_name
	else:
		browser.switch_to_alert().dismiss()


# 根据隧道名，在监控中返回隧道的所有状态，返回为数组：（index,名字，网关，拓扑，开始时间，状态），如果没有找到隧道就返回None
def get_ipsec_station_byname(browser, ipsec_name=""):
	into_fun(browser, menu=监控)
	browser.find_element_by_xpath('//*[@id="current"]/a/span').click()
	time.sleep(0.5)
	sum1 = browser.find_element_by_xpath('//*[@id="rules_count"]').text
	# //*[@id="vpn_monitor_static_tunnel_table"]/tbody/tr[2]/td[1]
	# //*[@id="vpn_monitor_static_tunnel_table"]/tbody/tr[2]/td[6]/text()
	# getname = "1"
	for x in range(2, 2 + int(sum1)):
		getname = browser.find_element_by_xpath(
			'//*[@id="vpn_monitor_static_tunnel_table"]/tbody/tr[' + str(x) + ']/td[2]').text.replace(' ', '')
		if getname == ipsec_name:
			out_id = browser.find_element_by_xpath(
				'//*[@id="vpn_monitor_static_tunnel_table"]/tbody/tr[' + str(x) + ']/td[1]').text.replace(' ', '')
			out_name = browser.find_element_by_xpath(
				'//*[@id="vpn_monitor_static_tunnel_table"]/tbody/tr[' + str(x) + ']/td[2]').text.replace(' ', '')
			out_gw = browser.find_element_by_xpath(
				'//*[@id="vpn_monitor_static_tunnel_table"]/tbody/tr[' + str(x) + ']/td[3]').text.replace(' ', '')
			out_topo = browser.find_element_by_xpath(
				'//*[@id="vpn_monitor_static_tunnel_table"]/tbody/tr[' + str(x) + ']/td[4]').text.replace(' ', '')
			out_start_time = browser.find_element_by_xpath(
				'//*[@id="vpn_monitor_static_tunnel_table"]/tbody/tr[' + str(x) + ']/td[5]').text.replace(' ', '')
			out_station = browser.find_element_by_xpath(
				'//*[@id="vpn_monitor_static_tunnel_table"]/tbody/tr[' + str(x) + ']/td[6]').text.replace(' ', '')
			return out_id, out_name, out_gw, out_topo, out_start_time, out_station
	else:
		return None


# 根据隧道名，在监控中断开隧道
def stop_ipsec_byname(browser, ipsec_name=""):
	into_fun(browser, menu=监控)
	browser.find_element_by_xpath('//*[@id="current"]/a/span').click()
	time.sleep(0.5)
	sum1 = browser.find_element_by_xpath('//*[@id="rules_count"]').text
	# //*[@id="vpn_monitor_static_tunnel_table"]/tbody/tr[2]/td[1]
	# //*[@id="vpn_monitor_static_tunnel_table"]/tbody/tr[2]/td[6]/text()
	# getname = "1"
	for x in range(2, 2 + int(sum1)):
		getname = browser.find_element_by_xpath(
			'//*[@id="vpn_monitor_static_tunnel_table"]/tbody/tr[' + str(x) + ']/td[2]').text.replace(' ', '')
		if getname == ipsec_name:
			browser.find_element_by_xpath(
				'//*[@id="vpn_monitor_static_tunnel_table"]/tbody/tr[' + str(x) + ']/td[7]/a/img').click()
			time.sleep(0.5)
			browser.find_element_by_xpath('//*[@id="link_but"]').click()
			break


# 随机数生成,并返回数组（随机数列表，输出长度）
def create_random_num(browser, num_len=1):
	into_fun(browser, 随机数生成)
	browser.find_element_by_xpath('//*[@id="random_math"]').clear()
	browser.find_element_by_xpath('//*[@id="random_math"]').send_keys(num_len)
	browser.find_element_by_xpath('/html/body/div[2]/input[2]').click()
	time.sleep(0.5)
	random_num = browser.find_element_by_xpath('/html/body/div[2]/div[2]').text
	# print(len(random_num))
	# if len(random_num)
	out_len = (len(random_num) - (num_len - 1)) // 2
	return random_num, out_len
