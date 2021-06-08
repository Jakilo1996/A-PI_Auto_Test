# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   ranzhi_project
# FileName:     get_log
# Author:      Jakiro
# Datetime:    2020/12/9 14:13
# Description:
# -----------------------------------------------------------------------------------

import logging
import sys

# 生成打印日志方法模块

def get_logging(log_path):
    '''
    参数为日志路径，设置出日志相关信息
    :param log_path:
    :return:
    '''
    # 实例化logging对象
    log_obj = logging.Logger('tes')
    # 设置log 等级
    # log_obj.setLevel(logging.DEBUG)
    # 设置日志格式
    log_fm = logging.Formatter('[%(asctime)s]:%(message)s')

    # 实例化FileHandler对象(将日志输出到指定路径)
    log_fh = logging.FileHandler(log_path, encoding='utf8')
    # 把读取出来的内容设置为事先定义日志格式
    log_fh.setFormatter(log_fm)
    # 输出日志
    log_obj.addHandler(log_fh)
    # 返回值为logging对象

    # 实例化对象streamhandler（把日志输出到控制台）
    log_sh = logging.StreamHandler(sys.stdout)
    # 把读取出来的数据内容设置为事先准备好的日志格式
    log_sh.setFormatter(log_fm)
    # 输出日志到控制台
    log_obj.addHandler(log_sh)

    return log_obj
