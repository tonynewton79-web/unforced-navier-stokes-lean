"""Exact tensor/dual pullback for an H8 source-frame stress.

The matrices are pointwise data. No derivative of the frame, source
provenance, or spatial symmetric-divergence inverse is certified here.
"""

from fractions import Fraction as Q


def _entries(M):
    """Convert a 3x3 rational matrix to an immutable exact array."""
    if len(M) != 3 or any(len(row) != 3 for row in M):
        raise ValueError("a 3x3 matrix is required")
    return tuple(tuple(Q(x) for x in row) for row in M)


def rotate_tensor(E, H):
    """Return the physical stress E H E^T at one point."""
    E, H = _entries(E), _entries(H)
    return tuple(tuple(sum((E[i][a]*H[a][b]*E[j][b]
                            for a in range(3) for b in range(3)), Q(0))
                       for j in range(3)) for i in range(3))


def pullback_gradient(E, G):
    """Return the source-frame gradient E^T G E at one point."""
    E, G = _entries(E), _entries(G)
    return tuple(tuple(sum((E[i][a]*G[i][j]*E[j][b]
                            for i in range(3) for j in range(3)), Q(0))
                       for b in range(3)) for a in range(3))


def dual_covector(E, G):
    """Coefficients of A,B,C,D in (E H E^T):G, including signs."""
    M = pullback_gradient(E, G)
    return (M[0][2]+M[2][0], M[1][2]+M[2][1],
            M[0][1]+M[1][0], M[2][2]-M[0][0])


def frobenius(H, G):
    """Exact entrywise Frobenius pairing, including nonsymmetric G."""
    H, G = _entries(H), _entries(G)
    return sum((H[i][j]*G[i][j]
                for i in range(3) for j in range(3)), Q(0))
