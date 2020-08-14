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

test_id = "141017"
# 对于已导入ip的条目，点击条目后面的clear ip
# 操作成功；shell先显示和UI一致；admin log正常


def test_c141017(browser):

    try:
        login_web(browser, url=dev1)

        add_multi_isp_save_wxw(browser, name='isp207', desc='miaoshu')

        import_ip_config_file_wxw(browser, name='isp207', save='yes', cancel='no')

        clear_isp_ip_wxw(browser, name='isp207')

        ip = get_isp_show_ip_wxw(browser, name='isp207')
        # print(ip)

        loginfo = get_log_info(browser, 管理日志)
        # print(loginfo)

        del_multi_isp_byname(browser, name='isp207')

        try:
            assert ip == "ip is null"
            assert "成功删除ISP [isp207]的归属IP"in loginfo
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert ip == "ip is null"
            assert "成功删除ISP [isp207]的归属IP" in loginfo

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s",  "test_c"+str(test_id)+".py"])
