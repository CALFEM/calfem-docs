.. _beam1we:
.. index:: 
   single: beam1we
   single: beam element
   single: elastic support
   single: 1D beam
   single: foundation beam
   single: Winkler foundation
   pair: finite element; beam
   pair: structural; element
   pair: elastic; support
   pair: 1D; element
   pair: foundation; beam
   pair: Winkler; foundation

beam1we
^^^^^^^

:Purpose:

    Compute element stiffness matrix for a one dimensional beam element on elastic support.

    .. figure:: images/beam1w.png
        :align: center
        :width: 70%

:Syntax:

.. only:: matlab

    .. code-block:: matlab

        Ke = beam1we(ex, ep)
        [Ke, fe] = beam1we(ex, ep, eq)

.. only:: python

    .. code-block:: python

        Ke = cfc.beam1we(ex, ep)
        Ke, fe = cfc.beam1we(ex, ep, eq)

:Description:

    :code:`beam1we` provides the global element stiffness matrix :math:`{\mathbf{K}}^e` for a one dimensional beam element with elastic support.

    The input variables

    :code:`ex`:math:`= [x_1 \;\; x_2]`
    :math:`\qquad` 
    :code:`ep`:math:`=  [E\;\; I \;\; k_{\bar{y}}]`

    supply the element nodal coordinates :math:`x_1` and :math:`x_2`, the modulus of elasticity :math:`E`, the moment of inertia :math:`I`, and the spring stiffness in the transverse direction :math:`k_{\bar{y}}`.

    The element load vector :math:`{\mathbf{f}}_l^e` can also be computed if a uniformly distributed load is applied to the element. The optional input variable

    :code:`eq`:math:`= [q_{\bar{y}}]`

    contains the distributed load per unit length, :math:`q_{\bar{y}}`.

    .. figure:: images/beam1e_2.png
        :align: center

:Theory:

    The element stiffness matrix :math:`\bar{\mathbf{K}}^e`, stored in :code:`Ke`, is computed according to

    .. math::

        \bar{\mathbf{K}}^e = \bar{\mathbf{K}}^e_0 + \bar{\mathbf{K}}^e_s

    where

    .. math::

        \bar{\mathbf{K}}^e_0 = \frac{D_{EI}}{L^3}
        \begin{bmatrix}
            12 & 6L & -12 & 6L \\
            6L & 4L^2 & -6L & 2L^2 \\
            -12 & -6L & 12 & -6L \\
            6L & 2L^2 & -6L & 4L^2
        \end{bmatrix}

    and

    .. math::

        \bar{\mathbf{K}}^e_s = \frac{k_{\bar{y}} L}{420}
        \begin{bmatrix}
            156 & 22L & 54 & -13L \\
            22L & 4L^2 & 13L & -3L^2 \\
            54 & 13L & 156 & -22L \\
            -13L & -3L^2 & -22L & 4L^2
        \end{bmatrix}

    where the bending stiffness :math:`D_{EI}` and the length :math:`L` are given by

    .. math::

        D_{EI} = EI \qquad L = x_2 - x_1

    The element loads :math:`\bar{\mathbf{f}}_l^e` stored in the variable :code:`fe` are computed according to

    .. math::

        \bar{\mathbf{f}}_l^e = q_{\bar{y}}
        \begin{bmatrix}
            \dfrac{L}{2} \\
            \dfrac{L^2}{12} \\
            \dfrac{L}{2} \\
            -\dfrac{L^2}{12}
        \end{bmatrix}