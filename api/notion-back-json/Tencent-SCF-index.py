# -*- coding: UTF-8 -*-
# 部署前请先安装库..
# 先新建文件夹，把本文件拖进去，然后重命名为 index.py 
# 然后在命令行执行 
# pip install requests -t .
# 然后再将本地文件夹上传至云函数
# https://cloud.tencent.com/document/product/583/39780#python-.E8.BF.90.E8.A1.8C.E6.97.B6
import json
import requests
from http.server import BaseHTTPRequestHandler

SK = "secret_pMesJhzV1rJFS9dt41iu7F62YIiiuteXCuffatK1Zmp"
ID = '0ff3d88f8ba143ea869bb2da7c9236c7'


def get_notion_data():
    global SK
    global ID
    url = "https://api.notion.com/v1/databases/{}/query".format(ID)
    headers = {
        "Accept": "application/json",
        "Notion-Version": "2021-08-16",
        "Content-Type": "application/json",
        "Authorization": SK
    }
    response = requests.request("POST", url, headers=headers).text
    dict_all = json.loads(response)
    short_dict = {}
    for i in dict_all['results']:
        # print(i)
        short = i['properties']['Short']['title'][0]['plain_text']
        url = i['properties']['url']['url']
        short_dict[short] = url
    return short_dict


def main_handler(event, context):
    data = get_notion_data()
    return{
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {"Content-Type":"application/json; charset=utf-8"},
        "body": json.dumps(data)
    }