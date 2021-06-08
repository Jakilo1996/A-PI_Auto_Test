# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   ranzhi_project
# FileName:     read_sql
# Author:      Jakiro
# Datetime:    2020/12/5 17:03
# Description:
# -----------------------------------------------------------------------------------


import pymysql

# 读取 mysql数据方法，修改数据库相关信息，需要在此文件修改
def read_sql(realname):
    # 连接数据库
    my_sql = pymysql.connect(host="127.0.0.1", user='root', password='123456',
                             database='ranzhi', port=3306, charset='utf8')
    # 建立游标
    cursor1 = my_sql.cursor()
    # 执行语句
    cursor1.execute("SELECT realname FROM sys_user WHERE realname = '{}'".format(realname))
    row_data = cursor1.fetchall()
    # print(type(han_data),han_data)
    for row in row_data:
        for cell_data in row:
            return cell_data
        # print(i)


if __name__ == '__main__':
    print(read_sql('谷小姐215958'))