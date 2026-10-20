"""Source-native exact normal form for five leading-profile pressure terms.

Checks the entire 0..3 eta-derivative source symbol at exact rational eta
samples, preserving variable coefficients and radial degrees. Also checks
the all-index scalar inequality needed to majorize the highest jet by a
profile with a D_X multiplier. Does not prove lower-jet norm bounds.
"""
import sympy as s
E=s.symbols('e')
count=0
for h in (s.Rational(1,200),s.Rational(1,400)):
    L=1-2*h*E**2;B=2*E/L;G=(1-E**2)/L
    D=s.Rational(1,2)-h;A=s.Rational(1,2)+h
    for k in (1,4):
        lam=2*h*k;q=2*h*(k+1)-2*A
        for a,c in ((k,0),(k+2,1)):
            r=a+1;m=a+c+1;N=m+1
            v=1+E/5;u=2-E/7;K=E+3
            F=1+3*E+E**2-E**3/7
            w0=B*(r-D-lam)/r;w1=-G/r
            W=w0*F+w1*s.diff(F,E)
            H=v*W+(u*(G*s.diff(W,E)+B*(lam-1-a)*W)+K*F)/m
            direct=-(B*(q-m)*H+G*s.diff(H,E))/(4*N**2)
            H0=v*w0+(u*(G*s.diff(w0,E)+B*(lam-1-a)*w0)+K)/m
            H1=v*w1+u*(G*(w0+s.diff(w1,E))+B*(lam-1-a)*w1)/m
            H2=u*G*w1/m
            hjs=[H0,H1,H2,s.Integer(0)]
            Ps=[]
            for j in range(4):
                prev=hjs[j-1] if j else s.Integer(0)
                Ps.append(-(B*(q-m)*hjs[j]+G*(s.diff(hjs[j],E)+prev))/(4*N**2))
            normalized=sum(Ps[j]*s.diff(F,E,j) for j in range(4))
            for z in (s.Rational(-1,2),s.Rational(0),s.Rational(3,5)):
                assert s.cancel((direct-normalized).subs(E,z))==0
                assert s.cancel((Ps[3]-u*G**3/(4*r*m*N**2)).subs(E,z))==0
                count+=1
print("PASS",count,"exact source-native leading-pressure normal-form samples")
count=0
for k in range(1,36):
    for a in range(k,k+10):
        r=a+1
        for c in (0,1,2,5,11,101,1001):
            m=a+c+1
            assert s.Rational(m,r)<=c+1
            count+=1
print("PASS",count,"highest-jet radial multiplier dominance inequalities")
