plantce
^^^^^^^

:Purpose:
    Compute element matrices for a rectangular (Turner-Clough)
    element in plane strain or plane stress.

    .. only:: html
        
        .. figure:: images/PLANTRE.svg
            :align: center
            :width: 400px
    
    .. only:: latex
        
        .. figure:: images/PLANTRE.svg
            :align: center
            :width: 70%

:Syntax:
    .. code:: matlab

        Ke = plantce(ex, ey, ep)
        [Ke, fe] = plantce(ex, ey, ep, eq)

:Description:
    ``plantce`` provides an element stiffness matrix ``Ke`` and an element
    load vector ``fe`` for a rectangular (Turner-Clough) element in plane strain
    or plane stress. This element can only be used if the material is isotropic and
    if the element edges are parallel to the coordinate axis.

    The element nodal coordinates :math:`(x_1, y_1)` and
    :math:`(x_3, y_3)` are supplied to the function
    by :math:`\mathbf{ex}` and :math:`\mathbf{ey}`. The state of stress ``ptype``, the element thickness :math:`t`
    and the material properties :math:`E` and :math:`\nu` are supplied by :math:`\mathbf{ep}`.
    For plane stress :math:`ptype=1` and for plane strain :math:`ptype=2`.

    .. math::

        \begin{array}{l}
        \mathbf{ex} = [\, x_1 \;\; x_3\,] \\
        \mathbf{ey} = [\, y_1 \;\; y_3\,]
        \end{array}
        \qquad
        \mathbf{ep} = [\, ptype \;\; t \;\; E \;\; \nu \,]

    If uniformly distributed loads are applied to the element,
    the element load vector ``fe`` is computed. The input variable

    .. math::

        eq = \begin{bmatrix}
            b_x \\
            b_y
        \end{bmatrix}

    containing loads per unit volume, :math:`b_x` and :math:`b_y`, is then given.

:Theory:
    The element stiffness matrix :math:`\mathbf{K}^e` and the
    element load vector :math:`\mathbf{f}_l^e`, stored in ``Ke`` and ``fe``,
    respectively, are computed according to

    .. math::

        \mathbf{K}^e = \int_A \mathbf{B}^{eT} \mathbf{D} \mathbf{B}^e t\, dA

    .. math::

        \mathbf{f}_l^e = \int_A \mathbf{N}^{eT} \mathbf{b} t\, dA

    where the constitutive matrix :math:`\mathbf{D}` is described in ``hooke``,
    see Section :ref:`material_functions`, and the body force vector :math:`\mathbf{b}`
    is defined by ``eq``.

    The evaluation of the integrals for the Turner-Clough element is based on a
    displacement field :math:`\mathbf{u}(x, y)` built up of a bilinear displacement
    approximation superposed by bubble functions in order to create a linear stress field over the element.
    The displacement field is expressed in terms of the nodal variables :math:`u_1, u_2, \dots, u_8` as

    .. math::

        \mathbf{u}(x, y) = \mathbf{N}^e \mathbf{a}^e

    where

    .. math::

        \mathbf{u} = \begin{bmatrix}
            u_x \\
            u_y
        \end{bmatrix}
        \quad
        \mathbf{N}^e = \begin{bmatrix}
            N^e_1 & N^e_5 & N^e_2 & -N^e_5 & N^e_3 & N^e_5 & N^e_4 & -N^e_5 \\
            N^e_6 & N^e_1 & -N^e_6 & N^e_2 & N^e_6 & N^e_3 & -N^e_6 & N^e_4
        \end{bmatrix}
        \quad
        \mathbf{a}^e = \begin{bmatrix}
            u_1 \\ u_2 \\ \vdots \\ u_8
        \end{bmatrix}

    With a local coordinate system located at the center of the element,
    the element shape functions :math:`N^e_1`–:math:`N^e_6` are obtained as

    .. math::

        N^e_1 = \frac{1}{4ab}(a-x)(b-y) \\
        N^e_2 = \frac{1}{4ab}(a+x)(b-y) \\
        N^e_3 = \frac{1}{4ab}(a+x)(b+y) \\
        N^e_4 = \frac{1}{4ab}(a-x)(b+y) \\
        N^e_5 = \frac{1}{8ab}\left[ (b^2-y^2) + \nu (a^2-x^2) \right] \\
        N^e_6 = \frac{1}{8ab}\left[ (a^2-x^2) + \nu (b^2-y^2) \right]

    where

    .. math::

        a = \frac{1}{2}(x_3 - x_1) \qquad b = \frac{1}{2}(y_3 - y_1)

    The matrix :math:`\mathbf{B}^e` is obtained as

    .. math::

        \mathbf{B}^e = \tilde{\nabla} \mathbf{N}^e \qquad
        \text{where} \quad \tilde{\nabla} = \begin{bmatrix}
            \dfrac{\partial}{\partial x} & 0 \\
            0 & \dfrac{\partial}{\partial y} \\
            \dfrac{\partial}{\partial y} & \dfrac{\partial}{\partial x}
        \end{bmatrix}

    Evaluation of the integrals for the Turner-Clough element can be done either
    analytically or numerically by use of a :math:`2 \times 2` point Gauss integration.
    The element load vector :math:`\mathbf{f}_l^e` yields

    .. math::

        \mathbf{f}_l^e = abt \begin{bmatrix}
            b_x \\ b_y \\ b_x \\ b_y \\
            b_x \\ b_y \\ b_x \\ b_y
        \end{bmatrix}
