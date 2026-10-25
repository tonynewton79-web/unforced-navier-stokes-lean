"""Source-native quadratic highest-jet scalar and denominator audit.
The complete bilinear pressure recurrence remains unproved.
"""
import sympy as s
z=s.symbols('z')
h=s.Rational(1,200)
G=(1-z*z)/(1-2*h*z*z)
B=2*z/(1-2*h*z*z)
D=s.Rational(1,2)-h
f=s.Function('f')(z)
u=s.Function('u')(z)
sample=0
for k in (2,3,7):
    for j in (1,k-1):
        i=k-j
        if i<1:
            continue
        for a,b in ((i,j),(i+2,j+1)):
            r=b+1
            N=a+b
            W=B*(r-D-2*h*j)/r*f-G/r*s.diff(f,z)
            H=u*(G*s.diff(W,z)+B*(2*h*j-1-b)*W)
            second=s.expand(H).coeff(s.Derivative(f,z,2))
            assert s.simplify(second+u*G**2/r)==0
            highest=-G*second/(4*(N+1)*(N+2)**2)
            assert s.simplify(highest-u*G**3/(4*r*(N+1)*(N+2)**2))==0
            sample+=1
print('PASS quadratic highest-jet source identities',sample)
count=0
for i in range(1,30):
    for j in range(1,30):
        for a in (i,i+1,i+9):
            for b in (j,j+1,j+3):
                N=a+b;r=b+1
                assert r*(N+1)*(N+2)**2 >= r*r*(b+2)**2
                count+=1
assert count==7569
print('PASS exact quadratic radial denominator domination',count)
