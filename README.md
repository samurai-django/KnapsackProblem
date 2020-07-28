<h1>ナップサック問題を使った演習</h1>



ナップサック問題：ナップサックの重量制限以下となる制約下で価値合計が最大となる荷物を選ぶ.  
　　　　I：荷物の集合={0,...,19},  
　　　　<img src="https://latex.codecogs.com/gif.latex?x_{i}">∈{0,1}: 荷物iを選ぶなら1，そうでない0とするバイナリ変数.  
　　　　<img src="https://latex.codecogs.com/gif.latex?w_{i}">：荷物iの重量，<img src="https://latex.codecogs.com/gif.latex?v_{i}">：荷物iの価値．  
　　　　C：重量制限

<h2>定式化</h2>

   Maximize
<div align="center">   
　　　<img src="https://latex.codecogs.com/gif.latex?\sum_{i\in&space;I}^{}&space;v_{i}{x_{i}}">
</div>   
   subject to
<div align="center">
　　　<img src="https://latex.codecogs.com/gif.latex?\sum_{i&space;\in&space;I}^{}&space;w_{i}x_{i}&space;\leq&space;C&space;\,&space;\,&space;\,&space;\,&space;x_{i}\in&space;\left&space;\{&space;0,1&space;\right&space;\}">
</div>

***


<h4>(2-1) C は 300(g)プラスマイナス50(g)以内</h4>
<div align="center">
　　　<img src="https://latex.codecogs.com/gif.latex?\sum_{i\in&space;I}^{}&space;v_{i}{x_{i}}">

　　　<img src="https://latex.codecogs.com/gif.latex?\sum_{i&space;\in&space;I}^{}&space;{w_{i}}x_{i}&space;\geq&space;300">

   <img src="https://latex.codecogs.com/gif.latex?\,&space;\,&space;\,&space;\,&space;\&space;\,&space;\,&space;\,&space;\sum_{i&space;\in&space;I}^{}&space;{w_{i}}x_{i}&space;\leq&space;500">
</div>
<h4>(2-2) C = 300(g)，必ず飴は1種類以上持っていく</h4>  

<h4>(2-3) C = 300(g)，果物を持っていく場合は3種類以上</h4>

<h4>(2-4) C = 300(g)，ガム80g以下ならばチョコレートは150g以上<h4>

<h4>(3-1) 価値をy円になるべく近づける</h4>  

***
データ

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







