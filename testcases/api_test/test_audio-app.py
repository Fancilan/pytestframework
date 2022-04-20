import json

import pytest
import allure
from manner.rest_client import RestClient
from common.get_data import get_data,get_config
from common.logger import logger


@allure.feature("******音频应用测试******")
class Test_audioApp:

   api_data = get_data("audio_app.yaml")

   url_data = get_config("setting.ini")


   def setup(self):
      logger.info("<------------------------- 开始执行用例 ------------------------->")

   def teardown(self):
      logger.info("<------------------------- 结束执行用例 ------------------------->")


   @allure.title("音频-音频专辑")
   @allure.description("小应用音频")
   @pytest.mark.parametrize('api_data',api_data)
   @allure.story("音频专辑")
   def test_audio_app(self, api_data, url=url_data):
      api = RestClient()
      url = url['PROD_APP_ENV'] + api_data['prod']['url']
      header = api_data['prod']['headers']
      raw = api_data['prod']['params']
      res = api.get(url, headers=header, params=raw)
      res1 = json.dumps(res.json(), sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)
      logger.info("接口响应结果 ==>> {}".format(res1))
      assert res.status_code == 200, "判断当前接口响应状态码，状态码为：%s" % res.status_code
      assert res.json()['errCode'] == 0, "判断当前接口errCode返回值，当前值为：%s" % res.json()['errCode']
