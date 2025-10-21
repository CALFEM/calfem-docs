.. _soli8e:
.. index:: 
   single: soli8e
   single: solid element
   single: 3D element
   single: 8 node element
   single: isoparametric element
   single: hexahedral element
   pair: finite element; solid
   pair: structural; element
   pair: stiffness; matrix
   pair: 3D; element
   pair: isoparametric; element
   pair: hexahedral; element

soli8e
^^^^^^

:Purpose:
    Compute element matrices for an 8 node isoparametric solid element.

    .. figure:: images/SOLI8E.png
        :width: 70%

:Syntax:
    .. code:: matlab

        Ke = soli8e(ex, ey, ez, ep, D)
        [Ke, fe] = soli8e(ex, ey, ez, ep, D, eq)

:Description:
    ``soli8e`` provides an element stiffness matrix ``Ke`` and an element
    load vector ``fe`` for an 8 node isoparametric solid element.

    The element nodal coordinates :math:`x_1, y_1, z_1, x_2` etc. are supplied to the function
    by :math:`\mathbf{ex}`, :math:`\mathbf{ey}` and :math:`\mathbf{ez}`, and the number of Gauss points :math:`n` are
    supplied by :math:`\mathbf{ep}`.

    :math:`(n \times n \times n)` integration points, :math:`n=1,2,3`

    The material properties are supplied by the
    constitutive matrix ``D``. Any arbitrary :math:`\mathbf{D}`-matrix with
    dimensions :math:`(6 \times 6)` may be given.
    For an isotropic elastic material the constitutive matrix can be formed
    by the function ``hooke``, see Section :ref:`material_functions`.

    .. math::

        \begin{aligned}
        \mathbf{ex} &= [\,x_1,\, x_2,\, \dots,\, x_8\,] \\
        \mathbf{ey} &= [\,y_1,\, y_2,\, \dots,\, y_8\,] \\
        \mathbf{ez} &= [\,z_1,\, z_2,\, \dots,\, z_8\,]
        \end{aligned}

    .. math::

        \mathbf{ep} = [\, n \,]

    .. math::

        \mathbf{D} =
        \begin{bmatrix}
            D_{11} & D_{12} & \cdots & D_{16} \\
            D_{21} & D_{22} & \cdots & D_{26} \\
            \vdots & \vdots & \ddots & \vdots \\
            D_{61} & D_{62} & \cdots & D_{66}
        \end{bmatrix}

    If different :math:`\mathbf{D}_i` matrices are used in the Gauss points these
    :math:`\mathbf{D}_i` matrices are stored in a global vector ``D``. For
    numbering of the Gauss points, see ``eci`` in ``soli8s``.

    .. math::

        \mathbf{D} =
        \begin{bmatrix}
            \mathbf{D}_1 \\
            \mathbf{D}_2 \\
            \vdots \\
            \mathbf{D}_{n^3}
        \end{bmatrix}

    If uniformly distributed loads are applied to the element,
    the element load vector ``fe`` is computed. The input variable

    .. math::

        \mathrm{eq} =
        \begin{bmatrix}
            b_x \\
            b_y \\
            b_z
        \end{bmatrix}

    containing loads per unit volume, :math:`b_x`, :math:`b_y`, and :math:`b_z`, is then given.

