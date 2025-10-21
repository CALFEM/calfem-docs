.. _flw2ts:
.. index:: 
   single: flw2ts
   single: triangular thermal stress
   single: heat flux
   single: temperature gradient
   single: thermal analysis
   pair: finite element; thermal
   pair: triangular; element
   pair: heat; flux
   pair: thermal; analysis
   pair: temperature; gradient

flw2ts
^^^^^^

:Purpose:
    Compute heat flux and temperature gradients in a triangular heat flow element.

:Syntax:
    .. code:: matlab
        
        [es, et] = flw2ts(ex, ey, D, ed)

:Description:
    ``flw2ts`` computes the heat flux vector ``es`` and the temperature gradient ``et`` (or corresponding quantities) in a triangular heat flow element.

    The input variables ``ex``, ``ey`` and the matrix ``D`` are defined in ``flw2te``. The vector ``ed`` contains the nodal temperatures :math:`\mathbf{a}^e` of the element and is obtained by the function ``extract`` as

    .. math::

        \mathbf{ed} = (\mathbf{a}^e)^T = [\;T_1\;\; T_2\;\; T_3\;]

    The output variables

    .. math::

        \mathbf{es} = \mathbf{q}^T = \left[\; q_x \; q_y \;\right]

    .. math::

        \mathbf{et} = (\nabla T)^T = \left[\begin{array}{l}
        \frac{\partial T}{\partial x}\;\;\frac{\partial T}{\partial y}
        \end{array} \right]

    contain the components of the heat flux and the temperature gradient computed in the directions of the coordinate axis.

:Theory:
    The temperature gradient and the heat flux are computed according to

    .. math::

        \nabla T = \bar{\mathbf{B}}\;\mathbf{C}^{-1}\;\mathbf{a}^e

    .. math::

        \mathbf{q} = - \mathbf{D} \nabla T

    where the matrices :math:`\mathbf{D}`, :math:`\bar{\mathbf{B}}`, and :math:`\mathbf{C}` are described in ``flw2te``. Note that both the temperature gradient and the heat flux are constant in the element.
