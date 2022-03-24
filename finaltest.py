#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 10:23:50 2022

@author: haohankao
"""


import requests
response = requests.get('https://api.t1league.basketball/season/1/stages/2/rosters')
data = response.json()
teamName=data[0]['team_name_alt']
#dea_players=[]
#dea_players_average=[] 
#number=[]
player_score=[]
average_mins=[]
average_blk=[]
for i in data:
    team=i['team_name_alt']
    name=i['name_alt']
    a_score=i['average']['points']
    t_second=i['average']['seconds']
    a_blk=i['average']['blk']
    if team  =='新北中信特攻':
       average_blk.append(a_blk)

print(average_blk)
   
import numpy as np
average_blk=np.array([0, 0.0666666667, 0.2142857143, 0, 0, 0.0952380952, 0.5714285714, 0, 0, 0, 0.1176470588, 0.8571428571, 2.4666666667, 0.75, 0.8333333333, 0.75])
print(average_blk.round(2))

'average_blk'=[0.   0.07 0.21 0.   0.   0.1  0.57 0.   0.   0.   0.12 0.86 2.47 0.75
 0.83 0.75]

import requests
response = requests.get('https://api.t1league.basketball/season/1/stages/2/rosters')
data = response.json()
teamName=data[0]['team_name_alt']
dea_players=[]
for i in data:
    team=i['team_name_alt']
    name=i['name_alt']
    if team  =='新北中信特攻':
        dea_players.append(name)



'dea_players':['李學林', '林秉聖', '魏嘉豪', '呂濟而', '東方譯慷', '謝亞軒', '阿巴西','劉韋辰', '劉旻諺', '周承睿', '譚傑龍', '馬龍', '伊布', '查拉帝', '厄力', '艾斯'] 
'player_score':[[0, 11.7333333333, 3.2857142857, 6.95, 2.25, 11, 22.85, 1.3846153846, 4, 2, 3.75, 15.85, 7.8, 5.6315789474, 27.5833333333, 3.3333333333]]
'averagemin':[[ 0, 31, 16, 26,  6, 25, 37, 4, 2, 6, 15, 38, 24, 23, 28, 16]


#算平均上場時間 api拿到的是秒數 必須換算成分鐘 然後把餘數拿掉
import numpy as np
average_mins=np.array([0, 1885, 971.7857142857, 1618.85, 398.75, 1542.45, 2225.9, 298.3846153846, 138, 374.5, 949.5, 2338.15, 1474.5333333333, 1399.3684210526, 1710.5833333333, 980, 0, 0, 0])
c=np.array([60])

print (np.floor_divide(average_mins,c))

#把平均上場時間除以球員平均得分
import numpy as np
player_score =np.array([0, 11.7333333333, 3.2857142857, 6.95, 2.25, 11, 22.85, 1.3846153846, 4, 2, 3.75, 15.85, 7.8, 5.6315789474, 27.5833333333, 3.3333333333])

averagemin =np.array([0, 31, 16, 26, 6, 25,37,  4, 2, 6, 15, 38, 24, 23, 28, 16])

print(np.divide(player_score,averagemin))

# 取 小數點第二位每分鐘得分 
import numpy as np
average_mins_score=np.array([0, 0.37849462, 0.20535714, 0.26730769,0.375, 0.44, 0.61756757, 0.34615385, 2, 0.33333333, 0.25, 0.41710526, 0.325, 0.24485126, 0.98511905, 0.20833333])

print(average_mins_score.round(2))

average_mins_score=[0. 0.38 0.21 0.27 0.38 0.44 0.62 0.35 2. 0.33 0.25 0.42 0.32 0.24
 0.99 0.21]

#dataframe 

import pandas as pd
data = {'dea_players':['李學林', '林秉聖', '魏嘉豪', '呂濟而', '東方譯慷', '謝亞軒', '阿巴西','劉韋辰', '劉旻諺', '周承睿', '譚傑龍', '馬龍', '伊布', '查拉帝', '厄力', '艾斯'],
       'average_mins_score':[0, 0.38, 0.21, 0.27, 0.38, 0.44, 0.62, 0.35, 2, 0.33, 0.25, 0.42, 0.32, 0.24
        ,0.99, 0.21],'平均CMJ':[40, 52 ,54,50, 52, 57, 58, 55, 47.3,50,38,54,50,54,60,40],
       'average_blk':[0, 0.07, 0.21, 0, 0, 0.1, 0.57, 0, 0, 0, 0.12, 0.86, 2.47, 0.75, 0.83, 0.75]}
       
member = pd.DataFrame(data)
member 
#更改欄位名稱 
data= member
member.columns = ['球員','每分鐘得分','平均CMJ中位數','每分鐘火鍋']
#data=data.drop(columns=['Unnamed: 0'])

#把所有值改為陣列
data.values.tolist()


data.to_csv('finaltest.csv',encoding='utf-8')


#繪圖
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('finaltest.csv')

x = data['每分鐘得分']
y = data['平均CMJ中位數']
c= data['每分鐘火鍋']
#散狀圖
fig, ax = plt.subplots(figsize=(5, 5))
ax.scatter(x, y)
plt.title('CMJ和每分鐘得分的是否有關聯')
#plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper right')
plt.xlabel('每分鐘得分')
plt.ylabel('平均CMJ中位數')
plt.show()



#相關性檢驗：當兩變數皆為類別型變數時，資料為順序關係可以斯皮爾曼等級相關(Spearman rank correlation)來了解變數間的相關性。
from scipy.stats import spearmanr
correlation, p = spearmanr(x, c)
print('Correlation:', correlation)
print('p-value:', p)
if p >= 0.05:
    print('H0 is accepted')
else:
    print('H0 is rejected')
 
    
#單因子變異數分析
data.isnull().any()
print(data.corr())
 
#Correlation: 0.44501857137528955
#p-value: 0.08411779628919294
#H0 is accepted
#檢驗同值性 相關係數的值會在1到-1之間，>0表示正相關，<0表示負相關。





#red_fruits=[]
#fruits=[{'name':'apple','color':'red'},
    #    {'name':'banana','color':'yellow'},
     #   {'name':'cherry','color':'red'},
       # {'name':'pear','color':'green'}]
for i in fruits:
    name=i['name']
    color=i['color']
   
    if color == 'red':
        red_fruits.append(i)

#print(red_fruits)
     # a_score=i[{'average':'point','color':'red'}]
       