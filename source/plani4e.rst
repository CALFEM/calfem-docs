.. _plani4e:
.. index:: 
   single: plani4e
   single: plane element
   single: isoparametric element
   single: 4 node element
   single: plane strain
   single: plane stress
   pair: finite element; plane
   pair: structural; element
   pair: stiffness; matrix
   pair: 2D; element
   pair: isoparametric; element
   pair: quadrilateral; element

plani4e
^^^^^^^

:Purpose:
    Compute element matrices for a 4 node isoparametric element in plane strain or plane stress.

    .. only:: html
        
        .. figure:: images/PLANI4E.svg
            :align: center
            :width: 400px
    
    .. only:: latex
        
        .. figure:: images/PLANI4E.svg
            :align: center
            :width: 70%

:Syntax:
    .. code:: matlab

        Ke = plani4e(ex, ey, ep, D)
        [Ke, fe] = plani4e(ex, ey, ep, D, eq)

:Description:
    ``plani4e`` provides an element stiffness matrix ``Ke`` and an element load vector ``fe`` for a 4 node isoparametric element in plane strain or plane stress.

    The element nodal coordinates :math:`x_1, y_1, x_2, \ldots` are supplied to the function by :math:`\mathbf{ex}` and :math:`\mathbf{ey}`. The type of analysis :math:`ptype`, the element thickness :math:`t`, and the number of Gauss points :math:`n` are supplied by :math:`\mathbf{ep}`:

    .. math::

        \begin{array}{lll}
        ptype=1 & \text{plane stress} & (n \times n) \text{ integration points} \\
        ptype=2 & \text{plane strain} & n=1,2,3
        \end{array}

    The material properties are supplied by the constitutive matrix :math:`D`. Any arbitrary :math:`\mathbf{D}`-matrix with dimensions from :math:`3 \times 3` to :math:`6 \times 6` may be given. For an isotropic elastic material the constitutive matrix can be formed by the function ``hooke``, see Section :ref:`material_functions`.

    .. math::

        \mathbf{ex} = [\,x_1 \;\, x_2 \;\; x_3\;\, x_4\,] \\
        \mathbf{ey} = [\,y_1 \;\,\, y_2 \;\; y_3\;\,\, y_4\,] \\
        \mathbf{ep} = [\,ptype \;\, t\;\, n\,]

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

    If different :math:`\mathbf{D}_i` matrices are used in the Gauss points, these :math:`\mathbf{D}_i` matrices are stored in a global vector ``D``. For numbering of the Gauss points, see ``eci`` in ``plani4s``.

    .. math::

        \mathbf{D} = \begin{bmatrix}
        \mathbf{D}_1 \\
        \mathbf{D}_2 \\
        \vdots \\
        \mathbf{D}_{n^2}
        \end{bmatrix}

    If uniformly distributed loads are applied to the element, the element load vector ``fe`` is computed. The input variable

    .. math::

        \mathrm{eq} = \begin{bmatrix}
        b_x \\
        b_y
        \end{bmatrix}

    containing loads per unit volume, :math:`b_x` and :math:`b_y`, is then given.

:Theory:
    The element stiffness matrix :math:`\mathbf{K}^e` and the element load vector :math:`\mathbf{f}_l^e`, stored in ``Ke`` and ``fe``, respectively, are computed according to

    .. math::

        \mathbf{K}^e = \int_A \mathbf{B}^{eT} \mathbf{D} \mathbf{B}^e t\, dA \\
        \mathbf{f}_l^e = \int_A \mathbf{N}^{eT} \mathbf{b} t\, dA

    with the constitutive matrix :math:`\mathbf{D}` defined by ``D``, and the body force vector :math:`\mathbf{b}` defined by ``eq``.

    The evaluation of the integrals for the isoparametric 4 node element is based on a displacement approximation :math:`\mathbf{u}(\xi, \eta)`, expressed in a local coordinate system in terms of the nodal variables :math:`u_1, u_2, \ldots, u_8` as

    .. math::

        \mathbf{u}(\xi, \eta) = \mathbf{N}^e \mathbf{a}^e

    where

    .. math::

        \mathbf{u} = \begin{bmatrix} u_x \\ u_y \end{bmatrix} \qquad
        \mathbf{N}^e = \begin{bmatrix}
        N_1^e & 0 & N_2^e & 0 & N_3^e & 0 & N_4^e & 0 \\
        0 & N_1^e & 0 & N_2^e & 0 & N_3^e & 0 & N_4^e
        \end{bmatrix} \qquad
        \mathbf{a}^e = \begin{bmatrix}
        u_1 \\ u_2 \\ \vdots \\ u_8
        \end{bmatrix}

    The element shape functions are given by

    .. math::

        N_1^e = \frac{1}{4}(1-\xi)(1-\eta) \qquad N_2^e = \frac{1}{4}(1+\xi)(1-\eta) \\
        N_3^e = \frac{1}{4}(1+\xi)(1+\eta) \qquad N_4^e = \frac{1}{4}(1-\xi)(1+\eta)

    The matrix :math:`\mathbf{B}^e` is obtained as

    .. math::

        \mathbf{B}^e = \tilde{\nabla} \mathbf{N}^e \qquad
        \text{where} \quad \tilde{\nabla} = \begin{bmatrix}
        \frac{\partial}{\partial x} & 0 \\
        0 & \frac{\partial}{\partial y} \\
        \frac{\partial}{\partial y} & \frac{\partial}{\partial x}
        \end{bmatrix}

    and

    .. math::

        \begin{bmatrix}
        \frac{\partial}{\partial x} \\
        \frac{\partial}{\partial y}
        \end{bmatrix}
        = (\mathbf{J}^T)^{-1}
        \begin{bmatrix}
        \frac{\partial}{\partial \xi} \\
        \frac{\partial}{\partial \eta}
        \end{bmatrix}
        \qquad
        \mathbf{J} = \begin{bmatrix}
        \frac{\partial x}{\partial \xi} & \frac{\partial x}{\partial \eta} \\
        \frac{\partial y}{\partial \xi} & \frac{\partial y}{\partial \eta}
        \end{bmatrix}

    If a larger :math:`\mathbf{D}`-matrix than :math:`3 \times 3` is used for plane stress (:math:`ptype=1`), the :math:`\mathbf{D}`-matrix is reduced to a :math:`3 \times 3` matrix by static condensation using :math:`\sigma_{zz} = \sigma_{xz} = \sigma_{yz} = 0`. These stress components are connected with the rows 3, 5 and 6 in the D-matrix respectively.

    If a larger :math:`\mathbf{D}`-matrix than :math:`3 \times 3` is used for plane strain (:math:`ptype=2`), the :math:`\mathbf{D}`-matrix is reduced to a :math:`3 \times 3` matrix using :math:`\varepsilon_{zz} = \gamma_{xz} = \gamma_{yz} = 0`. This implies that a :math:`3 \times 3` :math:`\mathbf{D}`-matrix is created by the rows and the columns 1, 2 and 4 from the original D-matrix.

    Evaluation of the integrals is done by Gauss integration.
