solveq
^^^^^^

:Purpose:

    Solve equation system.

:Syntax:

    .. code-block:: matlab

        a = solveq(K, f)
        a = solveq(K, f, bc)
        [a, r] = solveq(K, f, bc)

:Description:

    The function ``solveq`` solves the equation system

    .. math::

        \mathbf{K}\;\mathbf{a} = \mathbf{f}

    where :math:`\mathbf{K}` is a matrix and :math:`\mathbf{a}` and :math:`\mathbf{f}` are vectors.

    The matrix :math:`\mathbf{K}` and the vector :math:`\mathbf{f}` must be predefined. The solution of the system of equations is stored in a vector :math:`\mathbf{a}` which is created by the function.

    If some values of :math:`\mathbf{a}` are to be prescribed, the row number and the corresponding values are given in the boundary condition matrix

    .. math::

        \mathbf{bc} = \left[
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
        \right]

    where the first column contains the row numbers and the second column the corresponding prescribed values.

    If ``r`` is given in the function, support forces are computed according to

    .. math::

        \mathbf{r} = \mathbf{K}\;\mathbf{a} - \mathbf{f}

