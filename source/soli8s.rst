.. _soli8s:
.. index:: 
   single: soli8s
   single: solid stress
   single: 3D stress
   single: 8 node stress
   single: isoparametric stress
   single: hexahedral stress
   pair: finite element; stress
   pair: solid; stress
   pair: post-processing; stress
   pair: 3D; stress
   pair: isoparametric; stress
   pair: hexahedral; stress

soli8s
^^^^^^

:Purpose:
    Compute stresses and strains in an 8 node isoparametric solid element.

    .. figure:: images/SOLI8S.png
        :width: 70%
        :align: center

:Syntax:
    .. code:: matlab

        [es,et,eci]=soli8s(ex,ey,ez,ep,D,ed)

:Description:
    ``soli8s`` computes stresses ``es`` and the strains ``et``
    in an 8 node isoparametric solid element.

    The input variables :math:`\mathbf{ex}`, :math:`\mathbf{ey}`, :math:`\mathbf{ez}`, :math:`\mathbf{ep}` and
    the matrix :math:`\mathbf{D}` are defined in ``soli8e``.
    The vector :math:`\mathbf{ed}` contains the nodal displacements :math:`\mathbf{a}^e`
    of the element and is obtained by the function ``extract`` as

    .. math::

        \mathbf{ed} = (\mathbf{a}^e)^T = [\;u_1\;\; u_2\;\; \dots \;\; u_{24}\;]

    The output variables

    .. math::

        \mathrm{es} = \boldsymbol{\sigma}^T =
        \begin{bmatrix}
        \sigma^1_{xx} & \sigma^1_{yy} & \sigma^1_{zz} & \sigma^1_{xy} & \sigma^1_{xz} & \sigma^1_{yz} \\
        \sigma^2_{xx} & \sigma^2_{yy} & \sigma^2_{zz} & \sigma^2_{xy} & \sigma^2_{xz} & \sigma^2_{yz} \\
        \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
        \sigma^{n^3}_{xx} & \sigma^{n^3}_{yy} & \sigma^{n^3}_{zz} & \sigma^{n^3}_{xy} & \sigma^{n^3}_{xz} & \sigma^{n^3}_{yz}
        \end{bmatrix}

    .. math::

        \mathrm{et} = \boldsymbol{\varepsilon}^T =
        \begin{bmatrix}
        \varepsilon^1_{xx} & \varepsilon^1_{yy} & \varepsilon^1_{zz} & \gamma^1_{xy} & \gamma^1_{xz} & \gamma^1_{yz} \\
        \varepsilon^2_{xx} & \varepsilon^2_{yy} & \varepsilon^2_{zz} & \gamma^2_{xy} & \gamma^2_{xz} & \gamma^2_{yz} \\
        \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
        \varepsilon^{n^3}_{xx} & \varepsilon^{n^3}_{yy} & \varepsilon^{n^3}_{zz} & \gamma^{n^3}_{xy} & \gamma^{n^3}_{xz} & \gamma^{n^3}_{yz}
        \end{bmatrix}
        \qquad
        \mathbf{eci} =
        \begin{bmatrix}
        x_1 & y_1 & z_1 \\
        x_2 & y_2 & z_2 \\
        \vdots & \vdots & \vdots \\
        x_{n^3} & y_{n^3} & z_{n^3}
        \end{bmatrix}

    contain the stress and strain components, and the coordinates of
    the integration points. The index :math:`n` denotes the number of integration points
    used within the element, cf. ``soli8e``.

:Theory:
    The strains and stresses are computed according to

    .. math::

        \boldsymbol{\varepsilon} = \mathbf{B}^e \mathbf{a}^e

    .. math::

        \boldsymbol{\sigma} = \mathbf{D} \boldsymbol{\varepsilon}

    where the matrices :math:`\mathbf{D}`, :math:`\mathbf{B}^e`, and :math:`\mathbf{a}^e` are described
    in ``soli8e``, and where the integration points
    are chosen as evaluation points.
