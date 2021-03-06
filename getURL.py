import requests
import bs4
import pandas as pd
from time import sleep
import os
url = "https://pypi.tuna.tsinghua.edu.cn/simple/"
name = "./requirements.txt"
name1 = "./a.txt"
data = pd.read_csv(name1, header=None)

if os.path.exists("./packages/"):
    print("packages路径已存在")
else:
    os.mkdir("./packages/")

if os.path.exists("./packages_name/"):
    print("packages_name路径已存在")
else:
    os.mkdir("./packages_name/")



for i in range(len(data)):
    url_path = url + str(data.iloc[i, 0])
    # 获取依赖包的返回信息
    htext = requests.get(url_path).text
    bobj = bs4.BeautifulSoup(htext)
    j = []
    for a in bobj.find_all('a'):
        if "cp36" in str(a['href']) or "zip" in str(a['href']) or "py3" in str(a['href']) or "tar" in str(a['href']):
            if "macosx" in str(a['href']) or "i686" in str(a['href']) or "win32" in str(a['href']):
                pass
            else:
                j.append(str(a['href']).replace("../..", "https://pypi.tuna.tsinghua.edu.cn/").split("#")[0])
    url_con = pd.DataFrame(j)
    # 将每个依赖包对应的下载连接写入同名的TXT中
    url_con.to_csv("./packages_name/" + str(data.iloc[i, 0]) + ".txt", index=None, header=None)
    print("进度为：",i/len(data))
    print(str(data.iloc[i, 0]))
    # 为了礼貌延时1秒
    sleep(2)
