scalfact2
^^^^^^^^^

:Purpose:
    Determine scale factor for drawing computational results.


:Syntax:
    .. code:: matlab

        [sfac] = scalfact2(ex, ey, ed)
        [sfac] = scalfact2(ex, ey, ed, rat)

:Description:
    :func:`scalfact2` determines a scale factor :math:`sfac` for drawing computational results, such as displacements, section forces, or flux.

    Input variables are the coordinate matrices :math:`ex` and :math:`ey`, and the matrix :math:`ed` containing the quantity to be displayed.
    The scalar :math:`rat` defines the ratio between the geometric representation of the largest quantity to be displayed and the element size.
    If :math:`rat` is not specified, :math:`0.2` is used.

:Theory:
    The scale factor :math:`sfac` is computed so that the largest value in :math:`ed` is represented as a fraction :math:`rat` of the element size, ensuring a visually appropriate scaling of computational results.
