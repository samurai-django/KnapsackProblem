# KnapsackProblems
ナップサック問題を使った演習

(1-1)
ナップサック問題：ナップサックの重量制限以下となる制約下で価値合計が最大となる荷物を選ぶ．
I：荷物の集合={0,...,19}，
xi∈{0,1}: 荷物iを選ぶなら1，そうでない0とするバイナリ変数．
ci：荷物iの重量，pi：荷物iの価値．
C：重量制限
定式化
௜ݔ௜݌ ෍Maximize
௜∈ூ
subject to
௜ݔ௜ܿ ෍
௜∈ூ
ܥ ൑
ݔ ∋ ௜ሼ0,1
ሽ

(2-1) C は 300(g)プラスマイナス50(g)以内
(2-2) C = 300(g)，必ず飴は1種類以上持っていく
(2-3) C = 300(g)，果物を持っていく場合は3種類以上
(2-4) C = 300(g)，ガム80g以下ならばチョコレートは150g以上

(3-1) 価値をy円になるべく近づける