:Theory:
    The element stiffness matrix :math:`\mathbf{K}^e` and the
    element load vector :math:`\mathbf{f}_l^e`, stored in ``Ke`` and ``fe``,
    respectively, are computed according to

    .. math::

        \mathbf{K}^e = \int_V \mathbf{B}^{eT} \mathbf{D} \mathbf{B}^e \, dV

        \mathbf{f}_l^e = \int_V \mathbf{N}^{eT} \mathbf{b} \, dV

    with the constitutive matrix :math:`\mathbf{D}` defined by ``D``, and the body force
    vector :math:`\mathbf{b}` defined by ``eq``.

    The evaluation of the integrals for the isoparametric 8 node solid element
    is based on a displacement approximation :math:`\mathbf{u}(\xi, \eta, \zeta)`, expressed in a
    local coordinate system in terms of the nodal
    variables :math:`u_1, u_2, \dots, u_{24}` as

    .. math::

        \mathbf{u}(\xi, \eta, \zeta) = \mathbf{N}^e \mathbf{a}^e

        \mathbf{u} =
        \begin{bmatrix}
            u_x \\
            u_y \\
            u_z
        \end{bmatrix}
        \quad
        \mathbf{N}^e =
        \begin{bmatrix}
            N^e_1 & 0 & 0 & N^e_2 & 0 & 0 & \dots & N^e_8 & 0 & 0 \\
            0 & N^e_1 & 0 & 0 & N^e_2 & 0 & \dots & 0 & N^e_8 & 0 \\
            0 & 0 & N^e_1 & 0 & 0 & N^e_2 & \dots & 0 & 0 & N^e_8 \\
        \end{bmatrix}
        \quad
        \mathbf{a}^e =
        \begin{bmatrix}
            u_1 \\
            u_2 \\
            \vdots \\
            u_{24}
        \end{bmatrix}

    The element shape functions are given by

    .. math::

        \begin{aligned}
        N_1^e &= \frac{1}{8}(1-\xi)(1-\eta)(1-\zeta) & N_5^e &= \frac{1}{8}(1-\xi)(1-\eta)(1+\zeta) \\
        N_2^e &= \frac{1}{8}(1+\xi)(1-\eta)(1-\zeta) & N_6^e &= \frac{1}{8}(1+\xi)(1-\eta)(1+\zeta) \\
        N_3^e &= \frac{1}{8}(1+\xi)(1+\eta)(1-\zeta) & N_7^e &= \frac{1}{8}(1+\xi)(1+\eta)(1+\zeta) \\
        N_4^e &= \frac{1}{8}(1-\xi)(1+\eta)(1-\zeta) & N_8^e &= \frac{1}{8}(1-\xi)(1+\eta)(1+\zeta)
        \end{aligned}

    The :math:`\mathbf{B}^e`-matrix is obtained as

    .. math::

        \mathbf{B}^e = \tilde{\nabla} \mathbf{N}^e

    where

    .. math::

        \tilde{\nabla} =
        \begin{bmatrix}
            \frac{\partial}{\partial x} & 0 & 0 \\
            0 & \frac{\partial}{\partial y} & 0 \\
            0 & 0 & \frac{\partial}{\partial z} \\
            \frac{\partial}{\partial y} & \frac{\partial}{\partial x} & 0 \\
            \frac{\partial}{\partial z} & 0 & \frac{\partial}{\partial x} \\
            0 & \frac{\partial}{\partial z} & \frac{\partial}{\partial y}
        \end{bmatrix}
        \qquad
        \begin{bmatrix}
            \frac{\partial}{\partial x} \\
            \frac{\partial}{\partial y} \\
            \frac{\partial}{\partial z}
        \end{bmatrix}
        = (\mathbf{J}^T)^{-1}
        \begin{bmatrix}
            \frac{\partial}{\partial \xi} \\
            \frac{\partial}{\partial \eta} \\
            \frac{\partial}{\partial \zeta}
        \end{bmatrix}

    .. math::

        \mathbf{J} =
        \begin{bmatrix}
            \frac{\partial x}{\partial \xi} & \frac{\partial x}{\partial \eta} & \frac{\partial x}{\partial \zeta} \\
            \frac{\partial y}{\partial \xi} & \frac{\partial y}{\partial \eta} & \frac{\partial y}{\partial \zeta} \\
            \frac{\partial z}{\partial \xi} & \frac{\partial z}{\partial \eta} & \frac{\partial z}{\partial \zeta}
        \end{bmatrix}

    Evaluation of the integrals is done by Gauss integration.
