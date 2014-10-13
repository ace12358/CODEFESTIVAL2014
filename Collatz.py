#!/usr/bin/python
# -*- coding: utf-8 -*-

def main():
    # T(テストケース数)の入力
    T = int(raw_input())
    
    # 入力の読み込み
    N = list()
    for i in range(T):
        n = int(raw_input())
        N.append(n)

    # 出力
    for n in N:
        cnt = 0
        while(n != 1):
            if n%2==0:
                n = n/2
                cnt += 1
            else:
                n = 3*n +1
                cnt += 1
        print cnt
    print

if __name__=="__main__":
    main()
