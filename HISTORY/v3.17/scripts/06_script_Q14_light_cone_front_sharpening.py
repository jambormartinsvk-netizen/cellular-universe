import numpy as np
from scipy.spatial import Delaunay
from collections import deque
import sys, json

rng = np.random.default_rng(42)

def delaunay_adjacency(pts):
    tri = Delaunay(pts)
    N = len(pts)
    # collect edges from simplices
    s = tri.simplices
    pairs = []
    for a in range(4):
        for b in range(a+1, 4):
            pairs.append(np.sort(s[:, [a, b]], axis=1))
    E = np.unique(np.vstack(pairs), axis=0)
    adj = [[] for _ in range(N)]
    for u, v in E:
        adj[u].append(int(v))
        adj[v].append(int(u))
    return adj

def bfs_hops(adj, src, N):
    dist = np.full(N, -1, dtype=np.int32)
    dist[src] = 0
    dq = deque([src])
    while dq:
        u = dq.popleft()
        du = dist[u]
        for v in adj[u]:
            if dist[v] < 0:
                dist[v] = du + 1
                dq.append(v)
    return dist

def grow_network(N0, rounds, frac, seed):
    r = np.random.default_rng(seed)
    pts = r.random((N0, 3))
    for _ in range(rounds):
        N = len(pts)
        spacing = N ** (-1/3)
        d = 0.3 * spacing
        k = int(frac * N)
        idx = r.choice(N, size=k, replace=False)
        dirs = r.normal(size=(k, 3))
        dirs /= np.linalg.norm(dirs, axis=1)[:, None]
        parents = pts[idx]
        d1 = parents + dirs * d / 2
        d2 = parents - dirs * d / 2
        # replace parent by daughter1, append daughter2
        pts[idx] = np.clip(d1, 0, 1)
        pts = np.vstack([pts, np.clip(d2, 0, 1)])
    return pts

def analyze(pts, label, n_sources=3, seed=1):
    N = len(pts)
    adj = delaunay_adjacency(pts)
    center = np.array([0.5, 0.5, 0.5])
    # sources near center
    dc = np.linalg.norm(pts - center, axis=1)
    cand = np.argsort(dc)[:50]
    r = np.random.default_rng(seed)
    srcs = r.choice(cand, size=n_sources, replace=False)
    results = []
    for src in srcs:
        dist = bfs_hops(adj, src, N)
        rr = np.linalg.norm(pts - pts[src], axis=1)
        # boundary limit: max usable radius from this source
        p = pts[src]
        rmax_box = min(p.min(), (1 - p).min())
        tmax = dist.max()
        shells = []
        for t in range(1, tmax + 1):
            m = dist == t
            if m.sum() < 20:
                continue
            R = rr[m].mean()
            S = rr[m].std()
            if R + 3 * S > rmax_box:
                break
            shells.append((t, R, S, int(m.sum())))
        results.append(shells)
    # aggregate: fit per source, then combine
    chis, speeds = [], []
    all_shells = []
    for shells in results:
        sh = np.array(shells)
        if len(sh) < 6:
            continue
        t, R, S = sh[:, 0], sh[:, 1], sh[:, 2]
        # skip first few shells (lattice-scale transient)
        keep = t >= 4
        t, R, S = t[keep], R[keep], S[keep]
        if len(t) < 5:
            continue
        # speed: linear fit R vs t
        A = np.vstack([t, np.ones_like(t)]).T
        v, c0 = np.linalg.lstsq(A, R, rcond=None)[0]
        speeds.append(v)
        # chi: log-log fit sigma vs R
        chi, lc = np.polyfit(np.log(R), np.log(S), 1)
        chis.append(chi)
        all_shells.append(sh)
    # isotropy for first source
    src = srcs[0]
    dist = bfs_hops(adj, src, N)
    vec = pts - pts[src]
    rr = np.linalg.norm(vec, axis=1)
    # nodes at a fixed hop shell well inside box
    tref = None
    for shells in results[:1]:
        if shells:
            tref = shells[len(shells)//2][0]
    iso = None
    if tref:
        m = dist == tref
        v = vec[m]; rn = rr[m]
        # octant mean radii
        signs = (v > 0)
        oct_id = signs[:, 0] * 4 + signs[:, 1] * 2 + signs[:, 2]
        means = [rn[oct_id == o].mean() for o in range(8) if (oct_id == o).sum() > 5]
        iso = (np.std(means) / np.mean(means)) if means else None
    kbar = np.mean([len(a) for a in adj])
    out = {
        "label": label, "N": N, "kbar": float(kbar),
        "chi_mean": float(np.mean(chis)), "chi_std": float(np.std(chis)),
        "chi_all": [float(c) for c in chis],
        "speed_mean": float(np.mean(speeds)), "speed_std": float(np.std(speeds)),
        "iso_octant_rel_std": float(iso) if iso is not None else None,
        "n_sources_used": len(chis),
    }
    print(json.dumps(out, indent=1))
    return out, all_shells

if __name__ == "__main__":
    mode = sys.argv[1]
    N = int(sys.argv[2])
    if mode == "poisson":
        pts = rng.random((N, 3))
        analyze(pts, f"poisson_{N}")
    elif mode == "grown":
        # grow from N0 by 8%/round to ~N (14 rounds ~ 2.94x)
        rounds = 14
        N0 = int(N / (1.08 ** rounds))
        pts = grow_network(N0, rounds, 0.08, seed=7)
        analyze(pts, f"grown_{len(pts)}")
