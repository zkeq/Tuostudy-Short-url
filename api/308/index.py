# -*- coding: UTF-8 -*-
import json
import requests
# 引入 url 编码
import urllib.parse
from http.server import BaseHTTPRequestHandler

# 这个文件针对 vercel 开发，但是 vercel 要放在 /api 这个目录下面才会当做 函数 执行，总感觉不够优雅
# 有域名的话推荐同目录下的那个腾讯云函数的方式


def get_308(name):
    url = 'http://tuo-site.oss-cn-beijing.aliyuncs.com/data.json'  # 当然，这个数据源也可以换成 Notion 那个，其实就是把那个函数复制过来，我就不写了
    r = requests.get(url, headers={'referer': 'https://tuo.icodeq.com/'})
    _data = json.loads(r.text)
    try:
        url = _data[name]
    except KeyError:
        url = 'https://tuostudy.vercel.app/'
    print('获取到的原始链接为: ', urllib.parse.unquote(url))
    url = urllib.parse.quote(url, safe='/:?=&%20')
    return url


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        print('debug: ', self.__dict__)
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
