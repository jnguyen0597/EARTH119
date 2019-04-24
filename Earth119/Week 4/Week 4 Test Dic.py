# -*- coding: utf-8 -*-
"""

"""
import numpy as np



dDic = {'my_pi' : np.pi,
        'my_array' : np.arange(10),
        'my_str' : 'test',
        }

print( dDic['my_pi'])

print( dDic)
for key in dDic.keys():
    print( key)
    print( key, type( dDic[key]))






