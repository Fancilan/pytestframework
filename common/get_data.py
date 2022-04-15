import os
import pytest
from common.read_data import ReadFileData

data = ReadFileData()
BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
data = data

def get_data(yaml_file_name):
    try:
        data_file_path = os.path.join(BASE_PATH, "data", yaml_file_name)
        yaml_data = data.load_yaml(data_file_path)
    except Exception as ex:
        pytest.skip(str(ex))
    else:
        return yaml_data

def get_config(config_name):
    try:
        data_file_path = os.path.join(BASE_PATH, "config",config_name)
        config_data = data.load_ini(data_file_path)['host']     #可以不同测试环境的url开头
    except Exception as ex:
        pytest.skip(str(ex))
    else:
        return config_data

if __name__ == '__main__':

    get_data("login_data.yaml")

    get_config("setting.ini")
