elflux2
^^^^^^^

:Purpose:
    Draw element flow arrows for two dimensional elements.

:Syntax:
    .. code:: matlab

        [sfac] = elflux2(Ex, Ey, Es)
        [sfac] = elflux2(Ex, Ey, Es, plotpar)
        elflux2(Ex, Ey, Es, plotpar, sfac)

:Description:
    :math:`\mathrm{elflux2}` displays element heat flux vectors (or corresponding quantities) for a number of elements of the same type.
    The flux vectors are displayed as arrows at the element centroids.
    Note that only the flux vectors are displayed. To display the element mesh, use :math:`\mathrm{eldraw2}`.

    Input variables are the coordinate matrices :math:`\mathrm{Ex}` and :math:`\mathrm{Ey}`, and the element flux matrix :math:`\mathrm{Es}` defined in :math:`\mathrm{flw2ts}` or :math:`\mathrm{flw2qs}`.

    The variable :math:`\mathrm{plotpar}` sets plot parameters for the flux arrows:

    :math:`\mathrm{plotpar} = [\, \mathrm{arrowtype} \;\; \mathrm{arrowcolor} \,]`

    +-------------------+----------------+-------------------+----------------+
    | :math:`arrowtype` | Line style     | :math:`arrowcolor`| Color          |
    +===================+================+===================+================+
    | 1                 | solid          | 1                 | black          |
    +-------------------+----------------+-------------------+----------------+
    | 2                 | dashed         | 2                 | blue           |
    +-------------------+----------------+-------------------+----------------+
    | 3                 | dotted         | 3                 | magenta        |
    +-------------------+----------------+-------------------+----------------+
    |                   |                | 4                 | red            |
    +-------------------+----------------+-------------------+----------------+

    Default, if :math:`\mathrm{plotpar}` is omitted, is solid black arrows.

    The scale factor :math:`\mathrm{sfac}` is a scalar that the values are multiplied with to get a suitable arrow size in relation to the element size. The scale factor is set automatically if it is omitted in the input list.

:Limitations:
    Supported elements are triangular 3 node and quadrilateral 4 node elements.
