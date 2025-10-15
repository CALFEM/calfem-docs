beam2e
^^^^^^

.. index:: beam2e

:Purpose:

    Compute element stiffness matrix for a two-dimensional beam element.

    .. figure:: images/BEAM2E.png
        :align: center
        :width: 70%

:Syntax:

.. code-block:: matlab

    Ke = beam2e(ex, ey, ep)
    [Ke, fe] = beam2e(ex, ey, ep, eq)

:Description:

    :code:`beam2e` provides the global element stiffness matrix :math:`{\mathbf{K}}^e` for a two-dimensional beam element.

    The input variables:

    :code:`ex`:math:`= [x_1 \;\; x_2]`
    :math:`\qquad` 
    :code:`ey`:math:`= [y_1 \;\; y_2]`
    :math:`\qquad` 
    :code:`ep`:math:`=  [E \; A\; I]`

    supply the element nodal coordinates :math:`x_1`, :math:`y_1`, :math:`x_2`, and :math:`y_2`, the modulus of elasticity :math:`E`, the cross-section area :math:`A`, and the moment of inertia :math:`I`.

    The element load vector :math:`{\mathbf{f}}_l^e` can also be computed if a uniformly distributed transverse load is applied to the element. The optional input variable:

    :code:`eq`:math:`= [q_{\bar{x}} \; q_{\bar{y}}]`

    contains the distributed loads per unit length, :math:`q_{\bar{x}}` and :math:`q_{\bar{y}}`.

    .. figure:: images/BEAM2LOA.png
        :align: center
        :width: 70%
    
:Theory:

    The element stiffness matrix :math:`\mathbf{K}^e`, stored in :code:`Ke`, is computed according to:

    .. math::

        \mathbf{K}^e = \mathbf{G}^T \bar{\mathbf{K}}^e \mathbf{G}

    where:

    .. math::

        \bar{\mathbf{K}}^e =
        \begin{bmatrix}
        \frac{D_{EA}}{L} & 0 & 0 & -\frac{D_{EA}}{L} & 0 & 0 \\
        0 & \frac{12D_{EI}}{L^3} & \frac{6D_{EI}}{L^2} & 0 & -\frac{12D_{EI}}{L^3} & \frac{6D_{EI}}{L^2} \\
        0 & \frac{6D_{EI}}{L^2} & \frac{4D_{EI}}{L} & 0 & -\frac{6D_{EI}}{L^2} & \frac{2D_{EI}}{L} \\
        -\frac{D_{EA}}{L} & 0 & 0 & \frac{D_{EA}}{L} & 0 & 0 \\
        0 & -\frac{12D_{EI}}{L^3} & -\frac{6D_{EI}}{L^2} & 0 & \frac{12D_{EI}}{L^3} & -\frac{6D_{EI}}{L^2} \\
        0 & \frac{6D_{EI}}{L^2} & \frac{2D_{EI}}{L} & 0 & -\frac{6D_{EI}}{L^2} & \frac{4D_{EI}}{L}
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

    where the axial stiffness :math:`D_{EA}`, the bending stiffness :math:`D_{EI}`, and the length :math:`L` are given by:

    .. math::

        D_{EA} = EA, \quad D_{EI} = EI, \quad L = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}

    The transformation matrix :math:`\mathbf{G}` contains the direction cosines:

    .. math::

        n_{x\bar{x}} = n_{y\bar{y}} = \frac{x_2 - x_1}{L}, \quad
        n_{y\bar{x}} = -n_{x\bar{y}} = \frac{y_2 - y_1}{L}

    The element loads :math:`\mathbf{f}^e_l`, stored in the variable :code:`fe`, are computed according to:

    .. math::

        \mathbf{f}^e_l = \mathbf{G}^T \bar{\mathbf{f}}^e_l

    where:

    .. math::

        \bar{\mathbf{f}}^e_l =
        \begin{bmatrix}
        \frac{q_{\bar{x}}L}{2} \\
        \frac{q_{\bar{y}}L}{2} \\
        \frac{q_{\bar{y}}L^2}{12} \\
        \frac{q_{\bar{x}}L}{2} \\
        \frac{q_{\bar{y}}L}{2} \\
        -\frac{q_{\bar{y}}L^2}{12}
        \end{bmatrix}
