import yaml


class Get_Data:

    def __init__(self):
        pass
    def get_yml_data(self, name):
        """返回yaml文件中数据"""
        with open("./Data/{}.yml".format(name), "r", encoding="utf-8") as f:
            return yaml.load(f)
