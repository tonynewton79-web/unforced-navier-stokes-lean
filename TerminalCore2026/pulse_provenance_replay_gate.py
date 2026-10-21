"""Byte-level evidence replay for the source pulse covering.

Hash authentication is not a mathematical enclosure certificate.
This gate NEVER declares the unforced Navier--Stokes theorem proved.
"""
from __future__ import annotations
import argparse,hashlib,json,pathlib,tempfile
from full_pulse_cover_gate import audit,GateError

class EvidenceError(ValueError):pass
def digest(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
    return h.hexdigest()
def evidence_path(root,name):
    if not isinstance(name,str) or not name or pathlib.Path(name).is_absolute():
        raise EvidenceError('Expected relative evidence file path')
    root=pathlib.Path(root).resolve()
    p=(root/name).resolve()
    try:p.relative_to(root)
    except ValueError as exc:raise EvidenceError('Path traversal') from exc
    if not p.is_file():raise EvidenceError('Missing evidence file: '+name)
    return p
def inspect(doc,root):
    checked={}
    for hash_key,file_key in (
        ('source_pdf_sha256','source_pdf_file'),
        ('coefficient_derivation_file_sha256','coefficient_derivation_file'),
        ('interval_proof_file_sha256','interval_proof_file')):
        expect=doc.get(hash_key)
        if not isinstance(expect,str) or len(expect)!=64 or any(c not in '0123456789abcdef' for c in expect):
            raise EvidenceError('Invalid expected SHA-256: '+hash_key)
        p=evidence_path(root,doc.get(file_key))
        actual=digest(p)
        if actual!=expect:raise EvidenceError('Evidence-byte digest mismatch: '+file_key)
        checked[file_key]={'actual_sha256':actual,'bytes':p.stat().st_size}
    conditional=audit(doc)
    return {
      'status':'REPLAYED_BYTES_NOT_MATHEMATICALLY_VERIFIED_SOURCE_INTERVALS',
      'file_byte_hashes_verified':True,
      'analytic_source_enclosures_proved':False,
      'full_pulse_rational_checks':conditional,
      'unforced_theorem_1_1_proved':False,
      'evidence':checked}
def selftest():
    with tempfile.TemporaryDirectory() as temp:
      root=pathlib.Path(temp);file=root/'source.pdf';file.write_bytes(b'fixture')
      d={'source_pdf_file':'source.pdf','source_pdf_sha256':digest(file),
         'coefficient_derivation_file':'source.pdf','coefficient_derivation_file_sha256':digest(file),
         'interval_proof_file':'source.pdf','interval_proof_file_sha256':digest(file),
         'domain':'full_pulse_xi_0_13_eta_-1_1','cells':[]}
      try:inspect(d,root)
      except GateError:pass
      else:raise AssertionError('Empty pulse cover accepted')
      d['source_pdf_sha256']='0'*64
      try:inspect(d,root)
      except EvidenceError:pass
      else:raise AssertionError('Forged hash accepted')
      d['source_pdf_sha256']=digest(file);file.write_bytes(b'tampered')
      try:inspect(d,root)
      except EvidenceError:pass
      else:raise AssertionError('Tampered evidence accepted')
      d['source_pdf_file']='../../etc/passwd'
      try:inspect(d,root)
      except EvidenceError:pass
      else:raise AssertionError('Path traversal accepted')
    print('PASS four evidence-integrity negative controls')
    print('NO source-derived interval covering or full theorem proof')
if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--selftest',action='store_true')
    parser.add_argument('--input')
    parser.add_argument('--evidence-root')
    a=parser.parse_args()
    if a.selftest:selftest()
    else:
      if not a.input or not a.evidence_root:parser.error('Require --input and --evidence-root')
      with open(a.input) as f:data=json.load(f)
      print(json.dumps(inspect(data,a.evidence_root),indent=2))
