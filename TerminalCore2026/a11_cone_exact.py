"""Exact rational stress-cone sufficient checks, not a source-data certificate."""
from fractions import Fraction as F
from itertools import product
import json,sys
def q(x): return F(str(x))
def mul(x,y):
 z=[a*b for a,b in product(x,y)]
 return min(z),max(z)
def add(x,y):return x[0]+y[0],x[1]+y[1]
def neg(x):return -x[1],-x[0]
def sq(x):
 if x[0]<=0<=x[1]:return F(0),max(x[0]**2,x[1]**2)
 return min(x[0]**2,x[1]**2),max(x[0]**2,x[1]**2)
def inv(x):
 assert x[0]>0
 return F(1,x[1]),F(1,x[0])
def stage(z):
 a=tuple(map(q,z['a']));b=tuple(map(q,z['bs']))
 w=tuple(map(q,z['w']));p=tuple(map(q,z['ps1']))
 assert a[0]>0 and all(x[0]<=x[1] for x in (a,b,w,p))
 ba=mul(b,inv(a))
 v=add(a,mul(sq(b),inv(a)))
 Pc=mul(p,add((F(1),F(1)),neg(mul(mul(b,w),inv(a)))))
 Jc=mul(p,add(w,ba))
 gap=add(mul((F(2),F(2)),sq(add(Pc,neg(v)))),neg(mul(add(v,(F(-2),F(-2))),sq(Jc))))
 good=Pc[0]>max(F(2),v[1]) and gap[0]>0 and (z.get('regime')!='admissible' or v[0]>2)
 return {'conditional_interval_result':'PASS' if good else 'UNRESOLVED',
 'gap_lower':str(gap[0]),'Pc_lower':str(Pc[0]),'v_lower':str(v[0]),
 'SOURCE_INPUTS_VERIFIED':False}
def qhalf(lam):
 assert 0<lam<=F(1,20)
 return (lam-lam/100)/(1-lam)-320000000*lam**28 >=lam/2
assert F(80)+3*F(20,17)*76800000<300000000
assert F(5)+3*F(20,17)*5000000<20000000
assert F(20,17)*5120+20000000<21000000
for n in (20,25,40,100,10000):
 lam=F(1,n);a=2+3*lam;p=F(9,2);w=F(1)
 assert qhalf(lam)
 assert 2*(1-a/p)**2-(a-2)*w*w>=F(7,20)
# mandatory negative control
assert not ((F(21,10)-2)*(100*10)**2 <2*(100-F(21,10))**2)
print('PASS all exact arithmetic A11 cone and Q half-lambda tests; negative control')
demo={'a':['2.01','2.02'],'bs':['0','0'],'w':['-.1','.1'],
      'ps1':['10','11'],'regime':'admissible'}
print('SYNTHETIC NOT SOURCE',stage(demo))
if len(sys.argv)>1:
 with open(sys.argv[1]) as f: x=json.load(f)
 for z in x['cells']:print(z.get('name','cell'),stage(z))
