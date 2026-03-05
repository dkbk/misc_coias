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

    pdsList = []
    with open(rfn, "r") as f:
        pdsList = f.readlines()

    pdsSortList = []
    for n in range(len(pdsList)):
        s = pdsList[n]
        pdsSortList.append([])
        pdsSortList[n].append(s)
        pdsSortList[n].append(s[5:12])

    pdsSortList = sorted(pdsSortList, key=lambda x:x[1])

    with open(wfn, "w") as f:
        for n in range(len(pdsSortList)):
            f.write(pdsSortList[n][0])
