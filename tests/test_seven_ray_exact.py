"""Independent Fraction replay of the October 2026 H8 seven-ray centre.

The code is deliberately separate from the Lean definitions and uses no
floating-point arithmetic. It checks finite source algebra, not the open H8
weighted compact inverse or a Navier--Stokes singularity.
"""

from fractions import Fraction as F
import unittest


class SevenRayExactTests(unittest.TestCase):
    def test_source_covariance_and_tracefree_projector(self):
        t = F(1, 4)
        vectors = (
            (F(1), F(0), F(0)),
            (F(1), t, F(0)),
            (F(1), -t, F(0)),
            (F(1), F(0), t),
            (F(1), F(0), -t),
            (F(1), t, t),
            (F(1), t, -t),
        )
        raw = (F(1), F(1), F(59, 43), F(1), F(1), F(1), F(1))
        q = tuple(
            tuple(sum((raw[k] * v[i] * v[j] for k, v in enumerate(vectors)), F(0))
                  for j in range(3))
            for i in range(3)
        )
        self.assertEqual(q, (
            (F(317, 43), F(35, 86), F(0)),
            (F(35, 86), F(47, 172), F(0)),
            (F(0), F(0), F(1, 4)),
        ))
        tr = sum((q[i][i] for i in range(3)), F(0))
        self.assertEqual(tr, F(679, 86))
        b = (F(35), F(2), F(0))
        self.assertEqual(sum((x * x for x in b), F(0)), F(1229))
        for i in range(3):
            for j in range(3):
                tracefree = F(172, 1229) * (q[i][j] - (tr / 3 if i == j else 0))
                projector = b[i] * b[j] / 1229 - (F(1, 3) if i == j else 0)
                self.assertEqual(tracefree, projector, (i, j))

    def test_h8_floor_and_physical_efficiency(self):
        self.assertEqual(F(172, 1229) - F(1, 100), F(15971, 122900))
        scaled = tuple(F(172, 1229) * x for x in
                       (F(1), F(1), F(59, 43), F(1), F(1), F(1), F(1)))
        self.assertEqual(scaled, (F(172, 1229), F(172, 1229),
                                  F(236, 1229), F(172, 1229),
                                  F(172, 1229), F(172, 1229), F(172, 1229)))
        # Difference of squares cancels the two source-frame radicals.
        radial_axial = (4 * F(1, 2) - 35**2 * F(91, 200)) / 1229
        self.assertEqual(radial_axial, -F(4443, 9832))
        self.assertGreater(abs(radial_axial), F(9, 20))


if __name__ == "__main__":
    unittest.main()
