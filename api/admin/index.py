# -*- coding: UTF-8 -*-
from http.server import BaseHTTPRequestHandler
import json
from github import Github

# Authentication is defined via github.Auth
from github import Auth
import os

auth = Auth.Token(os.getenv("GITHUB_TOKEN"))
    

def get_data(path):
    g = Github(auth=auth)
    # Then play with your Github objects:
    repo = g.get_repo("Tuostudy-Short-url")
    contents = repo.get_contents(path)
    # base64解码
    content = json.loads(contents.decoded_content.decode('utf-8'))
    # To close connections after use
    g.close()

    return content


def post_data(path, data, message, branch="main"):
    g = Github(auth=auth)
    repo = g.get_repo("Tuostudy-Short-url")
    contents = repo.get_contents(path, ref=branch)
    
    # Ensure data is in the correct format
    if not isinstance(data, str):
        data = json.dumps(data, ensure_ascii=False, indent=4)
    
    repo.update_file(contents.path, message, data, contents.sha, branch=branch)
    g.close()
    return True


class handler(BaseHTTPRequestHandler):
    def _send_cors_headers(self):
        """ Sets headers required for CORS """
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.send_header("Access-Control-Allow-Credentials", "true")
    

    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self._send_cors_headers()
        self.end_headers()


    def do_GET(self):
        path = self.path
        # 获取查询参数，如果没有密码参数则默认为空
        query_components = {}
        if '?' in path:
            query_string = path.split('?')[1]
            for kv in query_string.split('&'):
                if '=' in kv:
                    k, v = kv.split('=')
                    query_components[k] = v
        
        password = query_components.get('password', '')
        
        if password != "ai-home-short":
            self.send_response(400)
            self._send_cors_headers()
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"code": 400, "message": "密码错误"}).encode('utf-8'))
            return
        
        data = {
            "code": 200,
            "path": "data/data.json",
            "data": get_data("data/data.json")
        }
        self.send_response(200)
        self._send_cors_headers()
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))
        return
    
    def do_POST(self):
        # 获取请求体的长度
        content_length = int(self.headers['Content-Length'])
        if not content_length:
            self.send_response(400)
            self.end_headers()
            return
        # 读取请求体的数据
        post_json = self.rfile.read(content_length)
        # 将数据从 JSON 格式转换为 Python 对象
        data = json.loads(post_json)
        try:
            if data["password"] != "ai-home-short":
                response = {
                    "code": 400,
                    "message": "密码错误"
                }
            else:
                
                if post_data("data/data.json", data["new_data"], data["message"].strip()):
                    # 返回响应
                    response = {
                        "code": 200,
                        "path": "data/data.json",
                        "data": data["new_data"]
                    }
        except Exception as e:
            response = {
                "code": 400,
                "message": "请求体格式错误: " + str(e),
                "reason": str(e)
            }

        self.send_response(200)
        self._send_cors_headers()
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))
        return