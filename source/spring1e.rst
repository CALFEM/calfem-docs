.. _spring1e:
.. index:: 
   single: spring1e
   single: spring element
   single: elastic spring
   single: simple element
   pair: finite element; spring
   pair: structural; element
   pair: stiffness; matrix
   pair: elastic; element

spring1e
^^^^^^^^

:Purpose:
    Compute element stiffness matrix for a spring element.

    .. only:: html
        
        .. figure:: images/SPRING1.svg
            :align: center
            :width: 400px
    
    .. only:: latex
        
        .. figure:: images/SPRING1.svg
            :align: center
            :width: 70%

:Syntax:

    .. only:: matlab

        .. code-block:: matlab

            Ke = spring1e(ep)

    .. only:: python

        .. code-block:: python

            Ke = cfc.spring1e(ep)

:Description:
    :code:`spring1e` provides the element stiffness matrix :math:`\bar{\mathbf{K}}^e` for a spring element.

    The input variable

    :code:`ep`:math:`= [k]`

    supplies the spring stiffness :math:`k` or the analog quantity defined in Table :ref:`tanalog`.

:Theory:
    The element stiffness matrix :math:`\mathbf{K}^e`, stored in :code:`Ke`, is computed according to

    .. math::

        \mathbf{K}^e = \begin{bmatrix}
            k & -k \\
            -k & k
        \end{bmatrix}

    where :math:`k` is defined by :code:`ep`.
