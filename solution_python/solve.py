from operator import index
from grpc import Status
from matplotlib.pyplot import cla
import numpy as np
import pandas as pd
import math


class Student:
    index = 0
    absence = 0
    status = 0

    def __init__(self, a, b, c):
        self.index = a
        self.absence = b
        self.status = c


# %%


def Read_data():
    Student_vec = []
    df = pd.read_csv("./data.csv")
    for row in df.iterrows():
        Student_vec.append(Student(row[1][0], row[1][1], row[1][2]))
    return Student_vec


# %%


from site import abs_paths
from time import process_time_ns

def solve():
    # st = Student
    Student_vec = Read_data()
    new_vec = sorted(Student_vec, key=lambda x: x.absence, reverse=True)

    lim = 5
    ask = 0
    absence = 0
    s_index = []
    s_absence = []
    s_status = []
    for i in new_vec:

        s_index.append(i.index)
        s_absence.append(i.absence)
        s_status.append(i.status)
        ask += 1
        absence += i.status
        if ask == 8:
            break


    return (absence / ask)

# %%

# c = 0
# for i in Student_vec:
#     if i.status > 0:
#         c += 1
#     # print(i.status)
# # print("---------")
# for i in new_vec:
#     print(i.index, i.absence, i.status)