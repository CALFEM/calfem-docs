.. _planqe:
.. index:: 
   single: planqe
   single: quadrilateral element
   single: plane element
   single: plane strain
   single: plane stress
   pair: finite element; plane
   pair: quadrilateral; element
   pair: plane; strain
   pair: plane; stress
   pair: 2D; element

planqe
^^^^^^

:Purpose:
    Compute element matrices for a quadrilateral element in plane strain or plane stress.

    .. figure:: images/PLANI4E.png
        :width: 70%
        :align: center    

:Syntax:
    .. code:: matlab

        Ke = planqe(ex, ey, ep, D)
        [Ke, fe] = planqe(ex, ey, ep, D, eq)

:Description:
    ``planqe`` provides an element stiffness matrix :math:`Ke` and an element load vector :math:`fe` for a quadrilateral element in plane strain or plane stress.

    The element nodal coordinates :math:`x_1`, :math:`y_1`, :math:`x_2`, etc. are supplied to the function by :math:`\mathbf{ex}` and :math:`\mathbf{ey}`. The type of analysis :math:`ptype` and the element thickness :math:`t` are supplied by :math:`\mathbf{ep}`:

    .. math::

        \begin{array}{lll}
        ptype=1 & \quad \text{plane stress} \\
        ptype=2 & \quad \text{plane strain}
        \end{array}

    The material properties are supplied by the constitutive matrix :math:`D`. Any arbitrary :math:`\mathbf{D}`-matrix with dimensions from :math:`3 \times 3` to :math:`6 \times 6` may be given. For an isotropic elastic material the constitutive matrix can be formed by the function ``hooke``, see Section :ref:`material_functions`.

    .. math::

        \mathbf{ex} = [\,x_1 \;\, x_2 \;\; x_3\;\, x_4\,] \\
        \mathbf{ey} = [\,y_1 \;\,\, y_2 \;\; y_3\;\,\, y_4\,] \\
        \mathbf{ep} = [\,ptype \;\, t\,]

    .. math::

        \mathbf{D} =
        \begin{bmatrix}
            D_{11} & D_{12} & D_{13} \\
            D_{21} & D_{22} & D_{23} \\
            D_{31} & D_{32} & D_{33}
        \end{bmatrix}
        \quad \text{or} \quad
        \mathbf{D} =
        \begin{bmatrix}
            D_{11} & D_{12} & D_{13} & D_{14} & D_{15} & D_{16} \\
            D_{21} & D_{22} & D_{23} & D_{24} & D_{25} & D_{26} \\
            D_{31} & D_{32} & D_{33} & D_{34} & D_{35} & D_{36} \\
            D_{41} & D_{42} & D_{43} & D_{44} & D_{45} & D_{46} \\
            D_{51} & D_{52} & D_{53} & D_{54} & D_{55} & D_{56} \\
            D_{61} & D_{62} & D_{63} & D_{64} & D_{65} & D_{66}
        \end{bmatrix}

    If uniformly distributed loads are applied on the element, the element load vector :math:`fe` is computed. The input variable

    .. math::

        eq = \begin{bmatrix}
            b_x \\
            b_y
        \end{bmatrix}

    contains loads per unit volume, :math:`b_x` and :math:`b_y`.

:Theory:
    In computing the element matrices, two more degrees of freedom are introduced. The location of these two degrees of freedom is defined by the mean value of the coordinates at the corner points. Four sets of element matrices are calculated using ``plante``. These matrices are then assembled and the two extra degrees of freedom are eliminated by static condensation.
