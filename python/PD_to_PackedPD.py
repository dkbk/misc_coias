#!/usr/bin/python3
# coding: UTF-8

import os
import sys


#
#
#
def to_base62(n):

    if n > 9 + 26:
        return chr(0x61 + (n - 10 - 26))

    if n > 9:
        return chr(0x41 + (n - 10))

    else:
        return chr(0x30 + n)


#
#
#
if __name__ == "__main__":

    # 引数の読み込み
    if len(sys.argv) < 2:
        sys.exit()

    # pdsListの一覧ファイル
    pdsListFile = sys.argv[1]
    if not os.path.exists(pdsListFile):
        sys.exit()

    pdsList = []
    with open(pdsListFile, "r") as f:
        pdsList = f.readlines()

    for i in range(len(pdsList)):

        s = pdsList[i].lstrip()
        l = len(s)
        if l < 8:
            continue

        n = 0 # 数字なし if l == 8:

        if l > 8:

            n = int(s[7:l-1])

            # Extended Packed Provisional Designation (62進数4桁表記[0-9A-Za-z]に変換)
            if n >= 620:

                n1 = 25 * (n - 620) + ord(s[6]) - ord('A')
                if s[6] > 'I':
                    n1 = n1 - 1

                n4, n3 = n1 // 62 ** 3, n1 % 62 ** 3
                n3, n2 = n3 // 62 ** 2, n3 % 62 ** 2
                n2, n1 = n2 // 62,      n2 % 62
                print("     _%s%s%s%s%s%s" %(chr(0x41 + int(s[2:4]) - 10), s[5], to_base62(n4), to_base62(n3), to_base62(n2), to_base62(n1)))
                continue

        # 3桁数字を分解
        n2, n1 = n // 10, n % 10
        print("     K%s%s%s%s%s" %(s[2:4], s[5], to_base62(n2), str(n1), s[6]))
