"""
@FileName：main.py\n
@Description：\n
@Author：NZQ\n
@Time：2022/10/11 12:53\n
"""
import numpy
import pandas as pd
from matplotlib import pyplot as plt
import Creat_data,solve
if __name__ == '__main__':

       sum = 0
       e_l = []
       num = 40
       for i in  range(0,num):
               Creat_data.Creat_data()
               e =  solve.solve()
               e_l.append(e)
               sum +=e

       ave = sum/num
       print('点名开始...\n')
       print('五门课程平均e值：',ave)
       #
       # Se = pd.Series(e_l)
       # print(Se)
       # Se.plot()
       #

       fig = plt.figure()
       ax = fig.add_subplot(1,1,1)
       ax.plot(e_l)
       plt.show()
       plt.savefig('../Data/p1.jpg')