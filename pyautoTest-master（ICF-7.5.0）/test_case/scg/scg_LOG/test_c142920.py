import pytest
import time
import sys
from os.path import dirname, abspath

from scg_def_acl import del_default_acl_group_lzy, del_all_acl_group_lzy

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_physical_interface import *
from page_obj.scg.scg_def_vlan_interface import *
from page_obj.scg.scg_def_firewall import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_log import *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def_sys import *
from page_obj.scg.scg_def import *

test_id = 142920
# 根据关键字查询traffic日志
# 设备初始状态没有流量日志，需更改日志过滤 再添加记录日志的ACL 再产生流量日志再做查询操作 注意还原时：ACL（添加日志及其他相关操作）、日志过滤、删除查询条件
def test_c142920(browser):
    try:
        login_web(browser, url=dev1)
        # 删除默认ACL
        del_default_acl_group_lzy(browser)

        # 添加ACL 全通开log
        add_acl_group_complete(browser, name='lzy', enable='yes')
        add_ipv4acl_lzy(browser, aclgroup_name='lzy', source_zone_interface='Z:any',
                        source_custom='no', fromip='', fromnetmask='',
                        source_address_object='yes', s_address_object='A:any',
                        mac='', dest_zone_interface='Z:any',
                        dest_custom='no', toip='', tonetmask='',
                        dest_address_object='yes', d_address_object='A:any',
                        service='P:any', schdule='-- 无 --',
                        accept='yes', drop='no',
                        auth='-- 无 --', icf='no', log='yes', save='yes', cancel='no')

        # 添加82到83 与83到82的路由
        shell_82 = Shell_SSH()
        shell_82.connect(hostip=dev2)
        shell_82.execute("en")
        shell_82.execute("conf t")
        shell_82.execute("ip route 13.1.1.0/24 gateway 12.1.1.1")
        shell_82.close()

        shell_83 = Shell_SSH()
        shell_83.connect(hostip=dev3)
        shell_83.execute("en")
        shell_83.execute("conf t")
        shell_83.execute("ip route 12.1.1.0/24 gateway 13.1.1.1")
        shell_83.close()

        # 流量日志过滤级别改为all
        edit_log_filter_lzy(browser, index="4", all='yes', debug='yes/no', info='yes/no', notice='yes/no',
                            warning='yes/no', error='yes/no', critical='yes/no', emerg='yes/no', alert="yes/no")

        # 删除日志
        delete_log(browser, log_type=流量日志)

        # 先用82ping83  使本条流量日志源地址=[12.1.1.2]
        sign_out_jyl(browser)
        login_web(browser, url=dev2)
        sleep(1)
        diag_ping(browser, ipadd="13.1.1.3", interface=interface_name_2)



        sign_out_jyl(browser)
        login_web(browser, url=dev1)
        # 查询日志
        advanced_query_security_or_traffic_log_lzy(browser, log_type=流量日志, advanced="yes", ambiguous_search="ICMP",
                                                   from_ip="", exclude_from_ip="", to_ip="", exclude_to_ip="",
                                                   from_port="", to_port="",
                                                   protocol="", exclude_protocol="", start_date="", start_time="",
                                                   end_date="", end_time=""
                                                   , level="unchange", select_all="yes/no", emerg="yes/no",
                                                   alert="yes/no",
                                                   critical="yes/no", error="yes/no", warning="yes/no", notice="yes/no",
                                                   info="yes/no",
                                                   debug="yes/no", module="unchange", modul_name="session")


        # 获取页面信息
        info1 = browser.find_element_by_xpath('//*[@id="log_record_traffic_table"]/tbody/tr[2]/td[7]').text
        # print(info1)


        # 还原
        # 删除ACL
        del_all_acl_group_lzy(browser)
        # 还原流量日志过滤级别error critical alert emerg
        edit_log_filter_lzy(browser, index="4", all='yes/no', debug='yes/no', info='yes/no', notice='yes/no',
                            warning='yes/no', error='yes', critical='yes', emerg='yes', alert="yes")
        # 删除日志
        delete_log(browser, log_type=流量日志)
        # 删82上路由
        shell_82 = Shell_SSH()
        shell_82.connect(hostip=dev2)
        shell_82.execute("en")
        shell_82.execute("conf t")
        shell_82.execute("no ip route 13.1.1.0/24 gateway 12.1.1.1")
        shell_82.close()
        # 删83上路由
        shell_83 = Shell_SSH()
        shell_83.connect(hostip=dev3)
        shell_83.execute("en")
        shell_83.execute("conf t")
        shell_83.execute("no ip route 12.1.1.0/24 gateway 13.1.1.1")
        shell_83.close()



        try:
            assert "ICMP" in info1
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "ICMP" in info1
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=[dev1, dev2, dev3])
        rail_fail(test_run_id, test_id)
        assert False



if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
