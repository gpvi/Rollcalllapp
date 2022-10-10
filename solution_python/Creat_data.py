"""
@FileName：Creat_data.py\n
@Description：\n
@Author：NZQ\n
@Time：2022/10/10 23:05\n
"""

"""
@FileName：DataCreat.py\n
@Description：\n
@Author：NZQ\n
@Time：2022/10/7 16:24\n
"""

"""
this file is used in creating data
"""
from random import randint
from traceback import print_tb
import pandas as pd
import numpy as np
import os
import sys
import random
import numpy

path = "../Data/"
data_demo_path = "demo1.csv"


# 定义学生类
class Student:
    index = 0
    absence = -1
    status = 0

    def __init__(self, a, b, c):
        self.index = a
        self.absence = b
        self.status = c


# 学生类列表
Student_vec = []
# 定义是否缺席
vis = [False] * 90
if __name__ == '__main__':
    # 20次课程，90位同学，最大缺勤总次数
    times = 20
    n = 90
    top = times * 10

    #   初始化
    for i in range(1, n + 1):
        st = Student
        st.index = i
        Student_vec.append(Student(i, -1, 0))

    # 随机生成5-8名长缺勤人数
    absence_num = 5 + random.randint(0, 3)
    s = set([])
    while (len(s) < absence_num):
        s.add(randint(0, n - 1))
    # print(type(s))
    # 缺勤次数分配
    for t in s:
        Student_vec[t].absence = round(min(times * 0.8 + randint(0, 3), top))
        top -= Student_vec[t].absence
        vis[t] = True
    # print(top)
    for temp in Student_vec:
        if temp.absence != -1:
            continue
        temp.absence = min(randint(0, times * 0.3), top)
        top = top - temp.absence
    # print(top)

    now_absence = randint(0, 3)

    # print(now_absence,"555")
    out_num = 0
    in_num = now_absence
    temp = randint(0, 100)
    if now_absence == 1:

        if temp < 10:
            out_num = 1
            in_num = 0

    elif now_absence == 2:

        if temp < 5:
            out_num = 2
            in_num = 0
        elif temp < 10:
            out_num = 1
            in_num = 1

    elif now_absence == 3:
        if temp < 3:
            out_num = 3
            in_num = 0
        elif temp < 10:
            out_num = 2
            in_num = 1
        elif temp < 20:
            out_num = 1
            in_num = 2
    veci = []
    veco = []
    c = 0;
    for i in vis:
        c += 1
        # print(c)
        if i:
            veci.append(c)
        else:
            veco.append(c)
    a_veoc = veco
    for i in veci[:5]:
        Student_vec[i - 1].status = 1

    for i in veco[:out_num]:
        Student_vec[i - 1].status = 1

    index = []
    absence = []
    stu = []
    for i in Student_vec:
        # print(i.status)
        index.append(i.index)
        absence.append(i.absence)
        stu.append(i.status)

table = {"index": index, "absence": absence, "status": stu}

df = pd.DataFrame(table)
# print(df.values)
df.to_csv('../Data/data.csv', index=None)
