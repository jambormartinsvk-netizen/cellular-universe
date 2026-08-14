#!/usr/bin/env python
"""Exact no-ODE audit: can frozen K7 background be a universal H(a)?"""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]; BASE=ROOT/'scripts'/'baseScripts'; sys.path.insert(0,str(BASE))
from a2_k4_g8.background_universality import audit  # noqa: E402
def h(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest().upper()
def write(p,payload):
    if p.exists(): raise FileExistsError(f'immutable output exists: {p}')
    if not p.parent.is_dir(): raise FileNotFoundError(f'missing output parent: {p.parent}')
    p.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n',encoding='utf-8')
def main():
    q=argparse.ArgumentParser(description=__doc__); q.add_argument('--max-runtime-seconds',type=float,default=10.0); q.add_argument('--output',type=Path); q.add_argument('--smoke',action='store_true'); a=q.parse_args()
    if not 0<a.max_runtime_seconds<=10:q.error('--max-runtime-seconds must be in (0,10]')
    if not a.smoke and a.output is None:q.error('--output required unless --smoke')
    if a.smoke: print(json.dumps({'smoke':'PASS','scope':'exact_symbolic_no_ode'},sort_keys=True));return 0
    x=audit(a.max_runtime_seconds);x['script_sha256']=h(__file__);x['shared_module_sha256']=h(BASE/'a2_k4_g8'/'background_universality.py');write(a.output.resolve(),x);print(json.dumps(x,indent=2,sort_keys=True));return 0 if x['verdict']=='REVIEW_ALGEBRA_UNCLOSED' else 1
if __name__=='__main__':
  try: raise SystemExit(main())
  except TimeoutError as e: print(json.dumps({'verdict':'TIMEOUT_UNCLOSED','error':str(e)}));raise SystemExit(124)
  except Exception as e: print(json.dumps({'verdict':'ERROR_UNCLOSED','error':repr(e)}));raise SystemExit(2)
