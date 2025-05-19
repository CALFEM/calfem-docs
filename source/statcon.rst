statcon - Static condensation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Purpose:**  

Reduce system of equations by static condensation.

**Syntax:**  

.. code:: matlab

    [K1, f1] = statcon(K, f)
    [K1, f1] = statcon(K, f, b)
    [K1, f1] = statcon(K, f, b, bc)

**Description:**  

``statcon`` reduces a system of equations

.. math::

    \mathbf{K}\;\mathbf{a} = \mathbf{f}

by static condensation.

The degrees of freedom to be eliminated are supplied to the function by the vector

.. math::

    \mathbf{b} = \begin{bmatrix}
    dof_1 \\
    dof_2 \\
    \vdots \\
    dof_{nb}
    \end{bmatrix}

where each row in ``b`` contains one degree of freedom to be eliminated.

The elimination gives the reduced system of equations

.. math::

    \mathbf{K}_1\;\mathbf{a}_1 = \mathbf{f}_1

where :math:`\mathbf{K}_1` and :math:`\mathbf{f}_1` are stored in ``K1`` and ``f1`` respectively.
