import numpy as np
from scipy.spatial import Delaunay
from scipy import sparse
from scipy.optimize import curve_fit
import json

rng = np.random.default_rng(11)
N = 100000
pts = rng.random((N, 3))
sp = N ** (-1/3)

margin = 0.15
allp=[pts]; orig=[np.arange(N)]; isreal=[np.ones(N,bool)]
for dx in (-1,0,1):
    for dy in (-1,0,1):
        for dz in (-1,0,1):
            if dx==dy==dz==0: continue
            q = pts + np.array([dx,dy,dz])
            m = np.all((q>-margin)&(q<1+margin),axis=1)
            allp.append(q[m]); orig.append(np.where(m)[0])
            isreal.append(np.zeros(m.sum(),bool))
P=np.vstack(allp); O=np.concatenate(orig); R=np.concatenate(isreal)
tri=Delaunay(P); s=tri.simplices
pairs=[]
for a in range(4):
    for b in range(a+1,4):
        pairs.append(np.column_stack([s[:,a],s[:,b]]))
Eraw=np.vstack(pairs)
# keep edges with at least one REAL endpoint
keep = R[Eraw[:,0]] | R[Eraw[:,1]]
Eraw = Eraw[keep]
E = np.column_stack([O[Eraw[:,0]], O[Eraw[:,1]]])
E = E[E[:,0]!=E[:,1]]
E = np.unique(np.sort(E,axis=1),axis=0)
kbar = 2*len(E)/N
d = pts[E[:,0]]-pts[E[:,1]]; d -= np.round(d)
maxlen=float(np.linalg.norm(d,axis=1).max())
print(json.dumps({"kbar":float(kbar),"theory":15.54,"max_edge_over_spacing":maxlen/sp}))

def om_formula(kvec):
    return np.sqrt(2*np.sum(1-np.cos(d@kvec))/N)

# dispersion fit: commensurate k in many directions via integer triples
tripls=[(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1),(1,1,1),
        (2,1,0),(2,0,1),(1,2,0),(2,1,1),(1,2,1),(1,1,2),(3,1,0),(2,2,1)]
recs=[]
for tr in tripls:
    v=np.array(tr,float); nv=np.linalg.norm(v)
    for mlt in range(1,13):
        kvec=2*np.pi*mlt*v
        ka=2*np.pi*mlt*nv*sp
        if ka>1.6: break
        recs.append((ka,om_formula(kvec),tr))
recs.sort()
kas=np.array([r[0] for r in recs]); oms=np.array([r[1] for r in recs])
# c from smallest ka points
small=kas<0.30
c0=np.mean(oms[small]/(kas[small]/sp))
y=oms/(c0*kas/sp)-1
w=kas<=1.0
Xodd=np.vstack([kas[w],kas[w]**2]).T
co,_ ,*_=np.linalg.lstsq(Xodd,y[w],rcond=None)
Xev=np.vstack([kas[w]**2,kas[w]**4]).T
ce,_ ,*_=np.linalg.lstsq(Xev,y[w],rcond=None)
res_odd=float(np.abs(y[w]-Xodd@co).max()); res_ev=float(np.abs(y[w]-Xev@ce).max())
# isotropy: spread of omega among directions at nearly equal ka
# collect groups with ka within 2% of each other around ka~0.9
grp=[(ka,om,tr) for ka,om,tr in recs if 0.8<ka<1.05]
rel=[om/ (c0*ka/sp) for ka,om,tr in grp]
print(json.dumps({"c":float(c0),
 "fit_alpha_beta":[float(co[0]),float(co[1])],"resid_odd":res_odd,
 "fit_beta_gamma":[float(ce[0]),float(ce[1])],"resid_even":res_ev,
 "n_kpoints":int(w.sum()),
 "iso_relspread_ka0.8_1.05":float(np.std(rel)/np.mean(rel))}))

# evolution validation on clean periodic graph
rows=np.concatenate([E[:,0],E[:,1]]); cols=np.concatenate([E[:,1],E[:,0]])
A=sparse.csr_matrix((np.ones(len(rows)),(rows,cols)),shape=(N,N))
L=sparse.diags(np.asarray(A.sum(axis=1)).ravel())-A

def evolve(kvec, periods=12, spp=120):
    phase=pts@kvec
    u=np.cos(phase); v=np.zeros(N)
    omp=om_formula(kvec)
    dt=2*np.pi/omp/spp
    pc=np.cos(phase)
    amps=[]
    for _ in range(periods*spp):
        v-=dt*(L@u); u+=dt*v
        amps.append(pc@u/N)
    t=np.arange(1,periods*spp+1)*dt; amps=np.array(amps)
    f=lambda t,Aa,wq,ph,tau: Aa*np.exp(-t/tau)*np.cos(wq*t+ph)
    p,_=curve_fit(f,t,amps,p0=[amps[0],omp,0.0,t[-1]],maxfev=30000)
    return omp,abs(p[1]),abs(p[3])

for mlt,axis,lab in [(3,(1,0,0),"x_k3"),(5,(1,0,0),"x_k5"),(8,(1,0,0),"x_k8"),
                     (3,(0,1,0),"y_k3"),(2,(1,1,1),"diag_k2"),(3,(1,1,1),"diag_k3")]:
    v=np.array(axis,float)
    kvec=2*np.pi*mlt*v
    ka=np.linalg.norm(kvec)*sp
    omp,omm,tau=evolve(kvec)
    print(json.dumps({"label":lab,"ka":float(ka),
        "omega_formula":float(omp),"omega_evolved":float(omm),
        "rel_diff":float((omm-omp)/omp),"tau":float(tau),
        "Q_periods":float(tau/(2*np.pi/omm))}))
