bar2ge
^^^^^^

:Purpose:
    Compute element stiffness matrix for a two dimensional geometric nonlinear bar.

    .. figure:: images/bar2g.png
        :align: center
        :width: 70%

:Syntax:
    .. code:: matlab
        
        Ke = bar2ge(ex, ey, ep, Qx)

:Description:
    ``bar2ge`` provides the element stiffness matrix ``Ke`` for a two dimensional
    geometric nonlinear bar element.

    The input variables::

        ex = [x1, x2]
        ey = [y1, y2]
        ep = [E, A]

    supply the element nodal coordinates
    :math:`x_1`, :math:`y_1`, :math:`x_2`, and :math:`y_2`, the modulus of elasticity :math:`E`,
    and the cross section area :math:`A`.

    The input variable::

        Qx = [Q_{\bar{x}}]

    contains the value of the axial force, which is positive in tension.

:Theory:
    The global element stiffness matrix :math:`\mathbf{K}^e`, stored in ``Ke``,
    is computed according to

    .. math::

        \mathbf{K}^e = \mathbf{G}^T\,\mathbf{\bar{K}}^e\,\mathbf{G}

    where

    .. math::

        \mathbf{\bar{K}}^e = \frac{D_{EA}}{L}
        \begin{bmatrix}
        1 & 0 & -1 & 0 \\
        0 & 0 & 0 & 0 \\
        -1 & 0 & 1 & 0 \\
        0 & 0 & 0 & 0
        \end{bmatrix}
        +
        \frac{Q_{\bar{x}}}{L}
        \begin{bmatrix}
        0 & 0 & 0 & 0 \\
        0 & 1 & 0 & -1 \\
        0 & 0 & 0 & 0 \\
        0 & -1 & 0 & 1
        \end{bmatrix}

    .. math::

        \mathbf{G} =
        \begin{bmatrix}
        n_{x\bar{x}} & n_{y\bar{x}} & 0 & 0 \\
        n_{x\bar{y}} & n_{y\bar{y}} & 0 & 0 \\
        0 & 0 & n_{x\bar{x}} & n_{y\bar{x}} \\
        0 & 0 & n_{x\bar{y}} & n_{y\bar{y}}
        \end{bmatrix}

    where the axial stiffness :math:`D_{EA}` and the length :math:`L` are given by

    .. math::

        D_{EA} = EA \qquad L = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}

    and the transformation matrix :math:`\mathbf{G}` contains the direction cosines

    .. math::

        n_{x\bar{x}} = n_{y\bar{y}} = \frac{x_2 - x_1}{L} \qquad
        n_{y\bar{x}} = -n_{x\bar{y}} = \frac{y_2 - y_1}{L}