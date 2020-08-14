import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_dev import *
from os.path import dirname, abspath
from page_obj.scg.scg_def_multi_isp import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141022"
# 对于已导入ip、添加路由的条目，点击delete
# 操作成功；shell先显示和UI一致；admin log正常


def test_c141022(browser):

    try:
        login_web(browser, url=dev1)

        add_multi_isp_save_wxw(browser, name='isp212', desc='miaoshu')

        import_ip_config_file_wxw(browser, name='isp212', save='yes', cancel='no')

        add_isp_route_wxw(browser, name='isp212', single_gateway='yes', device=interface_name_2, gateway='12.1.1.6',
                          multi_gateway='no', gateway_group='',
                          enable='yes', disable='no')
        del_multi_isp_byname(browser, name='isp212')

        exist = is_multi_isp_exist_wxw(browser, name='isp212')
        # print(exist)

        loginfo = get_log_info(browser, 管理日志)
        # print(loginfo)

        try:
            assert "删除ISP对象成功" in loginfo
            assert exist is False
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "删除ISP对象成功" in loginfo
            assert exist is False

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s",  "test_c"+str(test_id)+".py"])