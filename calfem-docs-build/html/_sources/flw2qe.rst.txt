flw2qe
^^^^^^


:Purpose:
     Compute element stiffness matrix for a quadrilateral heat flow element.

    .. figure:: images/f14.png
        :width: 70%
        :align: center

:Syntax:
    .. code-block:: matlab

        Ke = flw2qe(ex, ey, ep, D)
        [Ke, fe] = flw2qe(ex, ey, ep, D, eq)

:Description:
     ``flw2qe`` provides the element stiffness (conductivity) matrix ``Ke`` and
     the element load vector ``fe`` for a quadrilateral heat flow element.

     The element nodal coordinates :math:`x_1`, :math:`y_1`, :math:`x_2` etc,
     are supplied to the function by ``ex`` and ``ey``, the element thickness :math:`t`
     is supplied by ``ep`` and the thermal conductivities (or corresponding quantities)
     :math:`k_{xx}`, :math:`k_{xy}` etc are supplied by ``D``.

     .. math::

          \begin{array}{l}
          \mathbf{ex} = [\, x_1 \;\; x_2 \;\; x_3 \;\; x_4 \,] \\
          \mathbf{ey} = [\, y_1 \;\; y_2 \;\; y_3 \;\; y_4 \,]
          \end{array}
          \qquad
          \mathbf{ep} = \left[\, t \,\right]
          \qquad
          \mathbf{D} = \left[
                \begin{array}{cc}
                     k_{xx} & k_{xy} \\
                     k_{yx} & k_{yy}
                \end{array}
          \right]

     If the scalar variable ``eq`` is given in the function, the element load
     vector :math:`\mathbf{fe}` is computed, using

     .. math::

          \mathbf{eq} = \left[\, Q \,\right]

     where :math:`Q` is the heat supply per unit volume.

:Theory:
     In computing the element matrices, a fifth degree of freedom is introduced.
     The location of this extra degree of freedom is defined by the mean value of the coordinates in
     the corner points. Four sets of element matrices are calculated using
     ``flw2te``. These matrices are then assembled and the fifth degree of freedom is eliminated by static condensation.
