# import sys
# sys.path.append("/var/lib/jenkins/workspace/auto-test")
import json

import pytest
import allure
from manner.rest_client import RestClient
from common.get_data import get_data,get_config
from common.logger import logger


@allure.feature("******登录测试******")
class Test_adviserLogin:

   api_data = get_data("login_data.yaml")

   url_data = get_config("setting.ini")


   def setup(self):
      logger.info("<------------------------- 开始执行用例 ------------------------->")

   def teardown(self):
      logger.info("<------------------------- 结束执行用例 ------------------------->")


   @allure.title("编辑端登录测试")
   @allure.description("用例-是针对编辑端用户登录的接口测试")
   @pytest.mark.parametrize('api_data',api_data)
   @allure.story("二维码股市")
   def test_login(self, api_data, url=url_data):
      api = RestClient()
      url = url['TEST_ENV'] + api_data['test']['url']
      header = api_data['test']['headers']
      raw = api_data['test']['body']
      res = api.post(url,headers=header,json=raw)
      res1 = json.dumps(res.json(),sort_keys=True, indent=4, separators=(',', ': '),ensure_ascii=False)
      logger.info("接口响应结果 ==>> {}".format(res1))
      assert res.status_code == 200, "判断当前接口响应状态码，状态码为：%s" % res.status_code
      assert res.json()['errCode'] == 0, "判断当前接口errCode返回值，当前值为：%s" % res.json()['errCode']















