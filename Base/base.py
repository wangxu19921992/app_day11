import allure, time
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    def search_element(self, loc, timeout=15, poll_frequency=1.0):
        """
        定位单个元素
        :param loc: 定位类型 (By.ID, id属性值) (By.CLASS_NAME, class属性值) (By.XPATH, xpath属性值)
        :param timeout: 搜索元素超时时间
        :param poll_frequency: 搜索元素间隔
        :return: 元素定位对象
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    def search_elements(self, loc, timeout=15, poll_frequency=1): # {"ty":xx, "vale":xxx} (ty,value)
        """
        定位单个元素
        :param loc: 定位类型 (By.ID, id属性值) (By.CLASS_NAME, class属性值) (By.XPATH, xpath属性值)
        :param timeout: 搜索元素超时时间
        :param poll_frequency: 搜索元素间隔
        :return: 元素定位对象
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    def click_element(self, loc, timeout=15, poll_frequency=1):
        """
        点击元素
        :param loc: 定位类型 (By.ID, id属性值) (By.CLASS_NAME, class属性值) (By.XPATH, xpath属性值)
        :param timeout: 搜索元素超时时间
        :param poll_frequency: 搜索元素间隔
        :return:
        """
        self.search_element(loc, timeout, poll_frequency).click()

    def send_element(self, loc, text, timeout=15, poll_frequency=1):
        """
        输入内容
        :param loc: 定位类型 (By.ID, id属性值) (By.CLASS_NAME, class属性值) (By.XPATH, xpath属性值)
        :param text: 输入文本内容
        :param timeout:  搜索元素超时时间
        :param poll_frequency: 搜索元素间隔
        :return:
        """
        # 定位元素
        input_text = self.search_element(loc, timeout, poll_frequency)
        # 清空
        input_text.clear()
        # 输入
        input_text.send_keys(text)

    def scroll_screen(self, num):
        """
        滑动屏幕方法
        :param num: 1：向上滑动  2：向下滑动  3：向左滑动  4：向右滑动
        :return:
        """
        import time
        time.sleep(2) # 放置页面未跳转执行滑动失效
        # 获取手机分辨率 ('width', 'height')
        screen_size = self.driver.get_window_size()
        # 取宽
        width = screen_size.get("width")
        # 取高
        height = screen_size.get("height")
        # 根据num绝对滑动方向
        if num == 1:
            self.driver.swipe(width*0.5, height*0.8, width*0.5, height*0.3)
        if num == 2:
            self.driver.swipe(width*0.5, height*0.3, width*0.5, height*0.8)
        if num == 3:
            self.driver.swipe(width*0.8, height*0.5, width*0.3, height*0.5)
        if num == 4:
            self.driver.swipe(width * 0.3, height * 0.5, width * 0.8, height * 0.5)
    def get_toast(self, mes):
        """
        返回toast消息
        :param mes: xpath模糊匹配需要参数
        :return: toast消息
        """
        # 拼接xpath语句
        toat_path = "//*[contains(@text,'{}')]".format(mes) # 格式化

        return self.search_element((By.XPATH, toat_path), 5, 0.5).text
    def screen_shot(self, name="截图"):
        """
        截图操作
        :param name: 展示截图名字
        :return:
        """
        # 定义图片名字
        png_name = "./screen/{}.png".format(int(time.time()))
        # 截取图片
        self.driver.get_screenshot_as_file(png_name)
        # 图片添加到报告
        with open(png_name, "rb") as f:
            allure.attach(name, f.read(), allure.attach_type.PNG)


