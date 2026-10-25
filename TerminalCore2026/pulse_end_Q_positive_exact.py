from fractions import Fraction as F
k=F(202)*24*(F(20,247)**4)
assert k==F(775680000,3722098081)
assert k*F(1,20)**3<F(1,1000)
assert F(3,2)*(100+F(20,19))+50<202
assert F(99,100)-F(1,1000)>F(1,2)
print('PASS exact pulse exit Q>lambda/2 under independently verified |i(0)|,|i_eta(0)|<=100')
print('Full pulse and A11 support stress cone not certified')
