Statements and macros
====================

.. only:: matlab

    Statements describe algorithmic actions that can be executed. There are two different types of control statements, conditional and repetitive. The first group defines conditional jumps whereas the latter one defines repetition until a conditional statement is fulfilled. Macros are used to define new functions to the MATLAB or CALFEM structure, or to store a sequence of statements in an .m-file.

.. only:: python

    Statements describe algorithmic actions that can be executed. There are two different types of control statements, conditional and repetitive. The first group defines conditional jumps whereas the latter one defines repetition until a conditional statement is fulfilled. In Python, functions and modules are used to define new functionality or to store a sequence of statements in .py files.

Control statements
------------------

.. only:: matlab

    +-------------+--------------------------------+
    | ``if``      | Conditional jump               |
    +-------------+--------------------------------+
    | ``for``     | Initiate a loop                |
    +-------------+--------------------------------+
    | ``while``   | Define a conditional loop      |
    +-------------+--------------------------------+

.. only:: python

    +-------------+--------------------------------+
    | ``if``      | Conditional jump               |
    +-------------+--------------------------------+
    | ``for``     | Iterate over sequences         |
    +-------------+--------------------------------+
    | ``while``   | Define a conditional loop      |
    +-------------+--------------------------------+

Macros and Functions
--------------------

.. only:: matlab

    +-------------+--------------------------------+
    | ``function``| Define a new function          |
    +-------------+--------------------------------+
    | ``script``  | Store a sequence of statements |
    +-------------+--------------------------------+

.. only:: python

    +-------------+--------------------------------+
    | ``def``     | Define a new function          |
    +-------------+--------------------------------+
    | ``module``  | Store functions and statements |
    +-------------+--------------------------------+

.. only:: matlab

    if
    ^^

    .. index:: if

    :Purpose:

        Conditional jump.

    :Syntax:

    .. code-block:: matlab

        if condition
            statements
        elseif condition
            statements
        else
            statements
        end

    :Description:

        The ``if`` statement allows conditional execution of code blocks. The ``condition`` is evaluated and if true (nonzero), the corresponding ``statements`` are executed.

    :Examples:

        Simple if statement:

        .. code-block:: matlab

            if x > 0
                y = sqrt(x);
            else
                y = 0;
            end

        Multiple conditions:

        .. code-block:: matlab

            if x > 0
                result = 'positive';
            elseif x < 0
                result = 'negative';
            else
                result = 'zero';
            end

    :Note:

        In MATLAB, any nonzero value is considered true, and zero is false.

.. only:: python

    if
    ^^

    .. index:: if

    :Purpose:

        Conditional jump.

    :Syntax:

    .. code-block:: python

        if condition:
            statements
        elif condition:
            statements
        else:
            statements

    :Description:

        The ``if`` statement allows conditional execution of code blocks. The ``condition`` is evaluated and if ``True``, the corresponding ``statements`` are executed.

    :Examples:

        Simple if statement:

        .. code-block:: python

            if x > 0:
                y = np.sqrt(x)
            else:
                y = 0

        Multiple conditions:

        .. code-block:: python

            if x > 0:
                result = 'positive'
            elif x < 0:
                result = 'negative'
            else:
                result = 'zero'

    :Note:

        Python uses ``elif`` instead of ``elseif``, and requires colons and indentation instead of ``end``.

.. only:: matlab

    for
    ^^^

    .. index:: for

    :Purpose:

        Initiate a loop.

    :Syntax:

    .. code-block:: matlab

        for variable = expression
            statements
        end

    :Description:

        The ``for`` loop repeats ``statements`` for each value in the ``expression``. The ``variable`` takes on each value from the expression in sequence.

    :Examples:

        Simple counting loop:

        .. code-block:: matlab

            for i = 1:10
                fprintf('Iteration %d\n', i);
            end

        Loop over array elements:

        .. code-block:: matlab

            A = [1, 4, 9, 16];
            for element = A
                disp(element);
            end

        Nested loops:

        .. code-block:: matlab

            for i = 1:3
                for j = 1:3
                    A(i,j) = i + j;
                end
            end

    :Note:

        The loop variable takes on the values column by column if the expression is a matrix.

.. only:: python

    for
    ^^^

    .. index:: for

    :Purpose:

        Iterate over sequences.

    :Syntax:

    .. code-block:: python

        for variable in iterable:
            statements

    :Description:

        The ``for`` loop iterates over elements in an ``iterable`` (list, array, range, etc.). The ``variable`` takes on each value from the iterable in sequence.

    :Examples:

        Simple counting loop:

        .. code-block:: python

            for i in range(1, 11):  # 1 to 10
                print(f'Iteration {i}')

        Loop over array elements:

        .. code-block:: python

            A = np.array([1, 4, 9, 16])
            for element in A:
                print(element)

        Nested loops:

        .. code-block:: python

            A = np.zeros((3, 3))
            for i in range(3):
                for j in range(3):
                    A[i, j] = i + j

    :Note:

        Python uses ``range()`` for numeric sequences and requires colons and indentation.

