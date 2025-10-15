eldisp2
^^^^^^^

:Purpose:
    Draw the deformed mesh for a two dimensional structure.


:Syntax:
.. only:: matlab

    .. code-block:: matlab

        [sfac] = eldisp2(Ex, Ey, Ed)
        [sfac] = eldisp2(Ex, Ey, Ed, plotpar)
        eldisp2(Ex, Ey, Ed, plotpar, sfac)

.. only:: python

    .. code-block:: python

        sfac = cfc.eldisp2(Ex, Ey, Ed)
        sfac = cfc.eldisp2(Ex, Ey, Ed, plotpar)
        cfc.eldisp2(Ex, Ey, Ed, plotpar, sfac)

:Description:
    :code:`eldisp2` displays the deformed mesh for a two dimensional structure.

    Input variables are the coordinate matrices :code:`Ex` and :code:`Ey` formed by the function :code:`coordxtr`, and the element displacements :code:`Ed` formed by the function :code:`extract_ed`.

    The variable :code:`plotpar` sets plot parameters for linetype, linecolor and node marker:

    :code:`plotpar`:math:`= [\, linetype \quad linecolor \quad nodemark \,]`

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

    The scale factor :code:`sfac` is a scalar that the element displacements are multiplied with to get a suitable geometrical representation. The scale factor is set automatically if it is omitted in the input list.

:Limitations:
    Supported elements are bar, beam, triangular three node, and quadrilateral four node elements.
