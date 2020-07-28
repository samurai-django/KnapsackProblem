
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 02:45:18 2020

@author: yusuke yoshioka
"""

from pulp import *
import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/m19ss/Documents/Q2 2020/最適化モデル研究/三浦/レポート/napsac.csv")

n = df['name']
name_list = n.tolist()
v1 = df['value']
value_list = v1.tolist()
w1 = df['weight']
weight_list = w1.tolist()
v = value_list
# v = [120, 180, 20, 320, 240, 110, 90, 80, 330, 110, 170, 250, 160, 240, 140, 340, 210, 170, 310, 310]
w = weight_list
# w = [30, 40, 50, 60, 20, 40, 50, 40, 30, 60, 40, 30, 40, 50, 30, 30, 30, 50, 50, 30]
W = 300
W_min = 50
r = range(len(w))

# 数理モデル
M = 10000
y = 1500

m = LpProblem(sense=LpMaximize)

# 変数
x = [LpVariable('x%d' % i, cat=LpBinary) for i in r]
z = LpVariable('z', cat=LpBinary)

# 目的関数
m += lpDot(v, x)

# 制約
m += lpDot(w, x) <= W

# (3)
m += x[9] + x[10] + x[11] + x[12] + x[13] <= M * z
m += x[9] + x[10] + x[11] + x[12] + x[13] >= 3- (M * (1 - z))

m.solve()
print('(2-3) 荷物の価値:{} 円/ 組み合わせ:{}'.format(value(m.objective), [i for i in r if value(x[i]) > 0.5]))
# 実行結果
# (2-3) 荷物の価値:2320.0 円/ 組み合わせ:[4, 8, 10, 11, 12, 15, 16, 18, 19]
