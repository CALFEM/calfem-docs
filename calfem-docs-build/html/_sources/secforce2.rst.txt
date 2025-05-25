secforce2
^^^^^^^^^

:Purpose:
    Draw the section force diagrams of a two dimensional bar or beam element in its global position.

:Syntax:
    .. code:: matlab

        secforce2(ex, ey, es, plotpar, sfac)
        secforce2(ex, ey, es, plotpar, sfac, eci)
        [sfac] = secforce2(ex, ey, es)
        [sfac] = secforce2(ex, ey, es, plotpar)

:Description:
    The input variables :math:`\mathtt{ex}` and :math:`\mathtt{ey}` are defined in :math:`\mathtt{bar2e}` or :math:`\mathtt{beam2e}`. The input variable

    .. math::

        \mathtt{es} = \begin{bmatrix} S_1 \\ S_2 \\ \vdots \\ S_n \end{bmatrix}

    consists of a column matrix that contains section forces. The values in :math:`\mathtt{es}` are computed in, e.g., :math:`\mathtt{bar2s}` or :math:`\mathtt{beam2s}`.

    The variable :math:`\mathtt{plotpar}` sets plot parameters for the diagram:

    .. math::

        \mathtt{plotpar} = [\, \text{linecolor} \;\; \text{elementcolor} \,]

    where

    .. list-table::
        :widths: 20 30 20 30
        :header-rows: 1

        * - linecolor
          - color
          - elementcolor
          - color
        * - 1
          - black
          - 1
          - black
        * - 2
          - blue
          - 2
          - blue
        * - 3
          - magenta
          - 3
          - magenta
        * - 4
          - red
          - 4
          - red

    The scale factor :math:`\mathtt{sfac}` is a scalar that the section forces are multiplied with to get a suitable graphical representation. If :math:`\mathtt{sfac}` is omitted in the input list, the scale factor is set automatically.

    The input variable

    .. math::

        \mathtt{eci} = \begin{bmatrix} \bar{x}_1 \\ \bar{x}_2 \\ \vdots \\ \bar{x}_n \end{bmatrix}

    specifies the local :math:`\bar{x}`-coordinates of the quantities in :math:`\mathtt{es}`. If :math:`\mathtt{eci}` is not given, uniform distance is assumed.