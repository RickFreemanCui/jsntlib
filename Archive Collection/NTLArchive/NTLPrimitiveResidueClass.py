#-*- coding: utf-8 -*-

__all__  = ['primitiveResidueClass']
nickname =  'prc'

#簡化剩餘係
#求整數m的簡化剩餘係

from .NTLCoprimalityTest import coprimalityTest
from .NTLUtilities       import jsrange
from .NTLValidations     import int_check, pos_check

def primitiveResidueClass(n):
    int_check(n);   pos_check(n)

    #當(d,n)=1時，d遍歷n的簡化剩餘係
    rst = []
    for d in jsrange(1, n):
        if coprimalityTest(d, n) == 1:
            rst.append(d)

    return rst

# if __name__ == '__mian__':
#     prc = primitiveResidueClass(40)

#     print('The primitive residue class of 40 is')
#     for num in prc:
#         print(num, end=' ')
#     print()
