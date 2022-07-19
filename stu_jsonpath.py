import yaml
from jsonpath import jsonpath


with open('../PyDemo/test.yaml','r',encoding='utf-8') as f:
    result = yaml.load(f,Loader=yaml.SafeLoader)
    a=jsonpath(result,'$.name.[0].address')
print(a)
