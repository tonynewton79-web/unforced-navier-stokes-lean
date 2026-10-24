#!/usr/bin/env python3
"""Exact derivative constants from the 64 frozen certificates; NOT a PDE proof."""
from pathlib import Path
from fractions import Fraction as F

p=Path(__file__).with_name("XXVIII_64_CORNER_EXACT_CERTIFICATES.txt")
rows=[[F(x) for x in line.split()] for line in p.read_text().splitlines()
      if line.strip() and not line.startswith("#")]
assert len(rows)==64
L=[]
for col in range(8):
    derivatives=[]
    for axis in range(6):
        flip=1<<(5-axis)
        derivatives.append(max(abs(rows[i][col]-rows[i^flip][col])
                             for i in range(64))/2)
    L.append(derivatives)
assert L==[
 [0,1,1,F(1,4),F(1,4),F(1,4)],
 [1,16,16,F(31,4),F(31,4),F(31,4)],
 [0,8,8,2,2,2],
 [0,8,8,4,2,2],
 [0,8,8,2,4,10],
 [0,8,8,2,4,10],
 [0,0,0,0,0,8],
 [0,0,0,0,0,8]]
assert list(map(sum,L))==[F(11,4),F(225,4),F(22),F(24),F(32),F(32),F(8),F(8)]
assert [max(row[j] for row in rows) for j in range(8)]==[
 F(13,4),F(99,2),F(20),F(36),F(36),F(36),F(16),F(16)]
print("PASS 48 exact vertex directional differences and Lipschitz constants")
print("PASS isotropic gauge derivative <= 11/4 times max stress-entry derivative")
print("PASS worst ray coefficient derivative <= 225/4 times max derivative")
print("HOLD time-dependent source and physical H8 derivative norm certification")
