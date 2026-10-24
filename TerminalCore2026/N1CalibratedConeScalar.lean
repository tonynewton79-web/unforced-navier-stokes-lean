import Mathlib

/-!
Edition XXVII: exact finite scalar cone algebra and restricted fixed-inverse
minimax bounds. Does not formalize Reynolds-stress PDE, radial cutoffs,
the OpenAI forced carrier, nor the desired unforced NSE theorem.
-/
namespace TerminalCore2026

def xxviiA (mu M : ℝ) : ℝ := (3/8)*mu+(13/4)*M
def xxviiB (mu M : ℝ) : ℝ := (85/8)*mu+(471/4)*M

def xxviiD1 (rr tt zz mu M : ℝ) : ℝ :=
  rr-16*(tt+zz)+mu+33*M
def xxviiD2 (tt rt mu M : ℝ) : ℝ :=
  8*tt+2*rt+mu+10*M
def xxviiD3 (tt rt mu M : ℝ) : ℝ :=
  8*tt-2*rt+3*mu+26*M
def xxviiD4 (zz rz tz mu M : ℝ) : ℝ :=
  8*zz+2*rz-8*tz+2*mu+18*M
def xxviiD5 (zz rz tz mu M : ℝ) : ℝ :=
  8*zz-2*rz+8*tz+2*mu+18*M
def xxviiD6 (tz mu M : ℝ) : ℝ := 8*tz+mu+8*M
def xxviiD7 (tz mu M : ℝ) : ℝ := -8*tz+mu+8*M

theorem xxvii_rr (rr tt zz rt rz tz mu M : ℝ) :
    xxviiD1 rr tt zz mu M +
      xxviiD2 tt rt mu M + xxviiD3 tt rt mu M +
      xxviiD4 zz rz tz mu M + xxviiD5 zz rz tz mu M +
      xxviiD6 tz mu M + xxviiD7 tz mu M =
    rr + xxviiA mu M + xxviiB mu M := by
  unfold xxviiD1 xxviiD2 xxviiD3 xxviiD4 xxviiD5
    xxviiD6 xxviiD7 xxviiA xxviiB
  ring

theorem xxvii_tt (tt rt tz mu M : ℝ) :
    (xxviiD2 tt rt mu M + xxviiD3 tt rt mu M +
      xxviiD6 tz mu M + xxviiD7 tz mu M)/16 =
    tt + xxviiA mu M := by
  unfold xxviiD2 xxviiD3 xxviiD6 xxviiD7 xxviiA
  ring

theorem xxvii_zz (zz rz tz mu M : ℝ) :
    (xxviiD4 zz rz tz mu M + xxviiD5 zz rz tz mu M +
      xxviiD6 tz mu M + xxviiD7 tz mu M)/16 =
    zz + xxviiA mu M := by
  unfold xxviiD4 xxviiD5 xxviiD6 xxviiD7 xxviiA
  ring

theorem xxvii_rt (tt rt tz mu M : ℝ) :
    (xxviiD2 tt rt mu M-xxviiD3 tt rt mu M+
      xxviiD6 tz mu M+xxviiD7 tz mu M)/4 = rt := by
  unfold xxviiD2 xxviiD3 xxviiD6 xxviiD7
  ring

theorem xxvii_rz (zz rz tz mu M : ℝ) :
    (xxviiD4 zz rz tz mu M-xxviiD5 zz rz tz mu M+
      xxviiD6 tz mu M-xxviiD7 tz mu M)/4 = rz := by
  unfold xxviiD4 xxviiD5 xxviiD6 xxviiD7
  ring

theorem xxvii_tz (tz mu M : ℝ) :
    (xxviiD6 tz mu M-xxviiD7 tz mu M)/16 = tz := by
  unfold xxviiD6 xxviiD7
  ring

theorem xxvii_floor_1 (rr tt zz mu M : ℝ)
    (hrr : -M ≤ rr) (htt : tt ≤ M) (hzz : zz ≤ M) :
    mu ≤ xxviiD1 rr tt zz mu M := by
  unfold xxviiD1
  linarith

theorem xxvii_floor_2 (tt rt mu M : ℝ)
    (htt : -M ≤ tt) (hrt : -M ≤ rt) :
    mu ≤ xxviiD2 tt rt mu M := by
  unfold xxviiD2
  linarith

theorem xxvii_floor_3 (tt rt mu M : ℝ)
    (htt : -M ≤ tt) (hrt : rt ≤ M) (hmu : 0 ≤ mu) (hM : 0 ≤ M) :
    mu ≤ xxviiD3 tt rt mu M := by
  unfold xxviiD3
  linarith

theorem xxvii_floor_4 (zz rz tz mu M : ℝ)
    (hzz : -M ≤ zz) (hrz : -M ≤ rz) (htz : tz ≤ M)
    (hmu : 0 ≤ mu) :
    mu ≤ xxviiD4 zz rz tz mu M := by
  unfold xxviiD4
  linarith

theorem xxvii_floor_5 (zz rz tz mu M : ℝ)
    (hzz : -M ≤ zz) (hrz : rz ≤ M) (htz : -M ≤ tz)
    (hmu : 0 ≤ mu) :
    mu ≤ xxviiD5 zz rz tz mu M := by
  unfold xxviiD5
  linarith

theorem xxvii_floor_6 (tz mu M : ℝ)
    (htz : -M ≤ tz) :
    mu ≤ xxviiD6 tz mu M := by
  unfold xxviiD6
  linarith

theorem xxvii_floor_7 (tz mu M : ℝ)
    (htz : tz ≤ M) :
    mu ≤ xxviiD7 tz mu M := by
  unfold xxviiD7
  linarith

theorem xxvii_baseline_sharp (d1 d2 h mu : ℝ)
    (h1 : mu ≤ d1) (h2 : mu ≤ d2) (hh : mu ≤ h) :
    (85/8 : ℝ)*mu ≤ d1+(31/8)*d2+(23/4)*h := by
  linarith

theorem xxvii_fixed_inverse_minimax (a h b mu M : ℝ)
    (hh : mu+8*M ≤ h)
    (ha : mu+2*h+10*M ≤ 8*a)
    (hb : mu+31*a-2*h+33*M ≤ b) :
    (85/8 : ℝ)*mu+(471/4)*M ≤ b := by
  linarith

theorem xxvii_improved_gauge_budget (mu M : ℝ) :
    xxviiA mu M + xxviiB mu M = 11*mu+121*M := by
  unfold xxviiA xxviiB
  ring

#print axioms xxvii_rr
#print axioms xxvii_tt
#print axioms xxvii_zz
#print axioms xxvii_rt
#print axioms xxvii_rz
#print axioms xxvii_tz
#print axioms xxvii_baseline_sharp
#print axioms xxvii_fixed_inverse_minimax
end TerminalCore2026
