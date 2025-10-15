beam2te
^^^^^^^

:Purpose:

    Compute element stiffness matrix for a two dimensional Timoshenko beam element.

    .. figure:: images/BEAM2T.png
        :align: center
        :width: 70%
        :alt: Two dimensional beam element

        Two dimensional beam element

:Syntax:

    .. code-block:: matlab

        Ke = beam2te(ex, ey, ep)
        [Ke, fe] = beam2te(ex, ey, ep, eq)

:Description:

    :code:`beam2te` provides the global element stiffness matrix :math:`{\mathbf{K}}^e` for a
    two dimensional Timoshenko beam element.

    The input variables

    :code:`ex`:math:`= [x_1 \;\; x_2]`
    :math:`\qquad` 
    :code:`ey`:math:`= [y_1 \;\; y_2]`
    :math:`\qquad` 
    :code:`ep`:math:`=  [E \;\; G \;\; A \;\; I \;\; k_s]`

    supply the element nodal coordinates
    :math:`x_1`, :math:`y_1`, :math:`x_2`, and :math:`y_2`, the modulus of elasticity :math:`E`, the
    shear modulus :math:`G`, the cross section area :math:`A`, the moment of inertia :math:`I`
    and the shear correction factor :math:`k_s`.

    The element load vector :math:`{\mathbf{f}}_l^e` can also be computed if uniformly
    distributed loads are applied to the element.
    The optional input variable

    :code:`eq`:math:`= [q_{\bar{x}} \; q_{\bar{y}}]`

    contains the distributed loads per unit length, :math:`q_{\bar{x}}` and :math:`q_{\bar{y}}`.

    .. figure:: images/BEAM2LOA.png
        :align: center
        :width: 70%
        :alt: Uniformly distributed load

        Uniformly distributed load

:Theory:

    The element stiffness matrix :math:`\mathbf{K}^e`, stored in :code:`Ke`, is computed
    according to

    .. math::

        \mathbf{K}^e = \mathbf{G}^T \bar{\mathbf{K}}^e \mathbf{G}

    where :math:`\mathbf{G}` is described in :code:`beam2e`,
    and :math:`\bar{\mathbf{K}}^e` is given by

    .. math::

        \bar{\mathbf{K}}^e = \begin{bmatrix}
        \frac{D_{EA}}{L} & 0 & 0 & -\frac{D_{EA}}{L} & 0 & 0 \\
        0 & \frac{12D_{EI}}{L^3(1+\mu)} & \frac{6D_{EI}}{L^2(1+\mu)} & 0 & -\frac{12D_{EI}}{L^3(1+\mu)} & \frac{6D_{EI}}{L^2(1+\mu)} \\
        0 & \frac{6D_{EI}}{L^2(1+\mu)} & \frac{4D_{EI}(1+\frac{\mu}{4})}{L(1+\mu)} & 0 & -\frac{6D_{EI}}{L^2(1+\mu)} & \frac{2D_{EI}(1-\frac{\mu}{2})}{L(1+\mu)} \\
        -\frac{D_{EA}}{L} & 0 & 0 & \frac{D_{EA}}{L} & 0 & 0 \\
        0 & -\frac{12D_{EI}}{L^3(1+\mu)} & -\frac{6D_{EI}}{L^2(1+\mu)} & 0 & \frac{12D_{EI}}{L^3(1+\mu)} & -\frac{6D_{EI}}{L^2(1+\mu)} \\
        0 & \frac{6D_{EI}}{L^2(1+\mu)} & \frac{2D_{EI}(1-\frac{\mu}{2})}{L(1+\mu)} & 0 & -\frac{6D_{EI}}{L^2(1+\mu)} & \frac{4D_{EI}(1+\frac{\mu}{4})}{L(1+\mu)}
        \end{bmatrix}

    where the axial stiffness :math:`D_{EA}`, the bending stiffness :math:`D_{EI}`, and the length :math:`L` are given by

    .. math::

        D_{EA} = EA \qquad D_{EI} = EI \qquad L = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}

    and where

    .. math::

        \mu = \frac{12 D_{EI}}{L^2 G A k_s}

    The element loads :math:`\mathbf{f}^e_l` stored in
    the variable :code:`fe` are computed according to

    .. math::

        \mathbf{f}^e_l = \mathbf{G}^T \bar{\mathbf{f}}^e_l

    where

    .. math::

        \bar{\mathbf{f}}^e_l =
        \begin{bmatrix}
        \frac{q_{\bar{x}} L}{2} \\
        \frac{q_{\bar{y}} L}{2} \\
        \frac{q_{\bar{y}} L^2}{12} \\
        \frac{q_{\bar{x}} L}{2} \\
        \frac{q_{\bar{y}} L}{2} \\
        -\frac{q_{\bar{y}} L^2}{12}
        \end{bmatrix}