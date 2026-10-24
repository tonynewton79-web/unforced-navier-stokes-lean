from fractions import Fraction as F
l=F(1,20)
d=40960*l**28
e=2560*l**28/(1-d)
b=4*(l/100)*F(233,100)+1+2*(l/100)+2*e*(F(233,100)+F(1,2))
assert b<F(503,500)
w=F(503,1960)
cone=F(9,8)-F(3,20)*w*w
assert cone==F(85676973,76832000) and cone>F(9,20)
print('PASS exact conditional ratio and cone constants; SOURCE DATA NOT AUTHENTICATED')
