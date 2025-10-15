.. _gfunc:
.. index:: gfunc, dynamic analysis, time functions, interpolation

gfunc
^^^^^

:Purpose:  

    Form vector with function values at equally spaced points by linear interpolation.

    .. figure:: images/F32.png
        :width: 70%
        :align: center

        Piecewise linear time dependent function

:Syntax: 

    .. code:: matlab

        [t, g] = gfunc(G, dt)

:Description:  

    ``gfunc`` uses linear interpolation to compute values at equally spaced points for a discrete function :math:`g` given by

    .. math::

        G = \left[
        \begin{array}{cc}
        t_1 & g(t_1)\\
        t_2 & g(t_2)\\
        \vdots \\
        t_N & g(t_N)
        \end{array}
        \right],

    as shown in the figure above.

    Function values are computed in the range :math:`t_1 \leq t \leq t_N`, at equal increments, ``dt`` being defined by the variable ``dt``. The number of linear segments (steps) is :math:`(t_N-t_1)/dt`. The corresponding vector ``t`` is also computed. The result can be plotted by using the command ``plot(t, g)``.
