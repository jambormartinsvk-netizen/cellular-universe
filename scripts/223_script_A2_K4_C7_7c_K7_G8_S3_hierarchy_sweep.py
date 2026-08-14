#!/usr/bin/env python
"""Bounded G8 S3 hierarchy-tail convergence sweep; no score award."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]; BASE=ROOT/'scripts'/'baseScripts'; sys.path.insert(0,str(BASE))
from a2_k4_g8.s3_hierarchy_sweep import names, run_sweep  # noqa: E402
def digest(path: Path) -> str: return hashlib.sha256(path.read_bytes()).hexdigest().upper()
def write_immutable(path: Path, payload: dict[str, object]) -> None:
    if path.exists(): raise FileExistsError(f'immutable output exists: {path}')
    if not path.parent.is_dir(): raise FileNotFoundError(f'missing output parent: {path.parent}')
    path.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n',encoding='utf-8')
def main() -> int:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--max-runtime-seconds',type=float,default=45.0); p.add_argument('--output',type=Path); p.add_argument('--smoke',action='store_true'); a=p.parse_args()
    if not 0<a.max_runtime_seconds<=45: p.error('--max-runtime-seconds must be in (0,45]')
    if not a.smoke and a.output is None: p.error('--output is required unless --smoke')
    if a.smoke: print(json.dumps({'smoke':'PASS','lmax8_dynamic_state_count':len(names(8))},sort_keys=True)); return 0
    payload=run_sweep(a.max_runtime_seconds); payload['script_sha256']=digest(Path(__file__).resolve()); payload['shared_module_sha256']=digest(BASE/'a2_k4_g8'/'s3_hierarchy_sweep.py'); write_immutable(a.output.resolve(),payload); print(json.dumps(payload,indent=2,sort_keys=True)); return 0 if payload['verdict']=='PASS_G8_SCREEN_S3_HIERARCHY_CONVERGENCE' else 1
if __name__=='__main__':
    try: raise SystemExit(main())
    except TimeoutError as e: print(json.dumps({'verdict':'TIMEOUT_UNCLOSED','error':str(e)})); raise SystemExit(124)
    except Exception as e: print(json.dumps({'verdict':'ERROR_UNCLOSED','error':repr(e)})); raise SystemExit(2)
