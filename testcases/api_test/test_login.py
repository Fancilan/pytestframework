import sys
sys.path.append("/var/lib/jenkins/workspace/auto-test")

import pytest
import allure
from manner.rest_client import RestClient
from common.get_data import get_data,get_config
from common.logger import logger




class Test_example:

   api_data = get_data("base_data.yaml")

   url_data = get_config("setting.ini")

   api = RestClient()

   global api

   def setup(self):
      logger.info("<------------------------- 开始执行用例 ------------------------->")

   def teardown(self):
      logger.info("<------------------------- 结束执行用例 ------------------------->")

   @allure.title("登录测试")
   @allure.description("用例-是针对编辑端用户登录的接口测试")
   @pytest.mark.parametrize('api_data',api_data)
   def test_login(self, api_data, url=url_data):

      url = url['TEST_ENV'] + api_data['test']['url']
      header = api_data['test']['headers']
      raw = api_data['test']['body']
      res = api.post(url,headers=header,json=raw)
      logger.info("接口响应结果 ==>> {}".format(res.json()))
      assert res.status_code == 200, "判断当前接口响应状态码，状态码为：%s" % res.status_code
      assert res.json()['errCode'] == 0, "判断当前接口errCode返回值，当前值为：%s" % res.json()['errCode']















