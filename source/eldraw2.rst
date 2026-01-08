.. _eldraw2:
.. index:: 
   single: eldraw2
   single: element drawing
   single: mesh visualization
   single: undeformed mesh
   single: 2D visualization
   pair: visualization; elements
   pair: finite element; plotting
   pair: mesh; drawing
   pair: 2D; visualization

eldraw2
^^^^^^^

:Purpose:
    Draw the undeformed mesh for a two dimensional structure.


:Syntax:
.. only:: matlab

    .. code:: matlab

        eldraw2(Ex, Ey)
        eldraw2(Ex, Ey, plotpar)
        eldraw2(Ex, Ey, plotpar, elnum)

.. only:: python

    .. code-block:: python

        cfv.eldraw2(Ex, Ey)
        cfv.eldraw2(Ex, Ey, plotpar)
        cfv.eldraw2(Ex, Ey, plotpar, elnum)

:Description:
    :code:`eldraw2` displays the undeformed mesh for a two dimensional structure.

    Input variables are the coordinate matrices :code:`Ex` and :code:`Ey` formed by the function :code:`coordxtr`.

    The variable :code:`plotpar` sets plot parameters for linetype, linecolor and node marker:

    :code:`plotpar`:math:`= [\, \text{linetype} \;\; \text{linecolor} \;\; \text{nodemark} \,]`
    
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

    Default is solid black lines with circles at nodes.

    Element numbers can be displayed at the center of the element if a column vector :code:`elnum` with the element numbers is supplied. This column vector can be derived from the element topology matrix :code:`Edof`:

    :code:`elnum = \texttt{Edof}(:,1)`

    i.e. the first column of the topology matrix.

:Limitations:
    Supported elements are bar, beam, triangular three node, and quadrilateral four node elements.
