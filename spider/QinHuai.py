import requests
import time
import random
from bs4 import BeautifulSoup
import sys
import importlib
importlib.reload(sys)  #设置系统的编码为utf8，便于输入中文,>3.3版本的写法

def getlocation(name):#调用百度API查询位置
    bdurl='http://api.map.baidu.com/geocoder/v2/?address='
    output='json'
    ak='bUXeEu2f0Yf3q3DTGPTIYqW6XOp6z78U'  #输入申请的密匙
    callback='showLocation'
    uri=bdurl+name+'&output=t'+output+'&ak='+ak+'&callback='+callback
    res=requests.get(uri)
    s=BeautifulSoup(res.text)
    lng=s.find('lng')
    lat=s.find('lat')
    if lng:
        return lng.get_text()+','+lat.get_text()

header = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.9',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Cookie':'navCtgScroll=0; _lxsdk_cuid=1639f0b1318c8-0041da13dff894-d35346d-1fa400-1639f0b1319c8; _lxsdk=1639f0b1318c8-0041da13dff894-d35346d-1fa400-1639f0b1319c8; _hc.v=58389d39-ff71-2061-f8a5-9fdfcd24bc60.1527381693; s_ViewType=10; ua=dpuser_9757271275; ctu=996e5600e78c8cf16de1bb5d20c3a83d08d75173635324bdce6d80f033fd09cb; cy=5; cye=nanjing; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_s=163b12ab452-fe4-139-1d8%7C%7C141',
'Host':'www.dianping.com',
'Referer':'http://www.dianping.com/search/keyword/5/10_%E7%A7%A6%E6%B7%AE%E5%8C%BA',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
}

shop_addr=[]  #存放商家地址
shop_n=[]    #存放商家名字
loc_n=[]     #存放商家地址

page=list(range(1,51,1))
url='http://www.dianping.com/search/keyword/5/10_%E7%A7%A6%E6%B7%AE%E5%8C%BA/p'   #秦淮区
for i in page:
    html1 = requests.get(url+str(i)+'m6', headers=header).content
    soup1 = BeautifulSoup(html1, "html.parser")
    # 提取商家名字
    shop_names = soup1.find_all('div', class_='tit')
    for s in shop_names:
        shop_n.append(s.h4.string)


    #提取商家评分
    '''comment_scores=soup1.find_all('span', class_='comment-list')
    for spantag in comment_scores:
        blist = spantag.find_all('b')  # 在每个span标签下,查找所有的b标签
        score=(float(blist[0].string)+float(blist[1].string)+float(blist[2].string))/3 #取口味评分、环境评分、服务评分的平均值，作为后续热力图的count 值标准
        comment_s.append(score)'''


    # 提取商家地址
    shop_address = soup1.find_all('span', class_='addr')
    for a in shop_address:
        shop_addr.append(a.string)
        loc = getlocation(a.string)
        loc_n.append(loc)

    time.sleep(3 + random.uniform(1, 3))   #随机睡眠一段时间，再取爬取数据，模拟人为浏览，防止ip被封

#将信息写入csv文件
import pandas as pd

#字典中的key值即为csv中列名
dataframe = pd.DataFrame({'shop_name':shop_n,'shop_address':shop_addr,'location':loc_n})

#将DataFrame存储为csv,index表示是否显示行名，default=True
dataframe.to_csv("QinHuai.csv",index=False, sep=',')