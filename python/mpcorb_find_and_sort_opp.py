#!/usr/bin/python3
# coding: UTF-8

import os
import sys


if __name__ == "__main__":

    if len(sys.argv) < 4:
        sys.exit()

    mpcorbListFile = sys.argv[1]
    pdsListFile = sys.argv[2]
    wfn = sys.argv[3]

    if not os.path.exists(mpcorbListFile):
        sys.exit()

    if not os.path.exists(pdsListFile):
        sys.exit()

    # MPCORB.DAT 読み込み ※Packed形式で文字列昇順ソート済み
    mpcorbList = []
    with open(mpcorbListFile, "r") as f:
        mpcorbList = f.readlines()

    # 検索対象仮符号天体 読み込み
    pdsList = []
    with open(pdsListFile, "r") as f:
        pdsList = f.readlines()

    # リスト -> 辞書に変換
    pdsDict = {}
    for n in range(len(pdsList)):
        pdsDict[n] = pdsList[n]

    # 辞書ソート(文字列昇順) -> リスト
    pdsDictList = list(sorted(pdsDict.items(), key=lambda x:x[1]))
    pdsDictListRange = len(pdsDictList)

    #
    # 検索
    #

    pdsN = 0
    pdsK, pdsS = pdsDictList[pdsN]
    pdsD = pdsS[5:12]

    mpcorbListRange = len(mpcorbList)
    mpcN = 800000 # 確定番号天体を事前にスキップさせておく
    while mpcN < mpcorbListRange:

        mpcS = mpcorbList[mpcN]
        if len(mpcS) < 7:
            mpcN = mpcN + 1
            continue

        mpcD = mpcS[0:7]

        # 仮符号天体の場合は7文字必要、確定番号天体は5文字
        if mpcD.find(' ') >= 0 and mpcD.find(' ') < 7:
            mpcN = mpcN + 1
            continue

        if mpcD < pdsD:
            mpcN = mpcN + 1
            continue

        k, v = pdsDictList[pdsN] # 辞書の中身を書き換えるためキーを取得

        if mpcD == pdsD:
            pdsDict[k] = mpcS
            mpcN = mpcN + 1
        else:
            pdsDict[k] = '{0:<202}\n'.format(pdsD)

        # 次の仮符号天体に更新
        pdsN = pdsN + 1
        if pdsN >= pdsDictListRange:
            break
        pdsK, pdsS = pdsDictList[pdsN]
        pdsD = pdsS[5:12]

    #
    # 衝(opps):降順、不確実性(U):昇順、Packed仮符号:昇順 でソートし出力
    #

    pdsSortOppList = []
    for k, v in pdsDict.items(): # python 3.7 以降？

        pdsSortOppList.append([]) # 多重リスト化

        pdsSortOppList[k].append(v) # 0:文字列そのまま
        pdsSortOppList[k].append(int(0 if v[124:126] == "  " else v[124:126])) # 1:衝
        pdsSortOppList[k].append(v[105]) # 2:不確実性
        pdsSortOppList[k].append(v[0:7]) # 3:Packed仮符号

    pdsSortOppList = sorted(pdsSortOppList, key=lambda x: (-x[1], x[2], x[3]))

    with open(wfn, "w") as f:
        for n in range(len(pdsSortOppList)):
            f.write(pdsSortOppList[n][0])
