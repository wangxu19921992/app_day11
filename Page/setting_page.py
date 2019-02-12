from Base.base import Base
import Page


class SettingPage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)
    def logout(self):
        """退出登录操作"""
        # 向上滑动页面
        self.scroll_screen(1)
        # 点击退出按钮
        self.click_element(Page.logout_btn_id)
        # 点击确认退出按钮
        self.click_element(Page.logout_acc_btn_id)