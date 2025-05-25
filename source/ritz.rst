ritz
^^^^

:Purpose:

    Compute approximative eigenvalues and eigenvectors by the Lanczos method.

:Syntax:

    .. code-block:: matlab

        L = ritz(K, M, f, m)
        L = ritz(K, M, f, m, b)
        [L, X] = ritz(K, M, f, m)
        [L, X] = ritz(K, M, f, m, b)

:Description:

    ``ritz`` computes, by the use of the Lanczos algorithm, ``m`` approximative eigenvalues and ``m`` corresponding eigenvectors for a given pair of *n*-by-*n* matrices ``K`` and ``M`` and a given non-zero starting vector ``f``.

    If certain rows and columns in matrices :math:`\mathbf{K}` and :math:`\mathbf{M}` are to be eliminated in computing the eigenvalues, :math:`\mathbf{b}` must be given in the command. The rows (and columns) to be eliminated are described in the vector :math:`\mathbf{b}` defined as

    .. math::

        \mathbf{b} = \begin{bmatrix}
        dof_1 \\
        dof_2 \\
        \vdots \\
        dof_{nb}
        \end{bmatrix}

    .. note::

        If the number of vectors, ``m``, is chosen less than the total number of degrees-of-freedom, :math:`n`, only about the first ``m/2`` Ritz vectors are good approximations of the true eigenvectors. Recall that the Ritz vectors satisfy the ``M``-orthonormality condition

    .. math::

        \mathbf{X}^T \mathbf{M} \mathbf{X} = \mathbf{I}

    where :math:`\mathbf{I}` is the identity matrix.
