# -*- coding: utf-8 -*-
import requests
import yaml


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
                    'method': yaml_data[i]['method'],
                    'url': yaml_data[i]['url'],
                    'data': yaml_data[i]['data'],
                    'headers': yaml_data[i]['headers'],
                }
                _case_data.append(case_data)
        return _case_data


class RequestControl():

    def request_control(self, yaml_data, **kwargs):
        for i in range(len(yaml_data)):
            res = requests.request(method=yaml_data[i]['method'], url=yaml_data[i]['url'], data=yaml_data[i]['data'],
                                   headers=yaml_data[i]['headers'], **kwargs)
            try:
                cookie = res.cookies.get_dict()
            except:
                cookie = None
            status_code = res.status_code
            return {"response_data": res, "sql_data": {"sql": None}, "yaml_data": yaml_data,
                    "headers": yaml_data[i]['headers'], "cookie": cookie, "status_code": status_code}


class Test_yaml():
    def test_login(self):
        case_data = GetYamlData(r'D:\PycharmProjects\PyDemo\test.yaml').get_yaml_case_data()
        a = RequestControl().request_control(case_data)
        assert a["status_code"] == 200
