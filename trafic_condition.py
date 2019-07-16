import pandas as pd
import numpy as np
import requests
import json
import time 
import os

array = pd.read_csv('position.csv',encoding= 'gbk')
road_duration = pd.DataFrame (np.zeros((2,17)),index = (1,-1),columns = range(1,18),dtype=np.float64)
road_length = pd.DataFrame (np.zeros((1,17)),columns = range(1,18),dtype=np.float64)

OD_list_set_1 = [[11,12],[13,14],[28,29],[26,27],[30,25],[31,32],[21,20],[19,35]]
OD_list_set = [[1,2],[3,4],[5,6],[7,8],[10,33],[16,33],[15,22],[17,23],[22,23],[23,18],[7,9],[22,25],[34,24]]

def get_time():
    timenow=time.strftime("%Y-%m-%d-%H.%M.%S",time.localtime())
    return timenow
def get_road_info(ODList):
    oringin_url ='https://restapi.amap.com/v3/direction/driving?output=json&origin='
    destination_url ='&destination='
    key ='&extensions=all&output=xml&key=ad6ae7907e8cf8f6fb9209a268fa80f1'
    url =oringin_url+array.loc[ODList[0]-1,'高德地图经纬度']+destination_url+array.loc[ODList[1]-1,'高德地图经纬度']+key
    #print(url)
    try:
        r=requests.get(url)
        r_json = json.loads(r.text)
        paths =r_json['route']['paths'][0]
        distance = paths['distance']
        duration = paths['duration']
    except:
        pass
    # OD_metrix.loc[ODList[0],ODList[1]] = duration
    # distance_metrix.loc[ODList[0],ODList[1]] = distance
    return duration,distance
def reverse(ODList):
    oringin_url ='https://restapi.amap.com/v3/direction/driving?output=json&origin='
    destination_url ='&destination='
    key ='&extensions=all&output=xml&key=ad6ae7907e8cf8f6fb9209a268fa80f1'
    url =oringin_url+array.loc[ODList[1]-1,'高德地图经纬度']+destination_url+array.loc[ODList[0]-1,'高德地图经纬度']+key
    #print(url)
    try:
        r=requests.get(url)
        r_json = json.loads(r.text)
        paths =r_json['route']['paths'][0]
        duration_1 = paths['duration']
        distance = paths['distance']
    except:
        pass
    # OD_metrix.loc[ODList[1],ODList[0]] = duration_1
    # distance_metrix.loc[ODList[1],ODList[0]] = distance
    return duration_1,distance
def get_duration():
    start = time.time()
    k=0
    c=0
    for i in range(0,13):
        road_duration.iloc[0,i] = get_road_info(OD_list_set[i])[0]
        road_length.iloc[0,i] = get_road_info(OD_list_set[i])[1]
        road_duration.iloc[1,i] = reverse(OD_list_set[i])[0]
    for j in range(0,8,2):
        road_duration.iloc[0,13+k] = get_road_info(OD_list_set_1[j])[0]
        road_length.iloc[0,13+k] = get_road_info(OD_list_set_1[j])[1]
        k=k+1
    for b in range(1,8,2):
        road_duration.iloc[1,13+c] = get_road_info(OD_list_set_1[b])[0]
        c=c+1
    try:
        os.mkdir('traffic_condition')
        #print('flag =1')
    except:
        pass
        #print('flag =2')
    try:
        road_duration.to_csv('traffic_condition/D_'+get_time()+'.csv')
        road_length.to_csv('traffic_condition/L_'+get_time()+'.csv')
        print(get_time()+'success!!totally use :'+str(time.time()-start))
        return 1
    except:
        pass
        

def get_duration_1():
    k=0
    c=0
    for i in range(0,13):
        road_duration.iloc[0,i] = get_road_info(OD_list_set[i])[0]
        road_length.iloc[0,i] = get_road_info(OD_list_set[i])[1]
        road_duration.iloc[1,i] = reverse(OD_list_set[i])[0]
    for j in range(0,8,2):
        road_duration.iloc[0,13+k] = get_road_info(OD_list_set_1[j])[0]
        road_length.iloc[0,13+k] = get_road_info(OD_list_set_1[j])[1]
        k=k+1
    for b in range(1,8,2):
        road_duration.iloc[1,13+c] = get_road_info(OD_list_set_1[b])[0]
        c=c+1
    return road_duration,road_length

        




# def test(list):
#     oringin='https://restapi.amap.com/v3/direction/driving?output=json&origin='
#     destination ='&destination='
#     key ='&extensions=all&output=xml&key=ad6ae7907e8cf8f6fb9209a268fa80f1'
#     url =oringin+array.loc[list[0]-1,'高德地图经纬度']+destination+array.loc[list[1]-1,'高德地图经纬度']+key
#     r=requests.get(url)
#     r_json = json.loads(r.text)
#     print(r_json)

