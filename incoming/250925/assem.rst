assem
^^^^^

:Purpose:

    Assemble element matrices.

    .. figure:: images/ASSEM.png
        :width: 70%
        :align: center

:Syntax:

    .. code:: matlab

        K = assem(edof, K, Ke)
        [K, f] = assem(edof, K, Ke, f, fe)


:Description:

    ``assem`` adds the element stiffness matrix :math:`\mathbf{K}^e`, stored in ``Ke``, to the structure stiffness matrix :math:`\mathbf{K}`, stored in ``K``, according to the topology matrix :math:`\mathbf{edof}`.

    The element topology matrix :math:`\mathbf{edof}` is defined as

    .. math::

        \mathbf{edof} = [el \quad  \underbrace{dof_1\quad dof_2\quad\ldots \quad dof_{ned}}_{\text{global dof.}} ]

    where the first column contains the element number, and columns 2 to :math:`(ned+1)` contain the corresponding global degrees of freedom (:math:`ned` = number of element degrees of freedom).

    In the case where the matrix :math:`\mathbf{K}^e` is identical for several elements, assembling of these can be carried out simultaneously. Each row in :math:`\mathbf{Edof}` then represents one element, i.e. :math:`nel` is the total number of considered elements.

    .. math::

        \mathbf{Edof} = \left. \left[
        \begin{array}{c}
        el_1 \\
        el_2 \\
        \vdots \\
        el_{nel}
        \end{array}
        \quad
        \begin{array}{cccccc}
        dof_1 & dof_2 & \cdots & \cdots & \cdots & dof_{ned} \\
        dof_1 & dof_2 & \cdots & \cdots & \cdots & dof_{ned} \\
        \vdots & \vdots &  &  &  & \vdots \\
        dof_1 & dof_2 & \cdots & \cdots & \cdots & dof_{ned}
        \end{array}
        \right] \right\} \text{one row for each element}

    If :math:`\mathbf{fe}` and :math:`\mathbf{f}` are given in the function, the element load vector :math:`\mathbf{f}^e` is also added to the global load vector :math:`\mathbf{f}`.
