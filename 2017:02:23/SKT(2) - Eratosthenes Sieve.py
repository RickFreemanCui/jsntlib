# -*- coding: utf-8 -*-

#厄拉托塞師篩法
#返回10,000以內正整數的所有素數（默認情況）

import math

def eratosthenesSieve(N=10000):
    set = [1]*(N+1)                 #用於存儲10000個正整數的表格／狀態；其中，0表示篩去，1表示保留
    for index in range(2,int(math.sqrt(N))):  #篩法（平凡除法）
        ctr = 2
        while index * ctr <= N:
            set[index*ctr] = 0      #將index的倍數篩去
            ctr += 1

    rst = []
    for ptr in range(2,N):          #獲取結果
        if set[ptr] == 1:
            rst.append(ptr)
            ptr += 1

    return rst

if __name__ == '__main__':
    print eratosthenesSieve()
