step2
^^^^^


:Purpose:

    Compute the dynamic solution to a set of second order differential equations.

:Syntax:

    .. code-block:: matlab

        [a, da, d2a] = step2(K, C, M, f, a0, da0, bc, ip)
        [a, da, d2a] = step2(K, C, M, f, a0, da0, bc, ip, times)
        [a, da, d2a, ahist, dahist, d2ahist] = step2(K, C, M, f, a0, da0, bc, ip, times, dofs)

:Description:

    ``step2`` computes at equal time steps the solution to a set of second order differential equations of the form:

    .. math::

        \mathbf{M} \ddot{\mathbf{a}} + \mathbf{C} \dot{\mathbf{a}} + \mathbf{K} \mathbf{a} = \mathbf{f}(x, t), \\
        \mathbf{a}(0) = \mathbf{a}_0, \\
        \dot{\mathbf{a}}(0) = \mathbf{v}_0.

    In structural mechanics problems, ``K``, ``C`` and ``M`` represent the :math:`n \times n` stiffness, damping and mass matrices, respectively. ``a`` is the displacement, ``da`` ( = :math:`\dot{\mathbf{a}}` ) is the velocity and ``d2a`` ( = :math:`\ddot{\mathbf{a}}` ) is the acceleration.

    The matrix ``f`` contains the time-dependent load vectors. If no external loads are active, use ``[]`` for ``f``. The matrix ``f`` is organized as:

    .. math::

        f = \begin{bmatrix}
        \text{time history of the load at } dof_1 \\
        \text{time history of the load at } dof_2 \\
        \vdots \\
        \text{time history of the load at } dof_n
        \end{bmatrix}

    The dimension of ``f`` is:

        (number of degrees-of-freedom) × (number of timesteps + 1)

    The initial conditions are given by the vectors ``a0`` and ``da0``, containing initial displacements and initial velocities.

    The matrix ``bc`` contains the time-dependent prescribed displacement. If no displacements are prescribed, use ``[]`` for ``bc``. The matrix ``bc`` is organized as:

    .. math::

        bc = \begin{bmatrix}
        dof_1 & \text{time history of the displacement} \\
        dof_2 & \text{time history of the displacement} \\
        \vdots & \vdots \\
        dof_{m_2} & \text{time history of the displacement}
        \end{bmatrix}

    The dimension of ``bc`` is:

        (number of dofs with prescribed displacement) × (number of timesteps + 2)

    The time integration procedure is governed by the parameters given in the vector ``ip`` defined as:

    .. math::

        ip = [dt, T, \alpha, \delta]

    where ``dt`` specifies the time increment, ``T`` the total time, and ``alpha`` and ``delta`` are time integration constants for the Newmark family of methods.

    Frequently used values:

    +---------------------+---------------------+-----------------------------------------------+
    | :math:`\alpha`      | :math:`\delta`      | Method                                        |
    +---------------------+---------------------+-----------------------------------------------+
    | :math:`\frac{1}{4}` | :math:`\frac{1}{2}` | Average acceleration (trapezoidal) rule       |
    +---------------------+---------------------+-----------------------------------------------+
    | :math:`\frac{1}{6}` | :math:`\frac{1}{2}` | Linear acceleration                           |
    +---------------------+---------------------+-----------------------------------------------+
    | 0                   | :math:`\frac{1}{2}` | Central difference                            |
    +---------------------+---------------------+-----------------------------------------------+

    The computed values of :math:`\mathbf{a}`, :math:`\dot{\mathbf{a}}` and :math:`\ddot{\mathbf{a}}` are stored in ``a``, ``da`` and ``d2a``, respectively. The first column contains the initial values and the following columns contain the values for each time step.

    The dimension of ``a``, ``da`` and ``d2a`` is:

        (number of degrees-of-freedom) × (number of time steps + 1)

    If the values are to be stored only for specific times, the parameter ``times`` specifies at which times the solution will be stored. The values are stored in ``a``, ``da`` and ``d2a``, one column for each requested time according to ``times``. The dimension is then:

        (number of degrees-of-freedom) × (number of requested times + 1)

    If the history is to be stored in ``ahist``, ``dahist`` and ``d2ahist`` for some degrees of freedom, the parameter ``dofs`` specifies for which degrees of freedom the history is to be stored. The computed time histories are stored in ``ahist``, ``dahist`` and ``d2ahist``, one row for each requested degree of freedom according to ``dofs``. The dimension is:

        (number of specified degrees of freedom) × (number of timesteps + 1)

    In most cases only a few degrees-of-freedom are affected by the exterior load, and hence the matrix contains only few non-zero entries. In such cases it is possible to save space by defining ``f`` as sparse (a MATLAB built-in function).

