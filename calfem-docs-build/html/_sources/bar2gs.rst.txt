bar2gs
^^^^^^

:Purpose:
     Compute axial force and normal force in a two dimensional bar element.

    .. figure:: images/bar2s.png
        :align: center
        :width: 70%

:Syntax:
    .. code:: matlab

        [es, Qx] = bar2gs(ex, ey, ep, ed)
        [es, Qx] = bar2gs(ex, ey, ep, ed, eq)
        [es, Qx, edi] = bar2gs(ex, ey, ep, ed, eq, n)
        [es, Qx, edi, eci] = bar2gs(ex, ey, ep, ed, eq, n)

:Description:
     ``bar2gs`` computes the normal force in the two dimensional bar elements ``bar2g``.

     The input variables ``ex``, ``ey``, and ``ep`` are defined in ``bar2ge`` and the element nodal displacements, stored in ``ed``, are obtained by the function ``extract``. 
     The number of evaluation points for section forces and displacements are determined by ``n``. If ``n`` is omitted, only the ends of the bar are evaluated.

     The output variable ``Qx`` contains the axial force :math:`Q_{\bar{x}}` and the output variables

     .. math::

          \mathsf{es} =
          \left[
          \begin{array}{c}
          N(0)    \\
          N(\bar{x}_{2})\\
          \vdots  \\
          N(\bar{x}_{n-1})\\
          N(L) 
          \end{array}
            \right]
          \qquad
          \mathsf{edi} =
          \left[
          \begin{array}{c}
          {u}(0)    \\
          {u}(\bar{x}_{2})\\
          \vdots  \\
          {u}(\bar{x}_{n-1})\\
          {u}(L) 
          \end{array}
            \right]
          \qquad
          \mathsf{eci} =
          \left[
          \begin{array}{c}
          0  \\
          \bar x_{2} \\
          \vdots   \\
          \bar x_{n-1} \\
          L
          \end{array}
            \right]

     contain the normal force, the displacement, and the evaluation points on the local :math:`\bar{x}`-axis.
     :math:`L` is the length of the bar element.

:Theory:
     The nodal displacements in global coordinates are given by

     .. math::

          \mathbf{a}^e = \left[\; u_1\;\; u_2\;\; u_3\;\; u_4 \;\right]^T

     The transpose of :math:`\mathbf{a}^e` is stored in ``ed``.
     The nodal displacements in local coordinates are given by

     .. math::

          \mathbf{\bar{a}}^e = \mathbf{G} \mathbf{a}^e

     where the transformation matrix :math:`\mathbf{G}` is defined in ``bar2ge``.
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
