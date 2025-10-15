eigen
^^^^^

:Purpose:  

    Solve the generalized eigenvalue problem.

:Syntax:  

.. only:: matlab

    .. code-block:: matlab

        L = eigen(K, M)
        L = eigen(K, M, b)
        [L, X] = eigen(K, M)
        [L, X] = eigen(K, M, b)

.. only:: python

    .. code-block:: python

        L = cfc.eigen(K, M)
        L = cfc.eigen(K, M, b)
        L, X = cfc.eigen(K, M)
        L, X = cfc.eigen(K, M, b)

:Description:  

    :code:`eigen` solves the eigenvalue problem

    .. math::

        | \mathbf{K} - \lambda \mathbf{M} | = 0

    where :math:`\mathbf{K}` and :math:`\mathbf{M}` are square matrices. The eigenvalues :math:`\lambda` are stored in the vector :math:`\mathbf{L}` and the corresponding eigenvectors in the matrix :math:`\mathbf{X}`.

    If certain rows and columns in matrices :math:`\mathbf{K}` and :math:`\mathbf{M}` are to be eliminated in computing the eigenvalues, :code:`b` must be given in the function. The rows (and columns) that are to be eliminated are described in the vector :code:`b` defined as

    :code:`b`:math:`=\begin{bmatrix}
    dof_1 \\
    dof_2 \\
    \vdots \\
    dof_{nb}
    \end{bmatrix}`

    The computed eigenvalues are given in order ranging from the smallest to the largest. The eigenvectors are normalized so that

    .. math::

        \mathbf{X}^T \mathbf{M} \mathbf{X} = \mathbf{I}

    where :math:`\mathbf{I}` is the identity matrix.
