beam1e - One dimensional beam element
-------------------------------------

Purpose
^^^^^^^

Compute element stiffness matrix for a one dimensional beam element.

.. figure:: images/beam1e.png
    :align: center

Syntax
^^^^^^

.. code-block:: matlab

    Ke = beam1e(ex, ep)
    [Ke, fe] = beam1e(ex, ep, eq)

Description
^^^^^^^^^^^

``beam1e`` provides the global element stiffness matrix ``Ke`` for a one dimensional beam element.

The input variables

  ``ex = [x1 x2]``

  ``ep = [E I]``

supply the element nodal coordinates :math:`x_1` and :math:`x_2`, the modulus of elasticity :math:`E` and the moment of inertia :math:`I`.

The element load vector ``fe`` can also be computed if a uniformly distributed load is applied to the element.
The optional input variable

  ``eq = [q_ybar]``

then contains the distributed load per unit length, :math:`q_{\bar{y}}`.

.. figure:: images/beam1e_2.png
    :align: center

Theory
^^^^^^

The element stiffness matrix :math:`\bar{\mathbf{K}}^e`, stored in ``Ke``, is computed according to

.. math::

    \bar{\mathbf{K}}^e = \frac{D_{EI}}{L^3}
    \begin{bmatrix}
    12 & 6L & -12 & 6L \\
    6L & 4L^2 & -6L & 2L^2 \\
    -12 & -6L & 12 & -6L \\
    6L & 2L^2 & -6L & 4L^2
    \end{bmatrix}

where the bending stiffness :math:`D_{EI}` and the length :math:`L` are given by

.. math::

    D_{EI} = EI; \quad L = x_2 - x_1

The element loads :math:`\bar{\mathbf{f}}_l^e` stored in the variable ``fe`` are computed according to

.. math::

    \bar{\mathbf{f}}_l^e = q_{\bar{y}}
    \begin{bmatrix}
    \dfrac{L}{2} \\
    \dfrac{L^2}{12} \\
    \dfrac{L}{2} \\
    -\dfrac{L^2}{12}
    \end{bmatrix}
