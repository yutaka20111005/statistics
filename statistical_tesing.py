from scipy.stats import norm
import numpy as np
import math

print('Subject : 母平均の検定(分散既知の場合)')
print('　')

print('１．帰無仮説、対立仮説、優位水準の設定')

sigma = 5000 # 標準偏差
μ=44611 # 帰無仮説 H0
# 対立仮説 H1 : μ > 44611
level = 0.05 # 有意水準
print('有意水準 ＝ {:.0%}'.format(level))


print('２．標本抽出')
## norm.rvs(45000,5000,size=10) を使用し
## 独身男性の食費の月額平均を想定した下記データを準備
sample = [46237, 50077, 47099, 44303,43641, 40882, 50692, 40627, 45133, 50326]

ss=len(sample)
print(ss) ## サンプリサイズ　10

print('３．検定統計量の標本平均')
m = np.mean(sample)

print('４．標準正規分布の％点設定')
p_point = 1.65

print('５．棄却域算出・・・片側検定、右側検定')
r2 = μ + p_point*sigma/np.sqrt(ss)

print('６．丸め処理')
r2=math.ceil(r2)
print('棄却域：x_bar => ', r2)

print('７．検定')
print('標本平均の値＝',m)
print('検定結果：',end='')
if m<r2:
    print('帰無仮説を採択する。')
else:
    print('帰無仮説を棄却する。')
