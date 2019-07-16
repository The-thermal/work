import requests
from bs4 import BeautifulSoup
import time
import os
import re

headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive'}
def get_time():
    timenow=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    return timenow
def get_wind():
    try:
        url = 'https://www.haotq.com/c_chengdu.html'
        html = requests.get(url,headers=headers,timeout=30)
        html.encoding = 'utf-8'
        pro_html = BeautifulSoup(html.text,'lxml')
        table1 = pro_html.find('div',{'id':'divccbar'}).find('table',{'id':'foreccr'}).find_all('tr')
        td1 = table1[2].find_all('td')
        span1 = td1[0].find_all('span')
        # span1[0].text#风向
        # span1[1].text#风向数值
        td2 = table1[4].find_all('td')
        span2 = td2[0].find_all('span')
        # span2[0].text#风速
        # span2[1].text#风速数值
        td3 = table1[6].find_all('td')
        span3 = td3[0].find_all('span')
        # span3[0].text#湿度
        # span3[1].text#湿度数值
        table2 = pro_html.find('div',{'id':'divccbar'}).find('table',{'id':'foreccl'}).find_all('tr')
        td4 = table2[2].find_all('td')
        # print(td4[0].text)
        number1 = span2[1].text
        number1 = re.sub("\D","",number1)
        number2 = td4[0].text
        number2 = re.sub("\D","",number2)
        number3 = span3[1].text
        number3 = re.sub("\D","",number3)
        #print(number1,number2,number3)
        data_list = [span1[1].text,number1,number2,number3]#风向，风速，温度，湿度
    except:
        pass
    try:
        os.makedir('traffic_condition')
    except:
        pass
    try:
        f=open('traffic_condition/wheather.txt','a',encoding='utf-8')
        f.write(get_time()+' '+data_list[0]+' '+str(data_list[1])+' '+str(data_list[2])+' '+str(data_list[3])+'\r\n')
        f.close()
        print('success write wheather'+get_time())
    except:
        print('wrong can not write')


def get_wind_1():
    try:
        url = 'https://www.haotq.com/c_chengdu.html'
        html = requests.get(url,headers=headers,timeout=30)
        html.encoding = 'utf-8'
        pro_html = BeautifulSoup(html.text,'lxml')
        table1 = pro_html.find('div',{'id':'divccbar'}).find('table',{'id':'foreccr'}).find_all('tr')
        td1 = table1[2].find_all('td')
        span1 = td1[0].find_all('span')
        # span1[0].text#风向
        # span1[1].text#风向数值
        td2 = table1[4].find_all('td')
        span2 = td2[0].find_all('span')
        # span2[0].text#风速
        # span2[1].text#风速数值
        td3 = table1[6].find_all('td')
        span3 = td3[0].find_all('span')
        # span3[0].text#湿度
        # span3[1].text#湿度数值
        table2 = pro_html.find('div',{'id':'divccbar'}).find('table',{'id':'foreccl'}).find_all('tr')
        td4 = table2[2].find_all('td')
        # print(td4[0].text)
        number1 = span2[1].text
        number1 = re.sub("\D","",number1)
        number2 = td4[0].text
        number2 = re.sub("\D","",number2)
        number3 = span3[1].text
        number3 = re.sub("\D","",number3)
        #print(number1,number2,number3)
        data_list = [span1[1].text,number1,number2,number3]#风向，风速，温度，湿度
    except:
        pass
    return span1[1].text,number1,number2,number3
#print(get_wind_1())