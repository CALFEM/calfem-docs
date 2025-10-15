.. only:: python

    General purpose functions
    =========================

    The following are general purpose functions for managing variables, workspace, and output in IPython or Python interactive sessions. These are analogous to MATLAB's general functions.

    General functions
    -----------------

    help
    ^^^^

    .. index:: help

    :Purpose:
        Display documentation for a specific function or object.

    :Syntax:
        .. code-block:: ipython

            help(function_name)
            function_name?
            function_name??

    :Description:
        :code:`help(function_name)` displays the docstring/documentation for the specified function.
        :code:`function_name?` shows a summary in IPython.
        :code:`function_name??` shows the full docstring and source if available.

    :Example:
        Typing

        .. code-block:: ipython

            help(len)
            len?
            len??

        yields documentation for the :code:`len` function.

    :Note:
        In IPython, :code:`?` and :code:`??` are convenient shortcuts.

    type
    ^^^^

    .. index:: type

    :Purpose:
        Show the type of an object.

    :Syntax:
        .. code-block:: python

            type(obj)

    :Description:
        :code:`type(obj)` returns the type of the object.

    :Note:
        To display the source code of a function in IPython, use :code:`function_name??`.

    what
    ^^^^

    .. index:: what

    :Purpose:
        List variables in the current namespace.

    :Syntax:
        .. code:: python

            %who
            %whos

    :Description:
        :code:`%who` lists variable names in the interactive namespace.
        :code:`%whos` gives a detailed list with type and info.

    :Note:
        These are IPython magic commands.

    ...
    ^^^

    :Purpose:
        Line continuation.

    :Syntax:
        .. code:: python

            ...

    :Description:
        In Python, :code:`...` is used as an Ellipsis object or for line continuation in some contexts (e.g., multi-line lambdas or function definitions). For line continuation, use the backslash :code:`\` or parentheses.

    :Note:
        In IPython, multi-line statements are handled automatically.

    #
    ^

    :Purpose:
        Write a comment line.

    :Syntax:
        .. code:: python

            # arbitrary text

    :Description:
        Any text after :code:`#` is a comment.

    :Note:
        This is standard Python syntax.

    Variables and workspace
    -----------------------

    clear
    ^^^^^

    .. index:: clear

    :Purpose:
        Remove variables from workspace.

    :Syntax:
        .. code:: python

            del var1, var2
            %reset

    :Description:
        :code:`del var1` deletes a variable.
        :code:`%reset` (IPython magic) clears all variables (asks for confirmation).

    :Note:
        Use with caution; :code:`%reset` cannot be undone.

    disp
    ^^^^

    .. index:: disp

    :Purpose:
        Display a variable.

    :Syntax:
        .. code:: python

            print(A)
            display(A)  # in Jupyter/IPython

    :Description:
        :code:`print(A)` prints the value of :code:`A`.
        :code:`display(A)` (from :code:`IPython.display`) can be used for rich display in Jupyter.

    load
    ^^^^

    .. index:: load

    :Purpose:
        Load variables from disk.

    :Syntax:
        .. code:: python

            import numpy as np
            A = np.load('filename.npy')
            data = np.loadtxt('filename.txt')

    :Description:
        Use :code:`np.load` for binary NumPy files, :code:`np.loadtxt` or :code:`pandas.read_csv` for text files.

    :Note:
        There is no direct equivalent to MATLAB's :code:`load` for .mat files, but :code:`scipy.io.loadmat` can be used for MATLAB files.

    save
    ^^^^

    .. index:: save

    :Purpose:
        Save variables to disk.

    :Syntax:
        .. code:: python

            np.save('filename.npy', A)
            np.savetxt('filename.txt', A)

    :Description:
        Use :code:`np.save` for binary, :code:`np.savetxt` for text files. For multiple variables, consider using :code:`np.savez` or :code:`pickle`.

    who, whos
    ^^^^^^^^^

    .. index:: who
    .. index:: whos

    :Purpose:
        List variables in the workspace.

    :Syntax:
        .. code:: python

            %who
            %whos

    :Description:
        :code:`%who` lists variable names.
        :code:`%whos` gives detailed info.

    :Note:
        These are IPython magic commands.

    Files and command window
    ------------------------

    diary
    ^^^^^

    .. index:: diary

    :Purpose:
        Save session output to a file.

    :Syntax:
        .. code:: python

            %logstart filename
            %logstop

    :Description:
        :code:`%logstart filename` begins logging input/output to a file.
        :code:`%logstop` stops logging.

    :Note:
        These are IPython magic commands.

    echo
    ^^^^

    .. index:: echo

    :Purpose:
        Not directly applicable in Python. For script debugging, use print statements or logging.

    :Note:
        No direct equivalent. Use :code:`print` or the :code:`logging` module.

    format
    ^^^^^^

    .. index:: format

    :Purpose:
        Control output display format.

    :Syntax:
        .. code:: python

            # For NumPy arrays:
            np.set_printoptions(precision=5)
            np.set_printoptions(precision=15, suppress=True)

    :Description:
        Use :code:`np.set_printoptions` to control NumPy array display precision.

    :Note:
        For pandas DataFrames, use :code:`pd.set_option`.

    quit
    ^^^^

    .. index:: quit

    :Purpose:
        Terminate session.

    :Syntax:
        .. code:: python

            exit()
            quit()

    :Description:
        :code:`exit()` or :code:`quit()` exits the Python interpreter or IPython session.

    :Note:
        In Jupyter, use :code:`exit()` in a cell.

