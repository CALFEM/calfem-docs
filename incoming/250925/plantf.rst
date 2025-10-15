plantf
^^^^^^

:Purpose:
    Compute internal element force vector in a triangular element in plane strain or plane stress.

:Syntax:
    .. code:: matlab
    
        ef = plantf(ex, ey, ep, es)

:Description:
    ``plantf`` computes the internal element forces ``ef`` in a triangular element in plane strain or plane stress.

    The input variables :math:`\mathbf{ex}`, :math:`\mathbf{ey}` and :math:`\mathbf{ep}` are defined in ``plante``, and the input variable :math:`\mathbf{es}` is defined in ``plants``.

    The output variable

    .. math::

        \mathrm{ef} = \mathbf{f}_i^{eT} = \left[\, f_{i1}\; f_{i2}\; \dots \; f_{i6}\; \right]

    contains the components of the internal force vector.

:Theory:
    The internal force vector is computed according to

    .. math::

        \mathbf{f}_i^e = (\mathbf{C}^{-1})^T \int_A \bar{\mathbf{B}}^T \boldsymbol{\sigma}\; t\; dA

    where the matrices :math:`\bar{\mathbf{B}}` and :math:`\mathbf{C}` are defined in ``plante`` and :math:`\boldsymbol{\sigma}` is defined in ``plants``.

    Evaluation of the integral for the triangular element yields

    .. math::

        \mathbf{f}_i^e = (\mathbf{C}^{-1})^T \bar{\mathbf{B}}^T\,\boldsymbol{\sigma}\; t\; A

