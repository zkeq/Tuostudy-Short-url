# coding:utf-8
import json
import urllib.parse

import oss2
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    url: str


def oss_login(config_list):
    AK = config_list.get('AK')
    SK = config_list.get('SK')
    BUCKET_NAME = config_list.get('BUCKET_NAME')
    Endpoint = config_list.get('Endpoint')
    auth = oss2.Auth(AK, SK)
    _bucket = oss2.Bucket(auth, Endpoint, BUCKET_NAME)
    return _bucket


def oss_config_read():
    with open('oss_config.json', 'r', encoding='utf-8') as f:
        _config_dict = json.load(f)
        return _config_dict


def get_dict():
    bucket = oss_login(oss_config_read())
    bucket.get_object_to_file("data.json", "data.json")
    with open('data.json', 'r', encoding='utf-8') as f:
        _dict = json.load(f)
    return _dict


def post_new_el(item):
    name = item.name
    _dict = get_dict()
    exist_url = _dict.get(name)
    if exist_url:
        return False
    url = urllib.parse.quote(item.url, safe='/:?=&%20')
    _dict[item.name] = url
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(_dict, f, ensure_ascii=False)
    bucket = oss_login(oss_config_read())
    bucket.put_object_from_file("data.json", "data.json")
    return True


def post_update_el(item):
    name = item.name
    url = urllib.parse.quote(item.url, safe='/:?=&%20')
    _dict = get_dict()
    _dict[name] = url
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(_dict, f, ensure_ascii=False)
    bucket = oss_login(oss_config_read())
    bucket.put_object_from_file("data.json", "data.json")
    return True


def delete_el(item):
    _dict = get_dict()
    _dict.pop(item)
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(_dict, f, ensure_ascii=False)
    bucket = oss_login(oss_config_read())
    bucket.put_object_from_file("data.json", "data.json")
    return True


@app.get("/")
def main():
    _dict = get_dict()
    return _dict


@app.post("/new/")
async def create_item(item: Item):
    result = post_new_el(item)
    return {'result': result}


@app.post("/update/")
async def update_item(item: Item):
    result = post_update_el(item)
    return {'result': result}


@app.delete("/delete/{name}")
async def delete_item(name: str):
    result = delete_el(name)
    return {'result': result}


if __name__ == "__main__":
    uvicorn.run("fast:app", host="127.0.0.1", port=3211, log_level="info")
