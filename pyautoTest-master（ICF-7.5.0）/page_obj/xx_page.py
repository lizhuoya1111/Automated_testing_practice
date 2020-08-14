from .common import PageObject, PageElement, PageElements


class BaiduSearchPage(PageObject):
    search_input = PageElement(id_="kw", time_out=10)   # 搜索框
    search_button = PageElement(id_="su")  # 搜搜按钮
    settings = PageElement(link_text="设置")  # 设置
    search_setting = PageElement(css=".setpref")  # 搜索设置
    save_setting = PageElement(css=".prefpanelgo")  # 保存设置

    search_result = PageElements(xpath="//div/h3/a")  # 搜搜结果（定位一组元素）