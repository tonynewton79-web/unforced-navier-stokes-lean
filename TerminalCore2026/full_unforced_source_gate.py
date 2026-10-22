#!/usr/bin/env python3
"""Fail-closed necessary arithmetic/coverage audit for an UNFORCED theorem.

This test NEVER treats user-entered interval metadata as an authenticated
source certificate, a trusted Lean proof, or an unforced PDE solution.
"""
import argparse
import json
import re
from fractions import Fraction as Q
from pathlib import Path

STAGES = ('inner_axis','first_transition','axial_transition',
 'intermediate_power_law','axial_pulse','A10_interpolation',
 'A11_both_supports_and_gap','exterior_release','steep_decay',
 'terminal_collaring','heat_exterior','joining_patches')
PROOF_GATES = ('source_A11_root_and_eta_derivative',
 'source_A19_amplitude_and_eta_derivative',
 'same_profile_terminal_S_gauge','same_profile_terminal_Pi_gauge',
 'normalized_ten_state_interval_ODE',
 'weighted_velocity_pressure_Banach_recurrence',
 'actual_leading_profile_and_Appendix_B_contraction',
 'unforced_n1_n2_startup','unforced_all_order_source_correspondence',
 'physical_coordinate_zero_force_residual','Cartesian_axis_regularity',
 'blowup_and_energy_conditions','full_Lean_kernel_declarations_and_build')

def exact(x):
 if x is None or isinstance(x,(bool,float)): raise ValueError('No float, bool or missing rational')
 return Q(x)
def hash_ok(s): return isinstance(s,str) and bool(re.fullmatch('[0-9a-f]{64}',s))
def audit(d):
 problems=[];facts={}
 def check(ok,why):
  if not ok: problems.append(why)
  return ok
 if not isinstance(d,dict): d={}
 ident=d.get('source_identity') or {}
 if not isinstance(ident,dict):ident={}
 profile=ident.get('profile_sha256')
 check(hash_ok(profile),'missing authentic source profile hash')
 check(hash_ok(ident.get('source_pdf_sha256')),'missing primary source hash')
 check(bool(ident.get('source_equations_revision')),'missing equation provenance')
 stages=d.get('stage_intervals') or {}
 if not isinstance(stages,dict):stages={}
 for name in STAGES:
  x=stages.get(name)
  if not isinstance(x,dict):
   problems.append('missing full interval stage: '+name);continue
  check(hash_ok(profile) and x.get('profile_sha256')==profile,'wrong source on stage '+name)
  check(hash_ok(x.get('input_sha256')),'missing stage input hash: '+name)
  check(bool(x.get('sound_interval_proof')),'missing stage inclusion proof: '+name)
  if name in ('axial_pulse','A11_both_supports_and_gap','heat_exterior'):
   try:
    check(exact(x['min_Qs'])>0,'nonpositive Qs on '+name)
    check(exact(x['min_cone_margin'])>0,'cone not strict on '+name)
   except (KeyError,ValueError,TypeError,ZeroDivisionError):
    problems.append('missing rational stage margin: '+name)
 z=d.get('A11_same_profile_gauge') or {}
 if not isinstance(z,dict):z={}
 check(hash_ok(profile) and z.get('profile_sha256')==profile,'mismatched A11 gauge source')
 check(hash_ok(z.get('proof_input_sha256')),'missing A11 integration hash')
 check(z.get('total_eta_derivatives_proved') is True,'no TOTAL eta jet certificate')
 try:
  lam=exact(d['lambda']);h=exact(d['h'])
  alpha=exact(z['alpha_K_over_XE']);beta=exact(z['beta_inverse_E'])
  b0=exact(z['zero_gauge_Ns_over_E_bound'])
  f=exact(z['F_sup']);fp=exact(z['F_eta_sup'])
  g=exact(z['G_sup']);gp=exact(z['G_eta_sup'])
  check(0<lam<=Q(1,100),'lambda outside proven regime')
  check(0<h<=lam/100,'h outside proven regime')
  check(all(x>=0 for x in (alpha,beta,b0,f,fp,g,gp)),'negative interval upper bound')
  corr=alpha*((2+4*h)*f+fp)+beta*((1+2*h)*g+gp/2)
  total=b0+corr
  facts={'Ns_over_E_upper':str(total),'target':str(lam/2),'remaining_slack':str(lam/2-total)}
  check(b0<=lam/500,'zero-gauge whole-hull bound fails')
  check(corr<Q(249,500)*lam,'terminal correction exceeds budget')
  check(total<lam/2,'Ns/E exceeds lambda/2')
 except (KeyError,ValueError,TypeError,ZeroDivisionError) as e:
  problems.append('missing/invalid exact A11 rational data: '+str(e))
 other=d.get('analytic_lean_gates') or {}
 if not isinstance(other,dict):other={}
 for name in PROOF_GATES:
  x=other.get(name)
  if not isinstance(x,dict):
   problems.append('unproved full theorem gate: '+name);continue
  check(hash_ok(profile) and x.get('profile_sha256')==profile,'wrong profile gate: '+name)
  check(hash_ok(x.get('evidence_sha256')),'missing evidence hash: '+name)
  check(x.get('reviewed_source_proof') is True,'unreviewed proof: '+name)
 return {'status':('HOLD' if problems else 'CONDITIONAL_ARITHMETIC_PASS_SOURCE_REPLAY_REQUIRED'),
         'source_authenticated':False,'theorem_1_1_proved':False,
         'arithmetic':facts,'blockers':problems}

