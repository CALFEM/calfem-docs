extract_ed
^^^^^^^^^^

:Purpose:

    Extract element nodal quantities from a global solution vector.

    .. figure:: images/EXTRA.png
        :width: 70%
        :align: center

:Syntax:

.. only:: matlab

    .. code-block:: matlab

        ed = extract_ed(edof, a)

.. only:: python

    .. code-block:: python

        ed = cfc.extract_ed(edof, a)

:Description:

    The :code:`extract_ed` function extracts element displacements or corresponding quantities :math:`\mathbf{a}^e` from the global solution vector :math:`\mathbf{a}`, stored in :code:`a`.

    Input variables are the element topology matrix :code:`edof`, defined in :code:`assem`, and the global solution vector :code:`a`.

    The output variable

    :code:`ed`:math:`= (\mathbf{a}^e)^T`

    contains the element displacement vector.

    If :code:`Edof` contains more than one element, :code:`Ed` will be a matrix

    :code:`Ed`:math:`= \begin{bmatrix}
    (\mathbf{a}^e)_1^T \\
    (\mathbf{a}^e)_2^T \\
    \vdots \\
    (\mathbf{a}^e)_{nel}^T
    \end{bmatrix}`

    where row :math:`i` gives the element displacements for the element defined in row :math:`i` of :code:`Edof`, and :math:`nel` is the total number of considered elements.

:Example:

    For the two-dimensional beam element, the :code:`extract_ed` function will extract six nodal displacements for each element given in :code:`Edof`, and create a matrix :code:`Ed` of size :math:`(nel × 6)`.

    :code:`Ed`:math:`= \begin{bmatrix}
    u_1 & u_2 & u_3 & u_4 & u_5 & u_6 \\
    u_1 & u_2 & u_3 & u_4 & u_5 & u_6 \\
    \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
    u_1 & u_2 & u_3 & u_4 & u_5 & u_6
    \end{bmatrix}`
