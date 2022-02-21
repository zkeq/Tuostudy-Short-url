# -*- coding: UTF-8 -*-

# 有备案域名的话推荐这种用法
# 云函数业务地址：https://console.cloud.tencent.com/scf/list?rid=1&ns=default
# 很快，因为是 308 跳转，效率很高，但是不好的地方是 不备案绑定自己域名的话，链接为很长
# https://service-55pgd0rm-1303831731.gz.apigw.tencentcs.com/release/APIGWHtmlDemo-1645366165?dream
# 这么长的链接做短链...
# 以为我没备案域名，更多没有测试，但是这个接口可以用了


# 部署前请先安装库..
# 先新建文件夹，把本文件拖进去，然后重命名为 index.py 
# 然后在命令行执行 
# pip install requests -t .
# 然后再将本地文件夹上传至云函数
# https://cloud.tencent.com/document/product/583/39780#python-.E8.BF.90.E8.A1.8C.E6.97.B6


import json
import requests
from http.server import BaseHTTPRequestHandler


def get_308(name):
    url = 'http://tuo-site.oss-cn-beijing.aliyuncs.com/data.json'
    r = requests.get(url, headers={'referer': 'https://tuo.icodeq.com/'})
    _data = json.loads(r.text)
    try:
        url = _data[name]
    except KeyError:
        url = 'https://tuostudy.vercel.app/'
    return url


def main_handler(event, context):
    try:
        short = event.get('path').split('/')[-1]
    except IndexError:
        short = ''
    print(short)
    url = get_308(short)
    url = url.encode('utf-8')
    return{
        "isBase64Encoded": False,
        "statusCode": 308,
        "headers": {"Content-Type":"text/plain",
                    "Refresh": "0;url={}".format(url),
                    "location": url,
                    'Access-Control-Allow-Origin': '*',},
        "body": 'Redirecting to {} (308)'.format(url)
        }