.. only:: matlab

    while
    ^^^^^

    .. index:: while

    :Purpose:

        Define a conditional loop.

    :Syntax:

    .. code-block:: matlab

        while condition
            statements
        end

    :Description:

        The ``while`` loop repeats ``statements`` as long as the ``condition`` remains true (nonzero).

    :Examples:

        Simple while loop:

        .. code-block:: matlab

            i = 1;
            while i <= 10
                fprintf('Count: %d\n', i);
                i = i + 1;
            end

        Convergence loop:

        .. code-block:: matlab

            error = 1;
            tolerance = 1e-6;
            while error > tolerance
                % ... computation ...
                error = abs(new_value - old_value);
            end

    :Note:

        Be careful to ensure the condition eventually becomes false to avoid infinite loops.

.. only:: python

    while
    ^^^^^

    .. index:: while

    :Purpose:

        Define a conditional loop.

    :Syntax:

    .. code-block:: python

        while condition:
            statements

    :Description:

        The ``while`` loop repeats ``statements`` as long as the ``condition`` remains ``True``.

    :Examples:

        Simple while loop:

        .. code-block:: python

            i = 1
            while i <= 10:
                print(f'Count: {i}')
                i += 1

        Convergence loop:

        .. code-block:: python

            error = 1
            tolerance = 1e-6
            while error > tolerance:
                # ... computation ...
                error = abs(new_value - old_value)

    :Note:

        Be careful to ensure the condition eventually becomes ``False`` to avoid infinite loops.

.. only:: matlab

    function
    ^^^^^^^^

    .. index:: function

    :Purpose:

        Define a new function.

    :Syntax:

    .. code-block:: matlab

        function [output1, output2, ...] = function_name(input1, input2, ...)
            statements
        end

    :Description:

        The ``function`` keyword defines a new function with specified inputs and outputs. Functions should be saved in .m files with the same name as the function.

    :Examples:

        Simple function:

        .. code-block:: matlab

            function y = square(x)
                y = x^2;
            end

        Multiple inputs and outputs:

        .. code-block:: matlab

            function [sum_val, diff_val] = add_subtract(a, b)
                sum_val = a + b;
                diff_val = a - b;
            end

        Function with no outputs:

        .. code-block:: matlab

            function plot_data(x, y)
                figure;
                plot(x, y);
                xlabel('x');
                ylabel('y');
            end

    :Note:

        MATLAB functions must be saved in .m files. The filename should match the function name.

.. only:: python

    def
    ^^^

    .. index:: def

    :Purpose:

        Define a new function.

    :Syntax:

    .. code-block:: python

        def function_name(input1, input2, ...):
            statements
            return output1, output2, ...

    :Description:

        The ``def`` keyword defines a new function with specified inputs. Use ``return`` to specify outputs. Functions can be defined in .py files or interactively.

    :Examples:

        Simple function:

        .. code-block:: python

            def square(x):
                return x**2

        Multiple inputs and outputs:

        .. code-block:: python

            def add_subtract(a, b):
                sum_val = a + b
                diff_val = a - b
                return sum_val, diff_val

        Function with no return value:

        .. code-block:: python

            def plot_data(x, y):
                plt.figure()
                plt.plot(x, y)
                plt.xlabel('x')
                plt.ylabel('y')
                plt.show()

    :Note:

        Python functions use ``def`` and ``return``. Multiple return values are returned as tuples.

.. only:: matlab

    script
    ^^^^^^

    .. index:: script

    :Purpose:

        Store a sequence of statements.

    :Syntax:

    .. code-block:: matlab

        % filename: my_script.m
        % This is a script file
        statements

    :Description:

        Scripts are .m files that contain a sequence of MATLAB statements. They execute in the base workspace and can access and modify variables there.

    :Examples:

        Simple script (saved as ``analysis.m``):

        .. code-block:: matlab

            % Analysis script
            load data.mat;
            results = process_data(data);
            plot(results);
            save results.mat results;

        Script with calculations:

        .. code-block:: matlab

            % Calculate beam deflection
            L = 10;  % beam length
            E = 200e9;  % Young's modulus
            I = 1e-4;  % moment of inertia
            q = 1000;  % distributed load
            
            % Maximum deflection
            w_max = q * L^4 / (8 * E * I);
            fprintf('Maximum deflection: %.2e m\n', w_max);

    :Note:

        Scripts share the workspace with the command line. Variables created in scripts remain accessible.

.. only:: python

    module
    ^^^^^^

    .. index:: module

    :Purpose:

        Store functions and statements.

    :Syntax:

    .. code-block:: python

        # filename: my_module.py
        """Module documentation"""
        
        import numpy as np
        
        def function1():
            # function definition
            pass
            
        # module-level code
        statements

    :Description:

        Modules are .py files that contain Python code. They can include functions, classes, and executable statements. Use ``import`` to access module contents.

    :Examples:

        Simple module (saved as ``analysis.py``):

        .. code-block:: python

            """Data analysis module"""
            import numpy as np
            import matplotlib.pyplot as plt
            
            def load_data(filename):
                return np.loadtxt(filename)
            
            def plot_results(data):
                plt.figure()
                plt.plot(data)
                plt.show()
            
            # Module-level code (runs when imported)
            print("Analysis module loaded")

        Using the module:

        .. code-block:: python

            import analysis
            
            data = analysis.load_data('data.txt')
            analysis.plot_results(data)

        Alternative import:

        .. code-block:: python

            from analysis import load_data, plot_results
            
            data = load_data('data.txt')
            plot_results(data)

    :Note:

        Modules create their own namespace. Use ``import`` statements to access module contents.