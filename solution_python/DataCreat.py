"""
@FileName：DataCreat.py\n
@Description：\n
@Author：NZQ\n
@Time：2022/10/7 16:24\n
"""

"""
this file is used in creating data
"""
from random import  randint
import pandas as pd
import numpy as np
import os
import sys
import random

path = "../Data/"
data_demo_path = "demo1.csv"
class Student:
    index = 0
    absence = -1
    status = 0
    def __init__(self):
        self.index = 0
        self.absence = -1
        self.statu = 0



def set_is_empty(a):
    if a == set():
        return True
    else:
        return False

Student_vec =  []
vis = [0]*1000
if __name__ == '__main__':
    times = 20
    n = 90
    top = times*10
    st = Student

    for i in range(1,n+1):
        st.index = i
        Student_vec.append(st)

    absence_num = 5+random.randint(0,3)
    s = set()
    while (len(s)<absence_num):
        s.add(randint(n)+1)
    while not set_is_empty(s):
        idx = 




