.. _flw2i4e:
.. index:: 
   single: flw2i4e
   single: flow element
   single: heat flow
   single: thermal element
   single: 4 node element
   single: isoparametric element
   pair: finite element; thermal
   pair: heat; flow
   pair: thermal; analysis
   pair: 2D; flow
   pair: isoparametric; element

flw2i4e
^^^^^^^

:Purpose:
    Compute element stiffness matrix for a 4 node isoparametric heat flow element.

    .. only:: html
        
        .. figure:: images/flw2i4e.svg
            :align: center
            :width: 400px
    
    .. only:: latex
        
        .. figure:: images/flw2i4e.svg
            :align: center
            :width: 70%

:Syntax:

    .. code:: matlab

        Ke = flw2i4e(ex, ey, ep, D)
        [Ke, fe] = flw2i4e(ex, ey, ep, D, eq)

:Description:
    ``flw2i4e`` provides the element stiffness (conductivity) matrix ``Ke`` and
    the element load vector ``fe`` for a 4 node isoparametric heat flow element.

    The element nodal coordinates :math:`x_1`, :math:`y_1`, :math:`x_2` etc,
    are supplied to the function by ``ex`` and ``ey``. The element thickness
    :math:`t` and the number of Gauss points :math:`n`
    (:math:`n \times n` integration points, :math:`n=1,2,3`)
    are supplied to the function by ``ep`` and the thermal conductivities (or corresponding quantities)
    :math:`k_{xx}`, :math:`k_{xy}` etc are supplied by ``D``.

    .. math::

        \begin{array}{l}
        \mathbf{ex} = [\, x_1 \;\; x_2 \;\; x_3 \;\; x_4 \,] \\
        \mathbf{ey} = [\, y_1 \;\; y_2 \;\; y_3 \;\; y_4 \,]
        \end{array}
        \qquad
        \mathbf{ep} = [\, t \;\; n \,]
        \qquad
        \mathbf{D} = \begin{bmatrix}
            k_{xx} & k_{xy} \\
            k_{yx} & k_{yy}
        \end{bmatrix}

    If the scalar variable ``eq`` is given in the function, the element load
    vector :math:`fe` is computed, using

    .. math::

        \mathbf{eq} = [\, Q \,]

    where :math:`Q` is the heat supply per unit volume.

:Theory:
    The element stiffness matrix :math:`\mathbf{K}^e` and the element load vector
    :math:`\mathbf{f}_l^e`, stored in ``Ke`` and ``fe``, respectively, are computed
    according to

    .. math::

        \mathbf{K}^e = \int_A \mathbf{B}^{eT} \mathbf{D} \mathbf{B}^e t\, dA

    .. math::

        \mathbf{f}_l^e = \int_A \mathbf{N}^{eT} Q t\, dA

    with the constitutive matrix :math:`\mathbf{D}` defined by ``D``.

    The evaluation of the integrals for the isoparametric 4 node element
    is based on a temperature approximation :math:`T(\xi, \eta)`, expressed in a
    local coordinate system in terms of the nodal
    variables :math:`T_1`, :math:`T_2`, :math:`T_3` and :math:`T_4` as

    .. math::

        T(\xi, \eta) = \mathbf{N}^e \mathbf{a}^e

    where

    .. math::

        \mathbf{N}^e = [\, N_1^e \;\; N_2^e \;\; N_3^e \;\; N_4^e \,]
        \qquad
        \mathbf{a}^e = [\, T_1 \;\; T_2 \;\; T_3 \;\; T_4 \,]^T

    The element shape functions are given by

    .. math::

        N_1^e = \frac{1}{4}(1-\xi)(1-\eta) \qquad N_2^e = \frac{1}{4}(1+\xi)(1-\eta) \\
        N_3^e = \frac{1}{4}(1+\xi)(1+\eta) \qquad N_4^e = \frac{1}{4}(1-\xi)(1+\eta)

    The :math:`\mathbf{B}^e`-matrix is given by

    .. math::

        \mathbf{B}^e = \nabla \mathbf{N}^e
        = \begin{bmatrix}
            \frac{\partial}{\partial x} \\
            \frac{\partial}{\partial y}
        \end{bmatrix} \mathbf{N}^e
        = (\mathbf{J}^T)^{-1}
        \begin{bmatrix}
            \frac{\partial}{\partial \xi} \\
            \frac{\partial}{\partial \eta}
        \end{bmatrix} \mathbf{N}^e

    where :math:`\mathbf{J}` is the Jacobian matrix

    .. math::

        \mathbf{J} =
        \begin{bmatrix}
            \frac{\partial x}{\partial \xi} & \frac{\partial x}{\partial \eta} \\
            \frac{\partial y}{\partial \xi} & \frac{\partial y}{\partial \eta}
        \end{bmatrix}

    Evaluation of the integrals is done by Gauss integration.
