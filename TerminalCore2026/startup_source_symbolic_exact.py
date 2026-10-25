"""Independent exact symbolic startup replay, source (5.2)--(5.6).

The regular polynomial probes are NOT the imported leading profile.
The test verifies current/lower source decomposition at n=1 and n=2,
including Omega_0/Omega_1 and pressure axis integration.
"""
import sympy as S
from collections import defaultdict
e=S.symbols('eta');h=S.Rational(1,200)
A=S.Rational(1,2)+h;D=S.Rational(1,2)-h
b=-A-S.Rational(1,2);c=-A;C=S.Integer(3)
L=1-2*h*e*e;d=1-e*e
def clean(f):return {a:S.cancel(v) for a,v in f.items() if v!=0}
def add(*fs):
 z=defaultdict(lambda:S.Integer(0))
 for f in fs:
  for a,v in f.items():z[a]+=v
 return clean(z)
def sc(f,x):return clean({a:x*v for a,v in f.items()})
def mul(f,g):
 z=defaultdict(lambda:S.Integer(0))
 for a,x in f.items():
  for k,y in g.items():z[a+k]+=x*y
 return clean(z)
def dx(f):return clean({a-1:a*v for a,v in f.items() if a>0})
def divx(f):return clean({a-1:v for a,v in f.items()})
def X(f):return clean({a+1:v for a,v in f.items()})
def Int(f):
 assert min(f)>=0
 return clean({a+1:v/(a+1) for a,v in f.items()})
def T(f,p):return clean({a:((a-p)*v+D*e*S.diff(v,e))/L for a,v in f.items()})
def Z(f,p):return clean({a:(2*e*(p-a)*v+d*S.diff(v,e))/L for a,v in f.items()})
def Z2(f,p):return Z(Z(f,p),p-D)
def V(f,n):return sc(Int(Z(f,-A+2*h*n)),-1)
def same(f,g):
 diff=add(f,sc(g,-1))
 for a,v in diff.items():
  for eta in (S.Rational(0),S.Rational(1,3),S.Rational(-2,5)):
   assert S.cancel(v.subs(e,eta))==0,(a,eta)
 return len(set(f)|set(g))
phi=[{0:1+e+e*e,1:2-e},{1:1+2*e,2:e*e},{2:2+e}]
u=[{0:1+e,1:e*e},{1:2-e+e*e},{2:3+e*e}]
v=[V(u[n],n) for n in range(3)]
def omega(k):
 out=add(T(v[k],2*h*k),sc(X(dx(dx(v[k]))),-2))
 for i in range(k+1):
  j=k-i
  out=add(out,mul(v[i],add(dx(v[j]),sc(divx(v[j]),-S.Rational(1,2)))),
          mul(u[i],Z(v[j],2*h*j)))
 if k:out=add(out,sc(Z2(v[k-1],2*h*(k-1)),-1))
 assert 0 not in out
 return out
count=0
for n in range(3):count+=same(dx(v[n]),sc(Z(u[n],-A+2*h*n),-1))
for n in (1,2):
 om=omega(n-1)
 pp=add(sc(sum_source:=add(*(mul(phi[i],phi[n-i]) for i in range(n+1))),1/C**2),sc(divx(om),-S.Rational(1,2)))
 Pi=Int(pp)
 current=Int(sc(mul(phi[0],phi[n]),2/C**2))
 known=Int(add(sc(divx(om),-S.Rational(1,2)),
       sc(mul(phi[1],phi[1]),1/C**2) if n==2 else {}))
 count+=same(Pi,add(current,known))
 count+=same(dx(Pi),pp)
 rhs_s=add(T(phi[n],b+2*h*n),sc(Z2(phi[n-1],b+2*h*(n-1)),-1))
 rhs_u=add(T(u[n],c+2*h*n),Z(Pi,-2*A+2*h*n),
           sc(Z2(u[n-1],c+2*h*(n-1)),-1))
 cur_s=T(phi[n],b+2*h*n)
 cur_u=add(T(u[n],c+2*h*n),Z(current,-2*A+2*h*n))
 for i in range(n+1):
  j=n-i
  sterm=add(mul(v[i],add(dx(phi[j]),divx(phi[j]))),mul(u[i],Z(phi[j],b+2*h*j)))
  uterm=add(mul(v[i],dx(u[j])),mul(u[i],Z(u[j],c+2*h*j)))
  rhs_s=add(rhs_s,sterm);rhs_u=add(rhs_u,uterm)
  if not (i>0 and j>0):
   cur_s=add(cur_s,sterm);cur_u=add(cur_u,uterm)
 low_s=sc(Z2(phi[n-1],b+2*h*(n-1)),-1)
 low_u=add(sc(Z2(u[n-1],c+2*h*(n-1)),-1),Z(known,-2*A+2*h*n))
 if n==2:
  low_s=add(low_s,mul(v[1],add(dx(phi[1]),divx(phi[1]))),mul(u[1],Z(phi[1],b+2*h)))
  low_u=add(low_u,mul(v[1],dx(u[1])),mul(u[1],Z(u[1],c+2*h)))
 count+=same(rhs_s,add(cur_s,low_s))
 count+=same(rhs_u,add(cur_u,low_u))
 print('PASS exact source and pressure split at n=',n)
assert S.cancel(Z2(phi[0],b)[0].subs(e,0))==-S.Rational(1,100)
print('PASS',count,'exact coefficient comparisons; nonzero delayed startup negative control')
print('NOT a constructed unforced solution or a proof of convergence')
