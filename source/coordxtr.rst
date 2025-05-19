coordxtr - Extract element coordinates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index:: coordxtr

**Purpose:**  

Extract element coordinates from a global coordinate matrix.

.. figure:: images/COORD.png
    :width: 70%
    :align: center

**Syntax:**  

.. code:: matlab
    
    [Ex, Ey, Ez] = coordxtr(Edof, Coord, Dof, nen)

**Description:**  

``coordxtr`` extracts element nodal coordinates from the global coordinate matrix ``Coord`` for elements with equal numbers of element nodes and dof's.

Input variables are the element topology matrix ``Edof``, defined in ``assem``, the global coordinate matrix ``Coord``, the global topology matrix ``Dof``, and the number of element nodes ``nen`` in each element.

.. math::

    \mathbf{Coord} = \begin{bmatrix}
    x_1 & y_1 & [z_1] \\
    x_2 & y_2 & [z_2] \\
    x_3 & y_3 & [z_3] \\
    \vdots & \vdots & \vdots \\
    x_n & y_n & [z_n]
    \end{bmatrix}
    \qquad
    \mathbf{Dof} = \begin{bmatrix}
    k_1 & l_1 & \ldots & m_1 \\
    k_2 & l_2 & \ldots & m_2 \\
    k_3 & l_3 & \ldots & m_3 \\
    \vdots & \vdots & \ldots & \vdots \\
    k_n & l_n & \ldots & m_n
    \end{bmatrix}
    \qquad
    nen = [\;nen\;]

The nodal coordinates defined in row *i* of ``Coord`` correspond to the degrees of freedom of row *i* in ``Dof``. The components :math:`k_i`, :math:`l_i` and :math:`m_i` define the degrees of freedom of node *i*, and *n* is the number of global nodes for the considered part of the FE-model.

The output variables ``Ex``, ``Ey``, and ``Ez`` are matrices defined according to

.. math::

    \mathbf{Ex} = \begin{bmatrix}
    x_1^1 & x_2^1 & x_3^1 & \ldots & x_{nen}^1 \\
    x_1^2 & x_2^2 & x_3^2 & \ldots & x_{nen}^2 \\
    \vdots & \vdots & \vdots & \vdots & \vdots \\
    x_1^{nel} & x_2^{nel} & x_3^{nel} & \ldots & x_{nen}^{nel}
    \end{bmatrix}

where row *i* gives the *x*-coordinates of the element defined in row *i* of ``Edof``, and where *nel* is the number of considered elements.

The element coordinate data extracted by the function ``coordxtr`` can be used for plotting purposes and to create input data for the element stiffness functions.

.. note::
    For the two dimensional beam element, the ``extract`` function will extract six nodal displacements for each element given in the first column vector in ``Edof`` and store them in the variable ``ed`` as

    .. math::

        \mathbf{ed} = \begin{bmatrix}
        u_1 & u_2 & u_3 & u_4 & u_5 & u_6 \\
        u_1 & u_2 & u_3 & u_4 & u_5 & u_6 \\
        \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
        u_1 & u_2 & u_3 & u_4 & u_5 & u_6
        \end{bmatrix}

