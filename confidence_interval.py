from scipy.stats import norm
import numpy as np
import math

print('Subject : 母平均の区間推定（分散既知）、信頼区間、scipy.stats.norm 関数')
print('　')

print('１．母数の設定・・・標準偏差 5000')
sigma = 5000

## norm.rvs(30000,5000,size=25) を使用し
## 東京20代の食費データを想定した下記データを準備
sample = [23841, 26956, 29952, 24147, 
 33689, 33368, 38616, 33228,
 29278,  24352, 28566, 36842,
 32540, 35265, 32729, 29043,
 21024, 38025, 25130, 26061,
 24697, 36286, 22289, 33132,
 21533] 

ss=len(sample) ## sample size は 25
print('２．標本平均算出')
ms=np.mean(sample)
print(ms) ## 29623.56


print('３．信頼区間の算出')
# p_con が信頼度(confidence)を示す
p_con=0.95
q0=1.96
r1 = ms - q0*sigma/np.sqrt(ss)
r2 = ms + q0*sigma/np.sqrt(ss)

## 丸め処理 、注）信頼性を損なわないように。
## 「左端は切下げ、右端は切り上げ」が普通（らしい）。
## numpy.floor、numpy.ceil関数もある。
r1 = math.floor(r1)
r2 = math.ceil(r2)

print('信頼度', int(100*p_con),end='')
print('％の信頼区間：',r1,' ≦ μ ≦ ', r2)