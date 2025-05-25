dispbeam2
^^^^^^^^^

:Purpose:
    Draw the displacements for a two dimensional beam element.

:Syntax:
    .. code:: matlab

        [sfac] = dispbeam2(ex, ey, edi)
        [sfac] = dispbeam2(ex, ey, edi, plotpar)
        dispbeam2(ex, ey, edi, plotpar, sfac)

:Description:
    Input variables are the coordinate matrices :math:`ex` and :math:`ey`, see e.g. :math:`beam2e`, and the element displacements :math:`edi` obtained by e.g. :math:`beam2s`.

    The variable :math:`plotpar` sets plot parameters for linetype, linecolour and node marker:

    .. math::

        plotpar = [\, linetype \;\; linecolor \;\; nodemark \,]

    where

    .. list-table::
        :widths: 20 30 20 30
        :header-rows: 0

        *   - :math:`linetype = 1`
            - solid line
            - :math:`linecolor = 1`
            - black
        *   - 2
            - dashed line
            - 2
            - blue
        *   - 3
            - dotted line
            - 3
            - magenta
        *   - 
            - 
            - 4
            - red

    .. list-table::
        :widths: 20 30
        :header-rows: 0

        *   - :math:`nodemark = 1`
            - circle
        *   - 2
            - star
        *   - 0
            - no mark

    Default is dashed black lines with circles at nodes.

    The scale factor :math:`sfac` is a scalar that the element displacements are multiplied with to get a suitable geometrical representation. If :math:`sfac` is omitted in the input list, the scale factor is set automatically.