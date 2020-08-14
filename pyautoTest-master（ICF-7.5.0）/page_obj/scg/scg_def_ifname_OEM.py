# 解决接口名变动问题
# 设置为当前设备的类型

# 万兆测试、ICF、ICF_new_UI、SCG、科安达
oem_name = "ICF"

if oem_name == "SCG":
	interface_name_1 = "ge0/1"
	interface_name_2 = "ge0/2"
	interface_name_3 = "ge0/3"
	interface_name_4 = "ge0/4"
	interface_name_5 = "ge0/5"
	interface_name_6 = "ge0/6"
	interface_name_7 = "ge1/1"
	interface_name_8 = "ge1/2"
	interface_name_9 = "ge1/3"
	interface_name_10 = "ge1/4"

elif oem_name == "科安达" or oem_name == "ICF":
	interface_name_1 = "MGMT"
	interface_name_2 = "EXT"
	interface_name_3 = "P0"
	interface_name_4 = "P1"
	interface_name_5 = "P2"
	interface_name_6 = "P3"
	interface_name_7 = "ge1/1"
	interface_name_8 = "ge1/2"
	interface_name_9 = "ge1/3"
	interface_name_10 = "ge1/4"

elif oem_name == "万兆测试":
	interface_name_1 = "MGMT"
	interface_name_2 = "EXT"
	interface_name_3 = "P0"
	interface_name_4 = "P1"
	interface_name_5 = "P2"
	interface_name_6 = "P3"
	interface_name_7 = "F1"
	interface_name_8 = "F2"
	interface_name_9 = "F3"
	interface_name_10 = "F4"
	interface_name_11 = "X1"
	interface_name_12 = "X2"
	interface_name_13 = "X3"
	interface_name_14 = "X4"


# 解决服务器重新导入后网卡名变化
server_pc_1_eth0 = "eth4"
server_pc_1_eth1 = "eth5"

server_pc_2_eth0 = "eth4"
server_pc_2_eth1 = "eth5"

server_pc_3_eth0 = "eth4"
server_pc_3_eth1 = "eth5"

server_pc_4_eth0 = "eth4"
server_pc_4_eth1 = "eth4"

# 设备MAC地址
mac_pc2_interface_1 = "00:0C:29:7B:FF:7C"
mac_dev2_interface_2 = "00:16:31:E7:75:B7"
mac_dev3_interface_2 = "00:16:31:E8:2A:75"

# chrome下载目录，和conftest.py一致
path_download = r'C:\pytestdownload'
