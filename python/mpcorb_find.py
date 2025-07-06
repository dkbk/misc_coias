#!/usr/bin/python3
# coding: UTF-8

import os
import sys


if __name__ == "__main__":

    if len(sys.argv) < 4:
        sys.exit()

    mpcorbListFile = sys.argv[1]
    obsListFile = sys.argv[2]
    wfn = sys.argv[3]

    if not os.path.exists(mpcorbListFile):
        sys.exit()

    if not os.path.exists(obsListFile):
        sys.exit()

    # MPCORB.DAT 用のリスト

    mpcorbList = []
    with open(mpcorbListFile, "r") as f:
        mpcorbList = f.readlines()

    mpcorbListRange = len(mpcorbList)

    # 照会対象 用のリスト

    obsList = []
    with open(obsListFile, "r") as f:
        obsList = f.readlines()

    obsListRange = len(obsList)

    # 最後に元ファイルの順番でソートし直すためコピーしておく
    obsListRaw = obsList.copy()
    obsListRawRange = len(obsListRaw)

    # obsListはPacked仮符号の昇順ソートを事前に済ませておく

    for n1 in range(obsListRange - 1):

        n1s = obsList[n1]
        n1n = n1s[0:12]

        swapnum1 = n1
        swapnum2 = n1

        for n2 in range(n1 + 1, obsListRange):

            n2s = obsList[n2]
            n2n = n2s[0:12]

            if n2n < n1n:
                n1n = n2n
                swapnum2 = n2

        if swapnum1 != swapnum2:
            obsList[swapnum1], obsList[swapnum2] = obsList[swapnum2], obsList[swapnum1]

    updateList = []

    n2 = 800000

    for n1 in range(obsListRange):

        s1 = obsList[n1]
        d1 = s1[5:12]

        # MPCORB.DATに含まれてなかったときの処理
        n3 = n2
        found = False

        # MPCORB.DAT側のリストは配布元でPacked仮符号の昇順ソート済み
        while n2 < mpcorbListRange:

            s2 = mpcorbList[n2]
            n2 = n2 + 1
            if len(s2) < 7:
                continue;

            if d1 == s2[0:7]:
                found = True
                updateList.append(s2)
                break

        # MPCORB.DATに含まれてなかったときの処理
        if found == False:
            n2 = n3

    updateListRange = len(updateList)

    # 元ファイルの順番にソートし直し

    outputList = []

    for n1 in range(obsListRawRange):

        s1 = obsListRaw[n1]
        d1 = s1[5:12]

        # updateListに含まれてなかったときの処理
        found = False

        for n2 in range(updateListRange):

            s2 = updateList[n2]

            if d1 == s2[0:7]:
                found = True
                outputList.append(s2)
                break

        # updateListに含まれてなかったときの処理
        if found == False:
            outputList.append('{0:<202}\n'.format(d1))
            #outputList.append(d1 + '\n')

    outputRange = len(outputList)

    with open(wfn, "w") as f:
        for n in range(len(outputList)):
            f.write(outputList[n])
