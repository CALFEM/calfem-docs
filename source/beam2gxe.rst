
beam2gxe - Two dimensional geometric nonlinear exact beam element
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Purpose**

Compute element stiffness matrix for a two dimensional nonlinear beam element with exact solution.

.. figure:: images/BEAM2G.png
    :align: center
    :width: 70%

**Syntax**

.. code-block:: matlab

    Ke = beam2gxe(ex, ey, ep, Qx)
    [Ke, fe] = beam2gxe(ex, ey, ep, Qx, eq)

**Description**

``beam2gxe`` provides the global element stiffness matrix ``Ke`` for a two dimensional beam element with respect to geometrical nonlinearity considering exact solution.

The input variables:

- ``ex = [x1 x2]``
- ``ey = [y1 y2]``
- ``ep = [E A I]``

supply the element nodal coordinates :math:`x_1`, :math:`y_1`, :math:`x_2`, and :math:`y_2`, the modulus of elasticity :math:`E`, the cross section area :math:`A`, and the moment of inertia :math:`I`.

- ``Qx = [Q_xbar]``

contains the value of the predefined axial force :math:`Q_{\bar{x}}`, which is positive in tension.

The element load vector ``fe`` can also be computed if a uniformly distributed transverse load is applied to the element. The optional input variable

- ``eq = [q_ybar]``

then contains the distributed transverse load per unit length, :math:`q_{\bar{y}}`. Note that ``eq`` is a scalar and not a vector as in ``beam2e``.

**Theory**

The element stiffness matrix :math:`\mathbf{K}^e`, stored in the variable ``Ke``, is computed according to

.. math::

    \mathbf{K}^e = \mathbf{G}^T \bar{\mathbf{K}}^e \mathbf{G}

with

.. math::

    \bar{\mathbf{K}}^e = \begin{bmatrix}
    \frac{D_{EA}}{L} & 0 & 0 & -\frac{D_{EA}}{L} & 0 & 0 \\
    0 & \frac{12 D_{EI}}{L^3} \phi_5 & \frac{6 D_{EI}}{L^2} \phi_2 & 0 & -\frac{12 D_{EI}}{L^3} \phi_5 & \frac{6 D_{EI}}{L^2} \phi_2 \\
    0 & \frac{6 D_{EI}}{L^2} \phi_2 & \frac{4 D_{EI}}{L} \phi_3 & 0 & -\frac{6 D_{EI}}{L^2} \phi_2 & \frac{2 D_{EI}}{L} \phi_4 \\
    -\frac{D_{EA}}{L} & 0 & 0 & \frac{D_{EA}}{L} & 0 & 0 \\
    0 & -\frac{12 D_{EI}}{L^3} \phi_5 & -\frac{6 D_{EI}}{L^2} \phi_2 & 0 & \frac{12 D_{EI}}{L^3} \phi_5 & -\frac{6 D_{EI}}{L^2} \phi_2 \\
    0 & \frac{6 D_{EI}}{L^2} \phi_2 & \frac{2 D_{EI}}{L} \phi_4 & 0 & -\frac{6 D_{EI}}{L^2} \phi_2 & \frac{4 D_{EI}}{L} \phi_3
    \end{bmatrix}

.. math::

    \mathbf{G} = \begin{bmatrix}
    n_{x\bar{x}} & n_{y\bar{x}} & 0 & 0 & 0 & 0 \\
    n_{x\bar{y}} & n_{y\bar{y}} & 0 & 0 & 0 & 0 \\
    0 & 0 & 1 & 0 & 0 & 0 \\
    0 & 0 & 0 & n_{x\bar{x}} & n_{y\bar{x}} & 0 \\
    0 & 0 & 0 & n_{x\bar{y}} & n_{y\bar{y}} & 0 \\
    0 & 0 & 0 & 0 & 0 & 1
    \end{bmatrix}

where the axial stiffness :math:`D_{EA}`, the bending stiffness :math:`D_{EI}` and the length :math:`L` are given by

.. math::

    D_{EA} = EA; \quad D_{EI} = EI; \quad L = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}

The transformation matrix :math:`\mathbf{G}` contains the direction cosines

.. math::

    n_{x\bar{x}} = n_{y\bar{y}} = \frac{x_2 - x_1}{L} \qquad
    n_{y\bar{x}} = -n_{x\bar{y}} = \frac{y_2 - y_1}{L}

For axial compression (:math:`Q_{\bar{x}} < 0`):

.. math::

    \phi_2 = \frac{1}{12} \frac{k^2 L^2}{1 - \phi_1} \qquad
    \phi_3 = \frac{1}{4} \phi_1 + \frac{3}{4} \phi_2

.. math::

    \phi_4 = -\frac{1}{2} \phi_1 + \frac{3}{2} \phi_2 \qquad
    \phi_5 = \phi_1 \phi_2

with

.. math::

    k = \sqrt{\frac{-Q_{\bar{x}}}{D_{EI}}} \qquad \phi_1 = \frac{kL}{2} \cot \frac{kL}{2}

For axial tension (:math:`Q_{\bar{x}} > 0`):

.. math::

    \phi_2 = -\frac{1}{12} \frac{k^2 L^2}{1 - \phi_1} \qquad
    \phi_3 = \frac{1}{4} \phi_1 + \frac{3}{4} \phi_2

.. math::

    \phi_4 = -\frac{1}{2} \phi_1 + \frac{3}{2} \phi_2 \qquad
    \phi_5 = \phi_1 \phi_2

with

.. math::

    k = \sqrt{\frac{Q_{\bar{x}}}{D_{EI}}} \qquad \phi_1 = \frac{kL}{2} \coth \frac{kL}{2}

Element Loads
^^^^^^^^^^^^^

The element loads :math:`\mathbf{f}^e_l` stored in the variable ``fe`` are computed according to

.. math::

    \mathbf{f}^e_l = \mathbf{G}^T \bar{\mathbf{f}}^e_l

where

.. math::

    \bar{\mathbf{f}}^e_l = qL \begin{bmatrix} 0 \\ \frac{1}{2} \\ \frac{L}{12} \psi \\ 0 \\ \frac{1}{2} \\ -\frac{L}{12} \psi \end{bmatrix}

For an axial compressive force (:math:`Q_{\bar{x}} < 0`):

.. math::

    \psi = 6 \left( \frac{2}{(kL)^2} - \frac{1 + \cos kL}{kL \sin kL} \right)

and for an axial tensile force (:math:`Q_{\bar{x}} > 0`):

.. math::

    \psi = -6 \left( \frac{2}{(kL)^2} - \frac{1 + \cosh kL}{kL \sinh kL} \right)
