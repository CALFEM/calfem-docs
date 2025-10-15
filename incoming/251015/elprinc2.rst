elprinc2
^^^^^^^^

:Purpose:
    Draw element principal stresses as arrows for two dimensional elements.
    

:Syntax:
.. only:: matlab

    .. code-block:: matlab

        [sfac] = elprinc2(Ex, Ey, Es)
        [sfac] = elprinc2(Ex, Ey, Es, plotpar)
        elprinc2(Ex, Ey, Es, plotpar, sfac)

.. only:: python

    .. code-block:: python

        sfac = cfc.elprinc2(Ex, Ey, Es)
        sfac = cfc.elprinc2(Ex, Ey, Es, plotpar)
        cfc.elprinc2(Ex, Ey, Es, plotpar, sfac)

:Description:
    :code:`elprinc2` displays element principal stresses for a number of elements of the same type. The principal stresses are displayed as arrows at the element centroids. Note that only the principal stresses are displayed. To display the element mesh, use :code:`eldraw2`.

    Input variables are the coordinate matrices :code:`Ex` and :code:`Ey`, and the element stresses matrix :code:`Es` defined in :code:`plants` or :code:`planqs`.

    The variable :code:`plotpar` sets plot parameters for the principal stress arrows:

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

    The scale factor :code:`sfac` is a scalar that values are multiplied with to get a suitable arrow size in relation to the element size. The scale factor is set automatically if it is omitted in the input list.

:Limitations:
    Supported elements are triangular 3 node and quadrilateral 4 node elements.
