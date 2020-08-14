
import sys
import os
import time
from os.path import dirname, abspath
from page_obj.common.ssh import *
from page_obj.common.rail import *
from page_obj.scg.scg_button import *
from page_obj.scg.scg_def_ifname_OEM import *
# from page_obj.scg.scg_def import check_alert
# from page_obj.scg.scg_def import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))


#   该方法用来确认元素（XPATH）是否存在，如果存在返回flag=true，否则返回false
def is_element_exist(driver, element, type="xpath"):

	browser = driver
	if type == "xpath":
		try:
			browser.find_element_by_xpath(element)
			return True
		except:
			return False


# 截图功能
def screenshot(driver):
	try:
		s = os.path.basename(sys.argv[0])
		s1 = s.split(".", 1)

		path = os.path.join('..', 'pic', str(s1[0])+"bai.png")
		print(path)
		picture_url = driver.save_screenshot(path)
		print("%s ：截图成功！！！" % picture_url)
	except BaseException as msg:
		print("%s ：截图失败！！！" % msg)

		# print sys.argv  # 输入参数列表
		# print sys.argv[0]  # 第0个就是这个python文件本身的路径（全路径）
		# print os.path.basename(sys.argv[0])  # 当前文件名名称
		# print os.path.basename(__file__)  # 当前文件名名称


# 封装导航栏,针对旧版本(安全通讯平台)，op1:第一级目录 op2：第二级目录 op3:第三级目录,op2传参的样式为"display_日志记录"
# def into_fun_old(browser, op1="", op2="obviously", op3=""):
# 	# 切换到默认frame
# 	browser.switch_to.default_content()
# 	# 切换到左侧frame
# 	browser.switch_to.frame("lefttree")
# 	# 点击第一级菜单目录
# 	browser.find_element_by_xpath(op1).click()
# 	# 判断是否需要展开第二级目录，如果op2参数没有被传参，我们认为不需要展开二级菜单
# 	if op2 == "obviously":
# 		browser.find_element_by_xpath(op3).click()
# 		# 定位到默认frame
# 		browser.switch_to.default_content()
# 		# 定位到内容frame
# 		browser.switch_to.frame("content")
# 		time.sleep(1)
# 	else:
# 		if not browser.find_element_by_xpath(op2).is_displayed():
# 			# 如果不可见，点击加号，展开元素
# 			time.sleep(2)
# 			browser.find_element_by_xpath(op2[:-2]+"div").click()
# 		# 点击dhcp设定
# 		browser.find_element_by_xpath(op3).click()
# 		# 定位到默认frame
# 		browser.switch_to.default_content()
# 		# 定位到内容frame
# 		browser.switch_to.frame("content")
# 		time.sleep(1)


