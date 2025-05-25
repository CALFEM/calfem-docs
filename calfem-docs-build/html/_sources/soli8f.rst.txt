soli8f
^^^^^^^

:Purpose:
    Compute internal element force vector in an 8 node isoparametric solid element.

:Syntax:
    .. code:: matlab

        ef = soli8f(ex, ey, ez, ep, es)

:Description:
    ``soli8f`` computes the internal element forces :math:`\mathrm{ef}` in an 8 node isoparametric solid element.

    The input variables :math:`\mathbf{ex}`, :math:`\mathbf{ey}`, :math:`\mathbf{ez}` and :math:`\mathbf{ep}` are defined in ``soli8e``, and the input variable :math:`\mathbf{es}` is defined in ``soli8s``.

    The output variable

    .. math::

        \mathrm{ef} = \mathbf{f}_i^{eT} = \left[\, f_{i1}\; f_{i2}\; \dots \; f_{i24}\; \right]

    contains the components of the internal force vector.

:Theory:
    The internal force vector is computed according to

    .. math::

        \mathbf{f}_i^e = \int_V \mathbf{B}^{eT} \boldsymbol{\sigma} \; dV

    where the matrices :math:`\mathbf{B}` and :math:`\boldsymbol{\sigma}` are defined in ``soli8e`` and ``soli8s``, respectively.

    Evaluation of the integral is done by Gauss integration.
