# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   ranzhi_project
# FileName:     get_file_path
# Author:      Jakiro
# Datetime:    2020/12/5 17:02
# Description:
# -----------------------------------------------------------------------------------

import os

# 获得文件路径方法模块

def get_file_path(path):
    # 将文件中的'\'替换成'/'
    sep1 = os.path.sep
    print(type(sep1))
    print(sep1)
    path2 = '/'.join(path.split(sep1))
    # 获取项目名
    pro_name = path2.split('/')[0]
    # 获取当前文件路径
    sys_path = os.path.dirname(__file__)
    # 获取项目所在父目录
    parent_path = sys_path.split(pro_name)[0]
    # 获取整体路径
    all_path = os.path.join(parent_path, path)
    return all_path


if __name__ == '__main__':
    print(get_file_path(r'ranzhi_project/data_config/test_data.json'))
