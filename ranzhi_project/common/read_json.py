# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   ranzhi_project
# FileName:     read_json
# Author:      Jakiro
# Datetime:    2020/12/5 17:03
# Description:
# -----------------------------------------------------------------------------------

import json


# 自带类库

# 读取json文件方法
def read_json_data(path):
    with open(path, encoding='utf8') as fp:
        # load的参数是打开的文件对象
            # loads的参数是字符串
        return json.load(fp)


if __name__ == '__main__':
    print(read_json_data(r'C:\Users\Administrator\codes\test\project\ranzhi_project\data_config\login_test_data.json'))