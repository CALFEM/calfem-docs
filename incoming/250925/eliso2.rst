eliso2
^^^^^^

:Purpose:
    Display element iso lines for two dimensional elements.

:Syntax:
    .. code:: matlab

        eliso2(Ex, Ey, Ed, isov)
        eliso2(Ex, Ey, Ed, isov, plotpar)

:Description:
    :math:`\mathtt{eliso2}` displays element iso lines for a number of elements of the same type.
    Note that only the iso lines are displayed. To display the element mesh, use :math:`\mathtt{eldraw2}`.

    Input variables are the coordinate matrices :math:`\mathtt{Ex}` and :math:`\mathtt{Ey}` formed by the function :math:`\mathtt{coordxtr}`,
    and the element nodal quantities (e.g., displacement or energy potential) matrix :math:`\mathtt{Ed}` defined in :math:`\mathtt{extract}`.

    If :math:`\mathtt{isov}` is a scalar, it determines the number of iso lines to be displayed.
    If :math:`\mathtt{isov}` is a vector, it determines the values of the iso lines to be displayed
    (number of iso lines equal to the length of vector :math:`\mathtt{isov}`):

    :math:`\mathtt{isov} = [\, \text{iso lines} \,]`

    :math:`\mathtt{isov} = [\, \text{isovalue}(1) \; \ldots \; \text{isovalue}(n) \,]`

    The variable :math:`\mathtt{plotpar}` sets plot parameters for the iso lines:

    :math:`\mathtt{plotpar} = [\, \text{linetype} \;\; \text{linecolor} \;\; \text{textfcn} \,]`

    - :math:`\text{linetype}`: 1 = solid, 2 = dashed, 3 = dotted
    - :math:`\text{linecolor}`: 1 = black, 2 = blue, 3 = magenta, 4 = red
    - :math:`\text{textfcn}`: 0 = iso values not printed, 1 = iso values printed at the iso lines, 2 = iso values printed where the cursor indicates

    Default is solid, black lines and no iso values printed.

:Limitations:
    Supported elements are triangular 3 node and quadrilateral 4 node elements.
