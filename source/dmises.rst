.. _dmises:
.. index:: 
   single: dmises
   single: von Mises material
   single: elasto-plastic matrix
   single: continuum matrix
   single: isotropic hardening
   single: plasticity matrix
   pair: material; matrix
   pair: von Mises; material
   pair: elasto-plastic; matrix
   pair: constitutive; matrix
   pair: plasticity; matrix

dmises
^^^^^^

:Purpose:
    Form the elasto-plastic continuum matrix for an isotropic hardening von Mises material.

:Syntax:
    .. code:: matlab

        D = dmises(ptype, mp, es, st)

:Description:
    :code:`dmises` forms the elasto-plastic continuum matrix for an isotropic hardening von Mises material.

    The input variable :code:`ptype` is used to define the type of analysis, cf. :code:`hooke`.

    The vector :code:`mp` contains the material constants:

    .. only:: python

        :code:`mp = [`:math:`\small{E, \nu, h}`:code:`]`

    .. only:: matlab

        :code:`mp = [`:math:`\small{\, E\;\nu\;h\,}`:code:`]`

    where :math:`E` is the modulus of elasticity, :math:`\nu` is the Poisson's ratio, and :math:`h` is the plastic modulus.

    The matrix :code:`es` contains current stresses obtained from :code:`plants` or some similar :code:`s`-function, and the vector :code:`st` contains the current state parameters:

    .. only:: python

        :code:`st = [`:math:`\small{\, yi\;\sigma_y\;\varepsilon_{eff}^p\,}`:code:`]`

    .. only:: matlab

        :code:`st = [`:math:`\small{\, yi\;\sigma_y\;\varepsilon_{eff}^p\,}`:code:`]`

    where :math:`yi = 1` if the material behaviour is elasto-plastic, and :math:`yi = 0` if the material behaviour is elastic. The current yield stress is denoted by :math:`\sigma_y`, and the current effective plastic strain by :math:`\varepsilon_{eff}^p`.

:Note:
    Only the case :code:`ptype = 2` is implemented.
