extract_ed - Extract element nodal quantities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Extract element nodal quantities from a global solution vector.

.. figure:: images/EXTRA.png
    :width: 70%
    :align: center

**Syntax**

.. code:: matlab

    ed = extract_ed(edof, a)

**Description**

The ``extract_ed`` function extracts element displacements or corresponding quantities :math:`\mathbf{a}^e` from the global solution vector :math:`\mathbf{a}`, stored in ``a``.

Input variables are the element topology matrix :math:`\mathbf{edof}`, defined in ``assem``, and the global solution vector ``a``.

The output variable

.. math::

    \mathbf{ed} = (\mathbf{a}^e)^T

contains the element displacement vector.

If :math:`\mathbf{Edof}` contains more than one element, :math:`\mathbf{Ed}` will be a matrix

.. math::

    \mathbf{Ed} = \begin{bmatrix}
        (\mathbf{a}^e)_1^T \\
        (\mathbf{a}^e)_2^T \\
        \vdots \\
        (\mathbf{a}^e)_{nel}^T
    \end{bmatrix}

where row *i* gives the element displacements for the element defined in row *i* of ``Edof``, and *nel* is the total number of considered elements.

**Example**

For the two-dimensional beam element, the ``extract`` function will extract six nodal displacements for each element given in :math:`\mathbf{Edof}`, and create a matrix ``Ed`` of size *(nel × 6)*.

.. math::

    \mathbf{Ed} = \begin{bmatrix}
        u_1 & u_2 & u_3 & u_4 & u_5 & u_6 \\
        u_1 & u_2 & u_3 & u_4 & u_5 & u_6 \\
        \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
        u_1 & u_2 & u_3 & u_4 & u_5 & u_6
    \end{bmatrix}
