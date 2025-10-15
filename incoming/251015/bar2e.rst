bar2e
^^^^^

:Purpose:
    Compute element stiffness matrix for a two dimensional bar element.

    .. figure:: images/bar2e.png
        :align: center
        :width: 71%

:Syntax:

.. only:: matlab

    .. code-block:: matlab

        Ke = bar2e(ex, ey, ep)
        [Ke, fe] = bar2e(ex, ey, ep, eq)

.. only:: python

    .. code-block:: python

        Ke = cfc.bar2e(ex, ey, ep)
        Ke, fe = cfc.bar2e(ex, ey, ep, eq)

:Description:
    :code:`bar2e` provides the global element stiffness matrix :math:`{\mathbf{K}}^e` for a two dimensional bar element.

    The input variables

    :code:`ex`:math:`= [x_1 \;\; x_2]`
    :math:`\qquad` 
    :code:`ey`:math:`= [y_1 \;\; y_2]`
    :math:`\qquad` 
    :code:`ep`:math:`=  [E \; A]`

    supply the element nodal coordinates :math:`x_1`, :math:`y_1`, :math:`x_2`, and :math:`y_2`, the modulus of elasticity :math:`E`, and the cross section area :math:`A`.

    The element load vector :math:`{\mathbf{f}}_l^e` can also be computed if a uniformly distributed load is applied to the element.
    The optional input variable

    :code:`eq`:math:`= [q_{\bar{x}}]`

    contains the distributed load per unit length, :math:`q_{\bar{x}}`.
    
    .. figure:: images/bar2e_2.png
        :align: center
        :width: 70%

:Theory:
    The element stiffness matrix :math:`\mathbf{K}^e`, stored in :code:`Ke`, is computed according to

    .. math::

        \mathbf{K}^e = \mathbf{G}^T \; \bar{\mathbf{K}}^e \; \mathbf{G}

    where

    .. math::

        \bar{\mathbf{K}}^e = \frac{D_{EA}}{L}
        \begin{bmatrix}
        1 & -1 \\
        -1 & 1
        \end{bmatrix}
        \qquad
        \mathbf{G} =
        \begin{bmatrix}
        n_{x\bar{x}} & n_{y\bar{x}} & 0 & 0 \\
        0 & 0 & n_{x\bar{x}} & n_{y\bar{x}}
        \end{bmatrix}

    where the axial stiffness :math:`D_{EA}` and the length :math:`L` are given by

    .. math::

        D_{EA} = EA; \qquad L = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}

    and the transformation matrix :math:`\mathbf{G}` contains the direction cosines

    .. math::

        n_{x\bar{x}} = \frac{x_2 - x_1}{L} \qquad n_{y\bar{x}} = \frac{y_2 - y_1}{L}

    The element load vector :math:`\mathbf{f}_l^e`, stored in :code:`fe`, is computed according to

    .. math::

        \mathbf{f}_l^e = \mathbf{G}^T \; \bar{\mathbf{f}}_l^e

    where

    .. math::

        \bar{\mathbf{f}}_l^e = \frac{q_{\bar{x}} L}{2}
        \begin{bmatrix}
        1 \\
        1
        \end{bmatrix}