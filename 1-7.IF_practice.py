# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 15:54:46 2019

@author: Ivan
"""

# 比較符號
a = 3
b = 2

a > b 

a < b

a == b

a != b

# 邏輯符號
not True

True and False 

True or True


# if 判斷式
# python 是以縮排為主的語言
a = 50
if a > 10:
    print('a 大於 10')
else:
    print('a 不大於 10')
    
# 判斷字串內是否（in）有"TMR"關鍵字 是就印出 YES!  否就印出NO
var = '今日頭條新聞，TMR公司開設行銷資料科學專班'
if 'TMR' in var:
    print('YES')
else:
    print('NO')

#區分偶數奇數 
for i in range(1, 21):
    if i % 2 == 0:
        print(i, '偶數')
    else:
        print(i, '奇數')
        
#火箭倒數
for i in [10,9,8,7,6,5,4,3,2,1,0]:
    if i > 0:
        print(i)
    else:
        print('發射')

#倍數和公倍數       
for i in range(1, 21):
    if i % 2 == 0 and i % 3 != 0:
        print(i, "是2的倍數")
    if i % 3 == 0 and i % 2 != 0:
        print(i, '是3的倍數')
    if i % 2 == 0 and i % 3 == 0:
        print(i, "2和3的公倍數")
#聖誕樹
for i in range (1, 12):
    for j in range(1, i):
        print("*", end=" ")
    print()
 
    
