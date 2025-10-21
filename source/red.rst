.. _red:
.. index:: 
   single: red
   single: matrix reduction
   single: model reduction
   single: matrix condensation
   pair: matrix; reduction
   pair: model; reduction
   pair: finite element; reduction
   pair: equation; elimination

red
^^^

:Purpose:

    Reduce the size of a square matrix by omitting rows and columns.

:Syntax:

.. only:: matlab

    .. code-block:: matlab

        B = red(A, b)
        [B, b] = red(A, b)

.. only:: python

    .. code-block:: python

        B = cfc.red(A, b)
        B, b = cfc.red(A, b)

:Description:

    :code:`B = red(A, b)` reduces the square matrix :code:`A` to a smaller matrix :code:`B` by omitting rows and columns of :code:`A`. The indices for rows and columns to be omitted are specified by the column vector :code:`b`.

:Example:

    Assume that the matrix :code:`A` is defined as

    :code:`A`:math:`= \begin{bmatrix}
    1 & 2 & 3 & 4 \\
    5 & 6 & 7 & 8 \\
    9 & 10 & 11 & 12 \\
    13 & 14 & 15 & 16
    \end{bmatrix}`

    and :code:`b` as

    :code:`b`:math:`= \begin{bmatrix}
    2 \\
    4
    \end{bmatrix}`

    The statement :code:`B = red(A, b)` results in the matrix

    :code:`B`:math:`= \begin{bmatrix}
    1 & 3 \\
    9 & 11
    \end{bmatrix}`