def main():
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument('dataset',nargs='?')
 ap.add_argument('--self-test',action='store_true')
 ap.add_argument('--template',action='store_true')
 args=ap.parse_args()
 if args.self_test:
  import copy
  p='a'*64
  d={'source_identity':{'profile_sha256':p,'source_pdf_sha256':'b'*64,'source_equations_revision':'2026'},
     'lambda':'1/100','h':'1/100000',
     'stage_intervals':{n:{'profile_sha256':p,'input_sha256':'c'*64,'sound_interval_proof':'SYNTHETIC',
         'min_Qs':'1/100','min_cone_margin':'1/100'} for n in STAGES},
     'A11_same_profile_gauge':{'profile_sha256':p,'proof_input_sha256':'c'*64,
       'total_eta_derivatives_proved':True,'alpha_K_over_XE':'1','beta_inverse_E':'1',
       'zero_gauge_Ns_over_E_bound':'1/50000',
       'F_sup':'1/10000000','F_eta_sup':'1/10000000',
       'G_sup':'1/10000000','G_eta_sup':'1/10000000'},
     'analytic_lean_gates':{n:{'profile_sha256':p,'evidence_sha256':'c'*64,'reviewed_source_proof':True}
           for n in PROOF_GATES}}
  positive=audit(d)
  assert positive['status'].startswith('CONDITIONAL_') and positive['theorem_1_1_proved'] is False
  def neg(mod):
   x=copy.deepcopy(d);mod(x)
   a=audit(x);assert a['status']=='HOLD' and a['theorem_1_1_proved'] is False
  neg(lambda x:x['source_identity'].pop('profile_sha256'))
  neg(lambda x:x['stage_intervals'].pop('axial_pulse'))
  neg(lambda x:x['stage_intervals']['heat_exterior'].update(profile_sha256='f'*64))
  neg(lambda x:x['stage_intervals']['A11_both_supports_and_gap'].update(min_Qs='0'))
  neg(lambda x:x['A11_same_profile_gauge'].pop('F_eta_sup'))
  neg(lambda x:x['A11_same_profile_gauge'].update(total_eta_derivatives_proved=False))
  neg(lambda x:x['A11_same_profile_gauge'].update(G_eta_sup='1'))
  neg(lambda x:x['A11_same_profile_gauge'].update(profile_sha256='e'*64))
  neg(lambda x:x.update(h='1/1000'))
  neg(lambda x:x['analytic_lean_gates'].pop('unforced_n1_n2_startup'))
  neg(lambda x:x['analytic_lean_gates']['physical_coordinate_zero_force_residual'].update(reviewed_source_proof=False))
  neg(lambda x:x['A11_same_profile_gauge'].update(F_sup=0.1))
  neg(lambda x:x['stage_intervals']['heat_exterior'].pop('sound_interval_proof'))
  neg(lambda x:x['analytic_lean_gates']['full_Lean_kernel_declarations_and_build'].pop('evidence_sha256'))
  print('PASS: 14 fail-closed adversarial negatives and synthetic arithmetic positive; never source certified')
  return
 if args.template:
  print(json.dumps({'source_identity':{'profile_sha256':None,'source_pdf_sha256':None,
    'source_equations_revision':None},'lambda':None,'h':None,
    'stage_intervals':{n:None for n in STAGES},
    'A11_same_profile_gauge':{'profile_sha256':None,'proof_input_sha256':None,
      'total_eta_derivatives_proved':None},
    'analytic_lean_gates':{n:None for n in PROOF_GATES}},indent=2));return
 if not args.dataset:ap.error('dataset path required')
 r=audit(json.loads(Path(args.dataset).read_text()))
 print(json.dumps(r,indent=2))
 if r['status']=='HOLD':raise SystemExit(2)
if __name__=='__main__':main()
