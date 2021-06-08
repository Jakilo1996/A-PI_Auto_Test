# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   ranzhi_project
# FileName:     read_excel
# Author:      Jakiro
# Datetime:    2020/12/5 17:02
# Description:
# -----------------------------------------------------------------------------------

import openpyxl


# 第三方库

# 去取excel文件模块 ，输出格式为列表套元组
def read_excel_data(file_path, sheet):
    # 打开表格  实例化workbook对象 将文件路径作为参数
    get_wb = openpyxl.load_workbook(file_path)
    # 指定sheet 页 默认为第一个
    get_sheet = get_wb[sheet]
    all_lists = []
    one_line_data_list = []
    stats = True
    # 循环遍历每一行的tuple对象
    for row_tuple in get_sheet:
        if stats:
            stats = False
            continue
        # 循环遍历每个单元格
        for cell in row_tuple:
            # 拼接 value
            one_line_data_list.append(cell.value)
            # 转化成元组
            one_line_data_tuple = tuple(one_line_data_list)
        # 清空临时列表
        one_line_data_list.clear()
        # 将临时元组添加到总列表中
        all_lists.append(one_line_data_tuple)

    return all_lists


if __name__ == '__main__':
    # print(read_excel_data(r'c:\\login_data.xlsx', 'Login_success'))
    list_a =read_excel_data(r'C:\Users\Administrator\Desktop\接口测试数据.xlsx','Sheet1')
    dict_1 ={}
    print(list_a)
    for i in list_a:
        a= i[0].split("Content-Disposition: form-data; name=")
        # print(a)
        # # b = a[1]
        if i[1] == None:
            dict_1[a[1]] = ''
        else:
            dict_1[a[1]] = i[1]

    print(dict_1)