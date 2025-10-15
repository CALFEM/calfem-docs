dyna2f
^^^^^^

:Purpose:

    Compute the dynamic solution to a set of uncoupled second-order differential equations.

:Syntax:

    .. code-block:: matlab

        Y = dyna2f(w2, xi, f, p, dt)

:Description:

    ``dyna2f`` computes the solution to the set of differential equations:

    .. math::

        \ddot{x}_i + 2 \xi_i\omega_i \dot{x}_i + \omega^{2}_i x_i = f_i g(t), \qquad i=1,\ldots,m

    The vectors ``w2``, ``xi`` and ``f`` are the squared circular frequencies :math:`\omega_i^2`, the damping ratios :math:`\xi_i`, and the applied forces :math:`f_i`, respectively. The force vector ``p`` contains the Fourier coefficients :math:`p(k)` formed by the command ``fft``.

    The solution in the frequency domain is computed at equal time increments defined by ``dt``. The result is stored in the :math:`m \times n` matrix ``Y``, where ``m`` is the number of equations and ``n`` is the number of frequencies resulting from the ``fft`` command. The dynamic solution in the time domain is achieved by the use of the command ``ifft``.

:Example:

    The dynamic solution to a set of uncoupled second-order differential equations can be computed by the following sequence of commands:

    .. code-block:: matlab

        >> g = gfunc(G, dt);
        >> p = fft(g);
        >> Y = dyna2f(w2, xi, f, p, dt);
        >> X = (real(ifft(Y.')))';

    where it is assumed that the input variables ``G``, ``dt``, ``w2``, ``xi`` and ``f`` are properly defined. Note that the ``ifft`` command operates on column vectors if ``Y`` is a matrix; therefore use the transpose of ``Y``. The output from the ``ifft`` command is complex. Therefore use ``Y.'`` to transpose rows and columns in ``Y`` in order to avoid the complex conjugate transpose of ``Y``.

    The time response is represented by the real part of the output from the ``ifft`` command. If the transpose is used and the result is stored in a matrix ``X``, each row will represent the time response for each equation as the output from the command ``dyna2``.

:See also:

    :ref:`gfunc`, :ref:`fft`, :ref:`ifft`
