
import csv
import json
import random

locat=[]

result=[]
#读入江宁区商家经纬度
with open('test.csv','r',encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]
for row in rows:
    loc=row[2]
    sloc=loc.split(',')
    lng=''
    lat=''
    if len(sloc)==2:#第一行是列名需要做判断
        lng=sloc[0]    # 经度
        lat=sloc[1]    # 纬度
        result.append([float(lng),float(lat)])
#读入高淳数据
with open('gaochun.csv','r',encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]
for row in rows:
    loc=row[2]
    sloc=loc.split(',')
    lng=''
    lat=''

    if len(sloc)==2:#第一行是列名需要做判断
        lng=sloc[0]
        lat=sloc[1]
        result.append([float(lng), float(lat)])
#读入六合数据
with open('LiuHe.csv','r',encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]
for row in rows:
    loc=row[2]
    sloc=loc.split(',')
    lng=''
    lat=''

    if len(sloc)==2:#第一行是列名需要做判断
        lng=sloc[0]
        lat=sloc[1]
        result.append([float(lng), float(lat)])
#读入鼓楼数据
with open('GuLou.csv','r',encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]
for row in rows:
    loc=row[2]
    sloc=loc.split(',')
    lng=''
    lat=''

    if len(sloc)==2:#第一行是列名需要做判断
        lng=sloc[0]
        lat=sloc[1]
        result.append([float(lng), float(lat)])
#读入溧水数据
with open('LiShui.csv','r',encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]
for row in rows:
    loc=row[2]
    sloc=loc.split(',')
    lng=''
    lat=''

    if len(sloc)==2:#第一行是列名需要做判断
        lng=sloc[0]
        lat=sloc[1]
        result.append([float(lng), float(lat)])
#读入雨花台区数据
with open('YuHuaTai.csv','r',encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]
for row in rows:
    loc=row[2]
    sloc=loc.split(',')
    lng=''
    lat=''

    if len(sloc)==2:#第一行是列名需要做判断
        lng=sloc[0]
        lat=sloc[1]
        result.append([float(lng), float(lat)])
#读入栖霞区数据
with open('QiXia.csv','r',encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]
for row in rows:
    loc=row[2]
    sloc=loc.split(',')
    lng=''
    lat=''

    if len(sloc)==2:#第一行是列名需要做判断
        lng=sloc[0]
        lat=sloc[1]
        result.append([float(lng), float(lat)])
#读入建邺区数据
with open('JianYe.csv','r',encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]
for row in rows:
    loc=row[2]
    sloc=loc.split(',')
    lng=''
    lat=''

    if len(sloc)==2:#第一行是列名需要做判断
        lng=sloc[0]
        lat=sloc[1]
        result.append([float(lng), float(lat)])
#读入玄武区数据
with open('XuanWu.csv','r',encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]
for row in rows:
    loc=row[2]
    sloc=loc.split(',')
    lng=''
    lat=''

    if len(sloc)==2:#第一行是列名需要做判断
        lng=sloc[0]
        lat=sloc[1]
        result.append([float(lng), float(lat)])
#读入浦口区数据
with open('PuKou.csv','r',encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]
for row in rows:
    loc=row[2]
    sloc=loc.split(',')
    lng=''
    lat=''

    if len(sloc)==2:#第一行是列名需要做判断
        lng=sloc[0]
        lat=sloc[1]
        result.append([float(lng), float(lat)])
#读入秦淮区数据
with open('QinHuai.csv','r',encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]
for row in rows:
    loc=row[2]
    sloc=loc.split(',')
    lng=''
    lat=''

    if len(sloc)==2:#第一行是列名需要做判断
        lng=sloc[0]
        lat=sloc[1]
        # count=1   #生成0-99的随机数设置count
        # temp_dict={}
        # temp_dict['lng'] = lng
        # temp_dict['lat'] = lat
        # temp_dict['count'] = count  # 概率
        # result.append(temp_dict)
        result.append([float(lng), float(lat)])



if __name__ == '__main__':
    lng_left = 118.36666666666666  # 南京经度范围
    lng_right = 119.23333333333333
    lat_left = 31.233333333333334  # 南京纬度范围
    lat_right = 32.6
    span_lng = (lng_right - lng_left) / 40
    span_lat = (lat_right - lat_left) / 40
    #将南京划分成400个区域，并求出400个区域中心经纬度，存入二维数组locat中
    for i in range(1, 41, 2):
        for j in range(1, 41, 2):
            locat.append([lng_left + span_lng * i, lat_left + span_lat * j])

    #统计每个区域内外卖商家数量
    points = []
    for i in range(0,400):
        count = 0
        for j in range(0,len(result)-1):
            if (result[j][0]>locat[i][0]-span_lng)&(result[j][0]<locat[i][0]+span_lng)&\
                    (result[j][1]>locat[i][1]-span_lat)&(result[j][1]<locat[i][1]+span_lat):
                count=count+1
        temp_dict = {}
        temp_dict['lng'] =locat[i][0]   #经度
        temp_dict['lat'] = locat[i][1]  #纬度
        temp_dict['count'] = count      #商家数目
        points.append(temp_dict)

    with open('data.json', 'w') as f:
         json.dump(points, f)

