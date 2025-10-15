planqs
^^^^^^

:Purpose:
    Compute stresses and strains in a quadrilateral element in plane strain or plane stress.

    .. figure:: images/PLANI4S.png
        :width: 70%

:Syntax:
    .. code:: matlab

        [es,et]=planqs(ex,ey,ep,D,ed)
        [es,et]=planqs(ex,ey,ep,D,ed,eq)

:Description:
    ``planqs`` computes the stresses ``es`` and the strains ``et`` in a quadrilateral element in plane strain or plane stress.

    The input variables :math:`\mathbf{ex}`, :math:`\mathbf{ey}`, :math:`\mathbf{ep}`, :math:`\mathbf{D}` and :math:`\mathbf{eq}` are defined in ``planqe``.
    The vector :math:`\mathbf{ed}` contains the nodal displacements :math:`\mathbf{a}^e` of the element and is obtained by the function ``extract`` as

    .. math::

        \mathbf{ed} = (\mathbf{a}^e)^T = [\,u_1\;\; u_2\;\; \dots  \;\; u_8\,]

    If body forces are applied to the element the variable :math:`\mathbf{eq}` must be included.

    The output variables

    .. math::

        \mathrm{es} = \boldsymbol{\sigma}^T = [\, \sigma_{xx}\; \sigma_{yy}\; [\sigma_{zz}]\; \sigma_{xy}\; [\sigma_{xz}]\; [\sigma_{yz}]\,]

    .. math::

        \mathrm{et} = \boldsymbol{\varepsilon}^T = [\,\varepsilon_{xx}\;\varepsilon_{yy}\;[\varepsilon_{zz}]\;\gamma_{xy}\;[\gamma_{xz}]\;[\gamma_{yz}]\,]

    contain the stress and strain components. The size of ``es`` and ``et`` follows the size of ``D``.
    Note that for plane stress :math:`\varepsilon_{zz} \neq 0`, and for plane strain :math:`\sigma_{zz} \neq 0`.

:Theory:
    By assembling triangular elements as described in ``planqe`` a system of equations containing 10 degrees of freedom is obtained. From this system of equations the two unknown displacements at the center of the element are computed.
    Then according to the description in ``plants`` the strain and stress components in each of the four triangular elements are produced.
    Finally the quadrilateral element strains and stresses are computed as area weighted mean values from the values of the four triangular elements.
    If uniformly distributed loads are applied on the element, the element load vector ``eq`` is needed for the calculations.
