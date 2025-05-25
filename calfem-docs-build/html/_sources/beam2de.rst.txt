beam2de
^^^^^^^

:Purpose:

    Compute element stiffness, mass and damping matrices for a two dimensional beam element.

    .. figure:: images/BEAM2D.png
        :align: center
        :width: 70%

:Syntax:

    .. code-block:: matlab

        [Ke, Me] = beam2de(ex, ey, ep)
        [Ke, Me, Ce] = beam2de(ex, ey, ep)

:Description:

    ``beam2de`` provides the global element stiffness matrix ``Ke``, the global element mass matrix ``Me``, and the global element damping matrix ``Ce``, for a two dimensional beam element.

    The input variables ``ex`` and ``ey`` are described in ``beam2e``, and

    .. math::

        ep = [ E,\; A,\; I,\; m,\; [a_0,\; a_1] ]

    contains the modulus of elasticity :math:`E`, the cross section area :math:`A`, the moment of inertia :math:`I`, the mass per unit length :math:`m`, and the Rayleigh damping coefficients :math:`a_0` and :math:`a_1`.  
    If :math:`a_0` and :math:`a_1` are omitted, the element damping matrix ``Ce`` is not computed.

:Theory:

    The element stiffness matrix :math:`\mathbf{K}^e`, the element mass matrix :math:`\mathbf{M}^e` and the element damping matrix :math:`\mathbf{C}^e`, stored in the variables ``Ke``, ``Me`` and ``Ce``, respectively, are computed according to

    .. math::

        \mathbf{K}^e = \mathbf{G}^T \bar{\mathbf{K}}^e \mathbf{G} \qquad
        \mathbf{M}^e = \mathbf{G}^T \bar{\mathbf{M}}^e \mathbf{G} \qquad
        \mathbf{C}^e = \mathbf{G}^T \bar{\mathbf{C}}^e \mathbf{G}

    where :math:`\mathbf{G}` and :math:`\bar{\mathbf{K}}^e` are described in ``beam2e``.

    The matrix :math:`\bar{\mathbf{M}}^e` is given by

    .. math::

        \bar{\mathbf{M}}^e = \frac{mL}{420}
        \begin{bmatrix}
        140 & 0 & 0 & 70 & 0 & 0 \\
        0 & 156 & 22L & 0 & 54 & -13L \\
        0 & 22L & 4L^2 & 0 & 13L & -3L^2 \\
        70 & 0 & 0 & 140 & 0 & 0 \\
        0 & 54 & 13L & 0 & 156 & -22L \\
        0 & -13L & -3L^2 & 0 & -22L & 4L^2
        \end{bmatrix}

    and the matrix :math:`\bar{\mathbf{C}}^e` is computed by combining :math:`\bar{\mathbf{K}}^e` and :math:`\bar{\mathbf{M}}^e`:

    .. math::

        \bar{\mathbf{C}}^e = a_0 \bar{\mathbf{M}}^e + a_1 \bar{\mathbf{K}}^e

