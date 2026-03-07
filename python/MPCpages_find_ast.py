#!/usr/bin/python3
# coding: UTF-8

import os
import sys


if __name__ == "__main__":

    if len(sys.argv) < 3:
        sys.exit()

    rfn = sys.argv[1]
    wfn = sys.argv[2]

    if not os.path.exists(rfn):
        sys.exit()

    # MPCPages.txtからコピーされたテキストファイルの読み込み

    pdsList = []
    with open(rfn, "r") as f:
        pdsList = f.readlines()

    # アスタリスク(*)を含む仮符号のみを抽出

    with open(wfn, "w") as f:

        for n1 in range(len(pdsList)):

            # 1行の中に複数天体が';'区切りで記載されている
            s1 = pdsList[n1]
            p1 = s1.split("; ") # 先頭に空白文字が残らないように

            for n2 in range(len(p1)):

                # 更に','で区切り、p2[0]の文字列に'*'が含まれていれば仮符号のみを表示
                s2 = p1[n2]
                p2 = s2.split(',')
                if p2[0].find('*') > 0:
                    f.write(p2[0][:-2] + '\n')
