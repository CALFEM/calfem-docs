eldisp2
^^^^^^^

:Purpose:
    Draw the deformed mesh for a two dimensional structure.


:Syntax:
    .. code:: matlab

        [sfac] = eldisp2(Ex, Ey, Ed)
        [sfac] = eldisp2(Ex, Ey, Ed, plotpar)
        eldisp2(Ex, Ey, Ed, plotpar, sfac)

:Description:
    :math:`\text{eldisp2}` displays the deformed mesh for a two dimensional structure.

    Input variables are the coordinate matrices :math:`\text{Ex}` and :math:`\text{Ey}` formed by the function :math:`\text{coordxtr}`, and the element displacements :math:`\text{Ed}` formed by the function :math:`\text{extract}`.

    The variable :math:`\text{plotpar}` sets plot parameters for linetype, linecolor and node marker:

    .. math::

        \text{plotpar} = [\, \text{linetype} \quad \text{linecolor} \quad \text{nodemark} \,]

    where

    .. list-table::
        :widths: 20 30 20 30
        :header-rows: 1

        * - linetype
          - line style
          - linecolor
          - color
        * - 1
          - solid line
          - 1
          - black
        * - 2
          - dashed line
          - 2
          - blue
        * - 3
          - dotted line
          - 3
          - magenta
        * -
          -
          - 4
          - red

    .. list-table::
        :widths: 20 30
        :header-rows: 1

        * - nodemark
          - marker
        * - 1
          - circle
        * - 2
          - star
        * - 0
          - no mark

    Default is dashed black lines with circles at nodes.

    The scale factor :math:`\text{sfac}` is a scalar that the element displacements are multiplied with to get a suitable geometrical representation. The scale factor is set automatically if it is omitted in the input list.

:Limitations:
    Supported elements are bar, beam, triangular three node, and quadrilateral four node elements.
