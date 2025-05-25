plani4f
^^^^^^^

:Purpose:
    Compute internal element force vector in a 4 node isoparametric element in plane strain or plane stress.

:Syntax:
    .. code:: matlab

        ef = plani4f(ex, ey, ep, es)

:Description:
    ``plani4f`` computes the internal element forces :math:`\mathrm{ef}` in a 4 node isoparametric element in plane strain or plane stress.

    The input variables :math:`\mathbf{ex}`, :math:`\mathbf{ey}` and :math:`\mathbf{ep}` are defined in ``plani4e``, and the input variable :math:`\mathbf{es}` is defined in ``plani4s``.

    The output variable

    .. math::

        \mathrm{ef} = \mathbf{f}_i^{eT} = \left[\, f_{i1}\; f_{i2}\; \dots \; f_{i8}\, \right]

    contains the components of the internal force vector.

:Theory:
    The internal force vector is computed according to

    .. math::

        \mathbf{f}_i^e = \int_A \mathbf{B}^{eT} \boldsymbol{\sigma} \; t \; dA

    where the matrices :math:`\mathbf{B}^e` and :math:`\boldsymbol{\sigma}` are defined in ``plani4e`` and ``plani4s``, respectively.

    Evaluation of the integral is done by Gauss integration.
