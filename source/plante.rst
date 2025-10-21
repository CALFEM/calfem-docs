.. _plante:
.. index:: 
   single: plante
   single: triangular element
   single: plane element
   single: plane strain
   single: plane stress
   pair: finite element; plane
   pair: triangular; element
   pair: plane; strain
   pair: plane; stress
   pair: 2D; element

plante
^^^^^^ 

:Purpose:
    Compute element matrices for a triangular element in plane strain or plane stress.

    .. figure:: images/PLANTE.png
        :width: 70%
        :align: center


:Syntax:
    .. code-block:: matlab

        Ke = plante(ex, ey, ep, D)
        [Ke, fe] = plante(ex, ey, ep, D, eq)

:Description:
    ``plante`` provides an element stiffness matrix ``Ke`` and an element load vector ``fe`` for a triangular element in plane strain or plane stress.

    The element nodal coordinates :math:`x_1, y_1, x_2, \ldots` are supplied to the function by :math:`\mathbf{ex}` and :math:`\mathbf{ey}`. The type of analysis ``ptype`` and the element thickness ``t`` are supplied by :math:`\mathbf{ep}`,

    .. math::

        \begin{array}{l}
        ptype=1 \quad \text{plane stress} \\
        ptype=2 \quad \text{plane strain}
        \end{array}

    and the material properties are supplied by the constitutive matrix ``D``. Any arbitrary :math:`\mathbf{D}`-matrix with dimensions from :math:`3 \times 3` to :math:`6 \times 6` may be given. For an isotropic elastic material the constitutive matrix can be formed by the function ``hooke``, see Section :ref:`material_functions`.

    .. math::

        \mathbf{ex} = [\,x_1 \;\; x_2 \;\; x_3\,] \\
        \mathbf{ey} = [\,y_1 \;\; y_2 \;\; y_3\,] \\
        \mathbf{ep} = [\,ptype \;\; t\,]

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

    If uniformly distributed loads are applied to the element, the element load vector ``fe`` is computed. The input variable

    .. math::

        \text{eq} = \begin{bmatrix}
            b_x \\
            b_y
        \end{bmatrix}

    containing loads per unit volume, :math:`b_x` and :math:`b_y`, is then given.

:Theory:
    The element stiffness matrix :math:`\mathbf{K}^e` and the element load vector :math:`\mathbf{f}_l^e`, stored in ``Ke`` and ``fe``, respectively, are computed according to

    .. math::

        \mathbf{K}^e = (\mathbf{C}^{-1})^T \int_A \bar{\mathbf{B}}^T \mathbf{D} \bar{\mathbf{B}}\, t\, dA\, \mathbf{C}^{-1}

    .. math::

        \mathbf{f}_l^e = (\mathbf{C}^{-1})^T \int_A \bar{\mathbf{N}}^T \mathbf{b}\, t\, dA

    with the constitutive matrix :math:`\mathbf{D}` defined by ``D``, and the body force vector :math:`\mathbf{b}` defined by ``eq``.

    The evaluation of the integrals for the triangular element is based on a linear displacement approximation :math:`\mathbf{u}(x, y)` and is expressed in terms of the nodal variables :math:`u_1, u_2, \ldots, u_6` as

    .. math::

        \mathbf{u}(x, y) = \mathbf{N}^e \mathbf{a}^e = \bar{\mathbf{N}}\, \mathbf{C}^{-1} \mathbf{a}^e

    where

    .. math::

        \mathbf{u} = \begin{bmatrix}
            u_x \\
            u_y
        \end{bmatrix}
        \quad
        \bar{\mathbf{N}} = \begin{bmatrix}
            1 & x & y & 0 & 0 & 0 \\
            0 & 0 & 0 & 1 & x & y
        \end{bmatrix}

    .. math::

        \mathbf{C} = \begin{bmatrix}
            1 & x_1 & y_1 & 0 & 0 & 0 \\
            0 & 0 & 0 & 1 & x_1 & y_1 \\
            1 & x_2 & y_2 & 0 & 0 & 0 \\
            0 & 0 & 0 & 1 & x_2 & y_2 \\
            1 & x_3 & y_3 & 0 & 0 & 0 \\
            0 & 0 & 0 & 1 & x_3 & y_3 \\
        \end{bmatrix}
        \quad
        \mathbf{a}^e = \begin{bmatrix}
            u_1 \\ u_2 \\ u_3 \\ u_4 \\ u_5 \\ u_6
        \end{bmatrix}

    The matrix :math:`\bar{\mathbf{B}}` is obtained as

    .. math::

        \bar{\mathbf{B}} = \tilde{\nabla} \bar{\mathbf{N}}
        \quad \text{where} \quad
        \tilde{\nabla} = \begin{bmatrix}
            \dfrac{\partial}{\partial x} & 0 \\
            0 & \dfrac{\partial}{\partial y} \\
            \dfrac{\partial}{\partial y} & \dfrac{\partial}{\partial x}
        \end{bmatrix}

    If a larger :math:`\mathbf{D}`-matrix than :math:`3 \times 3` is used for plane stress (:math:`ptype=1`), the :math:`\mathbf{D}`-matrix is reduced to a :math:`3 \times 3` matrix by static condensation using :math:`\sigma_{zz} = \sigma_{xz} = \sigma_{yz} = 0`. These stress components are connected with the rows 3, 5 and 6 in the D-matrix respectively.

    If a larger :math:`\mathbf{D}`-matrix than :math:`3 \times 3` is used for plane strain (:math:`ptype=2`), the :math:`\mathbf{D}`-matrix is reduced to a :math:`3 \times 3` matrix using :math:`\varepsilon_{zz} = \gamma_{xz} = \gamma_{yz} = 0`. This implies that a :math:`3 \times 3` :math:`\mathbf{D}`-matrix is created by the rows and the columns 1, 2 and 4 from the original D-matrix.

    Evaluation of the integrals for the triangular element yields

    .. math::

        \mathbf{K}^e = (\mathbf{C}^{-1})^T \bar{\mathbf{B}}^T \mathbf{D} \bar{\mathbf{B}}\, \mathbf{C}^{-1}\, t\, A

    .. math::

        \mathbf{f}_l^e = \frac{A t}{3} \begin{bmatrix} b_x & b_y & b_x & b_y & b_x & b_y \end{bmatrix}^T

    where the element area :math:`A` is determined as

    .. math::

        A = \frac{1}{2} \det \begin{bmatrix}
            1 & x_1 & y_1 \\
            1 & x_2 & y_2 \\
            1 & x_3 & y_3
        \end{bmatrix}
