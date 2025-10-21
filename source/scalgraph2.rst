.. _scalgraph2:
.. index:: 
   single: scalgraph2
   single: graphic scale
   single: scale bar
   single: visualization scale
   single: plot legend
   pair: visualization; scale
   pair: graphic; scale
   pair: plot; legend
   pair: 2D; scale

scalgraph2
^^^^^^^^^^

:Purpose:
    Draw a graphic scale.


:Syntax:
.. only:: matlab

    .. code-block:: matlab

        scalgraph2(sfac, magnitude)
        scalgraph2(sfac, magnitude, plotpar)

.. only:: python

    .. code-block:: python

        cfc.scalgraph2(sfac, magnitude)
        cfc.scalgraph2(sfac, magnitude, plotpar)

:Description:
    :code:`scalgraph2` draws a graphic scale to visualize the magnitude of displayed computational results. The input variable :code:`sfac` is a scale factor determined by the function :code:`scalfact2`. The variable :code:`magnitude` is defined as :math:`[S\;\;x\;\;y]`, where :math:`S` specifies the value corresponding to the length of the graphic scale, and :math:`(x, y)` are the coordinates of the starting point. If no coordinates are given, the starting point will be :math:`(0, -0.5)`.

:Theory:
    The variable :code:`plotpar` sets the graphic scale color:

    :code:`plotpar`:math:`= [color]`

    where

      .. list-table::
        :widths: 20 30
        :header-rows: 1

        * - :math:`color`
          - 
        * - 1
          - black
        * - 2
          - blue
        * - 3
          - magenta
        * - 4
          - red
