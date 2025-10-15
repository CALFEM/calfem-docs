statcon
^^^^^^^

:Purpose:  

    Reduce system of equations by static condensation.

:Syntax:  

.. only:: matlab

    .. code:: matlab

        [K1, f1] = statcon(K, f, b)

.. only:: python

    .. code-block:: python

        K1, f1 = cfc.statcon(K, f, b)

:Description:  

    :code:`statcon` reduces a system of equations

    .. math::

        \mathbf{K}\;\mathbf{a} = \mathbf{f}

    by static condensation.

    The degrees of freedom to be eliminated are supplied to the function by the vector

    :code:`b`:math:`= \begin{bmatrix}
    dof_1 \\
    dof_2 \\
    \vdots \\
    dof_{nb}
    \end{bmatrix}`

    where each row in :code:`b` contains one degree of freedom to be eliminated.

    The elimination gives the reduced system of equations

    .. math::

        \mathbf{K}_1\;\mathbf{a}_1 = \mathbf{f}_1

    where :math:`\mathbf{K}_1` and :math:`\mathbf{f}_1` are stored in :code:`K1` and :code:`f1` respectively.
