from wind_condition import get_wind_1
from trafic_condition import get_duration_1
import gaussian_puff_function
from gaussian_puff_function import shift_road
from gaussian_puff_function import shift_coordinate
from gaussian_puff_function import Gaussian_puff
from gaussian_puff_function import vector_length
from gaussian_puff_function import how_far
import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import norm
import math

array = pd.read_csv('position.csv',encoding= 'gbk')
road_duration = pd.DataFrame (np.zeros((2,17)),index = (1,-1),columns = range(1,18),dtype=np.float64)
road_length = pd.DataFrame (np.zeros((1,17)),columns = range(1,18),dtype=np.float64)
OD_list_set = [[1,2],[2,1],[3,4],[4,3],[5,6],[6,5],[7,8],[8,7],[10,33],[33,10],[16,33],[33,16],[15,22],[22,15],[17,23],[23,17],[22,23],[23,22],[23,18],[18,23],[7,9],[9,7],[22,25],[25,22],[34,24],[24,34],[11,12],[13,14],[28,29],[26,27],[30,25],[31,32],[21,20],[19,35]]
road_name_dic = {(1,1):0,(1,-1):1,(2,1):2,(2,-1):3,(3,1):4,(3,-1):5,(4,1):6,(4,-1):7,(5,1):8,(5,-1):9,(6,1):10,(6,-1):11,(7,1):12,(7,-1):13,(8,1):14,(8,-1):15,(9,1):16,(9,-1):17,(10,1):18,(10,-1):19,(11,1):20,(11,-1):21,(12,1):22,(12,-1):23,(13,1):24,(13,-1):25,(14,1):26,(14,-1):27,(15,1):28,(15,-1):29,(16,1):30,(16,-1):31,(17,1):32,(17,-1):33}




def sys():
    # if float(get_wind_1()[1]) == 0:
    #     print('1')
        
    # else:
    shift_position = pd.DataFrame (np.zeros((2,35)),index = ('x','y'),columns = range(1,36),dtype=np.float64)
    #print(shift_position)
    scale_1 =0
    for i in range(1,18):
        squence = road_name_dic[(i,1)]
        position_1 = OD_list_set[squence][0]
        position_2 = OD_list_set[squence][1]
        x1 = float(array.iloc[position_1-1,4].split(',',1)[0])
        y1 = float(array.iloc[position_1-1,4].split(',',1)[1])
        x2 = float(array.iloc[position_2-1,4].split(',',1)[0])
        y2 = float(array.iloc[position_2-1,4].split(',',1)[1])
        wind = get_wind_1()[0]
        #print(i,shift_coordinate((x2+x1)/2,(y1+y2)/2,235.466633,-29062528.194120,wind),wind)
        #print(position_1,x1,y1,position_2,x2,y2,wind)
        #shift_road(x1,y1,x2,y2,wind)
        shift_position.loc['x',position_1] = shift_road(x1,y1,x2,y2,wind)[0]
        shift_position.loc['y',position_1] = shift_road(x1,y1,x2,y2,wind)[1]
        shift_position.loc['x',position_2]= shift_road(x1,y1,x2,y2,wind)[2]
        shift_position.loc['y',position_2] = shift_road(x1,y1,x2,y2,wind)[3]
        # print(shift_coordinate((x1+x2)/2,(y1+y2)/2,235.466633,-29062528.194120,wind))
        # print(shift_road(x1,y1,x2,y2,wind))
        # print(how_far(shift_road(x1,y1,x2,y2,wind)[0],shift_road(x1,y1,x2,y2,wind)[1],shift_road(x1,y1,x2,y2,wind)[2],shift_road(x1,y1,x2,y2,wind)[3]))
        # print(scale_1)
        if i == 1:
            dd = math.sqrt((x2-x1)**2+(y2-y1)**2)
            scale_1 = (416)/dd
            #print(scale_1)
            #以米计    
            dis = np.sqrt((x2-x1)**2+(y2-y1)**2)
            print(dis*scale_1)    
        else:
            dis = np.sqrt((x2-x1)**2+(y2-y1)**2)
            print(dis*scale_1)  
        
sys()

