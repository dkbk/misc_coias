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

    obsList = []
    with open(rfn, "r") as f:
        obsList = f.readlines()

    obsListRange = len(obsList)

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

    with open(wfn, "w") as f:
        for n in range(len(obsList)):
            f.write(obsList[n])
