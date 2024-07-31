from scipy.stats import norm
import numpy as np
import math

print('Subject : 統計検定2級過去問 2017年11月 問13(1)')
print('　')

print('１．母数の設定')
## 「非常に関心がある」比率を p とする
p = 0.483
n=1897 #回答総数 1897

print('２．信頼区間の算出')
# p_con が信頼度(confidence)を示す
p_con=0.95
q0=1.96
r1 = p - q0*np.sqrt(p*(1-p)/n)
r2 = p + q0*np.sqrt(p*(1-p)/n)

## 丸め処理
## print(round(r1,3),round(r2,3))

print('信頼度', int(100*p_con),end='')
print('％の信頼区間：',round(r1,3),' ≦ μ ≦ ', round(r2,3))