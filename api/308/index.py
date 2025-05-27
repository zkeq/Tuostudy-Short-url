# -*- coding: UTF-8 -*-
import json
import requests
# 引入 url 编码
import urllib.parse
from http.server import BaseHTTPRequestHandler
import os

def get_308(name):
    # 修改为读取本地文件
    file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'data.json')
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            _data = json.load(f)
        
        try:
            url = _data[name]
        except KeyError:
            url = 'https://tuo.icodeq.com/'
    except Exception as e:
        print(f"读取本地文件出错: {e}")
        url = 'https://tuo.icodeq.com/'
        
    print('获取到的原始链接为: ', urllib.parse.unquote(url))
    url = urllib.parse.quote(url, safe='/:?=&%20')
    return url


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        print('获取到的路径为:', self.path)
        path = self.path
        try:
            short = path.split('=')[-1]
        except IndexError:
            short = ''
        print('提取出来的短链为:', short)
        url = get_308(short)
        self.send_response(308)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('location', url)
        self.send_header('Refresh', '0;url={}'.format(url))
        self.send_header('Cache-Control', 'max-age=0, s-maxage=60, stale-while-revalidate=3600') # vercel 缓存
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write('Redirecting to {} (308)'.format(url).encode('utf-8'))
        return
