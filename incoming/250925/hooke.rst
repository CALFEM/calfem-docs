hooke
^^^^^

:Purpose:
    Compute material matrix for a linear elastic and isotropic material.

:Syntax:
    .. code:: matlab

        D = hooke(ptype, E, v)

:Description:
    The function :code:`hooke` computes the material matrix :math:`\mathbf{D}` for a linear elastic and isotropic material.

    The variable :code:`ptype` is used to define the type of analysis:

    * :code:`ptype = 1` - plane stress
    * :code:`ptype = 2` - plane strain  
    * :code:`ptype = 3` - axisymmetry
    * :code:`ptype = 4` - three dimensional analysis

    The material parameters :math:`E` and :math:`\nu` define the modulus of elasticity and the Poisson's ratio, respectively.

:Theory:
    For plane stress (:code:`ptype=1`), :math:`\mathbf{D}` is formed as

    .. math::

        \mathbf{D} = \frac{E}{1-\nu^2}
        \begin{bmatrix}
            1 & \nu & 0 \\
            \nu & 1 & 0 \\
            0 & 0 & \frac{1-\nu}{2}
        \end{bmatrix}

    For plane strain (:code:`ptype=2`) and axisymmetry (:code:`ptype=3`), :math:`\mathbf{D}` is formed as

    .. math::

        \mathbf{D} = \frac{E}{(1+\nu)(1-2\nu)}
        \begin{bmatrix}
            1-\nu & \nu & \nu & 0 \\
            \nu & 1-\nu & \nu & 0 \\
            \nu & \nu & 1-\nu & 0 \\
            0 & 0 & 0 & \frac{1}{2}(1-2\nu)
        \end{bmatrix}

    For the three dimensional case (:code:`ptype=4`), :math:`\mathbf{D}` is formed as

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
