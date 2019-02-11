# -*- coding: utf-8 -*-
__author__ = 'dongwenda'
__date__ = '2019/2/4 21:02'

import os
import re

import mitmproxy.http
import yaml


def get_yaml_info(file_path):
    # 返回yaml文件信息，dict
    with open(file_path, 'r', encoding='UTF-8') as f:
        content = yaml.load(f)
        return content

def get_text_info(filepath):
    # 返回大的文本信息，例如整个html
    with open(filepath, 'r', encoding='UTF-8') as f:
        return f.read()

cwd = os.getcwd()  # 当前目录路径
file_path = os.path.join(cwd, 'mock_config.yaml')  # yaml文件路径
txt_dir = os.path.join(cwd, 'txt')  # txt 文件夹
api = get_yaml_info(file_path)

def response(flow: mitmproxy.http.HTTPFlow):
    for api_path in api.keys():
        if re.match(api_path, flow.request.url):
            if api[api_path].startswith("file#"):
                res_txt = get_text_info(os.path.join(txt_dir, api[api_path].replace("file#", "")))
                flow.response.set_text(res_txt)
            else:
                flow.response.set_text(api[api_path])
