
# This file was *autogenerated* from the file generatormatrix.sage
from sage.all_cmdline import *   # import sage library

_sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0)#!/usr/bin/env sage

from twostepRMFE import *
from twostepinstance import *

def generatormatrixphi(instance):
	Result=[]
	for i in range(instance.k):
		v=[GF(_sage_const_2 )(_sage_const_0 )]*(i)+[GF(_sage_const_2 )(_sage_const_1 )]+[GF(_sage_const_2 )(_sage_const_0 )]*(instance.k-i-_sage_const_1 )
		Result.append(phi_RMFE(v,instance))
	return Result

#Generates the generator "matrix" (in this case a column vector) over H where the i-th element is the image of the i-th unit vector. Elements are given in the basis 1,c,c^2,... where h(c)=0, for the representing polynomial h=instance.h
def generatormatrixphi_element(instance):
	genmat=generatormatrixphi(instance)
	return matrix(instance.H, instance.k, _sage_const_1 , lambda i, j: genmat[i][_sage_const_0 ])


# Generates the generator matrix of phi, for a given instance. The matrix is a k x e binary matrix, with respect to the representation of GF(2^e) by polynomial instance.h

def generatormatrixphi_bits(instance):
	genmat=generatormatrixphi(instance)
	return matrix(GF(_sage_const_2 ), instance.k, instance.e, lambda i, j: genmat[i][_sage_const_0 ]._vector_()[j])

def generatormatrixpsi(instance):
	Result=[]
	for i in range(instance.e):
		Result.append(psi_RMFE([instance.c**i],[instance.k],instance))
	return matrix(GF(_sage_const_2 ),instance.e,instance.k, lambda i,j: Result[i][j])

def generatormatrixS_o_psi(instance):
	return generatormatrixpsi(instance)*ones_matrix(GF(_sage_const_2 ),instance.k,_sage_const_1 )

def Kerpsi(instance):
	M=generatormatrixpsi(instance)
	return [sum(v[i]*instance.c**i for i in range(len(v))) for v in M.kernel().basis()]
			

def KerS_o_psi(instance):
	M=generatormatrixS_o_psi(instance)
	return [sum(v[i]*instance.c**i for i in range(len(v))) for v in M.kernel().basis()]

def phi_of_one(instance):
	return phi_RMFE([GF(_sage_const_2 )(_sage_const_1 )]*instance.k,instance)[_sage_const_0 ]._vector_()



