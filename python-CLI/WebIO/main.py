import hashlib
import time
import urllib.parse
from functools import partial

import pywebio
import requests
from pywebio import start_server, config
from pywebio.input import *
from pywebio.output import *
import re


def login():
    """login page"""
    pywebio.output.clear()
    put_markdown("""# 登录 短链管理系统 🚀""")
    info_login = input_group('', [
        input("请输入你的用户名", name="users"),
        input("请输入你的密码", name="password", type=PASSWORD),
    ])
    if info_login["users"] == 'admin' and info_login["password"] == 'admin':
        return True
    else:
        return False


def get_now_dict():
    dict_data = requests.get('http://127.0.0.1:3211/').json()
    return dict_data


def del_el(el):
    result = requests.delete('http://127.0.0.1:3211/delete/{0}'.format(el)).json()
    if result['result']:
        pywebio.output.toast("删除成功", duration=3, color="success")
        close_popup()
        get_table()
        while True:
            login_su()
    else:
        pywebio.output.toast("删除失败", duration=3, color="warn")


def edit_row(choice, row):
    pywebio.output.toast("请稍等，正在处理中", duration=3, color="info")
    dict_data = get_now_dict()
    list_data = get_now_list(dict_data)
    row = re.findall('<a href="https://tuo.icodeq.com/(.*?)" target="_blank">', list_data[row - 1][1].embed_data()["content"])[0]
    url = dict_data[row]
    list_data = [(row, url)]
    get_table()
    if choice == '🖊️':
        popup("编辑短链", [
            put_markdown("""## 您当前选择的短链是: {0}""".format(row)),
            put_table(list_data, ["No", "内容"]),
            put_markdown("""#### 将本窗口关闭后请在下方的输入框中更新！""".format(row, url)),
            put_buttons(['我知道了，关闭弹窗在并下方更新。'], onclick=lambda _: close_popup()),
        ])
        url_info = input_group('编辑短链:', [input("请输入对应的长链: ", name="url", type=URL)])
        pywebio.output.toast("请稍等，正在为您更新短链", duration=3, color="info")
        dict_data = {"name": row, "url": url_info["url"]}
        list_data = [(row, url_info["url"])]
        data = requests.post('http://127.0.0.1:3211/update/', json=dict_data).json()
        print(data)
        if data['result']:
            pywebio.output.toast("短链更新成功！", duration=3, color="success")
            popup("更新成功",
                  [
                      put_markdown("""## 更新后的短链信息为:"""),
                      put_table(list_data, ["No", "内容"]),
                      put_buttons(['关闭弹窗'], onclick=lambda _: close_popup())
                  ])
        else:
            popup("更新失败", [
                put_buttons(['关闭弹窗'], onclick=lambda _: close_popup())])
        while True:
            login_su()
    if choice == '❌':
        pywebio.output.toast("您确认要删除吗？", duration=3, color="warn")
        popup("编辑短链", [
            put_markdown("""## 警告: 当前的操作属于敏感操作！""", color="red"),
            put_markdown("""### 当前选择的短链是: {0}""".format(row)),
            put_table(list_data, ["No", "内容"]),
            put_markdown("""您确认要删除吗？"""),
            put_buttons(['关闭弹窗'], onclick=lambda _: [close_popup()]),
            put_buttons(['确认删除'], onclick=lambda _: [del_el(row)])
        ])
        while True:
            login_su()


def get_now_list(dict_data):
    list_data = []
    num = 1
    for i in dict_data:
        dict_data[i] = urllib.parse.unquote(dict_data[i])
        u = "https://tuo.icodeq.com/{0}".format(i)
        list_data.append([num, put_link(u, url=u, new_window=True), dict_data[i],
                          put_buttons(['🖊️', '❌'], group=True, small=True, onclick=partial(edit_row, row=num))])
        num += 1
    return list_data


def get_table():
    data_dict = get_now_dict()
    data_list = get_now_list(data_dict)
    pywebio.output.clear()
    put_markdown("""# 欢迎使用 短链管理系统 🚀 """)
    put_table(data_list, ["No", "名称", "内容", "操作"])
    return data_dict, data_list


def login_su():
    get_table()
    info = select('添加新短链:', ['自定义生成短链', '随机生成的短链'])
    if info == '自定义生成短链':
        short_info = input_group('自定义生成短链:', [
            input("请输入短链: ", name="name"),
            input("请输入对应的长链: ", name="url", type=URL),
        ])
    else:
        short_info = input_group('随机生成的短链:', [
            input("要生成短链的位数: ", name="name", type=NUMBER, min=1, max=32),
            input("请输入对应的长链: ", name="url", type=URL),
        ])
        short_info["name"] = get_time_hash()[:short_info["name"]]
    pywebio.output.put_success("添加短链成功，正在刷新页面")
    print(short_info)
    data = requests.post('http://127.0.0.1:3211/new/', json=short_info)
    print(data.text)
    pywebio.output.toast("生成短链成功，正在刷新页面", duration=3, color="success")


@config(theme="yeti")
def main():
    lg = login()
    if lg:
        pywebio.output.toast("登录成功，正在为您跳转", duration=2, color="success")
        while True:
            login_su()
    else:
        pywebio.output.toast("登录失败！请检查您的账号和密码！", duration=3, color="error")
        main()


def get_time_hash():
    time_str = str(time.time())
    time_hash = hashlib.md5(time_str.encode('utf-8')).hexdigest()
    return time_hash


if __name__ == '__main__':
    pywebio.platform.tornado_http.start_server(main, port=3985, host='', debug=False, cdn=True, static_dir=None, allowed_origins=None, check_origin=None, auto_open_webbrowser=False, session_expire_seconds=None, session_cleanup_interval=None, max_payload_size='200M')
    # start_server(main, debug=True, port=3985, cdn="https://s-bj-2220-tuo-admin.oss.dogecdn.com/")