# 再次封装导航，只需传入最后一级目录名即可,参数中的英文均为小写,
def into_fun(browser, menu):
	browser.refresh()
	if oem_name == "ICF":

		# print("进入ICF导航")
		try:
			# print("Alert exists")
			alert_info = "init"
			while alert_info is not None:
				alert = browser.switch_to_alert()
				alert_info = alert.text
				print(alert_info)
				alert.accept()
		except:
			# print("无警告，点击返回")
			try:
				browser.find_element_by_xpath('// *[ @ id = "link_but"]').click()
			except:
				# print("无点击返回")
				pass
		browser.switch_to.default_content()
		# 定位到左侧frame
		browser.switch_to.frame("lefttree")

		if menu in [系统状态, 管理员, 系统升级, Web证书, 重启系统, 系统信息, 时间设定, DNS,
		            配置文件, 高可用性, SNMP设置, SNMP_Trap, 网络诊断, 服务器诊断]:
			browser.find_element_by_name(系统).click()
			if menu == 系统状态:
				browser.find_element_by_name(menu).click()
			elif menu in [管理员, 系统升级, Web证书, 重启系统]:
				if not browser.find_element_by_xpath(display_系统管理).is_displayed():
					# 如果不可见，点击加号，展开元素
					browser.find_element_by_name(系统管理).click()
				browser.find_element_by_name(menu).click()

			elif menu in [系统信息,  时间设定, DNS, 配置文件, 高可用性, SNMP设置, SNMP_Trap]:
				if not browser.find_element_by_xpath(display_配置).is_displayed():
					# 如果不可见，点击加号，展开元素
					browser.find_element_by_name(配置).click()
				browser.find_element_by_name(menu).click()

			elif menu in [网络诊断, 服务器诊断]:
				if not browser.find_element_by_xpath(display_诊断工具).is_displayed():
					# 如果不可见，点击加号，展开元素
					browser.find_element_by_name(诊断工具).click()
				browser.find_element_by_name(menu).click()

		elif menu in [物理接口, 子接口, 网桥, 静态路由, 策略路由, OSPF, ISP自动选择, 多网关组, 路由监控, DHCP设定, DHCP租用列表,
		              ARP列表, 桥MAC表, IPv6邻居列表, IPv6隧道]:
			browser.find_element_by_name(网络).click()
			if menu in [物理接口, 子接口, 网桥]:
				if not browser.find_element_by_xpath(display_接口设置).is_displayed():
					# 如果不可见，点击加号，展开元素
					browser.find_element_by_name(接口设置).click()
				browser.find_element_by_name(menu).click()
			elif menu in [静态路由, 策略路由, OSPF, ISP自动选择, 多网关组, 路由监控]:
				if not browser.find_element_by_xpath(display_路由).is_displayed():
					# 如果不可见，点击加号，展开元素
					browser.find_element_by_name(路由).click()
				browser.find_element_by_name(menu).click()
			elif menu in [DHCP设定, DHCP租用列表]:
				if not browser.find_element_by_xpath(display_DHCP).is_displayed():
					# 如果不可见，点击加号，展开元素
					browser.find_element_by_name(DHCP).click()
				browser.find_element_by_name(menu).click()
			elif menu in [ARP列表, 桥MAC表, IPv6邻居列表, IPv6隧道]:
				if not browser.find_element_by_xpath(display_MAC).is_displayed():
					# 如果不可见，点击加号，展开元素
					browser.find_element_by_name(MAC).click()
				browser.find_element_by_name(menu).click()

		elif menu in [模式切换, 自定义规则, 机器学习, 安全事件, 工业漏洞, ARP防护, 访问策略, IPV6访问策略, 地址, 地址范围,
		              地址组, IPv6地址, IPv6地址范围, IPv6地址组, 计划任务, 区域, 预定义服务, 自定义服务, 服务组, 目标地址转换,
		              源地址转换, 负载均衡]:
			browser.find_element_by_name(安全策略).click()
			if menu in [模式切换, 自定义规则, 机器学习, 安全事件, 工业漏洞, ARP防护, 访问策略, IPV6访问策略]:
				if not browser.find_element_by_xpath(display_工业防护策略).is_displayed():
					# 如果不可见，点击加号，展开元素
					browser.find_element_by_name(工业防护策略).click()
				browser.find_element_by_name(menu).click()
			elif menu in [地址, 地址范围, 地址组, IPv6地址, IPv6地址范围, IPv6地址组, 计划任务, 区域, 预定义服务, 自定义服务,
			              服务组]:
				if not browser.find_element_by_xpath(display_对象).is_displayed():
					# 如果不可见，点击加号，展开元素
					browser.find_element_by_name(对象).click()
				browser.find_element_by_name(menu).click()
			elif menu in [目标地址转换, 源地址转换, 负载均衡]:
				if not browser.find_element_by_xpath(display_地址转换).is_displayed():
					# 如果不可见，点击加号，展开元素
					browser.find_element_by_name(地址转换).click()
				browser.find_element_by_name(menu).click()

		elif menu in [主机标识, 应用加密, 手动密钥, 远程网关, 远程访问, 监控, CA证书]:
			browser.find_element_by_name(虚拟专网).click()
			browser.find_element_by_name(menu).click()

		elif menu in [Anti_DDoS设置, Anti_DDoS用户配置, Anti_DDoS规则列表, Anti_DDoS黑_白名单]:
			browser.find_element_by_name(DDoS防护).click()
			browser.find_element_by_name(menu).click()

		elif menu in [用户配置, 本地用户, 认证组, 认证服务器, 认证用户设置, 认证监控]:
			browser.find_element_by_name(认证用户).click()
			browser.find_element_by_name(menu).click()

		elif menu in [日志统计, 日志服务器, 日志过滤, 日志格式, 日志告警, 管理日志, 系统日志, 安全日志, 流量日志]:
			browser.find_element_by_name(日志).click()
			if menu == 日志统计:
				browser.find_element_by_name(menu).click()
			elif menu in [日志服务器, 日志过滤, 日志格式, 日志告警]:
				if not browser.find_element_by_xpath(display_日志设置).is_displayed():
					# 如果不可见，点击加号，展开元素
					browser.find_element_by_name(日志设置).click()
				browser.find_element_by_name(menu).click()
			elif menu in [管理日志, 系统日志, 安全日志, 流量日志]:
				if not browser.find_element_by_xpath(display_日志记录).is_displayed():
					# 如果不可见，点击加号，展开元素
					browser.find_element_by_name(日志记录).click()
				browser.find_element_by_name(menu).click()
				time.sleep(2)

		elif menu in [报表设置, 接口统计报表, 流量排行报表, 会话监控报表, 系统状态报表, 事件统计报表, 会话表, Anti_DDoS会话数,
		              Anti_DDoS会话速率, Anti_DDoS数据包速率, Top_N, 来源IP统计]:
			browser.find_element_by_name(报表).click()
			if menu in [报表设置, 接口统计报表, 流量排行报表, 会话监控报表, 系统状态报表, 事件统计报表, 会话表]:
				browser.find_element_by_name(menu).click()
			elif menu in [Anti_DDoS会话数, Anti_DDoS会话速率, Anti_DDoS数据包速率, Top_N, 来源IP统计]:
				if not browser.find_element_by_xpath(display_DDoS防护).is_displayed():
					# 如果不可见，点击加号，展开元素
					browser.find_element_by_name(DDoS防护).click()
				browser.find_element_by_name(menu).click()

		else:
			print("导航菜单未知，请检查是否输入错误，或切换函数。")

		browser.switch_to.default_content()
		# 定位到内容frame
		time.sleep(1)
		try:
			time.sleep(1)
			browser.switch_to.frame("content")
		except Exception as err:
			print(err)
			print("导航处进入，没有找到frame")

	elif oem_name == "SCG" or oem_name == "万兆测试":
		# print("进入SCG导航")
		# 有时间界面会出现告警，需要将告警信息print出来
		try:
			# print("Alert exists")
			alert = browser.switch_to_alert()
			print(alert.text)
			alert.accept()
		except Exception as err1:
			# print("无警告，点击返回")
			# print(err1)
			# print('文件', err1.__traceback__.tb_frame.f_globals['__file__'])
			# print('行号', err1.__traceback__.tb_lineno)
			pass
			try:
				browser.find_element_by_xpath('// *[ @ id = "link_but"]').click()
			except:
				# print("无点击返回")
				pass
		# browser.refresh()
		browser.switch_to.default_content()
		# 定位到左侧frame
		time.sleep(1)
		browser.switch_to.frame("lefttree")
		if menu in [系统状态, 管理员, 系统升级, Web证书, 重启系统, 系统信息, 时间设定, DNS,
		            配置文件, 高可用性, SNMP设置, SNMP_Trap, 网络诊断, 服务器诊断]:
			browser.find_element_by_name(系统).click()
			if menu == 系统状态:
				browser.find_element_by_name(menu).click()
			elif menu in [管理员, 系统升级, Web证书, 重启系统]:
				if not browser.find_element_by_xpath(display_系统管理).is_displayed():
					# 如果不可见，点击加号，展开元素
					browser.find_element_by_name(系统管理).click()
				browser.find_element_by_name(menu).click()

			elif menu in [系统信息,  时间设定, DNS, 配置文件, 高可用性, SNMP设置, SNMP_Trap]:
				if not browser.find_element_by_xpath(display_配置).is_displayed():
					# 如果不可见，点击加号，展开元素
					browser.find_element_by_name(配置).click()
				browser.find_element_by_name(menu).click()

			elif menu in [网络诊断, 服务器诊断]:
				if not browser.find_element_by_xpath(display_诊断工具).is_displayed():
					# 如果不可见，点击加号，展开元素
					browser.find_element_by_name(诊断工具).click()
				browser.find_element_by_name(menu).click()

		elif menu in [物理接口, 子接口, 网桥, DHCP设定, DHCP租用列表, ARP列表, 绑定列表, 桥MAC表, IPv6邻居列表,
		              IPv6隧道]:
			browser.find_element_by_name(网络).click()
			if menu in [物理接口, 子接口, 网桥]:
				if not browser.find_element_by_xpath(display_接口设置).is_displayed():
					# 如果不可见，点击加号，展开元素
					browser.find_element_by_name(接口设置).click()
				browser.find_element_by_name(menu).click()

			elif menu in [DHCP设定, DHCP租用列表]:
				if not browser.find_element_by_xpath(display_DHCP).is_displayed():
					# 如果不可见，点击加号，展开元素
					browser.find_element_by_name(DHCP).click()
				browser.find_element_by_name(menu).click()

			elif menu in [ARP列表, 绑定列表, 桥MAC表, IPv6邻居列表, IPv6隧道]:
				if not browser.find_element_by_xpath(display_MAC).is_displayed():
					# 如果不可见，点击加号，展开元素
					browser.find_element_by_name(MAC).click()
				browser.find_element_by_name(menu).click()

		elif menu in [静态路由, 策略路由, OSPF, ISP自动选择, 多网关组, 路由监控]:
			browser.find_element_by_name(路由).click()
			browser.find_element_by_name(menu).click()

		elif menu in [计划任务, Zone, IPv4地址, IPv4地址范围, IPv4地址组, IPv6地址, IPv6地址范围, IPv6地址组,
		              预定义, 自定义, 服务组]:
			browser.find_element_by_name(对象).click()
			if menu == 计划任务 or menu == Zone:
				browser.find_element_by_name(menu).click()

			elif menu in [IPv4地址, IPv4地址范围, IPv4地址组]:
				if not browser.find_element_by_xpath(display_IPv4).is_displayed():
					# 如果不可见，点击加号，展开元素
					browser.find_element_by_name(IPv4).click()
				browser.find_element_by_name(menu).click()

			elif menu in [IPv6地址, IPv6地址范围, IPv6地址组]:
				if not browser.find_element_by_xpath(display_IPv6).is_displayed():
					# 如果不可见，点击加号，展开元素
					browser.find_element_by_name(IPv6).click()
				browser.find_element_by_name(menu).click()

			elif menu in [预定义, 自定义, 服务组]:
				if not browser.find_element_by_xpath(display_服务).is_displayed():
					# 如果不可见，点击加号，展开元素
					try:
						browser.find_element_by_name(服务).click()
					except:
						browser.find_element_by_name('nav_obj_service').click()
				browser.find_element_by_name(menu).click()

		elif menu in [IPv4访问列表, IPv6访问列表, 目的NAT, 源NAT, 服务器负载均衡]:
			browser.find_element_by_name(防火墙).click()
			if menu == IPv4访问列表 or menu == IPv6访问列表:
				browser.find_element_by_name(menu).click()

			elif menu in [目的NAT, 源NAT, 服务器负载均衡]:
				if not browser.find_element_by_xpath(display_NAT).is_displayed():
					# 如果不可见，点击加号，展开元素
					browser.find_element_by_name(NAT).click()
				browser.find_element_by_name(menu).click()

		elif menu in [主机标识, 应用加密, 手动密钥, 远程网关, 远程访问, 虚拟专网监控, CA证书, VPN证书, 随机数生成]:
			browser.find_element_by_name(虚拟专网).click()
			browser.find_element_by_name(menu).click()

		elif menu in [安全站点, 证书配置, Portal站点, sslvpn本地用户]:
			browser.find_element_by_name(SSLVPN).click()
			browser.find_element_by_name(menu).click()

		elif menu in [用户配置, 本地用户, 认证组, 认证服务器, 认证用户设置, 认证监控]:
			browser.find_element_by_name(认证用户).click()
			browser.find_element_by_name(menu).click()

		elif menu in [Anti_DDoS设置, Anti_DDoS用户配置, Anti_DDoS规则列表, Anti_DDoS黑_白名单]:
			browser.find_element_by_name(Anti_DDoS).click()
			browser.find_element_by_name(menu).click()

		elif menu in [日志统计, 日志服务器, 日志过滤, 日志格式, 日志告警, 管理日志, 系统日志, 安全日志, 流量日志]:
			browser.find_element_by_name(日志).click()
			if menu == 日志统计:
				browser.find_element_by_name(menu).click()
			elif menu in [日志服务器, 日志过滤, 日志格式, 日志告警]:
				if not browser.find_element_by_xpath(display_日志设置).is_displayed():
					# 如果不可见，点击加号，展开元素
					browser.find_element_by_name(日志设置).click()
				browser.find_element_by_name(menu).click()
			elif menu in [管理日志, 系统日志, 安全日志, 流量日志]:
				if not browser.find_element_by_xpath(display_日志记录).is_displayed():
					# 如果不可见，点击加号，展开元素
					browser.find_element_by_name(日志记录).click()
				browser.find_element_by_name(menu).click()
				time.sleep(2)

		elif menu in [机器学习, 安全事件, 默认漏洞]:
			browser.find_element_by_name(工业控制).click()
			browser.find_element_by_name(menu).click()

		elif menu in [报表设置, 接口统计报表, 流量排行报表, 会话监控报表, 系统状态报表, 事件统计报表, 会话表, Anti_DDoS会话数,
		              Anti_DDoS会话速率, Anti_DDoS数据包速率, Top_N, 来源IP统计]:
			browser.find_element_by_name(报表).click()
			if menu in [报表设置, 接口统计报表, 流量排行报表, 会话监控报表, 系统状态报表, 事件统计报表, 会话表]:
				browser.find_element_by_name(menu).click()
			elif menu in [Anti_DDoS会话数, Anti_DDoS会话速率, Anti_DDoS数据包速率, Top_N, 来源IP统计]:
				if not browser.find_element_by_xpath(display_DDoS防护).is_displayed():
					# 如果不可见，点击加号，展开元素
					browser.find_element_by_name(DDoS防护).click()
				browser.find_element_by_name(menu).click()

		else:
			print("导航菜单未知，请检查是否输入错误，或切换函数。")
		browser.switch_to.default_content()
		# 定位到内容frame
		browser.switch_to.frame("content")

	elif oem_name == "ICF_new_UI":

		# print("进入ICF导航")
		try:
			# print("Alert exists")
			alert_info = "init"
			while alert_info is not None:
				alert = browser.switch_to_alert()
				alert_info = alert.text
				print(alert_info)
				alert.accept()
		except:
			# print("无警告，点击返回")
			try:
				browser.find_element_by_xpath('// *[ @ id = "link_but"]').click()
			except:
				# print("无点击返回")
				pass
		browser.switch_to.default_content()
		# 定位到左侧frame
		browser.switch_to.frame("lefttree")

		if menu in [系统状态, 管理员, 系统升级, Web证书, 重启系统, 系统信息, 时间设定, DNS,
		            配置文件, 高可用性, SNMP设置, SNMP_Trap, 网络诊断, 服务器诊断]:
			browser.find_element_by_name(系统).click()
			if menu == 系统状态:
				browser.find_element_by_name(menu).click()
			elif menu in [管理员, 系统升级, Web证书, 重启系统]:
				if not browser.find_element_by_xpath(display_系统管理).is_displayed():
					# 如果不可见，点击加号，展开元素
					browser.find_element_by_name(系统管理).click()
				browser.find_element_by_name(menu).click()

			elif menu in [系统信息,  时间设定, DNS, 配置文件, 高可用性, SNMP设置, SNMP_Trap]:
				if not browser.find_element_by_xpath(display_配置).is_displayed():
					# 如果不可见，点击加号，展开元素
					browser.find_element_by_name(配置).click()
				browser.find_element_by_name(menu).click()

			elif menu in [网络诊断, 服务器诊断]:
				if not browser.find_element_by_xpath(display_诊断工具).is_displayed():
					# 如果不可见，点击加号，展开元素
					browser.find_element_by_name(诊断工具).click()
				browser.find_element_by_name(menu).click()

		elif menu in [物理接口, 子接口, 网桥, 静态路由, 策略路由, OSPF, ISP自动选择, 多网关组, 路由监控, DHCP设定, DHCP租用列表,
		              ARP列表, 桥MAC表, IPv6邻居列表, IPv6隧道]:
			browser.find_element_by_name(网络).click()
			if menu in [物理接口, 子接口, 网桥]:
				if not browser.find_element_by_xpath(display_接口设置).is_displayed():
					# 如果不可见，点击加号，展开元素
					browser.find_element_by_name(接口设置).click()
				browser.find_element_by_name(menu).click()
			elif menu in [静态路由, 策略路由, OSPF, ISP自动选择, 多网关组, 路由监控]:
				if not browser.find_element_by_xpath(display_路由).is_displayed():
					# 如果不可见，点击加号，展开元素
					browser.find_element_by_name(路由).click()
				browser.find_element_by_name(menu).click()
			elif menu in [DHCP设定, DHCP租用列表]:
				if not browser.find_element_by_xpath(display_DHCP).is_displayed():
					# 如果不可见，点击加号，展开元素
					browser.find_element_by_name(DHCP).click()
				browser.find_element_by_name(menu).click()
			elif menu in [ARP列表, 桥MAC表, IPv6邻居列表, IPv6隧道]:
				if not browser.find_element_by_xpath(display_MAC).is_displayed():
					# 如果不可见，点击加号，展开元素
					browser.find_element_by_name(MAC).click()
				browser.find_element_by_name(menu).click()

		elif menu in [模式切换, 自定义规则, 机器学习, 安全事件, 工业漏洞, ARP防护, 访问策略, IPV6访问策略, 地址, 地址范围,
		              地址组, IPv6地址, IPv6地址范围, IPv6地址组, 计划任务, 区域, 预定义服务, 自定义服务, 服务组, 目标地址转换,
		              源地址转换, 负载均衡]:
			browser.find_element_by_name(安全策略).click()
			if menu in [模式切换, 自定义规则, 机器学习, 安全事件, 工业漏洞, ARP防护, 访问策略, IPV6访问策略]:
				if not browser.find_element_by_xpath(display_工业防护策略).is_displayed():
					# 如果不可见，点击加号，展开元素
					browser.find_element_by_name(工业防护策略).click()
				browser.find_element_by_name(menu).click()
			elif menu in [地址, 地址范围, 地址组, IPv6地址, IPv6地址范围, IPv6地址组, 计划任务, 区域, 预定义服务, 自定义服务,
			              服务组]:
				if not browser.find_element_by_xpath(display_对象).is_displayed():
					# 如果不可见，点击加号，展开元素
					browser.find_element_by_name(对象).click()
				browser.find_element_by_name(menu).click()
			elif menu in [目标地址转换, 源地址转换, 负载均衡]:
				if not browser.find_element_by_xpath(display_地址转换).is_displayed():
					# 如果不可见，点击加号，展开元素
					browser.find_element_by_name(地址转换).click()
				browser.find_element_by_name(menu).click()

		elif menu in [主机标识, 应用加密, 手动密钥, 远程网关, 远程访问, 监控, CA证书]:
			browser.find_element_by_name(虚拟专网).click()
			browser.find_element_by_name(menu).click()

		elif menu in [Anti_DDoS设置, Anti_DDoS用户配置, Anti_DDoS规则列表, Anti_DDoS黑_白名单]:
			browser.find_element_by_name(DDoS防护).click()
			browser.find_element_by_name(menu).click()

		elif menu in [用户配置, 本地用户, 认证组, 认证服务器, 认证用户设置, 认证监控]:
			browser.find_element_by_name(认证用户).click()
			browser.find_element_by_name(menu).click()

		elif menu in [日志统计, 日志服务器, 日志过滤, 日志格式, 日志告警, 管理日志, 系统日志, 安全日志, 流量日志]:
			browser.find_element_by_name(日志).click()
			if menu == 日志统计:
				browser.find_element_by_name(menu).click()
			elif menu in [日志服务器, 日志过滤, 日志格式, 日志告警]:
				if not browser.find_element_by_xpath(display_日志设置).is_displayed():
					# 如果不可见，点击加号，展开元素
					browser.find_element_by_name(日志设置).click()
				browser.find_element_by_name(menu).click()
			elif menu in [管理日志, 系统日志, 安全日志, 流量日志]:
				if not browser.find_element_by_xpath(display_日志记录).is_displayed():
					# 如果不可见，点击加号，展开元素
					browser.find_element_by_name(日志记录).click()
				browser.find_element_by_name(menu).click()
				time.sleep(2)

		elif menu in [报表设置, 接口统计报表, 流量排行报表, 会话监控报表, 系统状态报表, 事件统计报表, 会话表, Anti_DDoS会话数,
		              Anti_DDoS会话速率, Anti_DDoS数据包速率, Top_N, 来源IP统计]:
			browser.find_element_by_name(报表).click()
			if menu in [报表设置, 接口统计报表, 流量排行报表, 会话监控报表, 系统状态报表, 事件统计报表, 会话表]:
				browser.find_element_by_name(menu).click()
			elif menu in [Anti_DDoS会话数, Anti_DDoS会话速率, Anti_DDoS数据包速率, Top_N, 来源IP统计]:
				if not browser.find_element_by_xpath(display_DDoS防护).is_displayed():
					# 如果不可见，点击加号，展开元素
					browser.find_element_by_name(DDoS防护).click()
				browser.find_element_by_name(menu).click()

		else:
			print("导航菜单未知，请检查是否输入错误，或切换函数。")

		browser.switch_to.default_content()
		# 定位到内容frame
		time.sleep(1)
		try:
			time.sleep(1)
			browser.switch_to.frame("content")
		except Exception as err:
			print(err)
			print("导航处进入，没有找到frame")
