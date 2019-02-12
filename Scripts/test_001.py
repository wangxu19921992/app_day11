import allure


class Test_001:

    @allure.step(title="步骤名称")
    def test_001_1(self):
        allure.attach("名字","文件内容")

        with open("./screen/abc.png", "rb") as f:
            allure.attach("图片名字", f.read(), allure.attach_type.PNG)
        assert False