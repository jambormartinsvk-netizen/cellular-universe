import numpy as np
from scipy.spatial import Delaunay
km=48*np.pi**2/35+2
for M,seed in [(60000,1),(200000,1),(200000,7)]:
    P=np.random.default_rng(seed).random((M,3))
    s=Delaunay(P).simplices
    pr=np.vstack([s[:,[i,j]] for i in range(4) for j in range(i+1,4)])
    Ed=np.unique(np.sort(pr,axis=1),axis=0)
    ins=np.all((P>0.25)&(P<0.75),axis=1)
    Ed=Ed[ins[Ed[:,0]] & ins[Ed[:,1]]]
    D=np.linalg.norm(P[Ed[:,1]]-P[Ed[:,0]],axis=1)*M**(1/3)
    m2,m4=(D**2).mean(),(D**4).mean()
    xi=m4/(20*m2)
    Om=np.sqrt(6/(km*m2))
    # mean degree check: 2E/N over interior
    print(f"M={M:7d} seed={seed}  <D2>={m2:.4f} <D4>={m4:.4f}  xi={xi:.6f}  Omega_cell=c/({1/Om:.3f} l0)")
