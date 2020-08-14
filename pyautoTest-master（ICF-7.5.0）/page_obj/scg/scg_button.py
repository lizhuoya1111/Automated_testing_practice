#!/usr/bin/python
# coding=utf-8


from page_obj.scg.scg_def_ifname_OEM import *

系统 = 'system'

系统状态 = 'sys_status'

系统管理 = 'system_admin'

管理员 = 'sys_administrators'

系统升级 = 'sys_update'

Web证书 = 'sys_webcert'

重启系统 = 'sys_operation'

##################################################################################

配置 = 'sys_Configuration'

系统信息 = 'sys_info'

时间设定 = 'sys_setting_time'

DNS = 'sys_setting_dns'

配置文件 = 'sys_conffile'

高可用性 = 'sys_ha'

SNMP设置 = 'sys_snmp_setting'

SNMP_Trap = 'sys_snmp_trap'

诊断工具 = 'sys_diagnostics'

网络诊断 = 'sys_diagnostics_network'

服务器诊断 = 'sys_diagnostics_server'

##################################################################################

网络 = 'network'

接口设置 = 'nav_net_interface'

物理接口 = 'net_interface'

子接口 = 'net_interface_vlan'

网桥 = 'net_interface_bridge'

DHCP = 'subr_net_dhcp'

DHCP设定 = 'net_dhcp_set'

DHCP租用列表 = 'net_dhcp_lease'

MAC = 'nav_net_mac'

ARP列表 = 'net_arp_list'

绑定列表 = 'net_ipmac'

桥MAC表 = 'br_mac'

IPv6邻居列表 = 'net_nd_dynamic'

IPv6隧道 = 'net_tunnel'


##################################################################################

安全策略 = 'security_policy'

工业防护策略 = 'Industrial_protection_strategy'

模式切换 = 'icf_changemod'

自定义规则 = 'icf_cusproto'


路由 = 'route'

静态路由 = 'route_static'

策略路由 = 'route_policy'

OSPF = 'route_ospf_status'

ISP自动选择 = 'route_isp'

多网关组 = 'route_maintenance_multigw'

路由监控 = 'route_monitor'

##################################################################################

对象 = 'nav_object'

计划任务 = 'obj_schedule_weekly'

Zone = 'obj_zone'

区域 = Zone

IPv4 = 'obj_ipv4_object'

IPv4地址 = 'obj_address'

地址 = IPv4地址

IPv4地址范围 = 'obj_address_iprange'

地址范围 = IPv4地址范围

IPv4地址组 = 'obj_address_netgroup'

地址组 = IPv4地址组

IPv6 = '//*[text()="IPv6"]'

IPv6地址 = 'obj_address_ipv6'

IPv6地址范围 = 'obj_address_ipv6_iprange'

IPv6地址组 = 'obj_address_ipv6_netgroup'

服务 = 'subr_obj_service'

预定义 = 'obj_service'

预定义服务 = 预定义

自定义 = 'obj_service_custom'

自定义服务 = 自定义

服务组 = 'obj_service_group'


##################################################################################

防火墙 = 'firewall'

IPv4访问控制列表 = 'fw_acl'

访问策略 = IPv4访问控制列表
IPv4访问列表 = IPv4访问控制列表

IPv6访问控制列表 = 'fw_acl_ipv6'

IPV6访问策略 = IPv6访问控制列表
IPv6访问列表 = IPv6访问控制列表

NAT = 'address_translation'

地址转换 = NAT

目的NAT = 'fw_nat_dnat'

目的地址转换 = 目标地址转换 = 目的NAT

源NAT = 'fw_nat_snat'

源地址转换 = 源NAT

服务器负载均衡 = 'fw_nat_loadbalance'

负载均衡 = 服务器负载均衡

##################################################################################

虚拟专网 = 'nav_vpn'

主机标识 = 'vpn_hip'

应用加密 = 'vpn_server_application_encryption'

手动密钥 = 'vpn_manual_key'

远程网关 = 'vpn_remote_gateway'

远程访问 = 'vpn_remote_access'

虚拟专网监控 = 'vpn_monitor_static_tunnel'

监控 = 'vpn_monitor_static_tunnel'

VPN证书 = 'vpn_certadmin_gm'

CA证书 = 'vpn_certadmin'

随机数生成 = 'vpn_random'

##################################################################################

SSLVPN = 'SSLVPN'

