.. _plants:
.. index:: 
   single: plants
   single: triangular stress
   single: plane stress
   single: plane strain
   single: triangular element stress
   pair: finite element; stress
   pair: triangular; element
   pair: plane; stress
   pair: plane; strain
   pair: 2D; stress

plants
^^^^^^

:Purpose:
    Compute stresses and strains in a triangular element in plane strain or plane stress.

    .. image:: images/PLANTS.png
        :width: 70%
        :align: center

:Syntax:
    .. code:: matlab

        [es, et] = plants(ex, ey, ep, D, ed)


:Description:
    ``plants`` computes the stresses ``es`` and the strains ``et`` in a triangular element in plane strain or plane stress.

    The input variables :math:`\mathbf{ex}`, :math:`\mathbf{ey}`, :math:`\mathbf{ep}` and :math:`\mathbf{D}` are defined in ``plante``.
    The vector :math:`\mathbf{ed}` contains the nodal displacements :math:`\mathbf{a}^e` of the element and is obtained by the function ``extract`` as

    .. math::

        \mathbf{ed} = (\mathbf{a}^e)^T = [\, u_1\;\; u_2\;\; \dots \;\; u_6\,]

    The output variables

    .. math::

        \mathrm{es} = \boldsymbol{\sigma}^T = \left[\, \sigma_{xx}\; \sigma_{yy}\; [\sigma_{zz}]\; \sigma_{xy}\; [\sigma_{xz}]\; [\sigma_{yz}]\, \right]

    .. math::

        \mathrm{et} = \boldsymbol{\varepsilon}^T = [\, \varepsilon_{xx}\; \varepsilon_{yy}\; [\varepsilon_{zz}]\; \gamma_{xy}\; [\gamma_{xz}]\; [\gamma_{yz}]\,]

    contain the stress and strain components. The size of ``es`` and ``et`` follows the size of ``D``.
    Note that for plane stress :math:`\varepsilon_{zz} \neq 0`, and for plane strain :math:`\sigma_{zz} \neq 0`.

:Theory:
    The strains and stresses are computed according to

    .. math::

        \boldsymbol{\varepsilon} = \bar{\mathbf{B}}\, \mathbf{C}^{-1}\, \mathbf{a}^e

    .. math::

        \boldsymbol{\sigma} = \mathbf{D}\, \boldsymbol{\varepsilon}

    where the matrices :math:`\mathbf{D}`, :math:`\bar{\mathbf{B}}`, :math:`\mathbf{C}` and :math:`\mathbf{a}^e` are described in ``plante``.
    Note that both the strains and the stresses are constant in the element.
