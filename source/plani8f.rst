plani8f
^^^^^^^

:Purpose:
    Compute internal element force vector in an 8 node isoparametric element in plane strain or plane stress.

:Syntax:
    .. code:: matlab

        ef = plani8f(ex, ey, ep, es)

:Description:
    ``plani8f`` computes the internal element forces :math:`\mathrm{ef}` in an 8 node isoparametric element in plane strain or plane stress.

    The input variables :math:`\mathbf{ex}`, :math:`\mathbf{ey}` and :math:`\mathbf{ep}` are defined in ``plani8e``, and the input variable :math:`\mathbf{es}` is defined in ``plani8s``.

    The output variable

    .. math::

        \mathrm{ef} = \mathbf{f}_i^{eT} = \left[\, f_{i1}\; f_{i2}\; \dots \; f_{i16}\; \right]

    contains the components of the internal force vector.

:Theory:
    The internal force vector is computed according to

    .. math::

        \mathbf{f}_i^e = \int_A \mathbf{B}^{eT} \boldsymbol{\sigma} \; t \; dA

    where the matrices :math:`\mathbf{B}^e` and :math:`\boldsymbol{\sigma}` are defined in ``plani8e`` and ``plani8s``, respectively.

    Evaluation of the integral is done by Gauss integration.
