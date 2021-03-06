# 爬取大众点评外卖商家数据
# 1.设计思路
（1）获取外卖商家数据
由于大众点评在输入搜索内容后，最多显示50页的搜索结果。为了获得更多的商家外卖数据，我采取分区爬取数据的方法，即先分别获取江宁区、建邺区、鼓楼区、浦口区、雨花台区、高淳区、栖霞区、玄武区、溧水区、秦淮区、六合区的外卖商家数据页面。然后利用BeautifulSoup包解析页面，得到外卖商家的店名和地址。利用百度地图API可以根据商家地址得到对应的经纬度。然后将商家名字、地址和经纬度写入csv文件中，用于后续数据处理。
（2）将数据处理成百度地图热力图API需要的格式
首先从csv文件中读出商家的经度、纬度，存在一个二维数组result中。接着因为实验最终需要显示南京市每个区域的外卖商家数量热力图，所以需要先对南京市进行地图建模，也就是将南京市划分成网格状。本次实验中我将南京市分成了大小相同的400个区域，并计算出每个区域中心的经纬度，存在一个二维数组locat中。然后将每个商家的经纬度与各个区域中心的经纬度比较，计算出每个区域的商家数量。
由于百度地图制作热力图的数据格式是固定的，所以需要将商家数据处理成下列格式。
var points =[ {"lng":经度,"lat":纬度,"count":数值}, 
{"lng":经度,"lat":纬度,"count":数值}, 
...
  ]

于是，我们就把每个区域中心的商家数量作为count值，并和该区域中心的经度、纬度组成字典，然后将所有字典写入数组points中，这样就得到了热力图的数据。由于最后的热力图绘制需要在html页面完成，所以最后还需要将数组points中的内容写入json文件中，便于前台页面调用数据展示热力图。
（3）绘制热力图
    新建一个html文件，利用百度API提供的绘制热力图的方法，导入事先处理好的json数据，绘制热力图。由于绘制南京市外卖商家数据热力图，所以要修改BMap.Point中的值为南京市中心的值，修改级别为12。
# -
