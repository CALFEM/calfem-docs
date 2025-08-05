************
Introduction
************

.. only:: matlab

    CALFEM is a MATLAB toolbox for finite element applications. This manual concerns mainly the finite element functions, but it also contains descriptions of some often-used MATLAB functions.

    The finite element analysis can be carried out either interactively or in a batch-oriented fashion. In the interactive mode, the functions are evaluated one by one in the MATLAB command window. In the batch-oriented mode, a sequence of functions is written in a file named `.m` file and evaluated by writing the file name in the command window. The batch-oriented mode is a more flexible way of performing finite element analysis because the `.m` file can be written in an ordinary editor. This way of using CALFEM is recommended because it gives a structured organization of the functions. Changes and reruns are also easily executed in the batch-oriented mode.

.. only:: python

    CALFEM is a Python package for finite element applications. This manual concerns mainly the finite element functions, but it also contains descriptions of some often-used Python functions.

    The finite element analysis can be carried out either interactively or in a batch-oriented fashion. In the interactive mode, the functions are evaluated one by one in an interactive Python session. In the batch-oriented mode, a sequence of functions is written in a file named `.py` file and evaluated by calling python interpreter with the filename as an argument. The batch-oriented mode is a more flexible way of performing finite element analysis because the `.py` file can be written in an ordinary editor. This way of using CALFEM is recommended because it gives a structured organization of the functions. Changes and reruns are also easily executed in the batch-oriented mode.

A command line typically consists of functions for vector and matrix operations, calls to functions in the CALFEM finite element library, or commands for workspace operations. An example of a command line for a matrix operation is:

.. only:: matlab

    .. code-block:: matlab

        C = A + B'

    where the two-by-two matrices :code:`A` and :code:`B` are added together, and the result is stored in matrix :code:`C`. The matrix :code:`B'` is the transpose of  :code:`B`. In MATLAB, the transpose operator is denoted by a single quote `'`.

.. only:: python

    .. code-block:: python

        C = A + B.T

    where the two-by-two matrices :code:`A` and :code:`B` are added together, and the result is stored in matrix :code:`C`. The matrix :code:`B.T` is the transpose of  :code:`B`. In MATLAB, the transpose operator is denoted by a  `T`.

An example of a call to the element library is:

.. code-block:: matlab

    Ke = spring1e(k)

where the two-by-two element stiffness matrix :math:`K^e` is computed for a spring element with spring stiffness :code:`k`, and is stored in the variable :code:`Ke`.  The input argument is given within parentheses `( )` after the name of the function. Some functions have multiple input arguments and/or multiple output arguments. For example:

.. code-block:: matlab

    [lambda, X] = eigen(K, M)

computes the eigenvalues and eigenvectors of a pair of matrices 
:code:`K` and :code:`M`. The output variables - the eigenvalues stored in the vector :code:`lambda` and the corresponding eigenvectors stored in the matrix :code:`X` - are surrounded by brackets `[ ]` and separated by commas. The input arguments are given inside the parentheses and also separated by commas.

The statement:

.. only:: matlab

    .. code-block:: matlab

        help function

.. only:: python

    .. code-block:: python

        help(function)

provides information about the purpose and syntax for the specified function.

The available functions are organized in groups as follows.  Each group is described in a separate chapter.

.. +--------------------------+--------------------------------------------------+
.. | Groups of functions      |                                                  |
.. +--------------------------+--------------------------------------------------+
.. | General purpose commands | For managing variables, workspace,               |
.. |                          | output, etc.                                     |
.. +--------------------------+--------------------------------------------------+
.. | Matrix functions         | For matrix handling                              |
.. +--------------------------+--------------------------------------------------+
.. | Material functions       | For computing material matrices                  |
.. +--------------------------+--------------------------------------------------+
.. | Element functions        | For computing element matrices and element       |
.. |                          | forces                                           |
.. +--------------------------+--------------------------------------------------+
.. | System functions         | For setting up and solving systems of            |
.. |                          | equations                                        |
.. +--------------------------+--------------------------------------------------+
.. | Statement functions      | For algorithm definitions                        |
.. +--------------------------+--------------------------------------------------+
.. | Graphics functions       | For plotting                                     |
.. +--------------------------+--------------------------------------------------+