安全站点 = 'sslvpn_safe_site'

证书配置 = 'sslvpn_certadmin'

Portal站点 = 'sslvpn_portal_list'

sslvpn本地用户 = 'sslvpn_portal_user'


##################################################################################

认证用户 = 'nav_auth'

用户配置 = 'aut_user_profile'

本地用户 = 'aut_user'

认证组 = 'aut_group_local'

认证服务器 = 'aut_server'

认证用户设置 = 'aut_setting'

认证监控 = 'aut_onlineusers'

##################################################################################

Anti_DDoS = 'DDoS_Protection'

DDoS防护 = Anti_DDoS

Anti_DDoS设置 = 'sec_antidos_setting'

Anti_DDoS用户配置 = 'sec_lmtprofile'

Anti_DDoS规则列表 = 'sec_antidos_list'

Anti_DDoS黑_白名单 = 'sec_bwlist'

##################################################################################

日志 = 'nav_log'

日志统计 = 'log_statistic'

日志设置 = 'nav_log_settings'

日志服务器 = 'log_setting_server'

日志过滤 = 'log_setting_filter'

日志格式 = 'log_setting_fieldselectsetting'

日志告警 = 'log_alert_email'

日志记录 = 'log_log_record'

管理日志 = 'log_record_admin'

系统日志 = 'log_record_system'

安全日志 = 'log_record_security'

流量日志 = 'log_record_traffic'

############################################################################

ICF = '//*[text()="ICF"]'
机器学习 = 'white_list_device'
安全事件 = 'icf_event_list'
默认漏洞 = 'icf_black_list'
工业漏洞 = 默认漏洞
ARP防护 = 绑定列表
工业控制 = 'Industrial_control'


##################################################################################

报表 = 'nav_reporter'

报表设置 = 'reporter_setting'

接口统计报表 = 'reporter_interface'

流量排行报表 = 'reporter_traffic_topip'

会话监控报表 = 'reporter_session'

系统状态报表 = 'reporter_system'

事件统计报表 = 'reporter_counter'

会话表 = 'reporter_sessiontab'

报表Anti_DDoS = 'rep_DDoS_Protection'

报表DDoS防护 = 报表Anti_DDoS

Anti_DDoS会话数 = 'reporter_antidossessionnumber'

Anti_DDoS会话速率 = 'reporter_antidossessionrate'

Anti_DDoS数据包速率 = 'reporter_packagerate'

Top_N = 'reporter_antidostopn'

来源IP统计 = 'reporter_antidosipstatic'


################################# 折叠按钮 ############################

if oem_name == "ICF":
	display_系统管理 = '//*[text()="系统管理"]/../ul'
	display_配置 = '//*[text()="配置"]/../ul'
	display_诊断工具 = '//*[text()="诊断工具"]/../ul'
	display_接口设置 = '//*[text()="接口设置"]/../ul'
	display_路由 = '//*[text()="路由"]/../ul'
	display_DHCP = '//*[text()="DHCP"]/../ul'
	display_MAC = '//*[text()="MAC"]/../ul'
	display_工业防护策略 = '//*[text()="工业防护策略"]/../ul'
	display_对象 = '//*[text()="对象"]/../ul'
	display_地址转换 = '//*[text()="地址转换"]/../ul'
	display_日志设置 = '//*[text()="日志设置"]/../ul'
	display_日志记录 = '//*[text()="日志记录"]/../ul'
	display_DDoS防护 = '//*[text()="DDoS防护"]/../ul'
else:
	display_系统管理 = '//*[text()="系统管理"]/../ul'
	display_配置 = '//*[text()="配置"]/../ul'
	display_诊断工具 = '//*[text()="诊断工具"]/../ul'
	display_接口设置 = '//*[text()="接口设置"]/../ul'
	display_DHCP = '//*[text()="DHCP"]/../ul'
	display_MAC = '//*[text()="MAC"]/../ul'
	display_IPv4 = '//*[text()="IPv4"]/../ul'
	display_IPv6 = '//*[text()="IPv6"]/../ul'
	display_服务 = '//*[text()="服务"]/../ul'
	display_NAT = '//*[text()="NAT"]/../ul'
	display_日志设置 = '//*[text()="日志设置"]/../ul'
	display_日志记录 = '//*[text()="日志记录"]/../ul'
	display_AntiDDoS = '//*[text()="Anti-DDoS "]/../ul'
