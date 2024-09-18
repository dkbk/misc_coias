## 使い方

実行ファイル、入力ファイル、出力ファイルは同じディレクトリにあることを前提としています。

※obs80形式データはCOIASのsend_mpc.txtの中に表記されている1行80文字の測定データを指します。<br>※obs80形式データファイルはobs80形式データを纏めたファイルを指します。


### obs80_find_COIAS.py

obs80形式データファイルからCOIAS関連の行を抽出します。

例 ITF(Isolated Tracklet File)からCOIASの測定データを抽出します。

MPC [MPCAT-OBS: Observation Archive](https://www.minorplanetcenter.net/iau/ECS/MPCAT-OBS/MPCAT-OBS.html) から
The Isolated Tracklet File の itf.txt.gz (約100MB) をダウンロードし、展開すると itf.txt (約700MB) が得られます。

```bash
python3 obs80_find_COIAS.py itf.txt COIAS_itf.txt
```

itf.txt にあるCOIAS関連の行を COIAS_itf.txt に出力します。


### obs80_find_ast_COIAS.py

obs80形式データファイルからアスタリスク(*)がついているCOIAS関連の行を抽出します。

例 MPS(Minor Planet Circulars Supplement)の差分ファイルからCOIASの測定データを抽出します。

MPC [Mid-Month Batches of Minor Planet Circulars Supplement (MPS)](https://www.minorplanetcenter.net/iau/ECS/MPCUPDATE/MidMonthMPS.html) から
最新の Observations (GZIP compressed) (約30MB) をダウンロードし、展開すると tot_00.obs (約100MB) が得られます。<br>
※ファイル名は、発行日がyyyymmdd形式でつけられていて OBS_yyyymmdd.txt.gz になっています。

```bash
python3 obs80_find_ast_COIAS.py tot_00.txt COIAS_ast.txt
```

tot_00.txt にあるアスタリスク(*)がついているCOIAS関連の行を COIAS_ast.txt に出力します。


### obs80_sort.py

obs80形式データファイルを読み込み、7文字のPacked仮符号を昇順ソートで並べ替えて出力します。<br>

```bash
python3 obs80_sort.py COIAS_ast.txt COIAS_ast_sorted.txt
```

COIAS_ast.txt を読み込み、7文字のPacked仮符号を昇順ソートして COIAS_ast_sorted.txt に出力します。


### mpcorb_find.py

小惑星の軌道要素などが纏められている MPCORB.DAT と obs80形式データファイル を読み込み、obs80形式データファイルにある7文字のPacked仮符号を MPCORB.DAT から見つけて該当行を抽出します。

MPC [The MPC Orbit (MPCORB) Database](https://www.minorplanetcenter.net/iau/MPCORB.html) から
MPCORB.DAT.gz (約80MB) をダウンロードし、展開すると MPCORB.DAT (約270MB) が得られます。

```bash
python3 mpcorb_find.py MPCORB.DAT COIAS_ast.txt COIAS_mpcorb.txt
```

MPCORB.DAT と COIAS_ast.txt を読み込み、衝:降順 U:昇順 Packed仮符号:昇順 で並び替えた後に COIAS_mpcorb.txt に出力します。

## 備考

アスタリスク(*)付きの仮符号天体を数多く測定されている方は、MPC [WAMO](https://www.minorplanetcenter.net/wamo/) で出力された 仮符号に書き換えられた後の測定データ を纏めてテキストファイルに保存することで、そのテキストファイル ＝ COIAS_ast.txt として扱えますので mpcorb_find.py で MPCORB.DAT と照合できます。
