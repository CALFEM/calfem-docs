spring1s
^^^^^^^^

:Purpose:
    Compute spring force in a spring element.

    .. figure:: images/SPRING3.png
        :width: 70%
        :align: center

:Syntax:
    .. code:: matlab

        es = spring1s(ep, ed)

:Description:
    :math:`\mathrm{spring1s}` computes the spring force :math:`\mathrm{es}` in a spring element.

    The input variable :math:`\mathrm{ep}` is defined in :math:`\mathrm{spring1e}` and the
    element nodal displacements :math:`\mathrm{ed}` are obtained by the function :math:`\mathrm{extract}`.

    The output variable

    .. math::

        \mathrm{es} = \left[\,N\,\right]

    contains the spring force :math:`N`, or the analog quantity.

:Theory:
    The spring force :math:`N`, or analog quantity, is computed according to

    .. math::

        N = k \left(u_2 - u_1\right)
