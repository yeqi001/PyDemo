# -*- coding: utf-8 -*-
import json

filepath = "../PyDemo/test.json"


def read_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        result = json.load(f)
        print(type(result))
        return result


def write_json(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as f:
        # ensure_ascii=False写入内容显示中文，True写入内容会转换
        json.dump(data, f, ensure_ascii=False)

data="123"
#write_json(filepath,data)
print(read_json(filepath))