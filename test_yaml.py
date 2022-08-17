# -*- coding: utf-8 -*-
import sys

import requests
import yaml
import pytest
from loguru import logger

import jsonpath


def res_data(switch: bool):
    if isinstance(switch, bool):
        def log_decorator(func):
            def log(*args, **kwargs):
                data = func(*args, **kwargs)
                if switch:
                    _data = data['yaml_data']['data']
                    _url = data['yaml_data']['url']
                    _dependent_case = data['yaml_data']['dependence_case']
                    # 判断如果有依赖数据，则展示
                    if _dependent_case is True:
                        _dependent_case = data['yaml_data']['dependence_case_data']
                    else:
                        _dependent_case = "暂无依赖用例数据"
                    if data['yaml_data']['requestType'] == 'PARAMS':
                        params_data = "?"
                        for k, v in _data.items():
                            if v is None or v == '':
                                params_data += (k + "&")
                            else:
                                params_data += (k + "=" + str(v) + "&")
                        _url += params_data[:-1]
                        _data = ""
                    logger.remove()
                    logger.add('../PyDemo/test/{time:YYYY-MM-DD}run.log', retention="1 day")
                    logger.add(sys.stdout, colorize=True, format='<g>{message}</g>')
                    logger.info(f"\n===========================================================================\n"
                                f"测试标题: {data['yaml_data']['detail']}\n"
                                f"请求方式: {data['yaml_data']['method']}\n"
                                f"请求头:   {data['yaml_data']['headers']}\n"
                                f"请求路径: {_url}\n"
                                f"请求内容: {_data}\n"
                                f"依赖测试用例: {_dependent_case}\n"
                                f"接口响应内容: {data['response_data']}\n"
                                f"接口响应时长: {data['res_time']}ms\n"
                                f"Http状态码: {data['status_code']}\n"
                                f"数据库断言数据: {data['sql_data']}\n"
                                "===========================================================================")
                    return data
                else:
                    return data

            return log

        return log_decorator
    else:
        raise TypeError("日志开关只能为 True 或者 False")


def res_runtime(timeout: int):
    if isinstance(timeout, int):
        def log_decorator(func):
            def time(*args, **kwargs):
                res = func(*args, **kwargs)
                _res_time = res['res_time']
                if timeout < _res_time:
                    logger.remove()
                    logger.add('../PyDemo/test/{time:YYYY-MM-DD}time.log', retention="1 day")
                    logger.add(sys.stdout, colorize=True, format='<level>{message}</level>')
                    logger.error("测试用例执行时间较长，请关注!!!\n"
                                 f"请求响应时间: {_res_time}ms\n"
                                 f"测试用例标题: {res['yaml_data']['detail']}\n"
                                 "===========================================================================")
                    return res
                else:
                    return res

            return time

        return log_decorator
    else:
        raise TypeError("参数只能为数字")


class GetYamlData():
    def __init__(self, filepath):
        self.filepath = filepath

    def get_yaml_data(self):
        with open(self.filepath, 'r', encoding='utf-8') as f:
            result = yaml.load(f, Loader=yaml.SafeLoader)
        return result

    def get_yaml_case_data(self):
        yaml_data = self.get_yaml_data()
        _case_data = []
        for i, j in yaml_data.items():
            if i != 'case_common':
                case_data = {
                    'detail': yaml_data[i]['detail'],
                    'method': yaml_data[i]['method'],
                    'url': yaml_data[i]['url'],
                    'data': yaml_data[i]['data'],
                    'headers': yaml_data[i]['headers'],
                    'assert': yaml_data[i]['assert'],
                    'dependence_case': yaml_data[i]['dependence_case'],
                    'dependence_case_data': yaml_data[i]['dependence_case_data'],
                    'requestType': yaml_data[i]['requestType']
                }
                _case_data.append(case_data)
        return _case_data


class RequestControl:

    @res_runtime(3000)
    @res_data(True)
    def request_control(self, yaml_data, **kwargs):
        res = requests.request(method=yaml_data['method'], url=yaml_data['url'], data=yaml_data['data'],
                               headers=yaml_data['headers'], **kwargs)
        try:
            cookie = res.cookies.get_dict()
        except:
            cookie = None
        res_time = round(res.elapsed.total_seconds() * 3000)
        status_code = res.status_code
        # print(res)
        return {"response_data": res.json(), "yaml_data": yaml_data, "cookie": cookie, "res_time": res_time,
                "status_code": status_code, "sql_data": None}


class Assert:

    def __init__(self, data):
        self.data = data

    def assert_(self):
        for key, value in self.data['yaml_data']['assert'].items():
            if value['AssertType'] == 'sql':
                pass
            else:
                _jsonpath = jsonpath.jsonpath(self.data['response_data'], value['jsonpath'])[0]
                _type = value['type']
                _value = value['value']
                assert _jsonpath == _value


case_data = GetYamlData(r'D:\Program Files\workspace\PyDemo\test.yaml').get_yaml_case_data()


class Testyaml:
    @pytest.mark.parametrize('data', case_data)
    def test_login(self, data):
        a = RequestControl().request_control(data)
        # print(a["response_data"].text)
        # print(a["cookie"])
        Assert(a).assert_()


if __name__ == '__main__':
    pytest.main(['-s', 'test_yaml.py'])
