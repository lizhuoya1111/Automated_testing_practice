#!/usr/bin/python
# coding=utf-8

系统 = '//*[text()="系统"]'
# '//*[@id="menu"]/div[1]/header/a'

系统状态 = '//*[text()="系统状态"]'

系统管理 = '//*[text()="系统管理"]'

管理员 = '//*[text()="管理员"]'

系统升级 = '//*[@id="menu"]/div[1]/div/ul/li[2]/ul/li[3]/span/a/span[2]'

Web证书 = '//*[@id="menu"]/div[1]/div/ul/li[2]/ul/li[4]/span/a/span'

重启系统 = '//*[@id="menu"]/div[1]/div/ul/li[2]/ul/li[5]/span/a/span'

##################################################################################

配置 = '//*[@id="menu"]/div[1]/div/ul/li[3]/span'

系统信息 = '//*[@id="menu"]/div[1]/div/ul/li[3]/ul/li[1]/span/a/span'

时间设定 = '//*[@id="menu"]/div[1]/div/ul/li[3]/ul/li[2]/span/a/span[2]'

DNS = '//*[@id="menu"]/div[1]/div/ul/li[3]/ul/li[3]/span/a/span'

配置文件 = '//*[@id="menu"]/div[1]/div/ul/li[3]/ul/li[4]/span/a/span'

高可用性 = '//*[@id="menu"]/div[1]/div/ul/li[3]/ul/li[5]/span/a/span[2]'

SNMP设置 = '//*[@id="menu"]/div[1]/div/ul/li[3]/ul/li[6]/span/a/span'

SNMP_Trap = '//*[@id="menu"]/div[1]/div/ul/li[3]/ul/li[7]/span/a/span'

诊断工具 = '//*[@id="menu"]/div[1]/div/ul/li[4]/span'

网络诊断 = '//*[@id="menu"]/div[1]/div/ul/li[4]/ul/li[1]/span/a/span[2]'

服务器诊断 = '//*[@id="menu"]/div[1]/div/ul/li[4]/ul/li[2]/span/a/span'

##################################################################################

网络 = '//*[@id="menu"]/div[2]/header/a'

接口设置 = '//*[@id="menu"]/div[2]/div/ul/li[1]/div'

物理接口 = '//*[@id="menu"]/div[2]/div/ul/li[1]/ul/li[1]/span/a/span'

子接口 = '//*[@id="menu"]/div[2]/div/ul/li[1]/ul/li[2]/span/a/span'

网桥 = '//*[@id="menu"]/div[2]/div/ul/li[1]/ul/li[3]/span/a'

DHCP = '//*[@id="menu"]/div[2]/div/ul/li[2]/span'

DHCP设定 = '//*[@id="menu"]/div[2]/div/ul/li[2]/ul/li[1]/span/a/span'

DHCP租用列表 = '//*[@id="menu"]/div[2]/div/ul/li[2]/ul/li[2]/span/a/span'

MAC = '//*[@id="menu"]/div[2]/div/ul/li[3]/span'

ARP列表 = '//*[@id="menu"]/div[2]/div/ul/li[3]/ul/li[1]/span/a/span'

绑定列表 = '//*[@id="menu"]/div[2]/div/ul/li[3]/ul/li[2]/span/a/span'

桥MAC表 = '//*[@id="menu"]/div[2]/div/ul/li[3]/ul/li[3]/span/a/span'

IPv6邻居列表 = '//*[@id="menu"]/div[2]/div/ul/li[3]/ul/li[4]/span/a/span'

IPv6隧道 = '//*[@id="menu"]/div[2]/div/ul/li[3]/ul/li[5]/span/a/span'

ddns_status = '//*[@id="menu"]/div[2]/div/ul/li[3]/ul/li[6]/span/a/span'

##################################################################################

路由 = '//*[@id="menu"]/div[3]/header/a'

静态路由 = '//*[@id="menu"]/div[3]/div/ul/li[1]/span/a'

策略路由 = '//*[@id="menu"]/div[3]/div/ul/li[2]/span/a'

OSPF = '//*[@id="menu"]/div[3]/div/ul/li[3]/span/a'

ISP自动选择 = '//*[@id="menu"]/div[3]/div/ul/li[4]/span/a'

多网关组 = '//*[@id="menu"]/div[3]/div/ul/li[5]/span/a'

路由监控 = '//*[@id="menu"]/div[3]/div/ul/li[6]/span/a'

##################################################################################

对象 = '//*[@id="menu"]/div[4]/header/a'

Zone = '//*[@id="menu"]/div[4]/div/ul/li[1]/span/a'

IPv4 = '//*[@id="menu"]/div[4]/div/ul/li[2]/span'

IPv4地址 = '//*[@id="menu"]/div[4]/div/ul/li[2]/ul/li[1]/span/a/span'

IPv4地址范围 = '//*[@id="menu"]/div[4]/div/ul/li[2]/ul/li[2]/span/a/span'
#//*[@id="menu"]/div[4]/div/ul/li[2]/ul/li[3]/span/a
IPv4地址组 = '//*[@id="menu"]/div[4]/div/ul/li[2]/ul/li[3]/span/a/span'

IPv6 = '//*[@id="menu"]/div[4]/div/ul/li[3]/span'

IPv6地址 = '//*[@id="menu"]/div[4]/div/ul/li[3]/ul/li[1]/span/a/span'

