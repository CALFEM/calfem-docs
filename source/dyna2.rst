.. _dyna2:
.. index:: dyna2, dynamic analysis, differential equations

dyna2
^^^^^

Compute the dynamic solution to a set of uncoupled second-order differential equations.

:Syntax:

   .. code:: matlab
      
      X = dyna2(w2, xi, f, g, dt)

:Description:

   ``dyna2`` computes the solution to the set

   .. math::

      \ddot{x}_i + 2 \xi_i \omega_i \dot{x}_i + \omega^{2}_i x_i = f_i g(t), \qquad i=1,\ldots,m

   of differential equations, where :math:`g(t)` is a piecewise linear time function.

   The vectors ``w2``, ``xi``, and ``f`` contain the squared circular frequencies :math:`\omega_i^2`, the damping ratios :math:`\xi_i`, and the applied forces :math:`f_i`, respectively.

   The vector ``g`` defines the load function in terms of straight line segments between equally spaced points in time. This function may have been formed by the command ``gfunc``.

   The dynamic solution is computed at equal time increments defined by ``dt``. Including the initial zero vector as the first column vector, the result is stored in the :math:`m \times n` matrix ``X``, where :math:`n-1` is the number of time steps.

.. note:: 
   
   The accuracy of the solution is *not* a function of the output time increment ``dt``, since the command produces the exact solution for straight line segments in the loading time function.

:See also:

   :ref:`gfunc`
