.. _flw2te:
.. index:: 
   single: flw2te
   single: triangular element
   single: heat flow
   single: thermal element
   single: 2D flow
   pair: finite element; thermal
   pair: triangular; element
   pair: heat; flow
   pair: thermal; analysis
   pair: 2D; flow

flw2te
^^^^^^

:Purpose:
    Compute element stiffness matrix for a triangular heat flow element.

    .. figure:: images/FLW2TE.png
        :width: 70%
        :align: center
        :alt: Two dimensional heat flow elements    

:Syntax:
    .. code-block:: matlab

        Ke = flw2te(ex, ey, ep, D)
        [Ke, fe] = flw2te(ex, ey, ep, D, eq)

:Description:
    ``flw2te`` provides the element stiffness (conductivity) matrix ``Ke`` and
    the element load vector ``fe`` for a triangular heat flow element.

    The element nodal coordinates :math:`x_1`, :math:`y_1`, :math:`x_2` etc,
    are supplied to the function by ``ex`` and ``ey``, the element thickness :math:`t`
    is supplied by ``ep`` and the thermal conductivities (or corresponding quantities)
    :math:`k_{xx}`, :math:`k_{xy}` etc are supplied by ``D``.

    .. math::

        \begin{array}{l}
        \mathbf{ex} = [\, x_1 \;\; x_2 \;\; x_3\,] \\
        \mathbf{ey} = [\, y_1 \;\; y_2 \;\; y_3\,]
        \end{array}
        \qquad
        \mathbf{ep} = [\, t \,]
        \qquad
        \mathbf{D} = \begin{bmatrix}
            k_{xx} & k_{xy} \\
            k_{yx} & k_{yy}
        \end{bmatrix}

    If the scalar variable ``eq`` is given in the function, the
    element load vector :math:`\mathbf{fe}`
    is computed, using

    .. math::

        \mathbf{eq} = [\, Q \,]

    where :math:`Q` is the heat supply per unit volume.

:Theory:
    The element stiffness matrix :math:`\mathbf{K}^e` and the
    element load vector :math:`\mathbf{f}_l^e`, stored in ``Ke`` and ``fe``,
    respectively, are computed according to

    .. math::

        \mathbf{K}^e = (\mathbf{C}^{-1})^T \int_A \bar{\mathbf{B}}^T
        \mathbf{D} \bar{\mathbf{B}}\, t\, dA\, \mathbf{C}^{-1}

    .. math::

        \mathbf{f}_l^e = (\mathbf{C}^{-1})^T \int_A \bar{\mathbf{N}}^T Q\, t\, dA

    with the constitutive matrix :math:`\mathbf{D}` defined by ``D``.

    The evaluation of the integrals for the triangular element is based on the linear
    temperature approximation :math:`T(x, y)` and is expressed
    in terms of the nodal variables :math:`T_1`, :math:`T_2` and :math:`T_3` as

    .. math::

        T(x, y) = \mathbf{N}^e \mathbf{a}^e = \bar{\mathbf{N}}\, \mathbf{C}^{-1} \mathbf{a}^e

    where

    .. math::

        \bar{\mathbf{N}} = [\, 1 \;\; x \;\; y\,]
        \qquad
        \mathbf{C} = \begin{bmatrix}
            1 & x_1 & y_1 \\
            1 & x_2 & y_2 \\
            1 & x_3 & y_3
        \end{bmatrix}
        \qquad
        \mathbf{a}^e = \begin{bmatrix}
            T_1 \\
            T_2 \\
            T_3
        \end{bmatrix}

    and hence it follows that

    .. math::

        \bar{\mathbf{B}} = \nabla \bar{\mathbf{N}} = \begin{bmatrix}
            0 & 1 & 0 \\
            0 & 0 & 1
        \end{bmatrix}
        \qquad
        \nabla = \begin{bmatrix}
            \dfrac{\partial}{\partial x} \\
            \dfrac{\partial}{\partial y}
        \end{bmatrix}

    Evaluation of the integrals for the triangular element yields

    .. math::

        \mathbf{K}^e = (\mathbf{C}^{-1})^T \bar{\mathbf{B}}^T
        \mathbf{D} \bar{\mathbf{B}}
        \mathbf{C}^{-1} t A

    .. math::

        \mathbf{f}_l^e = \frac{Q A t}{3} \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}

    where the element area :math:`A` is determined as

    .. math::

        A = \frac{1}{2} \det \mathbf{C}