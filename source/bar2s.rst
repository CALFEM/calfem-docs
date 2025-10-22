.. _bar2s:
.. index:: 
   single: bar2s
   single: bar stress
   single: normal force
   single: 2D bar stress
   single: axial force
   pair: finite element; stress
   pair: bar; stress
   pair: post-processing; stress
   pair: 2D; stress

bar2s
^^^^^


:Purpose:
    Compute normal force in a two dimensional bar element.

     .. only:: html
          
          .. figure:: images/bar2s.svg
               :align: center
               :width: 400px

     .. only:: latex

          .. figure:: images/bar2s.svg
               :align: center
               :width: 70%

:Syntax:

.. only:: matlab

    .. code:: matlab

        es = bar2s(ex, ey, ep, ed)
        es = bar2s(ex, ey, ep, ed, eq)
        [es, edi] = bar2s(ex, ey, ep, ed, eq, n)
        [es, edi, eci] = bar2s(ex, ey, ep, ed, eq, n)

.. only:: python

    .. code-block:: python

        es = cfc.bar2s(ex, ey, ep, ed)
        es = cfc.bar2s(ex, ey, ep, ed, eq)
        es, edi = cfc.bar2s(ex, ey, ep, ed, eq, n)
        es, edi, eci = cfc.bar2s(ex, ey, ep, ed, eq, n)    

:Description:
     :code:`bar2s` computes the normal force in the two dimensional bar element :code:`bar2e`.

     The input variables :code:`ex`, :code:`ey`, and :code:`ep` are defined in :code:`bar2e` and the element nodal displacements, stored in :code:`ed`, are obtained by the function :code:`extract_ed`. If distributed loads are applied to the element, the variable :code:`eq` must be included.
     The number of evaluation points for section forces and displacements are determined by :code:`n`. If :code:`n` is omitted, only the ends of the bar are evaluated.

     The output variables

     :code:`es`:math:`= \begin{bmatrix}
     N(0) \\
     N(\bar{x}_2) \\
     \vdots \\
     N(\bar{x}_{n-1}) \\
     N(L)
     \end{bmatrix}` 
     :math:`\qquad`
     :code:`edi`:math:`= \begin{bmatrix}
     u(0) \\
     u(\bar{x}_2) \\
     \vdots \\
     u(\bar{x}_{n-1}) \\
     u(L)
     \end{bmatrix}` 
     :math:`\qquad` 
     :code:`eci`:math:`= \begin{bmatrix}
     0 \\
     \bar{x}_2 \\
     \vdots \\
     \bar{x}_{n-1} \\
     L
     \end{bmatrix}` 

     contain the normal force, the displacement, and the evaluation points on the local :math:`\bar{x}`-axis. :math:`L` is the length of the bar element.

:Theory:
     The nodal displacements in global coordinates

     .. math::

          \mathbf{a}^e = \begin{bmatrix} u_1 & u_2 & u_3 & u_4 \end{bmatrix}^T

     are also shown in :code:`bar2e`. The transpose of :math:`\mathbf{a}^e` is stored in :code:`ed`.

     The nodal displacements in local coordinates are given by

     .. math::

          \mathbf{\bar{a}}^e = \mathbf{G} \mathbf{a}^e

     where the transformation matrix :math:`\mathbf{G}` is defined in :code:`bar2e`.

     The displacement :math:`u(\bar{x})` and the normal force :math:`N(\bar{x})` are computed from

     .. math::

          u(\bar{x}) = \mathbf{N} \mathbf{\bar{a}}^e + u_p(\bar{x})

     .. math::

          N(\bar{x}) = D_{EA} \mathbf{B} \mathbf{\bar{a}}^e + N_p(\bar{x})

     where

     .. math::

          \mathbf{N} = \begin{bmatrix} 1 & \bar{x} \end{bmatrix} \mathbf{C}^{-1}
          = \begin{bmatrix} 1-\frac{\bar{x}}{L} & \frac{\bar{x}}{L} \end{bmatrix}

     .. math::

          \mathbf{B} = \begin{bmatrix} 0 & 1 \end{bmatrix} \mathbf{C}^{-1}
          = \frac{1}{L} \begin{bmatrix} -1 & 1 \end{bmatrix}

     .. math::

          u_p(\bar{x}) = -\frac{q_{\bar{x}}}{D_{EA}}\left(\frac{\bar{x}^2}{2}-\frac{L\bar{x}}{2}\right)

     .. math::

          N_p(\bar{x}) = -q_{\bar{x}}\left(\bar{x}-\frac{L}{2}\right)

     where :math:`D_{EA}`, :math:`L`, :math:`q_{\bar{x}}` are defined in :code:`bar2e` and

     .. math::

          \mathbf{C}^{-1} = \begin{bmatrix} 1 & 0 \\ -\frac{1}{L} & \frac{1}{L} \end{bmatrix}
