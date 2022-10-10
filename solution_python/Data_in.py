"""
@FileName：Data_in.py\n
@Description：\n
@Author：NZQ\n
@Time：2022/10/7 16:23\n
"""
import pandas as pd

path1 = "./Data/demo1.csv"


def read_data():
    df = pd.read_csv(path1)
    return df

if __name__ == '__main__':
    read_data()