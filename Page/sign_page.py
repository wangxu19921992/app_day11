from Base.base import Base
import Page

class SingPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_exits_accout(self):
        """点击已有账号去登录"""
        self.click_element(Page.exits_account_id)