# -*- coding: UTF-8 -*-
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
    data = 'Redirecting to {} (308)'.format(url)
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
        self.send_header('location', data)
        self.send_header('Refresh', '0;url={}'.format(data))
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(data.encode('utf-8'))
        return
