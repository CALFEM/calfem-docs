plantcs
^^^^^^^

:Purpose:
    Compute stresses and strains in a Turner-Clough element in plane strain or plane stress.

    .. only:: html
        
        .. figure:: images/plantrs.svg
            :align: center
            :width: 400px
    
    .. only:: latex
        
        .. figure:: images/plantrs.svg
            :align: center
            :width: 70%

:Syntax:
    .. code:: matlab

        [es, et] = plantcs(ex, ey, ep, ed)

:Description:
    ``plantcs`` computes the stresses ``es`` and the strains ``et`` in a rectangular Turner-Clough element in plane strain or plane stress. The stress and strain components are computed at the center of the element.

    The input variables :math:`\mathbf{ex}`, :math:`\mathbf{ey}`, and :math:`\mathbf{ep}` are defined in ``plantce``. The vector :math:`\mathbf{ed}` contains the nodal displacements :math:`\mathbf{a}^e` of the element and is obtained by the function ``extract`` as

    .. math::

        \mathbf{ed} = (\mathbf{a}^e)^T = [\, u_1\;\; u_2\;\; \dots \;\; u_8\,]

    The output variables

    .. math::

        \mathrm{es} = \boldsymbol{\sigma}^T = [\, \sigma_{xx}\; \sigma_{yy}\; [\sigma_{zz}]\; \sigma_{xy}\; [\sigma_{xz}]\; [\sigma_{yz}]\,]

    .. math::

        \mathrm{et} = \boldsymbol{\varepsilon}^T = [\, \varepsilon_{xx}\; \varepsilon_{yy}\; [\varepsilon_{zz}]\; \gamma_{xy}\; [\gamma_{xz}]\; [\gamma_{yz}]\,]

    contain the stress and strain components. The size of ``es`` and ``et`` follows the size of ``D``. Note that for plane stress :math:`\varepsilon_{zz} \neq 0`, and for plane strain :math:`\sigma_{zz} \neq 0`.

:Theory:
    The strains and stresses are computed according to

    .. math::

        \boldsymbol{\varepsilon} = \mathbf{B}^e\,\mathbf{a}^e

    .. math::

        \boldsymbol{\sigma} = \mathbf{D}\;\boldsymbol{\varepsilon}

    where the matrices :math:`\mathbf{D}`, :math:`\mathbf{B}^e`, and :math:`\mathbf{a}^e` are described in ``plantce``, and where the evaluation point :math:`(x, y)` is chosen to be at the center of the element.
