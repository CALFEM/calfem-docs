.. _elflux2:
.. index:: 
   single: elflux2
   single: flow arrows
   single: flux visualization
   single: thermal visualization
   single: 2D visualization
   pair: visualization; flow
   pair: flux; arrows
   pair: thermal; visualization
   pair: 2D; visualization
   pair: post-processing; visualization

elflux2
^^^^^^^

:Purpose:
    Draw element flow arrows for two dimensional elements.

:Syntax:
.. only:: matlab

    .. code-block:: matlab

        [sfac] = elflux2(Ex, Ey, Es)
        [sfac] = elflux2(Ex, Ey, Es, plotpar)
        elflux2(Ex, Ey, Es, plotpar, sfac)

.. only:: python

    .. code-block:: python

        sfac = cfv.elflux2(Ex, Ey, Es)
        sfac = cfv.elflux2(Ex, Ey, Es, plotpar)
        cfv.elflux2(Ex, Ey, Es, plotpar, sfac)

:Description:
    :code:`elflux2` displays element heat flux vectors (or corresponding quantities) for a number of elements of the same type.
    The flux vectors are displayed as arrows at the element centroids.
    Note that only the flux vectors are displayed. To display the element mesh, use :code:`eldraw2`.

    Input variables are the coordinate matrices :code:`Ex` and :code:`Ey`, and the element flux matrix :code:`Es` defined in :code:`flw2ts` or :code:`flw2qs`.

    The variable :code:`plotpar` sets plot parameters for the flux arrows:

    :code:`plotpar`:math:`= [\, arrowtype \;\; arrowcolor \,]`

    where

    .. list-table::
        :widths: 20 30 20 30
        :header-rows: 1

        * - :math:`arrowtype`
          - 
          - :math:`arrowcolor`
          - 
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

    Default, if :code:`plotpar` is omitted, is solid black arrows.

    The scale factor :code:`sfac` is a scalar that the values are multiplied with to get a suitable arrow size in relation to the element size. The scale factor is set automatically if it is omitted in the input list.

:Limitations:
    Supported elements are triangular 3 node and quadrilateral 4 node elements.
