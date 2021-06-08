# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   ranzhi_project
# FileName:     raed_yaml
# Author:      Jakiro
# Datetime:    2020/12/5 17:04
# Description:
# -----------------------------------------------------------------------------------

import yaml
# 安装时PYyaml 导入时 yaml

# 读取yaml文件模块

def read_yaml_data(path):
    with open(path, encoding='utf8') as ry:
        # 打开yaml文件
        return yaml.safe_load(ry)


if __name__ == '__main__':
    read_yaml_data()
