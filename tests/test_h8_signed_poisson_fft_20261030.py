"""Independent periodic Fourier-pressure reconstruction; not an H8 existence test."""
import numpy as np
def work(n,lam):
    a=2*np.pi*np.arange(n)/n
    x=a[:,None,None];y=a[None,:,None];z=np.zeros((1,1,8))
    f=np.sin(x)+np.sin(2*x)/3
    fp=np.cos(x)+2*np.cos(2*x)/3
    ux=np.broadcast_to(f*np.sin(y)+lam*np.cos(2*y)+z,(n,n,8))
    uy=np.broadcast_to(fp*np.cos(y)+z,(n,n,8))
    u=[ux,uy,np.zeros_like(ux)]
    k=np.fft.fftfreq(n,d=1/n);kz=np.fft.fftfreq(8,d=1/8)
    ks=[k[:,None,None],k[None,:,None],kz[None,None,:]]
    ks2=sum(q*q for q in ks)
    safe=np.where(ks2==0,1,ks2)
    phat=np.zeros_like(ux,dtype=complex)
    for i in range(3):
        for j in range(3):
            phat-=ks[i]*ks[j]/safe*np.fft.fftn(u[i]*u[j],norm="forward")
    phat[0,0,0]=0
    pressure=np.fft.ifftn(phat,norm="forward").real
    g=lam*np.cos(2*y)+z
    face_work=((pressure[n//2]-pressure[0])*g).sum()*(2*np.pi/n)*(2*np.pi/8)
    return face_work,pressure.mean()
def test_signed_pressure_poisson_fft():
    expected=224*np.pi**2/195
    for n in (16,32):
        for lam in (-2,-1,0,1,2):
            got,mean=work(n,lam)
            assert abs(got-lam*expected)<1e-10,(n,lam,got,lam*expected)
            assert abs(mean)<1e-12
