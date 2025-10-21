.. only:: matlab

    General purpose functions
    =========================

    The general purpose functions are used for managing variables and workspace, control of output, etc. The functions listed here are a subset of the general purpose functions described in the MATLAB manual. The functions can be divided into the following groups:

    .. list-table:: General functions
        :widths: 30 120 
        :header-rows: 0

        * - help
          - Online documentation
        * - type
          - List file 
        * - what
          - Directory listing of .m-files, .mat-files and .mex-files 
        * - ...
          - Continuation 
        * - %
          - Write a comment line 
 
    .. list-table:: Variables and workspace
        :widths: 30 120 
        :header-rows: 0

        * - clear
          - Remove variables from workspace
        * - disp
          - Display a variable in matrix bank on display screen
        * - load
          - Retrieve variable from disk and load in workspace 
        * - save
          - Save workspace variables on disk 
        * - who, whos
          - List directory of variables in matrix bank

    .. list-table:: Files and command window
        :widths: 30 120 
        :header-rows: 0

        * - diary
          - Save session in a disk file
        * - echo
          - Control output on the display screen
        * - format
          - Control the output display format 
        * - quit
          - Terminate CALFEM session

    General functions
    -----------------

    help
    ^^^^

    .. index:: help

    :Purpose:
        Display a description of purpose and syntax for a specific function.

    :Syntax:
        .. code:: matlab

            help function_name

    :Description:
        :code:`help` provides an online documentation for the specified function.

    :Example:
        Typing

        .. code:: matlab

            >> help spring1e

        yields

        .. code:: none

            Ke=spring1e(ep)
            -------------------------------------------------------------
            PURPOSE
            Compute element stiffness matrix for spring (analog) element.

            INPUT:  ep = [k]; spring stiffness or analog quantity.

            OUTPUT: Ke : stiffness matrix, dim(Ke)= 2 x 2
            -------------------------------------------------------------

    .. Note::

        This is a MATLAB built-in function. For more information about the :code:`help` function, type :code:`help help`.

    type
    ^^^^

    .. index:: type

    :Purpose:
        List file.

    :Syntax:
        .. code:: matlab

            type filename

    :Description:
        :code:`type filename` lists the specified file. Use path names in the usual way for your operating system. If a filename extension is not given, :code:`.m` is added by default. This makes it convenient to list the contents of :code:`.m`-files on the screen.

    .. Note::

        This is a MATLAB built-in function. For more information about the :code:`type` function, type :code:`help type`.

    what
    ^^^^

    .. index:: what

    :Purpose:
        Directory listing of :code:`.m`-files, :code:`.mat`-files and :code:`mex`-files.

    :Syntax:
        .. code:: matlab

            what
            what dirname

    :Description:
        :code:`what` lists the :code:`.m`-files, :code:`.mat`-files and :code:`.mex`-files in the current directory.

        :code:`what dirname` lists the files in directory :code:`dirname` in the MATLAB search path. The syntax of the path depends on your operating system.

    .. Note::
        
        This is a MATLAB built-in function. For more information about the :code:`what` function, type :code:`help what`.

    ...
    ^^^

    :Purpose:
        Continuation.

    :Syntax:
        .. code:: matlab

            ...

    :Description:
        An expression can be continued on the next line by using :code:`...` .

    .. Note::
        
        This is a MATLAB built-in function.

    %
    ^

    :Purpose:
        Write a comment line.

    :Syntax:
        .. code:: matlab

            % arbitrary text

    :Description:
        An arbitrary text can be written after the symbol :code:`\%`.

    .. Note::
        
        This is a MATLAB built-in character.

    Variables and workspace
    -----------------------

    clear
    ^^^^^

    .. index:: clear

    :Purpose:
        Remove variables from workspace.

    :Syntax:
        .. code:: matlab

            clear
            clear name1 name2 name3 ...

    :Description:
        :code:`clear` removes all variables from workspace.

        :code:`clear name1 name2 name3 ...` removes specified variables from workspace.

    .. Note::
        
        This is a MATLAB built-in function. For more information about the :code:`clear` function, type :code:`help clear`.

    .. _diary:

    disp
    ^^^^

    .. index:: disp

    :Purpose:
        Display a variable in matrix bank on display screen.

    :Syntax:
        .. code:: matlab

            disp(A)

    :Description:
        :code:`disp(A)` displays the matrix :code:`A` on the display screen.

    .. Note::
        
        This is a MATLAB built-in function. For more information about the :code:`disp` function, type :code:`help disp`.

    load
    ^^^^

    .. index:: load

    :Purpose:
        Retrieve variable from disk and load in workspace.

    :Syntax:
        .. code:: matlab

            load filename
            load filename.ext

    :Description:
        :code:`load filename` retrieves the variables from the binary file :code:`filename.mat`.

        :code:`load filename.ext` reads the ASCII file :code:`filename.ext` with numeric data arranged in :math:`m` rows and :math:`n` columns. The result is an :math:`m \times n` matrix residing in workspace with the name :code:`filename`, i.e. with the extension stripped.

    .. Note::
        
        This is a MATLAB built-in function. For more information about the :code:`load` function, type :code:`help load`.

    save
    ^^^^

    .. index:: save

    :Purpose:
        Save workspace variables on disk.

    :Syntax:
        .. code:: matlab

            save filename
            save filename variables
            save filename variables -ascii

    :Description:
        :code:`save filename` writes all variables residing in workspace in a binary file named :code:`filename.mat`.

        :code:`save filename variables` writes named variables, separated by blanks, in a binary file named :code:`filename.mat`.

        :code:`save filename variables -ascii` writes named variables in an ASCII file named :code:`filename`.

    .. Note::
        
        This is a MATLAB built-in function. For more information about the :code:`save` function, type :code:`help save`.

    who, whos
    ^^^^^^^^^

    .. index:: who
    .. index:: whos

    :Purpose:
        List directory of variables in matrix bank.

    :Syntax:
        .. code:: matlab

            who
            whos

    :Description:
        :code:`who` lists the variables currently in memory.

        :code:`whos` lists the current variables and their size.

    :Examples:

        .. code:: matlab

            who

            Your variables are:

            A       B       C       K       M       X       k       lambda

        .. code:: matlab

            whos

            Name         Size            Bytes  Class     Attributes

            A            3x3                72  double              
            B            3x3                72  double              
            C            3x3                72  double              
            K           20x20             3200  double              
            M           20x20             3200  double              
            X           20x20             3200  double              
            k            1x1                 8  double              
            lambda      20x1               160  double              

    .. Note::
        
        These are MATLAB built-in functions. For more information about the functions, type :code:`help who` or :code:`help whos`.


    Files and command window
    ------------------------

    diary
    ^^^^^

    .. index:: diary

    :Purpose:
        Save session in a disk file.

    :Syntax:
        .. code:: matlab

            diary filename
            diary off
            diary on

    :Description:
        :code:`diary filename` writes a copy of all subsequent keyboard input and most of the resulting output (but not graphs) on the named file. If the file :code:`filename` already exists, the output is appended to the end of that file.

        :code:`diary off` stops storage of the output.

        :code:`diary on` turns it back on again, using the current filename or default filename :code:`diary` if none has yet been specified.

        The :code:`diary` function may be used to store the current session for later runs. To make this possible, finish each command line with semicolon ';' to avoid the storage of intermediate results on the named diary file.

    .. Note::
        
        This is a MATLAB built-in function. For more information about the :code:`diary` function, type :code:`help diary`.

    .. _disp:


    .. _echo:

    echo
    ^^^^

    .. index:: echo

    :Purpose:
        Control output on the display screen.

    :Syntax:
        .. code:: matlab

            echo on
            echo off
            echo

    :Description:
        :code:`echo on` turns on echoing of commands inside Script-files.

        :code:`echo off` turns off echoing.

        :code:`echo` by itself toggles the echo state.

    .. Note::
        
        This is a MATLAB built-in function. For more information about the :code:`echo` function, type :code:`help echo`.

    .. _format:

    format
    ^^^^^^

    .. index:: format

    :Purpose:
        Control the output display format.

    :Syntax:
        See the listing below.

    :Description:
        :code:`format` controls the output format. By default, MATLAB displays numbers in a short format with five decimal digits.

    .. list-table::
        :widths: 21 20 25
        :header-rows: 1

        * - Command
          - Result
          - Example
        * - :code:`format short`
          - 5 digit scaled fix point
          - :code:`3.1416`
        * - :code:`format short`
          - 16 digit scaled fix point
          - :code:`3.141592653589793`
        * - :code:`format short e`
          - 5 digit floating point
          - :code:`3.1416e+00`
        * - :code:`format long e`
          - 16 digit floating point 
          - :code:`3.141592653589793e+00`
   
    .. Note::
        
        This is a MATLAB built-in function. For more information about the :code:`format` function, type :code:`help format`.

    quit
    ^^^^

    .. index:: quit

    :Purpose:
        Terminate CALFEM session.

    :Syntax:
        .. code:: matlab

            quit

    :Description:
        :code:`quit` terminates CALFEM without saving the workspace.

    .. Note::
        
        This is a MATLAB built-in function. For more information about the :code:`quit` function, type :code:`help quit`.


