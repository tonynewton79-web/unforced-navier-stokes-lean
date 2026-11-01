"""Regression checks for the exact periodic H8 translation projection.

These test finite-dimensional algebra and an explicit regular shear, not
the still-open authentic singular H8 closure or a Lean PDE theorem.
"""
import sympy as sp


def test_rank_one_projection():
    a, b = sp.symbols("a b", real=True)
    W = sp.Matrix([a, b])
    N = W.dot(W)
    P = W * W.T / N
    assert sp.simplify(P * P - P) == sp.zeros(2)
    assert sp.simplify(P.T - P) == sp.zeros(2)


def test_projection_derivative_on_mode():
    a, b, da, db = sp.symbols("a b da db", real=True)
    W = sp.Matrix([a, b])
    dW = sp.Matrix([da, db])
    N = W.dot(W)
    P = W * W.T / N
    dP = (dW * W.T + W * dW.T) / N - 2 * W.dot(dW) * P / N
    assert sp.simplify(dP * W - (sp.eye(2) - P) * dW) == sp.zeros(2, 1)


def test_exact_shear_translation_defect():
    t, z = sp.symbols("t z", real=True)
    U = sp.exp(-t) * sp.sin(z - t**2)
    W = sp.diff(U, z)
    G = sp.simplify(sp.diff(U, t) - sp.diff(U, z, 2))
    assert sp.simplify(G + 2*t*W) == 0
    assert sp.simplify(sp.diff(W, t) - sp.diff(W, z, 2) - sp.diff(G, z)) == 0


def test_shear_offdiagonal_mode_coupling():
    theta, dtheta = sp.symbols("theta dtheta", real=True)
    a = sp.sin(theta)
    residual_channel = dtheta
    off_diagonal = dtheta * (sp.cos(theta) - 1)
    assert sp.simplify(sp.diff(a, theta)*dtheta - residual_channel - off_diagonal) == 0


def test_adjoint_normalization_requires_defect():
    x, y, a, b, c, d = sp.symbols("x y a b c d", real=True)
    W = sp.Matrix([x, y])
    L = sp.Matrix([[a, b], [c, d]])
    ell = W/(W.dot(W))
    defect = sp.Matrix([1, 2])
    Wdot = L*W + defect
    elldot = -L.T*ell - ell.dot(defect)*ell
    assert sp.simplify(elldot.dot(W)+ell.dot(Wdot)) == 0
