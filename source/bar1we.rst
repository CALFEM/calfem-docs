.. _bar1we:
.. index:: 
   single: bar1we
   single: bar element
   single: elastic support
   single: 1D bar
   single: foundation
   pair: finite element; bar
   pair: structural; element
   pair: elastic; support
   pair: 1D; element
   pair: foundation; stiffness

bar1we
^^^^^^

:Purpose:

    Compute element stiffness matrix for a one dimensional bar element with elastic support.

    .. only:: html
        
        .. figure:: images/bar1w_1.svg
            :align: center
            :width: 400px

    .. only:: latex

        .. figure:: images/bar1w_1.svg
            :align: center
            :width: 70%

:Syntax:

.. only:: matlab

    .. code:: matlab

        Ke = bar1we(ex, ep)
        [Ke, fe] = bar1we(ex, ep, eq)

.. only:: python

    .. code-block:: python

        Ke = cfc.bar1we(ex, ep)
        Ke, fe = cfc.bar1we(ex, ep, eq)

:Description:

    :code:`bar1we` provides the element stiffness matrix :math:`\bar{\mathbf{K}}^e` for a one dimensional bar element with elastic support.

    The input variables

    :code:`ex`:math:`= [x_1\;\; x_2]` 
    :math:`\qquad` 
    :code:`ep`:math:`= [E\; A\; k_{\bar{x}}]`

    supply the element nodal coordinates :math:`x_1` and :math:`x_2`, the modulus of elasticity :math:`E`, the cross section area :math:`A` and the stiffness of the axial springs :math:`k_{\bar{x}}`.

    The element load vector :math:`\bar{\mathbf{f}}_l^e` can also be computed if a uniformly distributed load is applied to the element.
       
    The optional input variable

    :code:`eq`:math:`= [q_{\bar{x}}]`

    contains the distributed load per unit length, :math:`q_{\bar{x}}`.

    .. only:: html

        .. figure:: images/bar1e_2.svg
            :align: center
            :width: 400px

    .. only:: latex

        .. figure:: images/bar1e_2.svg
            :align: center
            :width: 70%

    Bar element with distributed load

:Theory:

    The element stiffness matrix :math:`\bar{\mathbf{K}}^e`, stored in ``Ke``, is computed according to

    .. math::

        \bar{\mathbf{K}}^e = \bar{\mathbf{K}}^e_0 + \bar{\mathbf{K}}^e_s

    where

    .. math::

        \bar{\mathbf{K}}^e_0 = \frac{D_{EA}}{L}
        \begin{bmatrix}
            1 & -1 \\
          -1 &  1
        \end{bmatrix}

    .. math::

        \bar{\mathbf{K}}^e_s = k_{\bar{x}} L
        \begin{bmatrix}
            \frac{1}{3} & \frac{1}{6} \\
            \frac{1}{6} & \frac{1}{3}
        \end{bmatrix}

    where the axial stiffness :math:`D_{EA}` and the length :math:`L` are given by

    .. math::

        D_{EA} = EA; \qquad L = x_2 - x_1

    The element load vector :math:`\bar{\mathbf{f}}_l^e`, stored in ``fe``, is computed according to

    .. math::

        \bar{\mathbf{f}}_l^e = \frac{q_{\bar{x}} L}{2}
        \begin{bmatrix}
            1 \\
            1
        \end{bmatrix}