"""Exact rational reconstruction of the seven-ray four-field H8 stress.

The XXV source specifies ray coordinates in the co-rotating orthonormal
cylindrical frame (e_r, e_theta, e_z). The physical trace-free tensor is
the ray-coefficient perturbation plus its scalar isotropic pressure gauge.
For a genuinely different orthonormal frame, use R H R^T explicitly;
spatial derivatives of R are not handled by this pointwise certificate.
"""

from fractions import Fraction as Q


QUARTER_RAYS = (
    (Q(1), Q(0), Q(0)),
    (Q(1), Q(1, 4), Q(0)),
    (Q(1), Q(-1, 4), Q(0)),
    (Q(1), Q(0), Q(1, 4)),
    (Q(1), Q(0), Q(-1, 4)),
    (Q(1), Q(1, 4), Q(1, 4)),
    (Q(1), Q(1, 4), Q(-1, 4)),
)


def coefficient_correction(A, B, C, D):
    return (
        -Q(3, 2) * D,
        2 * C - 4 * D,
        -2 * C - 4 * D,
        2 * A - 8 * B + 4 * D,
        -2 * A + 8 * B + 4 * D,
        8 * B,
        -8 * B,
    )


def ray_covariance(A, B, C, D):
    dc = coefficient_correction(A, B, C, D)
    return tuple(tuple(sum((dc[i] * QUARTER_RAYS[i][a] * QUARTER_RAYS[i][b]
                            for i in range(7)), Q(0))
                       for b in range(3)) for a in range(3))


def cylinder_tensor(A, B, C, D):
    S = ray_covariance(A, B, C, D)
    return tuple(tuple(S[i][j] + (D / 2 if i == j else 0)
                       for j in range(3)) for i in range(3))


def recover_four_coordinates(H):
    """Invert only on the four-dimensional frozen-frame trace-free subspace.

    Reject symmetric trace-free matrices outside this family, including an
    independent azimuthal diagonal mode. Never project them silently.
    """
    if len(H) != 3 or any(len(row) != 3 for row in H):
        raise ValueError("expected a 3x3 tensor")
    A, B, C, D = H[0][2], H[1][2], H[0][1], H[2][2]
    if H != cylinder_tensor(A, B, C, D):
        raise ValueError("tensor lies outside the frozen four-field subspace")
    return A, B, C, D


def rotate_tensor(H, R):
    """Conjugate by an explicitly provided (orthogonal) change of frame."""
    return tuple(tuple(sum((R[i][a] * H[a][b] * R[j][b]
                            for a in range(3) for b in range(3)), Q(0))
                       for j in range(3)) for i in range(3))


if __name__ == "__main__":
    for row in cylinder_tensor(Q(2, 7), Q(-3, 5), Q(7, 11), Q(-5, 13)):
        print(row)
