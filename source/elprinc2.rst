elprinc2
^^^^^^^^

:Purpose:
    Draw element principal stresses as arrows for two dimensional elements.
    

:Syntax:
    .. code:: matlab

        [sfac] = elprinc2(Ex, Ey, Es)
        [sfac] = elprinc2(Ex, Ey, Es, plotpar)
        elprinc2(Ex, Ey, Es, plotpar, sfac)

:Description:
    :math:`\text{elprinc2}` displays element principal stresses for a number of elements of the same type. The principal stresses are displayed as arrows at the element centroids. Note that only the principal stresses are displayed. To display the element mesh, use :math:`\text{eldraw2}`.

    Input variables are the coordinate matrices :math:`\text{Ex}` and :math:`\text{Ey}`, and the element stresses matrix :math:`\text{Es}` defined in :math:`\text{plants}` or :math:`\text{planqs}`.

    The variable :math:`\text{plotpar}` sets plot parameters for the principal stress arrows:

    .. math::

        \text{plotpar} = [\, \text{arrowtype} \;\; \text{arrowcolor} \,]

    where

    .. list-table::
        :widths: 20 30 20 30
        :header-rows: 0

        * - :math:`\text{arrowtype} = 1`
          - solid
          - :math:`\text{arrowcolor} = 1`
          - black
        * - 2
          - dashed
          - 2
          - blue
        * - 3
          - dotted
          - 3
          - magenta
        * - 
          - 
          - 4
          - red

    Default, if :math:`\text{plotpar}` is omitted, is solid black arrows.

    The scale factor :math:`\text{sfac}` is a scalar that values are multiplied with to get a suitable arrow size in relation to the element size. The scale factor is set automatically if it is omitted in the input list.

:Limitations:
    Supported elements are triangular 3 node and quadrilateral 4 node elements.
