flw3i8s
^^^^^^^

:Purpose:
    Compute heat flux and temperature gradients in an
    8 node isoparametric heat flow element.

:Syntax:
    .. code:: matlab
        
        [es, et, eci] = flw3i8s(ex, ey, ez, ep, D, ed)

:Description:
    ``flw3i8s`` computes the heat flux vector ``es`` and the temperature
    gradient ``et`` (or corresponding quantities)
    in an 8 node isoparametric heat flow element.

    The input variables :math:`\mathbf{ex}`, :math:`\mathbf{ey}`, :math:`\mathbf{ez}`, :math:`\mathbf{ep}` and
    the matrix :math:`\mathbf{D}` are defined in ``flw3i8e``.
    The vector :math:`\mathbf{ed}` contains the nodal temperatures :math:`\mathbf{a}^e`
    of the element and is obtained by the function ``extract`` as

    .. math::

        \mathbf{ed} = (\mathbf{a}^e)^T = [\,T_1\;\; T_2\;\; T_3\;\;\dots\;\; T_8\,]

    The output variables

    .. math::

        \mathbf{es} = \bar{\mathbf{q}}^T =
        \begin{bmatrix}
        q^1_x & q^1_y  & q^1_z \\
        q^2_x & q^2_y  & q^2_z \\
        \vdots  &  \vdots   &  \vdots\\
        q^{n^3}_x  & q^{n^3}_y  & q^{n^3}_z
        \end{bmatrix}

    .. math::

        \mathbf{et} = (\bar {\nabla} T)^T =
        \begin{bmatrix}
        \frac{\partial T}{\partial x}^1 &
        \frac{\partial T}{\partial y}^1 &
        \frac{\partial T}{\partial z}^1\\
        \frac{\partial T}{\partial x}^2 &
        \frac{\partial T}{\partial y}^2 &
        \frac{\partial T}{\partial z}^2\\
        \vdots & \vdots & \vdots \\
        \frac{\partial T}{\partial x}^{n^3} &
        \frac{\partial T}{\partial y}^{n^3} &
        \frac{\partial T}{\partial z}^{n^3}
        \end{bmatrix}
        \qquad
        \mathbf{eci} =
        \begin{bmatrix}
        x_1 & y_1 & z_1 \\
        x_2 & y_2 & z_2 \\
        \vdots  &  \vdots &  \vdots \\
        x_{n^3} & y_{n^3} & z_{n^3}
        \end{bmatrix}

    contain the heat flux, the temperature gradient,
    and the coordinates of the integration points.
    The index :math:`n` denotes the number of integration points
    used within the element, see ``flw3i8e``.

:Theory:
    The temperature gradient and the heat flux are computed according to

    .. math::

        \nabla T = \mathbf{B}^e\,\mathbf{a}^e

    .. math::

        \mathbf{q} = - \mathbf{D} \nabla T

    where the matrices :math:`\mathbf{D}`, :math:`\mathbf{B}^e`, and :math:`\mathbf{a}^e`
    are described in ``flw3i8e``, and where the integration points
    are chosen as evaluation points.
