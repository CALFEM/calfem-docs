dmises
^^^^^^

:Purpose:
    Form the elasto-plastic continuum matrix for an isotropic hardening von Mises material.

:Syntax:
    .. code:: matlab

        D = dmises(ptype, mp, es, st)

:Description:
    :math:`\text{dmises}` forms the elasto-plastic continuum matrix for an isotropic hardening von Mises material.

    The input variable :math:`\text{ptype}` is used to define the type of analysis, cf. :math:`\text{hooke}`.

    The vector :math:`\mathbf{mp}` contains the material constants:

    .. math::

        \mathbf{mp} = [\, E\;\nu\;h\,]

    where :math:`E` is the modulus of elasticity, :math:`\nu` is the Poisson's ratio, and :math:`h` is the plastic modulus.

    The matrix :math:`\text{es}` contains current stresses obtained from :math:`\text{plants}` or some similar :math:`s`-function, and the vector :math:`\text{st}` contains the current state parameters:

    .. math::

        \mathbf{st} = [\, yi\;\sigma_y\;\varepsilon_{eff}^p\,]

    where :math:`yi = 1` if the material behaviour is elasto-plastic, and :math:`yi = 0` if the material behaviour is elastic. The current yield stress is denoted by :math:`\sigma_y`, and the current effective plastic strain by :math:`\varepsilon_{eff}^p`.

:Note:
    Only the case :math:`\text{ptype} = 2` is implemented.
