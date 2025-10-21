.. _flw2i4s:
.. index:: 
   single: flw2i4s
   single: heat flux
   single: temperature gradient
   single: thermal analysis
   single: 4 node thermal
   single: flow analysis
   pair: finite element; thermal
   pair: heat; flux
   pair: thermal; analysis
   pair: post-processing; thermal
   pair: 2D; thermal
   pair: isoparametric; thermal

flw2i4s
^^^^^^^

:Purpose:
    Compute heat flux and temperature gradients in a 4 node isoparametric heat flow element.

:Syntax:
    ``[es, et, eci] = flw2i4s(ex, ey, ep, D, ed)``

:Description:
    ``flw2i4s`` computes the heat flux vector ``es`` and the temperature gradient ``et`` (or corresponding quantities) in a 4 node isoparametric heat flow element.

    The input variables :math:`\mathbf{ex}`, :math:`\mathbf{ey}`, :math:`\mathbf{ep}` and the matrix :math:`\mathbf{D}` are defined in ``flw2i4e``. The vector :math:`\mathbf{ed}` contains the nodal temperatures :math:`\mathbf{a}^e` of the element and is obtained by ``extract`` as

    .. math::

        \mathbf{ed} = (\mathbf{a}^e)^T = [\;T_1\;\; T_2\;\; T_3\;\; T_4\;]

    The output variables

    .. math::

        \mathbf{es} = \bar{\mathbf{q}}^T = \left[
        \begin{array}{cc}
        q^1_x & q^1_y  \\
        q^2_x & q^2_y  \\
        \vdots  &  \vdots   \\
        q^{n^2}_x & q^{n^2}_y
        \end{array}
        \right]

    .. math::

        \mathbf{et} = (\bar {\nabla} T)^T = \left[
        \begin{array}{cc}
        \frac{\partial T}{\partial x}^1 & \frac{\partial T}{\partial y}^1 \\
        \frac{\partial T}{\partial x}^2 & \frac{\partial T}{\partial y}^2 \\
        \vdots & \vdots \\
        \frac{\partial T}{\partial x}^{n^2} & \frac{\partial T}{\partial y}^{n^2}
        \end{array}
        \right]

        \qquad
        \mathbf{eci} = \left[
        \begin{array}{cc}
        x_1 & y_1 \\
        x_2 & y_2 \\
        \vdots  &  \vdots \\
        x_{n^2} & y_{n^2}
        \end{array}
        \right]

    contain the heat flux, the temperature gradient, and the coordinates of the integration points. The index :math:`n` denotes the number of integration points used within the element, cf. ``flw2i4e``.

:Theory:
    The temperature gradient and the heat flux are computed according to

    .. math::

        \nabla T = \mathbf{B}^e\,\mathbf{a}^e

    .. math::

        \mathbf{q} = - \mathbf{D} \nabla T

    where the matrices :math:`\mathbf{D}`, :math:`\mathbf{B}^e`, and :math:`\mathbf{a}^e` are described in ``flw2i4e``, and where the integration points are chosen as evaluation points.
