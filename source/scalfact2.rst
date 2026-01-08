.. _scalfact2:
.. index:: 
   single: scalfact2
   single: scale factor
   single: visualization scaling
   single: plot scaling
   single: drawing scale
   pair: visualization; scaling
   pair: plot; scaling
   pair: drawing; utilities
   pair: 2D; scaling

scalfact2
^^^^^^^^^

:Purpose:
    Determine scale factor for drawing computational results.


:Syntax:
.. only:: matlab

    .. code-block:: matlab


.. only:: python

    .. code-block:: python

        sfac = cfv.scalfact2(ex, ey, ed)
        sfac = cfv.scalfact2(ex, ey, ed, rat)

:Description:
    :code:`scalfact2` determines a scale factor :code:`sfac` for drawing computational results, such as displacements, section forces, or flux.

    Input variables are the coordinate matrices :code:`ex` and :code:`ey`, and the matrix :code:`ed` containing the quantity to be displayed.
    The scalar :code:`rat` defines the ratio between the geometric representation of the largest quantity to be displayed and the element size.
    If :code:`rat` is not specified, :math:`0.2` is used.

:Theory:
    The scale factor :code:`sfac` is computed so that the largest value in :code:`ed` is represented as a fraction :code:`rat` of the element size, ensuring a visually appropriate scaling of computational results.
