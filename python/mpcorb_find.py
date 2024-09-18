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

    #

    mpcorbList = []
    with open(mpcorbListFile, "r") as f:
        mpcorbList = f.readlines()

    mpcorbListRange = len(mpcorbList)

    #

    obsList = []
    with open(obsListFile, "r") as f:
        obsList = f.readlines()

    obsListRange = len(obsList)

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

    n2 = 720000

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

    # opps:降順 U:昇順 Packed仮符号:昇順 でソート

    for n1 in range(updateListRange - 1):

        s1 = updateList[n1]
        o1 = int(s1[124:126])
        u1 = s1[105]
        d1 = s1[0:7]

        swapnum1 = n1
        swapnum2 = n1

        for n2 in range(n1 + 1, updateListRange):

            s2 = updateList[n2]
            o2 = int(s2[124:126])
            u2 = s2[105]
            d2 = s2[0:7]

            if o2 > o1:
                o1 = o2
                u1 = u2
                d1 = d2
                swapnum2 = n2
            elif o2 == o1:
                if u2 < u1:
                    o1 = o2
                    u1 = u2
                    d1 = d2
                    swapnum2 = n2
                elif u2 == u1:
                    if d2 < d1:
                        o1 = o2
                        u1 = u2
                        d1 = d2
                        swapnum2 = n2

        if swapnum1 != swapnum2:
            updateList[swapnum1], updateList[swapnum2] = updateList[swapnum2], updateList[swapnum1]

    with open(wfn, "w") as f:
        for n in range(len(updateList)):
            f.write(updateList[n])
