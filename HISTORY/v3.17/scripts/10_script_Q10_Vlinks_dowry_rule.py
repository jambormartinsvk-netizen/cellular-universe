import numpy as np, json
rng=np.random.default_rng(7)

def simulate(N0,rounds,frac,C,init_n,split="half",spatial=False):
    pos=list(rng.random((N0,3))) if spatial else None
    V=[dict() for _ in range(N0)]
    for i in range(N0):
        while sum(V[i].values())<init_n:
            j=int(rng.integers(N0))
            if j!=i:
                V[i][j]=V[i].get(j,0)+1.0; V[j][i]=V[j].get(i,0)+1.0
    def total(i): return sum(V[i].values())
    def prune(i,sib):
        t=total(i)
        if t<=C+1e-9: return
        # proportional cut on non-sibling links (continuous reading)
        others=[k for k in V[i] if k!=sib]
        excess=t-C
        tot_o=sum(V[i][k] for k in others)
        if tot_o<=0: return
        f=excess/tot_o
        for k in others:
            cut=V[i][k]*f
            V[i][k]-=cut; V[k][i]-=cut
            if V[i][k]<1e-12: del V[i][k]; del V[k][i]
    traj=[]
    for r in range(rounds):
        N=len(V)
        idx=rng.choice(N,size=int(frac*N),replace=False)
        for p in idx:
            q=len(V); V.append(dict())
            if spatial:
                d=0.3*len(V)**(-1/3)
                u=rng.normal(size=3); u/=np.linalg.norm(u)
                child=np.clip(pos[p]+u*d/2,0,1); pos[p]=np.clip(pos[p]-u*d/2,0,1)
                pos.append(child)
            links=list(V[p].items())
            if split=="half":
                for (j,w) in links:
                    V[p][j]=w/2; V[j][p]=w/2
                    V[q][j]=V[q].get(j,0)+w/2; V[j][q]=V[j].get(q,0)+w/2
            else:
                for (j,w) in links:
                    if rng.random()<0.5:
                        del V[p][j]; del V[j][p]
                        V[q][j]=V[q].get(j,0)+w; V[j][q]=V[j].get(q,0)+w
            V[p][q]=V[p].get(q,0)+C/2; V[q][p]=V[q].get(p,0)+C/2
            prune(p,q); prune(q,p)
        ns=[total(i) for i in range(len(V))]
        traj.append((r+1,float(np.mean(ns)),float(np.std(ns))))
    return traj,V,(np.array(pos) if spatial else None)

C=27.0
# 1) sharpness under continuous reading (abstract), from below and above
for lab,init in [("half_start_5",5),("half_start_40",40)]:
    traj,V,_=simulate(3000,14,0.08,C,init,"half")
    g,m,sd=traj[-1]
    print(json.dumps({lab:{"final_mean":round(m,2),"std_over_mean":round(sd/m,3),
        "traj":[round(t[1],1) for t in traj[::3]]}}))

# 2) spatial area-law test: clean start (init 0), all links division-born
traj,V,P=simulate(800,22,0.12,C,0,"half",spatial=True)
g,m,sd=traj[-1]
print(json.dumps({"spatial":{"N_final":len(V),"mean_nV":round(m,2),
    "std_over_mean":round(sd/m,3)}}))
center=np.array([0.5,0.5,0.5])
res=[]
for R in [0.10,0.14,0.18,0.24,0.30]:
    inside=np.linalg.norm(P-center,axis=1)<R
    cross=0.0
    for i in range(len(V)):
        if inside[i]:
            for j,w in V[i].items():
                if not inside[j]: cross+=w
    res.append((R,cross))
    print(json.dumps({"R":R,"cross_weight":round(cross,1)}))
lr=np.log([r[0] for r in res]); lc=np.log([r[1] for r in res])
p=np.polyfit(lr,lc,1)[0]
print(json.dumps({"exponent_p":round(float(p),2),"kriterium":"[1.7,2.3] = plosny zakon"}))
