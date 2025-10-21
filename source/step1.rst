.. _step1:
.. index:: 
   single: step1
   single: time integration
   single: first order differential equations
   single: dynamic analysis
   single: time stepping
   pair: dynamics; time integration
   pair: differential equations; first order
   pair: numerical; integration
   pair: time; stepping

step1
^^^^^

:Purpose:

    Compute the dynamic solution to a set of first order differential equations.

:Syntax:

    .. code-block:: matlab

        [a,da] = step1(K, C, f, a0, bc, ip)
        [a,da] = step1(K, C, f, a0, bc, ip, times)
        [a,da, ahist, dahist] = step1(K, C, f, a0, bc, ip, times, dofs)

:Description:

    ``step1`` computes at equal time steps the solution to a set of first order differential equations of the form:

    .. math::

        \mathbf{C} \dot{\mathbf{a}} + \mathbf{K}\mathbf{a} = \mathbf{f}(x, t), \\
        \mathbf{a}(0) = \mathbf{a}_0

    The command solves transient field problems. In the case of heat conduction, ``K`` and ``C`` represent the :math:`n \times n` conductivity and capacity matrices, respectively. ``a`` is the temperature and ``da`` (i.e., :math:`\dot{\mathbf{a}}`) is the time derivative of the temperature.

    The matrix ``f`` contains the time-dependent load vectors. If no external loads are active, use ``[]`` for ``f``. The matrix ``f`` is organized as follows:

    .. code-block:: matlab

        f = [
        time history of the load at dof_1
        time history of the load at dof_2
        ...
        time history of the load at dof_n
        ]

    The dimension of ``f`` is:

        (number of degrees-of-freedom) × (number of timesteps + 1)

    The initial conditions are given by the vector ``a0`` containing initial values of ``a``.

    The matrix ``bc`` contains the time-dependent prescribed values of the field variable ``a``. If no field variables are prescribed, use ``[]`` for ``bc``. The matrix ``bc`` is organized as follows:

    .. code-block:: matlab

        bc = [
        dof_1   time history of the field variable
        dof_2   time history of the field variable
        ...
        dof_m2  time history of the field variable
        ]

    The dimension of ``bc`` is:

        (number of dofs with prescribed field values) × (number of timesteps + 2)

    The time integration procedure is governed by the parameters given in the vector ``ip`` defined as:

    .. code-block:: matlab

        ip = [dt, T, alpha]

    where ``dt`` specifies the length of the time increment, ``T`` is the total time, and ``alpha`` is the time integration constant. Frequently used values of ``alpha`` are:

    .. list-table::
        :header-rows: 1

        * - alpha
          - Method
        * - 0
          - Forward difference; forward Euler
        * - 0.5
          - Trapezoidal rule; Crank-Nicholson
        * - 1
          - Backward difference; backward Euler

    The computed values of ``a`` and ``da`` are stored in ``a`` and ``da``, respectively. The first column contains the initial values, and the following columns contain the values for each time step. The dimension is:

        (number of degrees-of-freedom) × (number of time steps + 1)

    If the values are to be stored only for specific times, the parameter ``times`` specifies at which times the solution will be stored. The values are stored in ``a`` and ``da``, one column for each requested time according to ``times``. The dimension is then:

        (number of degrees-of-freedom) × (number of requested times + 1)

    If the history is to be stored in ``ahist`` and ``dahist`` for some degrees of freedom, the parameter ``dofs`` specifies for which degrees of freedom the history is to be stored. The computed time histories are stored in ``ahist`` and ``dahist``, respectively, with one row for each requested degree of freedom. The dimension is:

        (number of specified degrees of freedom) × (number of timesteps + 1)

    The time history functions can be generated using the command ``gfunc``. If all the values of the time histories of ``f`` or ``bc`` are kept constant, these values need to be stated only once. In this case, the number of columns in ``f`` is one and in ``bc`` two.

    In most cases, only a few degrees-of-freedom are affected by the exterior load, and hence the matrix contains only a few non-zero entries. In such cases, it is possible to save space by defining ``f`` as ``sparse`` (a MATLAB built-in function).

    .. note::
        Reference: Bathe, K.J.: *Finite Element Procedures in Engineering Analysis*, Prentice-Hall, Englewood Cliffs, New Jersey, pp. 511-514, 1982.
