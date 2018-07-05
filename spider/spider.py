from bs4 import BeautifulSoup
import traceback
import random
import requests
import csv
import re
def getlocation(name):#调用百度API查询位置
    bdurl='http://api.map.baidu.com/geocoder/v2/?address='
    output='json'
    ak='bUXeEu2f0Yf3q3DTGPTIYqW6XOp6z78U'#输入你刚才申请的密匙
    callback='showLocation'
    uri=bdurl+name+'&output=t'+output+'&ak='+ak+'&callback='+callback
    res=requests.get(uri)
    s=BeautifulSoup(res.text)
    lng=s.find('lng')
    lat=s.find('lat')
    if lng:
        return lng.get_text()+','+lat.get_text()

#url='https://nj.lianjia.com/ershoufang/pg'
#url='http://waimai.meituan.com/home/wtsqrmjq1h67'
# '''headers={ 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#         'Accept-Encoding': 'gzip, deflate',
#         'Accept-Language': 'zh-CN,zh;q=0.8',
#         'Cache-Control': 'no-cache',
#         'Connection': 'keep-alive',
#         'Host': 'waimai.meituan.com',
#         # 'Cookie': cookiestr,
#         'Pragma': 'no-cache',
#         'Upgrade-Insecure-Requests': '1',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',}#请求头，模拟浏览器登陆'''
#page=list(range(0,101,1))

user_agents = [
'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
'Opera/9.25 (Windows NT 5.1; U; en)',
'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
"Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ",
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
]
headers = {'User-Agent': random.choice(user_agents)}

city = {
'湛江': 'zhanjiang'}  # '阳江': 'yj','中山': 'zs','江门': 'jm', '清远': 'qingyuan','汕尾': 'sw','广州': 'gz', '深圳': 'sz',,'肇庆':'zq', '茂名': 'mm', '潮州': 'chaozhou', '珠海': 'zh', '河源': 'heyuan', '佛山': 'fs'

def get_ip_list():
    list = open('ip.txt', 'r').read()  # 从文件中读取
    return list


def get_random_ip(ip_list):
    proxies = random.choice(ip_list)
    return proxies

ip_list = get_ip_list()
global proxies
proxies = get_random_ip(ip_list)  # 从IP池中随机选取一个IP

# 重新获取IP，并请求
def re_connection(real_url, base_url):  #
    global proxies
    request = None
    while 1:
        try:
            host = base_url
            # time.sleep(1)
            headers = {'Host': host, 'Connection': 'keep-alive', 'Origin': 'http://' + base_url,
                       'User-Agent': random.choice(user_agents), 'Accept': '*/*', 'Referer': real_url,
                       'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.8'}
            request = requests.get(real_url, headers=headers, proxies=proxies)  # 发送网络请求,
            if re.search('403 Forbidden', request.text):
                proxies = get_random_ip(ip_list)  # 403被限制访问，从IP池中重新随机选取一个IP
                continue
            break
        except:
            traceback.print_exc()
            print("ZZzzzz...")
            proxies = get_random_ip(ip_list)  # 其他错误，从IP池中重新随机选取一个IP
            print(" continue...")
            continue
    return request

send_p=[]
start_p=[]
send_t=[]
shop_n=[]
score_n=[]

#for i in page:#循环访问美团的网页
#response=requests.get(url+str(i))
url='http://waimai.meituan.com/home/wtsqrmjq1h67'
response=requests.get(url)
print(response.text)
soup=BeautifulSoup(response.text,"html.parser")
#提取起送价格
start_prices=soup.find_all('span',class_='start-price')
for price in start_prices:
    start_p.append(price.string)
print(start_p)
# 提取配送费
send_prices = soup.find_all('span', class_='send-price')
for sprice in send_prices:
    send_p.append(sprice.string)
print(send_p)
# 提取配送时间
send_times = soup.find_all('span', class_='send-time')
for tprice in send_prices:
    send_t.append(tprice.string)
