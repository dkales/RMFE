
# This file was *autogenerated* from the file FFTpreproc.sage
from sage.all_cmdline import *   # import sage library

_sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0)#!/usr/bin/env sage

#Computes a list data with the following structure: i-th component is [G,D] where G and D are the bases in Algorithm 2 of Gao-Mateer10 at recursion level m-i, i=0,...,m-2. The last component contains all [beta_j^{-1}] for levels j=m,...,2.
 
def FFTpreproc(m,B):
    data=[]
    Binv=[]
    assert (B[_sage_const_0 ].parent()).cardinality()==_sage_const_2 **m
    C=B[:]
    for level in range(_sage_const_0 ,m-_sage_const_1 ):
        cc=C[-_sage_const_1 ]**(-_sage_const_1 )
    Binv.append(cc)
    G=[cc*C[j] for j in range(m-level-_sage_const_1 )]
    D=[G[j]**_sage_const_2 -G[j] for j in range(m-level-_sage_const_1 )]
                                                                       
    G1=G[:]
    D1=D[:] 
    datacurrent=[G1,D1]
    data.append(datacurrent)
    C=D
    data.append(Binv)         
    return data

