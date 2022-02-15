# coding:utf-8
import json
import os
import time
import hashlib
from prettytable import PrettyTable


# 读取json文件
def read_json(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except:
            data = {}
    return data


# 写入json文件
def write_json(file_name, _data):
    with open(file_name, 'w+', encoding='utf-8') as f:
        json.dump(_data, f, ensure_ascii=False)


# 写入 TXT 文件
def write_txt(file_name, _data):
    with open(file_name, 'a', encoding='utf-8') as f:
        f.write(_data)


def user_loop():
    # 判断是否存在文件
    if os.path.exists('data.json'):
        data_json = read_json('data.json')
    else:
        data_json = {}
    data = str(input('请输入短链（例如 abc)：'))
    _data = data
    while data_json.get(_data):
        print('检测到您输入的短链已存在，再次进行操作即为覆盖')
        print('您确定要覆盖吗？\n')
        print('1.确认覆盖')
        print('2.重新输入\n')
        data_input = input('请输入：')
        if data_input == '1':
            print('您已经确认覆盖，请稍等...')
            _data = None
        if data_input == '2':
            print('您已经选择重新输入，请重新输入')
            data = str(input('请输入短链（例如 abc)：'))
            _data = data
    url = str(input('请输入要转换的长链（请输入完整网址）：'))
    print('-' * 50)
    print('-' * 50)
    print('-' * 50)
    print('-' * 50)
    data_json[data] = url
    write_json('data.json', data_json)
    print('转换成功！\n')
    print('请将本文件夹下的 data.json 文件上传到 OSS！\n')
    print('下次需要追加内容时 请确保之前生成的 data.json 文件在同一目录！\n')
    print('否则之前生成的数据就会丢失\n')
    print('在本目录的 address.txt 文件中可看到详细信息 ！\n')
    url_finale = '您本次生成的短链为：' + 'https://tuo.icodeq.com/' + data + '\n'
    print(url_finale)
    write_txt('address.txt', url_finale)
    url_before = '此链接对应的长链为：' + url + '\n' + '\n' + '------------------------------------\n'
    print(url_before)
    write_txt('address.txt', url_before)
    print('------------------------------------\n')
    print('您可以选择继续生成或者点击右上角退出~\n')
    print('------------------------------------\n')
    input('添加完成，按回车键继续')


def time_2_hash(data):
    now_time = time.time()
    url_hash = hashlib.md5(str(now_time).encode('utf-8')).hexdigest()
    data_hash = url_hash[0:data]
    return data_hash


def hash_loop():
    data = int(input('请输入短链的位数(整数1-32)：'))
    data_hash = time_2_hash(data)
    url = str(input('请输入要转换的长链（请输入完整网址）：'))
    print('-' * 50)
    print('-' * 50)
    print('-' * 50)
    print('-' * 50)
    # 判断是否存在文件
    if os.path.exists('data.json'):
        data_json = read_json('data.json')
    else:
        data_json = {}
    # 如果字典中存在该数据
    while data_json.get(data_hash):
        data_hash = time_2_hash(data)
    data_json[data_hash] = url
    write_json('data.json', data_json)
    print('转换成功！\n')
    print('请将本文件夹下的 data.json 文件上传到 OSS！\n')
    print('下次需要追加内容时 请确保之前生成的 data.json 文件在同一目录！\n')
    print('否则之前生成的数据就会丢失\n')
    print('在本目录的 address.txt 文件中可看到详细信息 ！\n')
    url_finale = '您本次生成的短链为：' + 'https://tuo.icodeq.com/' + data_hash + '\n'
    print(url_finale)
    write_txt('address.txt', url_finale)
    url_before = '此链接对应的长链为：' + url + '\n' + '\n' + '------------------------------------\n'
    print(url_before)
    write_txt('address.txt', url_before)
    print('------------------------------------\n')
    print('您可以选择继续生成或者点击右上角退出~\n')
    print('------------------------------------\n')
    input('添加完成，按回车键继续')


def print_table(data_json):
    table = PrettyTable(['编号', '短链', '长链'])
    _keys = list(data_json.keys())
    _values = list(data_json.values())
    for i in range(len(_keys)):
        table.add_row([i+1, 'https://tuo.icodeq.com/' + _keys[i], _values[i]])
    print(table)
    return _keys


def replace_mode():
    print('当前的所有短链为：')
    if os.path.exists('data.json'):
        data_json = read_json('data.json')
    else:
        data_json = {}
    _keys = print_table(data_json)
    data_line = input('请输入您要操作的编号: ')
    # 输入删除或替换
    print('您当前选择的短链为: {0}'.format(_keys[int(data_line) - 1]))
    del_or_rep = input('您要执行的操作是？\n\n1. 删除 2. 更新\n\n请输入您要执行的操作:')
    if del_or_rep == '1':
        data_json.pop(_keys[int(data_line)-1])
        print('您当前选择的短链为: {0}'.format(_keys[int(data_line) - 1]))
        print('---------------------删除成功---------------------')
        write_txt('address.txt', '------------------------------------\n')
        write_txt('address.txt', '删除短链成功: {0}\n'.format(_keys[int(data_line) - 1]))
        write_txt('address.txt', '------------------------------------\n')
        write_json('data.json', data_json)
        input('删除完成，按回车键继续')
    elif del_or_rep == '2':
        data = _keys[int(data_line) - 1]
        url = str(input('请输入您要为此短链更新的值（请输入完整网址）：'))
        data_json[data] = url
        write_json('data.json', data_json)
        url_finale = '您本次修改的短链为：' + 'https://tuo.icodeq.com/' + data + '\n'
        print(url_finale)
        write_txt('address.txt', url_finale)
        url_before = '修改后此链接对应的长链为：' + url + '\n'
        print(url_before)
        write_txt('address.txt', url_before)
        input('修改完成，按回车键继续')


def mode_see():
    if os.path.exists('data.json'):
        data_json = read_json('data.json')
    else:
        data_json = {}
    print_table(data_json)
    input('-------按回车键回到菜单-------')


if __name__ == '__main__':
    while True:
        print('-' * 27 + '\n')
        print('欢迎使用短链转换工具！'+ '\n')
        print('-' * 27)
        _mode = input('本工具有四种模式\n\n1. 自定义生成短链\n2. 设置要生成的短链位数 ，自动生成短链\n3. 删除或修改短链模式\n4. 查阅模式（只读模式）\n0. 退出\n\n请输入模式：')
        print('-' * 27)
        if _mode == '2':
            print('-' * 27)
            print('-' * 4 + '计算时间戳的哈希值模式' + '-' * 4)
            print('-' * 27)
            print('-' * 27)
            hash_loop()
        if _mode == '1':
            print('-' * 27)
            print('-' * 9 + '自定义模式' + '-' * 9)
            print('-' * 27)
            print('-' * 27)
            user_loop()
        if _mode == '3':
            replace_mode()
        if _mode == '4':
            mode_see()
        if _mode == '0':
            exit()