print(send_t)
#提取商家名字
shop_names=soup.find_all('div',class_='name')
for s in shop_names:
    shop_n.append(s.span.string)

#提取评分
score_nums=soup.find_all('span',class_='score-num f1')
for f in score_nums:
    score_n.append(f.string)
#print(i)

#houses=[]#定义列表用于存放房子的信息
n=0
num=len(send_p)
file=open('da.csv', 'w', newline='')
headers = ['name', 'start_price', 'send_price', 'send_time',  'score_num']
writers = csv.DictWriter(file, headers)
writers.writeheader()
while n<num:#循环将信息存放进列表
    start_price=start_p[n]
    send_price=send_p[n]
    send_time=send_t[n]
    shop_name=shop_n[n]
    score_num=score_n[n]

    shop = {
        'name': '',
        'start_price': '',
        'send_price': '',
        'send_time': '',
        'score_num': ''
    }
    #将房子的信息放进一个dict中
    shop['name']=shop_name
    shop['start_price']=start_price
    shop['send_price']=send_price
    shop['send_time']= send_time
    shop['shop_name']=shop_name
    shop['score_num']=score_num
    writers.writerow(shop)#将dict写入到csv文件中
    n+=1
    print(n)
file.close()
'''
from bs4 import BeautifulSoup
import requests
import csv
import re
def getlocation(name):#调用百度API查询位置
    bdurl='http://api.map.baidu.com/geocoder/v2/?address='
    output='json'
    ak='bUXeEu2f0Yf3q3DTGPTIYqW6XOp6z78U'#输入你刚才申请的密匙
    callback='showLocation'
    uri=bdurl+name+'&output=t'+output+'&ak='+ak+'&callback='+callback
    res=requests.get(uri)
    s=BeautifulSoup(res.text)
    lng=s.find('lng')
    lat=s.find('lat')
    if lng:
        return lng.get_text()+','+lat.get_text()

url='https://nj.lianjia.com/ershoufang/pg'
heade={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}#请求头，模拟浏览器登陆
page=list(range(0,101,1))
p=[]
hi =[]
fi=[]
for i in page:#循环访问链家的网页
    response=requests.get(url+str(i))
    soup=BeautifulSoup(response.text,"html.parser")
    #提取价格
    prices=soup.find_all('div',class_='priceInfo')
    for price in prices:
        p.append(price.span.string)

    #提取房源信息
    hs=soup.find_all('div',class_='houseInfo')
    for h in hs:
        hi.append(h.get_text())

    #提取关注度
    followInfo=soup.find_all('div',class_='followInfo')
    for f in followInfo:
        fi.append(f.get_text())
    print(i)

#houses=[]#定义列表用于存放房子的信息
n=0
num=len(p)
file=open('da2.csv', 'w', newline='')
headers = ['name', 'loc', 'style', 'size', 'price', 'foc']
writers = csv.DictWriter(file, headers)
writers.writeheader()
while n<num:#循环将信息存放进列表
    h0=hi[n].split('|')
    name=h0[0]
    loc=getlocation(name)
    style = re.findall(r'\s\d.\d.\s', hi[n])#用到了正则表达式提取户型
    if style:
        style=style[0]
    size=re.findall(r'\s\d+\.?\d+',hi[n])#用到了正则表达式提取房子面积
    if size:
        size=size[0]
    price=p[n]
    foc=re.findall(r'^\d+',fi[n])[0]##用到了正则表达式提取房子的关注度
    house = {
        'name': '',
        'loc': '',
        'style': '',
        'size': '',
        'price': '',
        'foc': ''
    }
    #将房子的信息放进一个dict中
    house['name']=name
    house['loc']=loc
    house['style']=style
    house['size']=size
    house['price']=price
    house['foc']=foc
    writers.writerow(house)#将dict写入到csv文件中
    n+=1
    print(n)
file.close()'''