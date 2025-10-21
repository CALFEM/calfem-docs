.. _beam2de:
.. index:: 
   single: beam2de
   single: dynamic beam element
   single: beam element
   single: mass matrix
   single: damping matrix
   single: 2D beam
   pair: finite element; beam
   pair: dynamic; beam
   pair: mass; matrix
   pair: damping; matrix
   pair: 2D; element

beam2de
^^^^^^^

:Purpose:

    Compute element stiffness, mass and damping matrices for a two dimensional beam element.

    .. figure:: images/BEAM2D.png
        :align: center
        :width: 70%

:Syntax:

.. only:: matlab

    .. code-block:: matlab

        [Ke, Me] = beam2de(ex, ey, ep)
        [Ke, Me, Ce] = beam2de(ex, ey, ep)

.. only:: python

    .. code-block:: python

        Ke, Me = cfc.beam2de(ex, ey, ep)
        Ke, Me, Ce = cfc.beam2de(ex, ey, ep)

:Description:

    :code:`beam2de` provides the global element stiffness matrix :math:`{\mathbf{K}}^e`, the global element mass matrix :math:`{\mathbf{M}}^e`, and the global element damping matrix :math:`{\mathbf{C}}^e`, for a two dimensional beam element.

    The input variables :code:`ex` and :code:`ey` are described in :code:`beam2e`, and

    :code:`ep`:math:`=  [ E,\; A,\; I,\; m,\; [a_0,\; a_1] ]`
    
    contains the modulus of elasticity :math:`E`, the cross section area :math:`A`, the moment of inertia :math:`I`, the mass per unit length :math:`m`, and the Rayleigh damping coefficients :math:`a_0` and :math:`a_1`.  
    If :math:`a_0` and :math:`a_1` are omitted, the element damping matrix :code:`Ce` is not computed.

:Theory:

    The element stiffness matrix :math:`\mathbf{K}^e`, the element mass matrix :math:`\mathbf{M}^e` and the element damping matrix :math:`\mathbf{C}^e`, stored in the variables :code:`Ke`, :code:`Me` and :code:`Ce`, respectively, are computed according to

    .. math::

        \mathbf{K}^e = \mathbf{G}^T \bar{\mathbf{K}}^e \mathbf{G} \qquad
        \mathbf{M}^e = \mathbf{G}^T \bar{\mathbf{M}}^e \mathbf{G} \qquad
        \mathbf{C}^e = \mathbf{G}^T \bar{\mathbf{C}}^e \mathbf{G}

    where :math:`\mathbf{G}` and :math:`\bar{\mathbf{K}}^e` are described in :code:`beam2e`.

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

