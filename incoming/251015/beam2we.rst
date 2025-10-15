beam2we
^^^^^^^

.. index:: beam2we

:Purpose:

    Compute element stiffness matrix for a two dimensional beam element on elastic support.

    .. figure:: images/beam2w.png
        :align: center
        :width: 70%

:Syntax:

.. only:: matlab

    .. code-block:: matlab

        Ke = beam2we(ex, ey, ep)
        [Ke, fe] = beam2we(ex, ey, ep, eq)

.. only:: python

    .. code-block:: python

        Ke = cfc.beam2we(ex, ey, ep)
        Ke, fe = cfc.beam2we(ex, ey, ep, eq)

:Description:

    :code:`beam2we` provides the global element stiffness matrix :math:`{\mathbf{K}}^e` for a two dimensional beam element with elastic support.

    The input variables

    :code:`ex`:math:`= [x_1 \;\; x_2]`
    :math:`\qquad` 
    :code:`ey`:math:`= [y_1 \;\; y_2]`
    :math:`\qquad` 
    :code:`ep`:math:`=  [E\;\; A\;\; I\;\; k_{\bar{x}}\;\; k_{\bar{y}}]`

    supply the element nodal coordinates :math:`x_1`, :math:`x_2`, :math:`y_1`, and :math:`y_2`, the modulus of elasticity :math:`E`, the cross section area :math:`A`, the moment of inertia :math:`I`, the spring stiffness in the axial direction :math:`k_{\bar{x}}`, and the spring stiffness in the transverse direction :math:`k_{\bar{y}}`.

    The element load vector :math:`{\mathbf{f}}_l^e` can also be computed if uniformly distributed loads are applied to the element. The optional input variable

    .. math::

        \text{eq} = [q_{\bar{x}}\;\; q_{\bar{y}}]

    contains the distributed load per unit length, :math:`q_{\bar{x}}` and :math:`q_{\bar{y}}`.

:Theory:

    The element stiffness matrix :math:`\mathbf{K}^e`, stored in :code:`Ke`, is computed according to

    .. math::

        \mathbf{K}^e = \mathbf{G}^T \bar{\mathbf{K}}^e \mathbf{G}

    where

    .. math::

        \bar{\mathbf{K}}^e = \bar{\mathbf{K}}^e_0 + \bar{\mathbf{K}}^e_s

    .. math::

        \bar{\mathbf{K}}^e_0 =
        \begin{bmatrix}
        \frac{D_{EA}}{L} & 0 & 0 & -\frac{D_{EA}}{L} & 0 & 0 \\
        0 & \frac{12 D_{EI}}{L^3} & \frac{6 D_{EI}}{L^2} & 0 & -\frac{12 D_{EI}}{L^3} & \frac{6 D_{EI}}{L^2} \\
        0 & \frac{6 D_{EI}}{L^2} & \frac{4 D_{EI}}{L} & 0 & -\frac{6 D_{EI}}{L^2} & \frac{2 D_{EI}}{L} \\
        -\frac{D_{EA}}{L} & 0 & 0 & \frac{D_{EA}}{L} & 0 & 0 \\
        0 & -\frac{12 D_{EI}}{L^3} & -\frac{6 D_{EI}}{L^2} & 0 & \frac{12 D_{EI}}{L^3} & -\frac{6 D_{EI}}{L^2} \\
        0 & \frac{6 D_{EI}}{L^2} & \frac{2 D_{EI}}{L} & 0 & -\frac{6 D_{EI}}{L^2} & \frac{4 D_{EI}}{L}
        \end{bmatrix}

    .. math::

        \bar{\mathbf{K}}^e_s = \frac{L}{420}
        \begin{bmatrix}
        140k_{\bar{x}} & 0 & 0 & 70k_{\bar{x}} & 0 & 0 \\
        0 & 156k_{\bar{y}} & 22k_{\bar{y}}L & 0 & 54k_{\bar{y}} & -13k_{\bar{y}}L \\
        0 & 22k_{\bar{y}}L & 4k_{\bar{y}}L^2 & 0 & 13k_{\bar{y}}L & -3k_{\bar{y}}L^2 \\
        70k_{\bar{x}} & 0 & 0 & 140k_{\bar{x}} & 0 & 0 \\
        0 & 54k_{\bar{y}} & 13k_{\bar{y}}L & 0 & 156k_{\bar{y}} & -22k_{\bar{y}}L \\
        0 & -13k_{\bar{y}}L & -3k_{\bar{y}}L^2 & 0 & -22k_{\bar{y}}L & 4k_{\bar{y}}L^2
        \end{bmatrix}

    .. math::

        \mathbf{G} =
        \begin{bmatrix}
        n_{x\bar{x}} & n_{y\bar{x}} & 0 & 0 & 0 & 0 \\
        n_{x\bar{y}} & n_{y\bar{y}} & 0 & 0 & 0 & 0 \\
        0 & 0 & 1 & 0 & 0 & 0 \\
        0 & 0 & 0 & n_{x\bar{x}} & n_{y\bar{x}} & 0 \\
        0 & 0 & 0 & n_{x\bar{y}} & n_{y\bar{y}} & 0 \\
        0 & 0 & 0 & 0 & 0 & 1
        \end{bmatrix}

    where the axial stiffness :math:`D_{EA}`, the bending stiffness :math:`D_{EI}` and the length :math:`L` are given by

    .. math::

        D_{EA} = EA;\quad D_{EI} = EI;\quad L = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}

    The transformation matrix :math:`\mathbf{G}` contains the direction cosines

    .. math::

        n_{x\bar{x}} = n_{y\bar{y}} = \frac{x_2 - x_1}{L} \qquad
        n_{y\bar{x}} = -n_{x\bar{y}} = \frac{y_2 - y_1}{L}

    The element loads :math:`\mathbf{f}^e_l` stored in the variable :code:`fe` are computed according to

    .. math::

        \mathbf{f}^e_l = \mathbf{G}^T \bar{\mathbf{f}}^e_l

    where

    .. math::

        \bar{\mathbf{f}}^e_l =
        \begin{bmatrix}
        \dfrac{q_{\bar{x}}L}{2} \\
        \dfrac{q_{\bar{y}}L}{2} \\
        \dfrac{q_{\bar{y}}L^2}{12} \\
        \dfrac{q_{\bar{x}}L}{2} \\
        \dfrac{q_{\bar{y}}L}{2} \\
        -\dfrac{q_{\bar{y}}L^2}{12}
        \end{bmatrix}
