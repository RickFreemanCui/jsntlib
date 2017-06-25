#-*- coding: utf-8 -*-

from .__abc__ import __symbol__

__all__  = ['Legendre',
            'default_numerator', 'default_denominator',
            'legendre_eval', 'legendre_simplify', 'legendre_reciprocate']
nickname = 'Legendre'

#Legendre符號類
#具備化簡、求值等基本功能

from .NTLExceptions           import DefinitionError, KeywordError
from .NTLPrimeFactorisation   import primeFactorisation
from .NTLTrivialDivision      import trivialDivision
from .NTLUtilities            import jssign
from .NTLValidations          import prime_check, str_check

# from .NTLJacobi import Jacobi

Symbol = __symbol__.ABCSymbol

# Legendre default form.
default_numerator   = 1
default_denominator = 2

def legendre_eval(legendre):
    _ret = legendre_simplify(legendre)

    a = _ret.numerator
    p = _ret.denominator

    if a == 1:      return 1
    if a == - 1:    return (-1)**((p-1)//2)
    if a == 2:      return (-1)**((p**2-1)//8)

    r = jssign(a)
    for _a in primeFactorisation(abs(a)):
        r *= Legendre(_a, p).eval()

    return r if r != p-1 else -1

def legendre_simplify(legendre):
    _ret = legendre

    while abs(_ret.numerator) not in [0, 1, 2]\
            and trivialDivision(abs(_ret.numerator)):
        _num = _ret.numerator
        _den = _ret.denominator

        if _den > abs(_num):
            _ret = legendre_reciprocate(_ret)

    return _ret

def legendre_reciprocate(legendre):
    _den = legendre.numerator
    _num = legendre.denominator * (-1)**((_den-1)//2) % _den

    if _num == _den - 1:    _num = -1
    _ret = Legendre(_num, _den)
    
    return _ret

class Legendre(Symbol):

    def __init__(self, _numerator, _denominator=None):
        prime_check(self.denominator)

    def cast(self, kind):
        str_check(kind)

        if kind == 'Legendre':
            return self
        elif kind == 'Jacobi':
            from .NTLJacobi import Jacobi
            _ret = Jacobi(self.numerator, self.denominator)
            return _ret
        else:
            raise KeywordError('%s is an unknown type of symbol.' %kind)

    # Virtual properties.
    nickname    = 'Legendre'
    numerator   = default_numerator
    denominator = default_denominator

    # Virtual functions.
    eval = legendre_eval
    simplify = legendre_simplify
    reciprocate = legendre_reciprocate

# if __name__ == '__main__':
#     l1 = Legendre(1, 2)
#     l2 = Legendre('2|3')
#     l3 = Legendre(l1)

#     print(l1, l1.eval())
#     print(l2, l2.eval())
#     print(l3, l3.eval())
