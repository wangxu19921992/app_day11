from Base.base import Base
import Page

class HomePage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_my_btn(self):
        """点击首页我按钮"""
        self.click_element(Page.home_my_btn_id)