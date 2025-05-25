hooke
^^^^^

:Purpose:
    Compute material matrix for a linear elastic and isotropic material.

:Syntax:
    .. code:: matlab

        D = hooke(ptype, E, v)

:Description:
    The function :code:`hooke` computes the material matrix :math:`\mathbf{D}` for a linear elastic and isotropic material.

    The variable :math:`\mathrm{ptype}` is used to define the type of analysis:

    .. math::

        \mathrm{ptype} = \left\{
            \begin{array}{ll}
                1 & \text{plane stress} \\
                2 & \text{plane strain} \\
                3 & \text{axisymmetry} \\
                4 & \text{three dimensional analysis}
            \end{array}
        \right.

    The material parameters :math:`E` and :math:`\nu` define the modulus of elasticity and the Poisson's ratio, respectively.

:Theory:
    For plane stress (:math:`\mathrm{ptype}=1`), :math:`\mathbf{D}` is formed as

    .. math::

        \mathbf{D} = \frac{E}{1-\nu^2}
        \begin{bmatrix}
            1 & \nu & 0 \\
            \nu & 1 & 0 \\
            0 & 0 & \frac{1-\nu}{2}
        \end{bmatrix}

    For plane strain (:math:`\mathrm{ptype}=2`) and axisymmetry (:math:`\mathrm{ptype}=3`), :math:`\mathbf{D}` is formed as

    .. math::

        \mathbf{D} = \frac{E}{(1+\nu)(1-2\nu)}
        \begin{bmatrix}
            1-\nu & \nu & \nu & 0 \\
            \nu & 1-\nu & \nu & 0 \\
            \nu & \nu & 1-\nu & 0 \\
            0 & 0 & 0 & \frac{1}{2}(1-2\nu)
        \end{bmatrix}

    For the three dimensional case (:math:`\mathrm{ptype}=4`), :math:`\mathbf{D}` is formed as

    .. math::

        \mathbf{D} = \frac{E}{(1+\nu)(1-2\nu)}
        \begin{bmatrix}
            1-\nu & \nu & \nu & 0 & 0 & 0 \\
            \nu & 1-\nu & \nu & 0 & 0 & 0 \\
            \nu & \nu & 1-\nu & 0 & 0 & 0 \\
            0 & 0 & 0 & \frac{1}{2}(1-2\nu) & 0 & 0 \\
            0 & 0 & 0 & 0 & \frac{1}{2}(1-2\nu) & 0 \\
            0 & 0 & 0 & 0 & 0 & \frac{1}{2}(1-2\nu)
        \end{bmatrix}
