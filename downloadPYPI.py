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
        print(len(files))  # 当前路径下所有非目录子文件
        a = 1
        for filename in files:
            # 读取依赖包名称
            name = filename.split(".")[0]
            # 创建依赖包对应存放路径
            if os.path.exists("./packages/" + name):
                print("路径已存在")
            else:
                os.mkdir("./packages/" + name)
            print("当前进度为：",str((a/len(files))*100)+"%")
            a = a + 1
            # 读取依赖包全部URL
            data = pd.read_csv(file_dir + filename, header=None)
            if len(data) >=26:
                data = data
            else:
                pass
            for i in range(len(data)):
                data_name = str(data.iloc[i, 0]).split("/")[-1]
                print(data_name)
                # 访问URL连接，将文件保存
                filepath = "./packages/" + name + "/" + data_name
                if os.path.exists(filepath):
                    print("文件已存在")
                else:
                    try:
                        urllib.request.urlretrieve(data.iloc[i, 0], filepath)
                    except:
                        with open("testname.txt","a+") as f:
                            f.write("{}".format(str(data.iloc[i, 0])))
                    # 礼貌延时
                    sleep(2)
                # urllib.request.urlretrieve(data.iloc[i,0])


file_name("./packages_name/")
