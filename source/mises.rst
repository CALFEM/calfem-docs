mises
^^^^^

:Purpose:
    Compute stresses and plastic strains for an elasto-plastic isotropic hardening von Mises material.

:Syntax:
    .. code:: matlab

        [es, deps, st] = mises(ptype, mp, est, st)

:Description:
    The :math:`\texttt{mises}` function computes updated stresses (:math:`\texttt{es}`), plastic strain increments (:math:`\texttt{deps}`), and state variables (:math:`\texttt{st}`) for an elasto-plastic isotropic hardening von Mises material.

    The input variable :math:`\texttt{ptype}` defines the type of analysis, see also :math:`\texttt{hooke}`. The vector :math:`\texttt{mp}` contains the material constants:

    :math:`\mathbf{mp} = [\, E\;\nu\;h\,]`

    where :math:`E` is the modulus of elasticity, :math:`\nu` is the Poisson's ratio, and :math:`h` is the plastic modulus.

    The input matrix :math:`\texttt{est}` contains trial stresses obtained by using the elastic material matrix :math:`\texttt{D}` in :math:`\texttt{plants}` or a similar :math:`\texttt{s}`-function. The input vector :math:`\texttt{st}` contains the state parameters:

    :math:`\mathbf{st} = [\, yi\;\sigma_y\;\varepsilon_{eff}^p\,]`

    at the beginning of the step. The scalar :math:`yi` indicates whether the material behaviour is elasto-plastic (:math:`yi = 1`) or elastic (:math:`yi = 0`). The current yield stress is denoted by :math:`\sigma_y` and the effective plastic strain by :math:`\varepsilon_{eff}^p`.

    The output variables :math:`\texttt{es}` and :math:`\texttt{st}` contain updated values obtained by integration of the constitutive equations over the actual displacement step. The increments of the plastic strains are stored in the vector :math:`\texttt{deps}`.

    If :math:`\texttt{es}` and :math:`\texttt{st}` contain more than one row, then every row will be treated by the command.

:Note:
    It is not necessary to check whether the material behaviour is elastic or elasto-plastic; this test is performed by the function. The computation is based on an Euler-Backward method, i.e., the radial return method.

    Only the cases :math:`\texttt{ptype} = 2, 3, 4` are implemented.
