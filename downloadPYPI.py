# -*- coding: utf-8 -*-  
import os
import urllib.request
import pandas as pd
import ssl
from time import sleep
ssl._create_default_https_context = ssl._create_unverified_context


def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print(root)  # 当前目录路径
        print(dirs)  # 当前路径下所有子目录
        print(files)  # 当前路径下所有非目录子文件
        for filename in files:
            # 读取依赖包名称
            name = filename.split(".")[0]
            # 创建依赖包对应存放路径
            if os.path.exists("./packages/" + name):
                print("路径已存在")
            else:
                os.mkdir("./packages/" + name)
            # 读取依赖包全部URL
            data = pd.read_csv(file_dir + filename, header=None)
            for i in range(len(data)):
                data_name = str(data.iloc[i, 0]).split("/")[-1]
                # 访问URL连接，将文件保存
                urllib.request.urlretrieve(data.iloc[i, 0], "./packages/" + name + "/" + data_name)
                # 礼貌延时
                sleep(1)
                # urllib.request.urlretrieve(data.iloc[i,0])


file_name("./packages_name/")
