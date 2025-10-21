.. _mises:
.. index:: 
   single: mises
   single: von Mises stress
   single: plasticity
   single: elasto-plastic
   single: isotropic hardening
   single: yield criterion
   pair: material; plasticity
   pair: von Mises; stress
   pair: elasto-plastic; material
   pair: constitutive; relations
   pair: plastic; strain

mises
^^^^^

:Purpose:
    Compute stresses and plastic strains for an elasto-plastic isotropic hardening von Mises material.

:Syntax:
    .. code:: matlab

        [es, deps, st] = mises(ptype, mp, est, st)

:Description:
    The :code:`mises` function computes updated stresses, :code:`es`, plastic strain increments :code:`deps`, and state variables :code:`st` for an elasto-plastic isotropic hardening von Mises material.

    The input variable :code:`ptype` defines the type of analysis, see also :code:`hooke`. The vector :code:`mp` contains the material constants:


    .. only:: python

        :code:`mp = [`:math:`\small{E, \nu, h}`:code:`]`

    .. only:: matlab

        :code:`mp = [`:math:`\small{\, E\;\nu\;h\,}`:code:`]`

    where :math:`E` is the modulus of elasticity, :math:`\nu` is the Poisson's ratio, and :math:`h` is the plastic modulus.

    The input matrix :code:`est` contains trial stresses obtained by using the elastic material matrix :code:`D` in :code:`plants` or a similar :code:`s`-function. The input vector :code:`st` contains the state parameters:

    .. only:: python

        :code:`st = [`:math:`\small{\, yi\;\sigma_y\;\varepsilon_{eff}^p\,}`:code:`]`

    .. only:: matlab

        :code:`st = [`:math:`\small{\, yi\;\sigma_y\;\varepsilon_{eff}^p\,}`:code:`]`

    at the beginning of the step. The scalar :math:`yi` indicates whether the material behaviour is elasto-plastic (:math:`yi = 1`) or elastic (:math:`yi = 0`). The current yield stress is denoted by :math:`\sigma_y` and the effective plastic strain by :math:`\varepsilon_{eff}^p`.

    The output variables :code:`es` and :code:`st` contain updated values obtained by integration of the constitutive equations over the actual displacement step. The increments of the plastic strains are stored in the vector :code:`deps`.

    If :code:`es` and :code:`st` contain more than one row, then every row will be treated by the command.

:Note:
    It is not necessary to check whether the material behaviour is elastic or elasto-plastic; this test is performed by the function. The computation is based on an Euler-Backward method, i.e., the radial return method.

    Only the cases :code:`ptype = 2, 3, 4` are implemented.
