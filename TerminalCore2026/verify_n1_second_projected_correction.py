"""Exact rational and periodic divergence-free tests for Edition XIX; no PDE existence proof."""
from fractions import Fraction as Q
from itertools import product
import sympy as s

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def neg(a): return tuple(-x for x in a)
def sub(a,b): return add(a,neg(b))
def B(a,b): return (a[0]*b[1]+2*a[1]*b[0], a[0]*b[0]-3*a[1]*b[1])

n=0
for p in product((-2,-1,0,1,2),repeat=6):
    u=(Q(p[0]),Q(p[1])); v=(Q(p[2]),Q(p[3])); w=(Q(p[4]),Q(p[5]))
    q1=add(add(B(u,v),B(v,u)),B(v,v))
    q2=add(add(add(add(B(u,w),B(w,u)),B(v,w)),B(w,v)),B(w,w))
    f=(Q(3),Q(-2))
    assert add(add(add(add(f,neg(f)),q1),neg(q1)),q2)==q2
    assert sub(B(add(add(u,v),w),add(add(u,v),w)),B(u,u))==add(q1,q2)
    n+=1

u=(Q(1),Q(2)); v=(Q(3),Q(5)); w=(Q(7),Q(11))
full=sub(B(add(add(u,v),w),add(add(u,v),w)),B(add(u,v),add(u,v)))
assert full!=add(add(add(B(u,w),B(w,u)),B(w,v)),B(w,w))
assert full!=add(add(add(B(u,w),B(w,u)),B(v,w)),B(w,w))

x,y,z=s.symbols("x y z",real=True)
def c(a,b):
    return s.Matrix([s.expand(sum(a[j]*s.diff(b[i],d) for j,d in enumerate((x,y,z)))) for i in range(3)])
def zero(v):
    return all(s.trigsimp(s.expand_trig(s.expand(t)))==0 for t in v)

u=s.Matrix([s.sin(y),s.sin(z),s.sin(x)])
v=s.Matrix([s.sin(y)*s.cos(z),0,0])
w=s.Matrix([0,s.sin(z)*s.cos(x),0])
assert all(zero([sum(s.diff(a[j],d) for j,d in enumerate((x,y,z)))]) for a in (u,v,w))
q1=c(u,v)+c(v,u)+c(v,v)
q2=c(u,w)+c(w,u)+c(v,w)+c(w,v)+c(w,w)
assert zero(c(u+v+w,u+v+w)-c(u,u)-q1-q2)
assert not zero(q2-c(v,w))
assert not zero(q2-c(w,v))

t,ss,h,K=s.symbols("t ss h K", positive=True)
amplification=(K/h)*((1-t)**(-h)-(1-ss)**(-h))
assert s.simplify(s.diff(amplification,t)-K*(1-t)**(-1-h))==0
assert s.simplify(s.limit(amplification,h,0,dir="+")-K*(s.log(1-ss)-s.log(1-t)))==0
print(f"PASS: {n}/{n} rational cases, missing-term negative controls, periodic PDE-mode algebra, and exact amplification check")
print("HOLD: genuine source, full pressure, corrected PDE and terminal singularity.")
