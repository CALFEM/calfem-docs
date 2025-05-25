red
^^^

:Purpose:

    Reduce the size of a square matrix by omitting rows and columns.

:Syntax:

    .. code:: matlab

        B = red(A, b)
        [B, b] = red(A, b)

:Description:

    ``B = red(A, b)`` reduces the square matrix ``A`` to a smaller matrix ``B`` by omitting rows and columns of ``A``. The indices for rows and columns to be omitted are specified by the column vector ``b``.

:Example:

    Assume that the matrix ``A`` is defined as

    .. math::

        A = \begin{bmatrix}
        1 & 2 & 3 & 4 \\
        5 & 6 & 7 & 8 \\
        9 & 10 & 11 & 12 \\
        13 & 14 & 15 & 16
        \end{bmatrix}

    and ``b`` as

    .. math::

        b = \begin{bmatrix}
        2 \\
        4
        \end{bmatrix}

    The statement ``B = red(A, b)`` results in the matrix

    .. math::

        B = \begin{bmatrix}
        1 & 3 \\
        9 & 11
        \end{bmatrix}