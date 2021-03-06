# -*- coding: utf-8 -*-

from __future__ import print_function

__all__ = [ 'BaseError',
            'DigitError', 'IntError', 'RealError', 'ComplexError', 
            'BoolError', 'ListError', 'TupleError', 'StringError', 'PolyError',
            'PNError', 'OEError', 'PCError',
            'DefinitionError', 'ArgumentError', 'KeywordError',
            'ExponentError', 'ResidueError', 'SolutionError']

import sys
import traceback

#自定義異常類型
#用於在NTL中反饋用戶異常信息

from .NTLUtilities import jsrange

class BaseError(Exception):

    '''
    Cautions:

    * Turn off system-default traceback function by set `sys.tracebacklimit` to 0.
    * But bugs appear in Python 3.6, so we have to set `sys.tracebacklimit` to None.
    * In Python 2.7, `trace.print_stack(limit=None)` dose not support negative limit.
    '''

    def tb_preparation(self):
        tb = traceback.extract_stack()
        length = len(tb)

        for ptr in jsrange(length):
            if 'NTLArchive' in tb[ptr][0]:
                index = ptr;    break

        return length, index

    def traceback_2(self):
        length, index = self.tb_preparation()

        print('Traceback (most recent call last):')
        print(''.join(traceback.format_stack()[:index])[:-1])
        sys.tracebacklimit = 0

    def traceback_3(self):
        length, index = self.tb_preparation()

        print('Traceback (most recent call last):')
        traceback.print_stack(limit=-index)
        sys.tracebacklimit = None

#數字參數異常
#The argument(s) must be (a) number(s).
class DigitError(BaseError):
    def __init__(self, message):
        if sys.version_info[0] > 2:
            self.traceback_3() 
        else:
            self.traceback_2()

        raise TypeError(message)

#整數參數異常
#The argument(s) must be integral.
class IntError(BaseError):
    def __init__(self, message):
        if sys.version_info[0] > 2:
            self.traceback_3() 
        else:
            self.traceback_2()

        raise TypeError(message)

#列表參數異常
#The argument(s) must be list type.
class ListError(BaseError):
    def __init__(self, message):
        if sys.version_info[0] > 2:
            self.traceback_3() 
        else:
            self.traceback_2()

        raise TypeError(message)

#元組參數異常
#The argument(s) must be tuple type.
class TupleError(BaseError):
    def __init__(self, message):
        if sys.version_info[0] > 2:
            self.traceback_3() 
        else:
            self.traceback_2()

        raise TypeError(message)

#多項式參數異常
#The argument(s) must be Polynomial type.
class PolyError(BaseError):
    def __init__(self, message):
        if sys.version_info[0] > 2:
            self.traceback_3() 
        else:
            self.traceback_2()

        raise TypeError(message)

#參數異常
#Function expected at most / least n arguments, got m.
class ArgumentError(BaseError):
    def __init__(self, message):
        if sys.version_info[0] > 2:
            self.traceback_3() 
        else:
            self.traceback_2()

        raise TypeError(message)

#實數功能異常
#The function is not defined for real number.
class RealError(BaseError):
    def __init__(self, message):
        if sys.version_info[0] > 2:
            self.traceback_3() 
        else:
            self.traceback_2()

        raise TypeError(message)

#複數功能異常
#The function is not defined for complex instance.
class ComplexError(BaseError):
    def __init__(self, message):
        if sys.version_info[0] > 2:
            self.traceback_3() 
        else:
            self.traceback_2()

        raise TypeError(message)

#正／負值參數異常
#The argument(s) must be positive/negative.
class PNError(BaseError):
    def __init__(self, message):
        if sys.version_info[0] > 2:
            self.traceback_3() 
        else:
            self.traceback_2()

        raise ValueError(message)

#奇／偶數參數異常
#The argument(s) must be odd/even.
class OEError(BaseError):
    def __init__(self, message):
        if sys.version_info[0] > 2:
            self.traceback_3() 
        else:
            self.traceback_2()

        raise ValueError(message)

#素／合數參數異常
#The argument(s) must be prime/composit.
class PCError(BaseError):
    def __init__(self, message):
        if sys.version_info[0] > 2:
            self.traceback_3() 
        else:
            self.traceback_2()

        raise ValueError(message)

#布爾參數異常
#The argument(s) must be bool type.
class BoolError(BaseError):
    def __init__(self, message):
        if sys.version_info[0] > 2:
            self.traceback_3() 
        else:
            self.traceback_2()

        raise ValueError(message)

#字符串參數異常
#The argument(s) must be (a) string(s).
class StringError(BaseError):
    def __init__(self, message):
        if sys.version_info[0] > 2:
            self.traceback_3() 
        else:
            self.traceback_2()

        raise ValueError(message)

#參數定義異常
#The argument must match a specific patern.
class DefinitionError(BaseError):
    def __init__(self, message):
        if sys.version_info[0] > 2:
            self.traceback_3() 
        else:
            self.traceback_2()

        raise ValueError(message)

#方程無解異常
#The polynomial has no integral solution.
class SolutionError(BaseError):
    def __init__(self, message):
        if sys.version_info[0] > 2:
            self.traceback_3() 
        else:
            self.traceback_2()

        raise RuntimeError(message)

#係數參數異常
#The coefficient of the univariate with greatest degree in divisor must be 1.
class ExponentError(BaseError):
    def __init__(self, message):
        if sys.version_info[0] > 2:
            self.traceback_3() 
        else:
            self.traceback_2()

        raise KeyError(message)

#取模參數異常
#The modulo of residue should not be 0.
class ResidueError(BaseError):
    def __init__(self, message):
        if sys.version_info[0] > 2:
            self.traceback_3() 
        else:
            self.traceback_2()

        raise ZeroDivisionError(message)

#關鍵詞參數異常
#Unknow attribute(s).
class KeywordError(BaseError):
    def __init__(self, message):
        if sys.version_info[0] > 2:
            self.traceback_3() 
        else:
            self.traceback_2()

        raise AttributeError(message)
