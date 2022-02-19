# -*- coding: UTF-8 -*-
import json
import requests
from http.server import BaseHTTPRequestHandler


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        _html = f.read()
    return _html


def url_2_html(url):
    html_file = read_file('./api/temp.html')
    html_file = html_file.replace('{{url}}', url)
    print(url)
    return html_file


def get_notion_data():
    url = "https://api.notion.com/v1/databases/0ff3d88f8ba143ea869bb2da7c9236c7/query"
    headers = {
        "Accept": "application/json",
        "Notion-Version": "2021-08-16",
        "Content-Type": "application/json",
        "Authorization": "secret_pMesJhzV1rJFS9dt41iu7F62YIiiuteXCuffatK1Zmp"
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


def get_308(name):
    _data = get_notion_data()
    try:
        url = _data[name]
    except KeyError:
        url = 'https://tuostudy.vercel.app/'
    data = url_2_html(url)
    return data


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        try:
            short = path.split('?')[1]
        except IndexError:
            short = ''
        print(short)
        data = get_308(short)
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(data.encode('utf-8'))
        return
