scalgraph2
^^^^^^^^^^

:Purpose:
    Draw a graphic scale.


:Syntax:
    .. code:: matlab

        scalgraph2(sfac, magnitude)
        scalgraph2(sfac, magnitude, plotpar)

:Description:
    ``scalgraph2`` draws a graphic scale to visualize the magnitude of displayed computational results. The input variable :math:`\mathit{sfac}` is a scale factor determined by the function ``scalfact2``. The variable :math:`\mathit{magnitude}` is defined as :math:`[S\;\;x\;\;y]`, where :math:`S` specifies the value corresponding to the length of the graphic scale, and :math:`(x, y)` are the coordinates of the starting point. If no coordinates are given, the starting point will be :math:`(0, -0.5)`.

:Theory:
    The variable ``plotpar`` sets the graphic scale color:

    :math:`\mathrm{plotpar} = [\mathrm{color}]`

    where

    .. list-table::
        :widths: 10 20
        :header-rows: 0

        * - :math:`\mathrm{color} = 1`
          - black
        * - 2
          - blue
        * - 3
          - magenta
        * - 4
          - red