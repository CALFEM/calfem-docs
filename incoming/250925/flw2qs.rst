flw2qs
^^^^^^

:Purpose:
    Compute heat flux and temperature gradients in a quadrilateral heat flow element.

:Syntax:
    .. code:: matlab

        [es, et] = flw2qs(ex, ey, ep, D, ed)
        [es, et] = flw2qs(ex, ey, ep, D, ed, eq)

:Description:
    ``flw2qs`` computes the heat flux vector ``es`` and the temperature gradient ``et`` (or corresponding quantities) in a quadrilateral heat flow element.

    The input variables ``ex``, ``ey``, ``eq`` and the matrix ``D`` are defined in ``flw2qe``.
    The vector ``ed`` contains the nodal temperatures :math:`\mathbf{a}^e` of the element and is obtained by the function ``extract`` as

    .. math::

        \mathbf{ed} = (\mathbf{a}^e)^T = [\;T_1\;\; T_2\;\; T_3\;\; T_4\;]

    The output variables

    .. math::

        \mathbf{es} = \mathbf{q}^T = \left[\; q_x \; q_y \;\right]

    .. math::

        \mathbf{et} = (\nabla T)^T = \left[\begin{array}{l}
        \frac{\partial T}{\partial x}\;\;\frac{\partial T}{\partial y}
        \end{array} \right]

    contain the components of the heat flux and the temperature gradient computed in the directions of the coordinate axis.

:Theory:
    By assembling four triangular elements as described in ``flw2te`` a system of equations containing 5 degrees of freedom is obtained. From this system of equations the unknown temperature at the center of the element is computed.
    Then according to the description in ``flw2ts`` the temperature gradient and the heat flux in each of the four triangular elements are produced.
    Finally the temperature gradient and the heat flux of the quadrilateral element are computed as area weighted mean values from the values of the four triangular elements. If heat is supplied to the element, the element load vector ``eq`` is needed for the calculations.

    .. note::

        If the input variables are given for a number of identical (``nie``) elements, i.e. ``Ex``, ``Ey``, and ``Ed`` are matrices, then the output variables are defined as

        .. math::

            \mathrm{Es} =
            \left[
            \begin{array}{cc}
            q^1_x & q^1_y  \\
            q^2_x & q^2_y  \\
            \vdots  &  \vdots   \\
            q^{nie}_x & q^{nie}_y
            \end{array}
            \right]
            \qquad
            \mathrm{Et} = \left[
            \begin{array}{cc}
            \frac{\partial T}{\partial x}^1 & \frac{\partial T}{\partial y}^1 \\
            \frac{\partial T}{\partial x}^2 & \frac{\partial T}{\partial y}^2 \\
            \vdots & \vdots \\
            \frac{\partial T}{\partial x}^{nie} & \frac{\partial T}{\partial y}^{nie}
            \end{array}
            \right]

        where :math:`\mathbf{q}^i` and :math:`\nabla T^i` are computed from the nodal values located in column ``i`` of ``Ed``.
