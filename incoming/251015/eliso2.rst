eliso2
^^^^^^

:Purpose:
    Display element iso lines for two dimensional elements.

:Syntax:
.. only:: matlab

    .. code-block:: matlab

        eliso2(Ex, Ey, Ed, isov)
        eliso2(Ex, Ey, Ed, isov, plotpar)

.. only:: python

    .. code-block:: python

        cfc.eliso2(Ex, Ey, Ed, isov)
        cfc.eliso2(Ex, Ey, Ed, isov, plotpar)

:Description:
    :code:`eliso2` displays element iso lines for a number of elements of the same type.
    Note that only the iso lines are displayed. To display the element mesh, use :code:`eldraw2`.

    Input variables are the coordinate matrices :code:`Ex` and :code:`Ey` formed by the function :code:`coordxtr`,
    and the element nodal quantities (e.g., displacement or energy potential) matrix :code:`Ed` defined in :code:`extract`.

    If :code:`isov` is a scalar, it determines the number of iso lines to be displayed.
    If :code:`isov` is a vector, it determines the values of the iso lines to be displayed
    (number of iso lines equal to the length of vector :code:`isov`):

    :code:`isov`:math:`= [\, \text{iso lines} \,]`

    :code:`isov`:math:`= [\, \text{isovalue}(1) \; \ldots \; \text{isovalue}(n) \,]`

    The variable :code:`plotpar` sets plot parameters for the iso lines:

    :code:`plotpar`:math:`= [\, linetype \;\; linecolor \;\; textfcn \,]`

    where

    .. list-table::
        :widths: 20 30 20 30 20 60
        :header-rows: 1

        * - :math:`linetype`
          - 
          - :math:`linecolor`
          -
          - :math:`textfcn`
          - 
        * - 1
          - solid line
          - 1
          - black
          - 0
          - iso values not printed
        * - 2
          - dashed line
          - 2
          - blue
          - 1
          - iso values printed at the iso lines
        * - 3
          - dotted line
          - 3
          - magenta
          - 1
          - iso values printed where the cursor indicates
        * -
          -
          - 4
          - red
          -
          -

    Default is solid, black lines and no iso values printed.

:Limitations:
    Supported elements are triangular 3 node and quadrilateral 4 node elements.
