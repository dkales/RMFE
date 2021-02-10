
# This file was *autogenerated* from the file field_iso.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_9 = Integer(9); _sage_const_29 = Integer(29); _sage_const_22 = Integer(22); _sage_const_21 = Integer(21); _sage_const_26 = Integer(26); _sage_const_19 = Integer(19); _sage_const_40 = Integer(40); _sage_const_41 = Integer(41); _sage_const_42 = Integer(42); _sage_const_43 = Integer(43); _sage_const_44 = Integer(44); _sage_const_45 = Integer(45); _sage_const_46 = Integer(46); _sage_const_47 = Integer(47); _sage_const_49 = Integer(49); _sage_const_51 = Integer(51); _sage_const_39 = Integer(39); _sage_const_38 = Integer(38); _sage_const_11 = Integer(11); _sage_const_10 = Integer(10); _sage_const_15 = Integer(15); _sage_const_14 = Integer(14); _sage_const_31 = Integer(31); _sage_const_30 = Integer(30); _sage_const_33 = Integer(33); _sage_const_32 = Integer(32); _sage_const_35 = Integer(35); _sage_const_34 = Integer(34); _sage_const_37 = Integer(37); _sage_const_13 = Integer(13); _sage_const_18 = Integer(18)
#H.<c>=GF(2^51, modulus="primitive")
#h=H.modulus()

#F.<a>=GF(2^3)
#f=F.modulus()

#P.<X>=PolynomialRing(GF(2))
#R.<Y>=PolynomialRing(F)

#g=R(h).factor()[0][0]


#field_iso_desc- Given m in Fq[X]/(g), where q=2^d, outputs element in F2[X]/(h) via the "canonical" isomorphism. It is required that g is irreducible in Fq[X], h is irreducible in F2[X] and g is one of the d factors of the factorization of h over Fq[X]. For technical reasons, indeterminate variables in F2[X] and Fq[X] are called differently: X and Y respectively. R needs to be defined as Fq[Y], P as F2[X], c is a root of h defining the field F2[X]/(h).
#Isomorphism is computed via the CRT isomorphism between Fq[X]/(h) and Fq[X]/(g)xFq[X]/(g_1)...xFq[X]/(g_d-1) where the g_i's are the other factors of h, which are the conjugates of g by the Frobenius action on Fq
#We use the fact that the image of F2[X]/(h) via the isomorphism consists of an element and its Frobenius conjugates. So in order to compute the preimage of m, we compute the Frobenius actions m_i on it, and do CRT on (m,m_1,...,m_d-1).
#However, we use the fact that this is the sum of the CRT-preimage of (m,0,...,0) and its Frobenius-conjugates.


#Trying to decrease complexity for the case of RMFE_23, by precomputing part of the .
H51 = GF(_sage_const_2 **_sage_const_51 , modulus="primitive", names=('c51',)); (c51,) = H51._first_ngens(1)
h51=H51.modulus()




def field_iso_desc(m,d,g,h,F,H,P,R):
    hR=R(h)
    Y=R.gen()
    a=R.base_ring().gen()
    if h==h51:
        s=R(a**_sage_const_2 *Y**_sage_const_49  + a*Y**_sage_const_47  + a*Y**_sage_const_46  + a**_sage_const_2 *Y**_sage_const_45  + a**_sage_const_2 *Y**_sage_const_44  + a*Y**_sage_const_43  + a**_sage_const_2 *Y**_sage_const_42  + a*Y**_sage_const_41  + a*Y**_sage_const_40  + a*Y**_sage_const_39  + a**_sage_const_2 *Y**_sage_const_38  + a**_sage_const_2 *Y**_sage_const_37  + a*Y**_sage_const_35  + a*Y**_sage_const_34  + (a**_sage_const_2  + a)*Y**_sage_const_33  + a*Y**_sage_const_32  + a**_sage_const_2 *Y**_sage_const_31  + a**_sage_const_2 *Y**_sage_const_30  + a*Y**_sage_const_29  + (a**_sage_const_2  + a)*Y**_sage_const_26  + a*Y**_sage_const_22  + a**_sage_const_2 *Y**_sage_const_21  + a**_sage_const_2 *Y**_sage_const_19  + a*Y**_sage_const_18  + a**_sage_const_2 *Y**_sage_const_15  + a**_sage_const_2 *Y**_sage_const_14  + (a**_sage_const_2  + a)*Y**_sage_const_13  + (a**_sage_const_2  + a)*Y**_sage_const_11  + (a**_sage_const_2  + a)*Y**_sage_const_10  + a*Y**_sage_const_9  + a**_sage_const_2 *Y**_sage_const_6  + a*Y**_sage_const_5  + a**_sage_const_2 *Y**_sage_const_4  + (a**_sage_const_2  + a)*Y**_sage_const_3  + a**_sage_const_2 *Y**_sage_const_2  + a**_sage_const_2  + _sage_const_1 )
	   
    else:
 	p=R(hR/g)
    	#p=prod (g.map_coefficients(lambda z:z.frobenius(i)) for i in range(1,d)) #Computing product of Frobenius-conjugates of g, not including g.
    	s=xgcd(p,g)[_sage_const_1 ]*p
    
    q=s*m                                                       #Computing CRT-preimage of (m,0,0,...,0)
    r=q.map_coefficients(lambda z:z.trace())  				     #Computing result as sum of Frobenius-conjugates mod h (i.e. coefficients of q are mapped to their trace)
    s=r.mod(hR)
    X=P.variable_name()
    t=P(s.change_variable_name(X))                                           #Horrible hack to get Sage to see this polynomial as a F2[X]-poly
    c=H.gen()
    return t(c)

def field_iso_asc(u,d,g,R):
    Y=R.variable_name()
    return R(u.polynomial(Y)).mod(g)



