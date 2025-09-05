spring1e
^^^^^^^^

:Purpose:
    Compute element stiffness matrix for a spring element.

    .. figure:: images/SPRING1.png
        :width: 70%
        :align: center

:Syntax:
    .. code:: matlab

        Ke = spring1e(ep)

:Description:
    :math:`\mathsf{spring1e}` provides the element stiffness matrix :math:`\bar{\mathbf{K}}^e` for a spring element.

    The input variable

    :math:`\mathsf{ep} = [\,k\,]`

    supplies the spring stiffness :math:`k` or the analog quantity defined in Table :ref:`tanalog`.

:Theory:
    The element stiffness matrix :math:`\mathbf{K}^e`, stored in :math:`\mathsf{Ke}`, is computed according to

    .. math::

        \mathbf{K}^e = \begin{bmatrix}
            k & -k \\
            -k & k
        \end{bmatrix}

    where :math:`k` is defined by :math:`\mathsf{ep}`.
