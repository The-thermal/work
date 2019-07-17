import scipy
import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import norm
import math

direction_dic = {'北':0,'南':1,'西':2,'东':3,'东北':4,'西北':5,'东南':6,'西南':7,'北偏东':8,'北偏西':9,'东偏北':10,'东偏南':11,'南偏东':12,'南偏西':13,'西偏南':14,'西偏北':15}
p = np.pi
cos_theta = np.cos(1/8*np.pi)
sin_theta = np.sin(1/8*np.pi)
wind_xaix_angle = [1.5*p,0.5*p,0,p,5*p/4,7*p/4,0.75*p,0.25*p,1.375*p,1.625*p,1.125*p,0.875*p,0.625*p,0.375*p,0.125*p,1.875*p]
Orthogonal_ListOfWindVector = [[1,0],[-1,0],[0,1],[0,-1],[1,-1],[1,1],[-1,-1],[-1,1],[cos_theta,-sin_theta],[cos_theta,sin_theta],[sin_theta,-cos_theta],[-sin_theta,-cos_theta],[-cos_theta,-sin_theta],[-cos_theta,sin_theta],[-sin_theta,cos_theta],[sin_theta,cos_theta]]
OD_list_set_1 = [[11,12],[13,14],[28,29],[26,27],[30,25],[31,32],[21,20],[19,35]]
OD_list_set = [[1,2],[3,4],[5,6],[7,8],[10,33],[16,33],[15,22],[17,23],[22,23],[23,18],[7,9],[22,25],[34,24]]


def vector_length(vector):
    Lx=np.sqrt(vector.dot(vector.T))
    return Lx
def shift_road(x1,y1,x2,y2,wind):
    o_vector = Orthogonal_ListOfWindVector[direction_dic[wind]]
    Orthogonal_dir = np.array([o_vector])/np.sqrt(o_vector[0]**2+o_vector[1]**2)
    #风向向量的正交向量并将其单位化
    line_dir = np.array([[x2-x1,y2-y1]])
    Lx=np.sqrt(Orthogonal_dir.dot(Orthogonal_dir.T))
    Ly=np.sqrt(line_dir.dot(line_dir.T))
    cos_angle= (Orthogonal_dir.dot(line_dir.T))/(Lx*Ly)
    #求出路与正交向量夹角
    touying = Ly*cos_angle/2*Orthogonal_dir
    #将路投影到风向量法向向量上
    x2_new = (x1+x2)/2+touying[0][0]
    y2_new = (y1+y2)/2+touying[0][1]
    x1_new = (x1+x2)/2-touying[0][0]
    y1_new = (y1+y2)/2-touying[0][1]
    #在原坐标系中计算出路投影向量的两端坐标
    return x1_new,y1_new,x2_new,y2_new
# x_aim = -29062528.194120   
# y_aim = 235.466633
def shift_coordinate(x_center,y_center,x_aim,y_aim,wind):
    direction_dic = {'北':0,'南':1,'西':2,'东':3,'东北':4,'西北':5,'东南':6,'西南':7}
    wind_angle = [1.5*np.pi,0.5*np.pi,0,np.pi,5*np.pi/4,7*np.pi/4,0.75*np.pi,0.25*np.pi]
    #基本信息
    w_angle = wind_angle[direction_dic[wind]]
    x = (x_aim-x_center)*np.cos(w_angle)+(y_aim-y_center)*np.sin(w_angle)
    y = (y_aim-y_center)*np.cos(w_angle)-(x_aim-x_center)*np.sin(w_angle)
    return x,y


def Gaussian_puff(x,y,q,t,u,point):#point = length_shift
    if x<0:
        concentration = 0
    else:
        H = 0.2
        z = 18 
        sigmay = 0.11*x*((1+0.0004*x)**(-1/2))
        sigmax = sigmay 
        sigmaz = 0.08*x*((1+0.00015*x)**(-1/2))
        b1 = -1*((x-u*t)**2)/(2*sigmax**2)
        B = math.exp(b1)
        a1 = -1*((z-H)**2)/(2*sigmaz**2)
        a2 = -1*((z+H)**2)/(2*sigmaz**2)
        A = math.exp(a1)+math.exp(a2)
        concentration =  q/(2*math.pi*sigmax*sigmaz)*B*A*(norm.cdf(point/sigmay)-norm.cdf(0))
    return concentration


def calculate(x1,y1,x2,y2,q,u,wind):
    shift_road(x1,y1,x2,y2,wind)

    
def how_far(point1x,point1y,point2x,point2y):
    x_recept = 235.466633
    y_recpet = -29062528.194120  
    a = point2y-point1y
    b = point1x-point2x
    c = point1y*(point2x-point1x)-(point2y-point1y)*point1x
    distance = np.abs((a*x_recept+b*y_recpet+c)/np.sqrt(a**2+b**2))
    return distance




