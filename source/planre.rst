planre
^^^^^^

:Purpose:
    Compute element matrices for a rectangular (Melosh) element in plane strain or plane stress.

    .. only:: html
        
        .. figure:: images/plantre.svg
            :align: center
            :width: 400px
    
    .. only:: latex
        
        .. figure:: images/plantre.svg
            :align: center
            :width: 70%

:Syntax:
    .. code:: matlab

        Ke = planre(ex, ey, ep, D)
        [Ke, fe] = planre(ex, ey, ep, D, eq)

:Description:
    planre provides an element stiffness matrix Ke and an element load vector fe for a rectangular (Melosh) element in plane strain or plane stress. This element can only be used if the element edges are parallel to the coordinate axis.

    The element nodal coordinates :math:`(x_1, y_1)` and :math:`(x_3, y_3)` are supplied to the function by ex and ey. The type of analysis ptype and the element thickness t are supplied by ep,

    .. math::

        \begin{array}{lll}
        ptype=1 \quad \mbox{plane stress} \\
        ptype=2 \quad \mbox{plane strain}
        \end{array}

    and the material properties are supplied by the constitutive matrix D. Any arbitrary D-matrix with dimensions from :math:`3 \times 3` to :math:`6 \times 6` may be given. For an isotropic elastic material the constitutive matrix can be formed by the function hooke, see Section Material.

    .. math::

        \begin{array}{l}
        \mathbf{ex} = [\,x_1 \;\, x_3\,]  \\
        \mathbf{ey} = [\,y_1 \;\, y_3\,]
        \end{array}
        \qquad
        \mathbf{ep} = [\,ptype \;\, t\,]

    .. math::

        \mathbf{D} = \begin{bmatrix}
        D_{11} & D_{12} & D_{13} \\
        D_{21} & D_{22} & D_{23} \\
        D_{31} & D_{32} & D_{33}
        \end{bmatrix}
        \quad \text{or} \quad
        \mathbf{D} = \begin{bmatrix}
        D_{11} & D_{12} & D_{13} & D_{14} & [D_{15}] & [D_{16}] \\
        D_{21} & D_{22} & D_{23} & D_{24} & [D_{25}] & [D_{26}] \\
        D_{31} & D_{32} & D_{33} & D_{34} & [D_{35}] & [D_{36}] \\
        D_{41} & D_{42} & D_{43} & D_{44} & [D_{45}] & [D_{46}] \\
        [D_{51}] & [D_{52}] & [D_{53}] & [D_{54}] & [D_{55}] & [D_{56}] \\
        [D_{61}] & [D_{62}] & [D_{63}] & [D_{64}] & [D_{65}] & [D_{66}]
        \end{bmatrix}

    If uniformly distributed loads are applied on the element, the element load vector fe is computed. The input variable

    .. math::

        eq = \begin{bmatrix}
        b_x \\
        b_y
        \end{bmatrix}

    containing loads per unit volume, :math:`b_x` and :math:`b_y`, is then given.

:Theory:
    The element stiffness matrix :math:`\mathbf{K}^e` and the element load vector :math:`\mathbf{f}_l^e`, stored in Ke and fe, respectively, are computed according to

    .. math::

        \mathbf{K}^e = \int_A \mathbf{B}^{eT} \mathbf{D} \mathbf{B}^e t\, dA

    .. math::

        \mathbf{f}_l^e = \int_A \mathbf{N}^{eT} \mathbf{b} t\, dA

    with the constitutive matrix :math:`\mathbf{D}` defined by D, and the body force vector :math:`\mathbf{b}` defined by eq.

    The evaluation of the integrals for the rectangular element is based on a bilinear displacement approximation :math:`\mathbf{u}(x,y)` and is expressed in terms of the nodal variables :math:`u_1, u_2, \dots, u_8` as

    .. math::

        \mathbf{u}(x, y) = \mathbf{N}^e \mathbf{a}^e

    where

    .. math::

        \mathbf{u} = \begin{bmatrix} u_x \\ u_y \end{bmatrix} \quad
        \mathbf{N}^e = \begin{bmatrix}
        N^e_1 & 0 & N^e_2 & 0 & N^e_3 & 0 & N^e_4 & 0 \\
        0 & N^e_1 & 0 & N^e_2 & 0 & N^e_3 & 0 & N^e_4
        \end{bmatrix}
        \quad
        \mathbf{a}^e = \begin{bmatrix}
        u_1 \\ u_2 \\ \vdots \\ u_8
        \end{bmatrix}

    With a local coordinate system located at the center of the element, the element shape functions :math:`N^e_1`–:math:`N^e_4` are obtained as

    .. math::

        N^e_1 = \frac{1}{4ab}(x - x_2)(y - y_4) \\
        N^e_2 = -\frac{1}{4ab}(x - x_1)(y - y_3) \\
        N^e_3 = \frac{1}{4ab}(x - x_4)(y - y_2) \\
        N^e_4 = -\frac{1}{4ab}(x - x_3)(y - y_1)

    where

    .. math::

        a = \frac{1}{2}(x_3 - x_1) \quad \text{and} \quad b = \frac{1}{2}(y_3 - y_1)

    The matrix :math:`\mathbf{B}^e` is obtained as

    .. math::

        \mathbf{B}^e = \tilde{\nabla} \mathbf{N}^e \qquad
        \text{where} \quad \tilde{\nabla} = \begin{bmatrix}
        \dfrac{\partial}{\partial x} & 0 \\
        0 & \dfrac{\partial}{\partial y} \\
        \dfrac{\partial}{\partial y} & \dfrac{\partial}{\partial x}
        \end{bmatrix}

    If a larger D-matrix than :math:`3 \\times 3` is used for plane stress (:math:`ptype=1`), the D-matrix is reduced to a :math:`3 \\times 3` matrix by static condensation using :math:`\sigma_{zz} = \sigma_{xz} = \sigma_{yz} = 0`. These stress components are connected with the rows 3, 5 and 6 in the D-matrix respectively.

    If a larger D-matrix than :math:`3 \\times 3` is used for plane strain (:math:`ptype=2`), the D-matrix is reduced to a :math:`3 \\times 3` matrix using :math:`\varepsilon_{zz} = \gamma_{xz} = \gamma_{yz} = 0`. This implies that a :math:`3 \\times 3` D-matrix is created by the rows and the columns 1, 2 and 4 from the original D-matrix.

    Evaluation of the integrals for the rectangular element can be done either analytically or numerically by use of a :math:`2 \\times 2` point Gauss integration. The element load vector :math:`\mathbf{f}_l^e` yields

    .. math::

        \mathbf{f}_l^e = abt \begin{bmatrix}
        b_x \\ b_y \\ b_x \\ b_y \\
        b_x \\ b_y \\ b_x \\ b_y
        \end{bmatrix}
