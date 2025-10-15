dispbeam2
^^^^^^^^^

:Purpose:
    Draw the displacements for a two dimensional beam element.

:Syntax:
 .. only:: matlab

   .. code:: matlab

        [sfac] = dispbeam2(ex, ey, edi)
        [sfac] = dispbeam2(ex, ey, edi, plotpar)
        dispbeam2(ex, ey, edi, plotpar, sfac)

.. only:: python

    .. code-block:: python

        sfac = cfc.dispbeam2(ex, ey, edi)
        sfac = cfc.dispbeam2(ex, ey, edi, plotpar)
        cfc.dispbeam2(ex, ey, edi, plotpar, sfac)

:Description:
    Input variables are the coordinate matrices :code:`ex` and :code:`ey`, see e.g. :code:`beam2e`, and the element displacements :code:`edi` obtained by e.g. :code:`beam2s`.

    The variable :code:`plotpar` sets plot parameters for linetype, linecolour and node marker:

    :code:`plotpar`:math:`= [\, linetype \;\; linecolor \;\; nodemark \,]`

    where

    .. list-table::
        :widths: 20 30 20 30 20 30
        :header-rows: 1

        * - :math:`linetype`
          - 
          - :math:`linecolor`
          - 
          - :math:`nodemark`
          - 
        * - 1
          - solid line
          - 1
          - black
          - 1
          - circle
        * - 2
          - dashed line
          - 2
          - blue
          - 2
          - asterisk
        * - 3
          - dotted line
          - 3
          - magenta
          - 0
          - no mark
        * -
          -
          - 4
          - red
          -
          -

    Default is dashed black lines with circles at nodes.

    The scale factor :code:`sfac` is a scalar that the element displacements are multiplied with to get a suitable geometrical representation. If :code:`sfac` is omitted in the input list, the scale factor is set automatically.