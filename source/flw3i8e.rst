flw3i8e
^^^^^^^

:Purpose:
    Compute element stiffness matrix for an 8 node isoparametric element.

    .. figure:: images/FLW3I8E.png
        :align: center
        :width: 70mm

:Syntax:
    .. code:: matlab

        Ke = flw3i8e(ex, ey, ez, ep, D)
        [Ke, fe] = flw3i8e(ex, ey, ez, ep, D, eq)

:Description:
    ``flw3i8e`` provides the element stiffness (conductivity) matrix ``Ke`` and
    the element load vector ``fe`` for an 8 node isoparametric heat flow element.

    The element nodal coordinates :math:`x_1`, :math:`y_1`, :math:`z_1`, :math:`x_2` etc,
    are supplied to the function by ``ex``, ``ey`` and ``ez``.
    The number of Gauss points :math:`n` (:math:`n \times n \times n` integration points, :math:`n=1,2,3`)
    are supplied to the function by ``ep`` and the thermal conductivities (or corresponding quantities)
    :math:`k_{xx}`, :math:`k_{xy}` etc are supplied by ``D``.

    .. math::

        \begin{array}{l}
        \mathbf{ex} = [\, x_1 \;\; x_2 \;\; x_3 \;\; \dots \;\; x_8 \,] \\
        \mathbf{ey} = [\, y_1 \;\; y_2 \;\; y_3 \;\; \dots \;\; y_8 \,] \\
        \mathbf{ez} = [\, z_1 \;\; z_2 \;\; z_3 \;\; \dots \;\; z_8 \,]
        \end{array}
        \qquad
        \mathbf{ep} = [\, n \,]
        \qquad
        \mathbf{D} =
        \begin{bmatrix}
            k_{xx} & k_{xy} & k_{xz} \\
            k_{yx} & k_{yy} & k_{yz} \\
            k_{zx} & k_{zy} & k_{zz}
        \end{bmatrix}

    If the scalar variable ``eq`` is given in the function, the element load
    vector :math:`\mathbf{fe}` is computed, using

    .. math::

        \mathbf{eq} = [\, Q \,]

    where :math:`Q` is the heat supply per unit volume.

:Theory:
    The element stiffness matrix :math:`\mathbf{K}^e` and the element load vector
    :math:`\mathbf{f}_l^e`, stored in ``Ke`` and ``fe``, respectively, are computed
    according to

    .. math::

        \mathbf{K}^e = \int_V \mathbf{B}^{eT} \mathbf{D} \mathbf{B}^e \, dV

        \mathbf{f}_l^e = \int_V \mathbf{N}^{eT} Q \, dV

    with the constitutive matrix :math:`\mathbf{D}` defined by ``D``.

    The evaluation of the integrals for the 3D isoparametric 8 node element
    is based on a temperature approximation :math:`T(\xi, \eta, \zeta)`, expressed in a
    local coordinate system in terms of the nodal variables :math:`T_1` to :math:`T_8` as

    .. math::

        T(\xi, \eta, \zeta) = \mathbf{N}^e \mathbf{a}^e

        \mathbf{N}^e = [\, N_1^e \;\; N_2^e \;\; N_3^e \;\; \dots \;\; N_8^e \,]
        \qquad
        \mathbf{a}^e = [\, T_1 \;\; T_2 \;\; T_3 \;\; \dots \;\; T_8 \,]^T

    The element shape functions are given by

    .. math::

        N_1^e = \frac{1}{8}(1-\xi)(1-\eta)(1-\zeta) \qquad
        N_2^e = \frac{1}{8}(1+\xi)(1-\eta)(1-\zeta) \\
        N_3^e = \frac{1}{8}(1+\xi)(1+\eta)(1-\zeta) \qquad
        N_4^e = \frac{1}{8}(1-\xi)(1+\eta)(1-\zeta) \\
        N_5^e = \frac{1}{8}(1-\xi)(1-\eta)(1+\zeta) \qquad
        N_6^e = \frac{1}{8}(1+\xi)(1-\eta)(1+\zeta) \\
        N_7^e = \frac{1}{8}(1+\xi)(1+\eta)(1+\zeta) \qquad
        N_8^e = \frac{1}{8}(1-\xi)(1+\eta)(1+\zeta)

    The :math:`\mathbf{B}^e`-matrix is given by

    .. math::

        \mathbf{B}^e = \nabla \mathbf{N}^e
        = \begin{bmatrix}
            \frac{\partial}{\partial x} \\
            \frac{\partial}{\partial y} \\
            \frac{\partial}{\partial z}
        \end{bmatrix} \mathbf{N}^e
        = (\mathbf{J}^T)^{-1}
        \begin{bmatrix}
            \frac{\partial}{\partial \xi} \\
            \frac{\partial}{\partial \eta} \\
            \frac{\partial}{\partial \zeta}
        \end{bmatrix} \mathbf{N}^e

    where :math:`\mathbf{J}` is the Jacobian matrix

    .. math::

        \mathbf{J} =
        \begin{bmatrix}
            \frac{\partial x}{\partial \xi} & \frac{\partial x}{\partial \eta} & \frac{\partial x}{\partial \zeta} \\
            \frac{\partial y}{\partial \xi} & \frac{\partial y}{\partial \eta} & \frac{\partial y}{\partial \zeta} \\
            \frac{\partial z}{\partial \xi} & \frac{\partial z}{\partial \eta} & \frac{\partial z}{\partial \zeta}
        \end{bmatrix}

    Evaluation of the integrals is done by Gauss integration.
