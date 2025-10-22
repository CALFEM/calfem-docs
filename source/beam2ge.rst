.. _beam2ge:
.. index:: 
   single: beam2ge
   single: geometric nonlinear
   single: beam element
   single: 2D beam
   single: nonlinear analysis
   single: large deformation
   pair: finite element; nonlinear
   pair: geometric; nonlinearity
   pair: beam; nonlinear
   pair: 2D; nonlinear
   pair: large; deformation

beam2ge
^^^^^^^

:Purpose:

    Compute element stiffness matrix for a two dimensional nonlinear beam element with respect to geometrical nonlinearity.

    .. only:: html

        .. figure:: images/beam2g.svg
            :align: center
            :width: 400px

    .. only:: latex

        .. figure:: images/beam2g.svg
            :align: center
            :width: 70%
            :alt: Two dimensional geometric nonlinear beam element

:Syntax:

.. only:: matlab

    .. code-block:: matlab

        Ke = beam2ge(ex, ey, ep, Qx)
        [Ke, fe] = beam2ge(ex, ey, ep, Qx, eq)

.. only:: python

    .. code-block:: python

        Ke = cfc.beam2ge(ex, ey, ep, Qx)
        Ke, fe = cfc.beam2ge(ex, ey, ep, Qx, eq)

:Description:

    :code:`beam2ge` provides the global element stiffness matrix :math:`{\mathbf{K}}^e` for a two dimensional beam element with respect to geometrical nonlinearity.

    The input variables:

    :code:`ex`:math:`= [x_1 \;\; x_2]`
    :math:`\qquad` 
    :code:`ey`:math:`= [y_1 \;\; y_2]`
    :math:`\qquad` 
    :code:`ep`:math:`=  [E \; A\; I]`

    supply the element nodal coordinates :math:`x_1`, :math:`y_1`, :math:`x_2`, and :math:`y_2`, the modulus of elasticity :math:`E`, the cross-section area :math:`A`, and the moment of inertia :math:`I`.

    The input variable

    :code:`Qx`:math:`= [Q_{\bar{x}}]`

    contains the value of the predefined axial force :math:`Q_{\bar{x}}`, which is positive in tension.

    The element load vector :math:`{\mathbf{f}}_l^e` can also be computed if a uniformly distributed transverse load is applied to the element. The optional input 
        
    :code:`eq`:math:`= [q_{\bar{y}}]`

    contains the distributed transverse load per unit length, :math:`q_{\bar{y}}`. Note that :code:`eq` is a scalar and not a vector as in :code:`beam2e`.

:Theory:

    The element stiffness matrix :math:`\mathbf{K}^e`, stored in the variable :code:`Ke`, is computed according to

    .. math::

        \mathbf{K}^e = \mathbf{G}^T \bar{\mathbf{K}}^e \mathbf{G}

    where :math:`\bar{\mathbf{K}}^e` is given by

    .. math::

        \bar{\mathbf{K}}^e = \bar{\mathbf{K}}^e_0 + \bar{\mathbf{K}}^e_{\sigma}

    with

    .. math::

        \bar{\mathbf{K}}^e_0 = \begin{bmatrix}
        \frac{D_{EA}}{L} & 0 & 0 & -\frac{D_{EA}}{L} & 0 & 0 \\
        0 & \frac{12 D_{EI}}{L^3} & \frac{6 D_{EI}}{L^2} & 0 & -\frac{12 D_{EI}}{L^3} & \frac{6 D_{EI}}{L^2} \\
        0 & \frac{6 D_{EI}}{L^2} & \frac{4 D_{EI}}{L} & 0 & -\frac{6 D_{EI}}{L^2} & \frac{2 D_{EI}}{L} \\
        -\frac{D_{EA}}{L} & 0 & 0 & \frac{D_{EA}}{L} & 0 & 0 \\
        0 & -\frac{12 D_{EI}}{L^3} & -\frac{6 D_{EI}}{L^2} & 0 & \frac{12 D_{EI}}{L^3} & -\frac{6 D_{EI}}{L^2} \\
        0 & \frac{6 D_{EI}}{L^2} & \frac{2 D_{EI}}{L} & 0 & -\frac{6 D_{EI}}{L^2} & \frac{4 D_{EI}}{L}
        \end{bmatrix}

    .. math::

        \bar{\mathbf{K}}^e_{\sigma} = Q_{\bar{x}} \begin{bmatrix}
        0 & 0 & 0 & 0 & 0 & 0 \\
        0 & \frac{6}{5L} & \frac{1}{10} & 0 & -\frac{6}{5L} & \frac{1}{10} \\
        0 & \frac{1}{10} & \frac{2L}{15} & 0 & -\frac{1}{10} & -\frac{L}{30} \\
        0 & 0 & 0 & 0 & 0 & 0 \\
        0 & -\frac{6}{5L} & -\frac{1}{10} & 0 & \frac{6}{5L} & -\frac{1}{10} \\
        0 & \frac{1}{10} & -\frac{L}{30} & 0 & -\frac{1}{10} & \frac{2L}{15}
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

        D_{EA} = EA;\quad D_{EI} = EI;\quad L = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}

    The transformation matrix :math:`\mathbf{G}` contains the direction cosines

    .. math::

        n_{x\bar{x}} = n_{y\bar{y}} = \frac{x_2 - x_1}{L} \qquad
        n_{y\bar{x}} = -n_{x\bar{y}} = \frac{y_2 - y_1}{L}

    The element loads :math:`\mathbf{f}^e_l` stored in :code:`fe` are computed according to

    .. math::

        \mathbf{f}^e_l = \mathbf{G}^T \bar{\mathbf{f}}^e_l

    where

    .. math::

        \bar{\mathbf{f}}^e_l = q_{\bar{y}} \begin{bmatrix} 0 \\ \frac{L}{2} \\ \frac{L^2}{12} \\ 0 \\ \frac{L}{2} \\ -\frac{L^2}{12} \end{bmatrix}
