# -*- coding: UTF-8 -*-
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


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        data = get_notion_data()
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'application/json; charset=utf-8')
        self.end_headers()
        self.wfile.write(data.dumps(_data).encode('utf-8'))
        return
