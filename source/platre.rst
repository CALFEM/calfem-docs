platre
^^^^^^

:Purpose:
    Compute element stiffness matrix for a rectangular plate element.

    .. only:: html
        
        .. figure:: images/PLATRE.svg
            :align: center
            :width: 400px
    
    .. only:: latex
        
        .. figure:: images/PLATRE.svg
            :align: center
            :width: 70%

:Syntax:
    .. code:: matlab

        Ke = platre(ex, ey, ep, D)
        [Ke, fe] = platre(ex, ey, ep, D, eq)

:Description:
    ``platre`` provides an element stiffness matrix :math:`Ke`, and an element load
    vector :math:`fe`, for a rectangular plate element. This element can only be used if the element edges are parallel
    to the coordinate axes.

    The element nodal coordinates :math:`x_1, y_1, x_2` etc. are supplied to the function
    by :math:`\mathbf{ex}` and :math:`\mathbf{ey}`, the element thickness :math:`t` 
    by :math:`\mathbf{ep}`, and the material properties by the
    constitutive matrix :math:`D`. Any arbitrary :math:`\mathbf{D}`-matrix with
    dimensions :math:`(3 \times 3)` and valid for plane stress may be given.
    For an isotropic elastic material the constitutive matrix can be formed
    by the function ``hooke`` (see Section :ref:`material_functions`).

    .. math::

        \begin{array}{l}
        \mathbf{ex} = [\, x_1 \;\; x_2 \;\; x_3 \;\; x_4 \,] \\
        \mathbf{ey} = [\, y_1 \;\; y_2 \;\; y_3 \;\; y_4 \,]
        \end{array}
        \qquad
        \mathbf{ep} = [\, t \,]
        \qquad
        \mathbf{D} = \begin{bmatrix}
            D_{11} & D_{12} & D_{13} \\
            D_{21} & D_{22} & D_{23} \\
            D_{31} & D_{32} & D_{33}
        \end{bmatrix}

    If a uniformly distributed load is applied to the element,
    the element load vector :math:`fe` is computed. The input variable

    .. math::

        \mathbf{eq} = [\, q_z \,]

    then contains the load :math:`q_z` per unit area in the :math:`z`-direction.

:Theory:
    The element stiffness matrix :math:`\mathbf{K}^e` and the 
    element load vector :math:`\mathbf{f}_l^e`, stored in :math:`Ke` and :math:`fe`
    respectively, are computed according to

    .. math::

        \mathbf{K}^e = (\mathbf{C}^{-1})^T \int_A \bar{\mathbf{B}}^T
        \tilde{\mathbf{D}} \, \bar{\mathbf{B}} \, dA \, \mathbf{C}^{-1}

    .. math::

        \mathbf{f}_l^e = (\mathbf{C}^{-1})^T \int_A \bar{\mathbf{N}}^T q_z \, dA

    where the constitutive matrix

    .. math::

        \tilde{\mathbf{D}} = \frac{t^3}{12} \mathbf{D}

    and where :math:`\mathbf{D}` is defined by :math:`D`.

    The evaluation of the integrals for the rectangular plate element is based
    on the displacement approximation :math:`w(x, y)` and is expressed 
    in terms of the nodal variables :math:`u_1, u_2, \ldots, u_{12}` as

    .. math::

        w(x, y) = \mathbf{N}^e \mathbf{a}^e = \bar{\mathbf{N}} \mathbf{C}^{-1} \mathbf{a}^e

    where

    .. math::

        \bar{\mathbf{N}} = [\, 1 \;\; x \;\; y \;\; x^2 \;\; x y \;\; y^2 \;\; x^3 \;\; x^2 y \;\; x y^2 \;\; y^3 \;\; x^3 y \;\; x y^3 \,]

    .. math::

        \mathbf{C} = \left[
        \begin{array}{cccccccccccc}
        1 & -a & -b & a^2 & ab & b^2 & -a^3 & -a^2b & -ab^2 & -b^3 & a^3b & ab^3 \\
        0 & 0 & 1 & 0 & -a & -2b & 0 & a^2 & 2ab & 3b^2 & -a^3 & -3ab^2 \\
        0 & -1 & 0 & 2a & b & 0 & -3a^2 & -2ab & -b^2 & 0 & 3a^2b & b^3 \\
        1 & a & -b & a^2 & -ab & b^2 & a^3 & -a^2b & ab^2 & -b^3 & -a^3b & -ab^3 \\
        0 & 0 & 1 & 0 & a & -2b & 0 & a^2 & -2ab & 3b^2 & a^3 & 3ab^2 \\
        0 & -1 & 0 & -2a & b & 0 & -3a^2 & 2ab & -b^2 & 0 & 3a^2b & b^3 \\
        1 & a & b & a^2 & ab & b^2 & a^3 & a^2b & ab^2 & b^3 & a^3b & ab^3 \\
        0 & 0 & 1 & 0 & a & 2b & 0 & a^2 & 2ab & 3b^2 & a^3 & 3ab^2 \\
        0 & -1 & 0 & -2a & -b & 0 & -3a^2 & -2ab & -b^2 & 0 & -3a^2b & -b^3 \\
        1 & -a & b & a^2 & -ab & b^2 & -a^3 & a^2b & -ab^2 & b^3 & -a^3b & -ab^3 \\
        0 & 0 & 1 & 0 & -a & 2b & 0 & a^2 & -2ab & 3b^2 & -a^3 & -3ab^2 \\
        0 & -1 & 0 & 2a & -b & 0 & -3a^2 & 2ab & -b^2 & 0 & -3a^2b & -b^3
        \end{array}
        \right]

    .. math::

        \mathbf{a}^e = [\, u_1 \;\; u_2 \;\; \ldots \;\; u_{12} \,]^T

    and where

    .. math::

        a = \frac{1}{2}(x_3 - x_1) \qquad b = \frac{1}{2}(y_3 - y_1)

    The matrix :math:`\bar{\mathbf{B}}` is obtained as

    .. math::

        \bar{\mathbf{B}} = \stackrel{*}{\nabla} \bar{\mathbf{N}} =
        \left[
        \begin{array}{cccccccccccc}
        0 & 0 & 0 & 2 & 0 & 0 & 6x & 2y & 0 & 0 & 6xy & 0 \\
        0 & 0 & 0 & 0 & 0 & 2 & 0 & 0 & 2x & 6y & 0 & 6xy \\
        0 & 0 & 0 & 0 & 2 & 0 & 0 & 4x & 4y & 0 & 6x^2 & 6y^2 \\
        \end{array}
        \right]

    where

    .. math::

        \stackrel{*}{\nabla} = \begin{bmatrix}
        \frac{\partial^2}{\partial x^2} \\
        \frac{\partial^2}{\partial y^2} \\
        2 \frac{\partial^2}{\partial x \partial y}
        \end{bmatrix}

    Evaluation of the integrals for the rectangular plate element is
    done analytically. Computation of the integrals for the element
    load vector :math:`\mathbf{f}_l^e` yields

    .. math::

        \mathbf{f}_l^e = q_z L_x L_y \begin{bmatrix}
        \frac{1}{4} \\ \frac{L_y}{24} \\ -\frac{L_x}{24} \\ \frac{1}{4} \\ \frac{L_y}{24} \\ \frac{L_x}{24} \\
        \frac{1}{4} \\ -\frac{L_y}{24} \\ \frac{L_x}{24} \\ \frac{1}{4} \\ -\frac{L_y}{24} \\ -\frac{L_x}{24}
        \end{bmatrix}

    where

    .. math::

        L_x = x_3 - x_1 \qquad L_y = y_3 - y_1
