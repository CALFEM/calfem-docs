.. _bar2gs:
.. index:: 
   single: bar2gs
   single: geometric nonlinear stress
   single: bar stress
   single: 2D bar stress
   single: nonlinear stress
   single: axial force
   pair: finite element; stress
   pair: geometric; nonlinear
   pair: bar; stress
   pair: 2D; stress
   pair: nonlinear; stress

bar2gs
^^^^^^

:Purpose:
    Compute axial force and normal force in a two dimensional bar element.

    .. figure:: images/bar2s.png
        :align: center
        :width: 70%

:Syntax:

.. only:: matlab

    .. code:: matlab

        [es, Qx] = bar2gs(ex, ey, ep, ed)
        [es, Qx, edi] = bar2gs(ex, ey, ep, ed, n)
        [es, Qx, edi, eci] = bar2gs(ex, ey, ep, ed, n)

.. only:: python

    .. code-block:: python

        es, Qx = cfc.bar2gs(ex, ey, ep, ed)
        es, Qx, edi = cfc.bar2gs(ex, ey, ep, ed, n)
        es, Qx, edi, eci = cfc.bar2gs(ex, ey, ep, ed, n)    

:Description:
     :code:`bar2gs` computes the normal force in the two dimensional bar elements :code:`bar2ge`.

     The input variables :code:`ex`, :code:`ey`, and :code:`ep` are defined in :code:`bar2ge` and the element nodal displacements, stored in :code:`ed`, are obtained by the function :code:`extract_ed`. The number of evaluation points for section forces and displacements are determined by ``n``. If ``n`` is omitted, only the ends of the bar are evaluated.

     The output variable :code:`Qx` contains the axial force :math:`Q_{\bar{x}}` and the output variables

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

     contain the normal force, the displacement, and the evaluation points on the local :math:`\bar{x}`-axis.
     :math:`L` is the length of the bar element.

:Theory:
     The nodal displacements in global coordinates are given by

     .. math::

          \mathbf{a}^e = \left[\; u_1\;\; u_2\;\; u_3\;\; u_4 \;\right]^T

     The transpose of :math:`\mathbf{a}^e` is stored in :code:`ed`.
     The nodal displacements in local coordinates are given by

     .. math::

          \mathbf{\bar{a}}^e = \mathbf{G} \mathbf{a}^e

     where the transformation matrix :math:`\mathbf{G}` is defined in :code:`bar2ge`.
     The displacements associated with bar action are determined as

     .. math::

          {\mathbf{\bar{a}}}^e_{\text{bar}} = \left[ \begin{array}{r} \bar{u}_1 \\ \bar{u}_3 \end{array}\right]

     The displacement :math:`u(\bar{x})` and the normal force :math:`N(\bar{x})` are computed from

     .. math::

          u(\bar{x}) = {\mathbf{N}} \mathbf{\bar{a}}^e_{\text{bar}}

     .. math::

          N(\bar{x}) = D_{EA} \mathbf{B} \mathbf{\bar{a}}^e_{\text{bar}}

     where

     .. math::

          \mathbf{N} = \left[\begin{array}{rr} 1 & \bar{x} \end{array}\right] \mathbf{C}^{-1} = \left[\begin{array}{rr} 1-\frac{\bar{x}}{L} & \frac{\bar{x}}{L} \end{array}\right]

     .. math::

          \mathbf{B} = \left[\begin{array}{rr} 0 & 1 \end{array}\right] \mathbf{C}^{-1} = \frac{1}{L}\left[\begin{array}{rr} -1 & 1 \end{array}\right]

     where :math:`D_{EA}` and :math:`L` are defined in ``bar2ge`` and

     .. math::

          \mathbf{C}^{-1} = \left[ \begin{array}{rr} 1 & 0 \\ -\frac{1}{L} & \frac{1}{L} \end{array}\right]

     An updated value of the axial force is computed as

     .. math::

          Q_{\bar{x}} = N(0)
