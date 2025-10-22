.. _coordxtr:
.. index:: 
   single: coordxtr
   single: coordinate extraction
   single: element coordinates
   single: geometry utilities
   pair: finite element; coordinates
   pair: geometry; extraction
   pair: element; coordinates
   pair: mesh; utilities

coordxtr
^^^^^^^^

:Purpose:  

    Extract element coordinates from a global coordinate matrix.

    .. only:: html

        .. figure:: images/COORD.svg
            :width: 70%
            :align: center

    .. only:: latex

        .. figure:: images/COORD.svg
            :width: 70%
            :align: center

:Syntax:  

.. only:: matlab

    .. code-block:: matlab
       
        [Ex, Ey, Ez] = coordxtr(Edof, Coord, Dof, nen)

.. only:: python

    .. code-block:: python

        Ex, Ey, Ez = cfc.coordxtr(Edof, Coord, Dof, nen)

:Description:  

    :code:`coordxtr` extracts element nodal coordinates from the global coordinate matrix :code:`Coord` for elements with equal numbers of element nodes and dof's.

    Input variables are the element topology matrix :code:`Edof`, defined in :code:`assem`, the global coordinate matrix :code:`Coord`, the global topology matrix :code:`Dof`, and the number of element nodes :math:`nen` in each element.

    :code:`Coord`:math:`= \begin{bmatrix}
    x_1 & y_1 & [z_1] \\
    x_2 & y_2 & [z_2] \\
    x_3 & y_3 & [z_3] \\
    \vdots & \vdots & \vdots \\
    x_n & y_n & [z_n]
    \end{bmatrix}`
    :math:`\qquad`
    :code:`Dof`:math:`= \begin{bmatrix}
    k_1 & l_1 & \ldots & m_1 \\
    k_2 & l_2 & \ldots & m_2 \\
    k_3 & l_3 & \ldots & m_3 \\
    \vdots & \vdots & \ldots & \vdots \\
    k_n & l_n & \ldots & m_n
    \end{bmatrix}`
    :math:`\qquad`
    :code:`nen`:math:`= [\;nen\;]`

    The nodal coordinates defined in row :math:`i` of :code:`Coord` correspond to the degrees of freedom of row :math:`i` in :code:`Dof`. The components :math:`k_i`, :math:`l_i` and :math:`m_i` define the degrees of freedom of node :math:`i`, and :math:`n` is the number of global nodes for the considered part of the FE-model.

    The output variables :code:`Ex`, :code:`Ey`, and :code:`Ez` are matrices defined according to

    :code:`Ex`:math:`= \begin{bmatrix}
    x_1^1 & x_2^1 & x_3^1 & \ldots & x_{nen}^1 \\
    x_1^2 & x_2^2 & x_3^2 & \ldots & x_{nen}^2 \\
    \vdots & \vdots & \vdots & \vdots & \vdots \\
    x_1^{nel} & x_2^{nel} & x_3^{nel} & \ldots & x_{nen}^{nel}
    \end{bmatrix}`

    where row :math:`i` gives the :math:`x`-coordinates of the element defined in row :math:`i` of :code:`Edof`, and where :math:`nel` is the number of considered elements.

    The element coordinate data extracted by the function :code:`coordxtr` can be used for plotting purposes and to create input data for the element stiffness functions.

..
    .. note::
        For the two dimensional beam element, the :code:`extract_ed` function will extract six nodal displacements for each element given in the first column vector in :code:`Edof` and store them in the variable :code:`ed` as

        :code:`ed`:math:`= \begin{bmatrix}
        u_1 & u_2 & u_3 & u_4 & u_5 & u_6 \\
        u_1 & u_2 & u_3 & u_4 & u_5 & u_6 \\
        \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
        u_1 & u_2 & u_3 & u_4 & u_5 & u_6
        \end{bmatrix}`