IPv6地址范围 = '//*[@id="menu"]/div[4]/div/ul/li[3]/ul/li[2]/span/a/span'

IPv6地址组 = '//*[@id="menu"]/div[4]/div/ul/li[3]/ul/li[3]/span/a/span'

服务 = '//*[@id="menu"]/div[4]/div/ul/li[4]/span'

预定义 = '//*[@id="menu"]/div[4]/div/ul/li[4]/ul/li[1]/span/a/span'

自定义 = '//*[@id="menu"]/div[4]/div/ul/li[4]/ul/li[2]/span/a/span'

服务组 = '//*[@id="menu"]/div[4]/div/ul/li[4]/ul/li[3]/span/a/span'

计划任务 = '//*[@id="menu"]/div[4]/div/ul/li[5]/span'

基础计划任务 = '//*[@id="menu"]/div[4]/div/ul/li[5]/ul/li[1]/span/a/span[2]'

周计划任务 = '//*[@id="menu"]/div[4]/div/ul/li[5]/ul/li[2]/span/a/span'

##################################################################################

防火墙 = '//*[@id="menu"]/div[5]/header/a'

IPv4访问控制列表 = '//*[@id="menu"]/div[5]/div/ul/li[1]/span/a'

IPv6访问控制列表 = '//*[@id="menu"]/div[5]/div/ul/li[2]/span/a'

NAT = '//*[@id="menu"]/div[5]/div/ul/li[3]/span'

目的NAT = '//*[@id="menu"]/div[5]/div/ul/li[3]/ul/li[1]/span/a/span'

源NAT = '//*[@id="menu"]/div[5]/div/ul/li[3]/ul/li[2]/span/a/span'

服务器负载均衡 = '//*[@id="menu"]/div[5]/div/ul/li[3]/ul/li[3]/span/a/span'

##################################################################################

虚拟专网 = '//*[@id="menu"]/div[6]/header/a'

主机标识 = '//*[@id="menu"]/div[6]/div/ul/li[1]/span/a'

应用加密 = '//*[@id="menu"]/div[6]/div/ul/li[2]/span/a'

手动秘钥 = '//*[@id="menu"]/div[6]/div/ul/li[3]/span/a'

远程网关 = '//*[@id="menu"]/div[6]/div/ul/li[4]/span/a'

远程访问 = '//*[@id="menu"]/div[6]/div/ul/li[5]/span/a'

监控 = '//*[@id="menu"]/div[6]/div/ul/li[6]/span/a'

CA证书 = '//*[@id="menu"]/div[6]/div/ul/li[7]/span/a'

##################################################################################

认证用户 = '//*[@id="menu"]/div[7]/header/a'

用户配置 = '//*[@id="menu"]/div[7]/div/ul/li[1]/span/a'

本地用户 = '//*[@id="menu"]/div[7]/div/ul/li[2]/span/a'

认证组 = '//*[@id="menu"]/div[7]/div/ul/li[3]/span/a'

认证服务器 = '//*[@id="menu"]/div[7]/div/ul/li[4]/span/a'

认证用户设置 = '//*[@id="menu"]/div[7]/div/ul/li[4]/span/a'

认证监控 = '//*[@id="menu"]/div[7]/div/ul/li[6]/span/a'

##################################################################################

日志 = '//*[@id="menu"]/div[8]/header/a'

日志统计 = '//*[@id="menu"]/div[8]/div/ul/li[1]/span/a'

设置 = '//*[@id="menu"]/div[8]/div/ul/li[2]/span'

日志服务器 = '//*[@id="menu"]/div[8]/div/ul/li[2]/ul/li[1]/span/a/span'

日志过滤 = '//*[@id="menu"]/div[8]/div/ul/li[2]/ul/li[2]/span/a/span'

日志格式 = '//*[@id="menu"]/div[8]/div/ul/li[2]/ul/li[3]/span/a/span'

日志告警 = '//*[@id="menu"]/div[8]/div/ul/li[2]/ul/li[4]/span/a/span'
#//*[@id="menu"]/div[8]/div/ul/li[3]/div
日志记录 = '//*[@id="menu"]/div[8]/div/ul/li[3]/span'
#//*[@id="menu"]/div[8]/div/ul/li[3]/ul/li[1]/span/a/span
管理日志 = '//*[@id="menu"]/div[8]/div/ul/li[3]/ul/li[1]/span/a/span'

系统日志 = '//*[@id="menu"]/div[8]/div/ul/li[3]/ul/li[2]/span/a/span'

流量日志 = '//*[@id="menu"]/div[8]/div/ul/li[3]/ul/li[3]/span/a/span'

安全日志 = '//*[@id="menu"]/div[8]/div/ul/li[3]/ul/li[3]/span/a/span'

##################################################################################

报表 = '//*[@id="menu"]/div[9]/header/a'

报表设置 = '//*[@id="menu"]/div[9]/div/ul/li[1]/span/a'

接口统计 = '//*[@id="menu"]/div[9]/div/ul/li[2]/span/a'

流量 = '//*[@id="menu"]/div[9]/div/ul/li[3]/span/a'

会话监控 = '//*[@id="menu"]/div[9]/div/ul/li[4]/span/a'

报表系统状态 = '//*[@id="menu"]/div[9]/div/ul/li[5]/span/a'

事件统计 = '//*[@id="menu"]/div[9]/div/ul/li[6]/span/a'

会话表 = '//*[@id="menu"]/div[9]/div/ul/li[7]/span/a'

