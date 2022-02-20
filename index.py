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
    return url


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        try:
            short = path.split('?')[1]
        except IndexError:
            short = ''
        print(short)
        url = get_308(short)
        self.send_response(308)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('location', url)
        self.send_header('Refresh', '0;url={}'.format(url))
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write('Redirecting to {} (308)'.format(url).encode('utf-8'))
        return
