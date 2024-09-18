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

    with open(wfn, "w") as f:
        for n in range(len(obsList)):
            s = obsList[n]
            if s[12] == '*' and s[13] == '4' and s[77:80] == "T09":
                f.write(s)
