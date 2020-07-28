<h1>ナップサック問題を使った演習</h1>



ナップサック問題：ナップサックの重量制限以下となる制約下で価値合計が最大となる荷物を選ぶ.  
　　　　I：荷物の集合={0,...,19},  
　　　　<img src="https://latex.codecogs.com/gif.latex?x_{i}">∈{0,1}: 荷物iを選ぶなら1，そうでない0とするバイナリ変数.  
　　　　<img src="https://latex.codecogs.com/gif.latex?w_{i}">：荷物iの重量，<img src="https://latex.codecogs.com/gif.latex?v_{i}">：荷物iの価値．  
　　　　C：重量制限
***
    
**定式化  

<img src="https://latex.codecogs.com/gif.latex?Maximize&space;\sum_{i\in&space;I}^{}&space;w_i{x_{i}}">

<img src="https://latex.codecogs.com/gif.latex?subject&space;\;&space;\,&space;to">

　　　<img src="https://latex.codecogs.com/gif.latex?\sum_{i\in&space;I}^{}&space;w_{i}x_{i}&space;\leq&space;C">

　　　<img src="https://latex.codecogs.com/gif.latex?x_{i}&space;\:&space;\in&space;\left&space;\{&space;0,1&space;\right&space;\}">

***



#### (2-1) C は 300(g)プラスマイナス50(g)以内  
#### (2-2) C = 300(g)，必ず飴は1種類以上持っていく  
#### (2-3) C = 300(g)，果物を持っていく場合は3種類以上  
#### (2-4) C = 300(g)，ガム80g以下ならばチョコレートは150g以上  

#### (3-1) 価値をy円になるべく近づける  




| I    | name | weight | value |
|:------:|:-------:|:-----------:|:--------------:|
| 0    | ミントガム         | 30         |      120 |
| 1    | コーラガム        | 40          |      180 |
| 2    | オレンジガム     | 50          |      20 |
| 3    | アップルガム         | 60          |      320 |
| 4    | ミントチョコレート        | 20          |      240 |
| 5    | ミルクチョコレート     | 40          |      110 |
| 6    | ストロベリーチョコレート         | 50          |      90 |
| 7    | ナッツチョコレート        | 40          |      80 |
| 8    | ウィスキーチョコレート     | 30          |      330 |
| 9    | リンゴ         | 60          |      110 |
| 10    | ナシ        | 40          |      170 |
| 11    | キウイ     | 30          |      250 |
| 12    | オレンジ         | 40          |      160 |
| 13    | バナナ        | 50          |      240 |
| 14    | 梅飴     | 30          |      140 |
| 15    | オレンジキャンディ         | 30          |      340 |
| 16    | スイカ飴        | 30          |      210 |
| 17    | ミント飴     | 50          |      170 |
| 18    | 黒飴         | 50          |      310 |
| 19    | キャラメル        | 30          |      310 |







