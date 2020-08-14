import pytest
import time
import sys
from os.path import dirname, abspath
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_interface import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.common.telnet import *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_vlan_interface import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "139816"
# 描述输入字符串长度超过256（英文字符），输入中文字符超过85（每个中文占三个字符）
# PS: 英文字符时 最多输入256个 超出256 就输入不了了  中文超出85输入 保存时会报错
# 无法成功配置，系统报错


def test_c139816(browser):
    try:
        login_web(browser, url=dev1)

        # 添加zone name为lzy 输入中文字符超过85（每个中文占三个字符）
        add_obj_zone(browser, "abc",
                     "啊啊啊啊啊啊啊啊啊啊不不不不不不不不不不啛啛喳喳错错错错错错啊啊啊啊啊啊啊啊啊啊不不不不不不不不不不啛啛喳喳错错错错错错啊啊啊啊啊啊啊啊啊啊不不不不不不不不不不啛啛喳喳错错错错错错",
                     [interface_name_5, interface_name_6])
        sleep(1)
        info1 = browser.find_element_by_class_name('layui-layer-content').text
        # print(info1)
        browser.find_element_by_class_name('layui-layer-btn0').click()


        try:
            assert '描述格式输入错误' in info1
            rail_pass(test_run_id, test_id)
        except Exception as err1:
            print(err1)
            rail_fail(test_run_id, test_id)
            assert '描述格式输入错误' in info1
    except Exception as err:
        # 如果上面的步骤有报错，重启设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + test_id + ".py"])