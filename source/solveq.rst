.. _solveq:
.. index:: 
   single: solveq
   single: equation solver
   single: linear system
   single: boundary conditions
   pair: finite element; solver
   pair: linear algebra; solver
   pair: boundary conditions; enforcement
   pair: system; solution

solveq
^^^^^^

:Purpose:

    Solve equation system.

:Syntax:

.. only:: matlab

    .. code-block:: matlab

        a = solveq(K, f)
        a = solveq(K, f, bcP, bc)
        [a, r] = solveq(K, f, bc)

.. only:: python

    .. code-block:: python

        a = cfc.solveq(K, f)
        a = cfc.solveq(K, f, bcPrescr, bcVal)
        a, r = cfc.solveq(K, f, bcPrescr, bcVal)

:Description:

    The function :code:`solveq` solves the equation system

    .. math::

        \mathbf{K}\;\mathbf{a} = \mathbf{f}

    where :math:`\mathbf{K}` is a matrix and :math:`\mathbf{a}` and :math:`\mathbf{f}` are vectors.

    The matrix :math:`\mathbf{K}` and the vector :math:`\mathbf{f}` must be predefined. The solution of the system of equations is stored in a vector :math:`\mathbf{a}` which is created by the function.

    .. only:: matlab

        If some values of :math:`\mathbf{a}` are to be prescribed, the row number and the corresponding values are given in the boundary condition matrix

        :code:`bc`:math:`= \left[
        \begin{array}{c}
        dof_1 \\
        dof_2 \\
        \vdots \\
        dof_{nbc}
        \end{array}
        \quad
        \begin{array}{c}
        u_1 \\
        u_2 \\
        \vdots \\
        u_{nbc}
        \end{array}
        \right]`

        where the first column contains the row numbers and the second column the corresponding prescribed values.

    .. only:: python

        If some values of :math:`\mathbf{a}` are to be prescribed, the row number and the corresponding values are given in the boundary condition matrices

        :code:`bcPresc`:math:`= \left[
        \begin{array}{c}
        dof_1 \\
        dof_2 \\
        \vdots \\
        dof_{nbc}
        \end{array}
        \right]`
        :math:`\qquad`
        :code:`bcVal`:math:`= \left[
        \begin{array}{c}
        u_1 \\
        u_2 \\
        \vdots \\
        u_{nbc}
        \end{array}
        \right]`

        where :code:`bcPresc` contains the row numbers and :code:`bcVal` the corresponding prescribed values. If :code:`bcVal` is omitted, all prescribed values are assumed to be 0.

    If ``r`` is given in the function, support forces are computed according to

    :code:`r`:math:`= \mathbf{K}\;\mathbf{a} - \mathbf{f}`

