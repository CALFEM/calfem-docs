disp_array
^^^^^^^^^^

:Purpose:
    Display an array as a table.

:Syntax:

    .. code-block:: python

        cfu.disp_array(arr, headers=[], fmt=".4e", tablefmt="psql", showindex=False)


:Description:
    :code:`disp_h1` displays ``arr`` as a table with optional headers defined as a list in the ``headers`` argument. ``tablefmt`` is a string determining what kind of table format to use. Example of formats can be:

    * "plain" - No extra formatting except blanks space.
    * "psql" - Default format. Text based table with lines for colums and headers.
    * "grid" - Text based table with a stronger line after the headers.
    * "html" - Displays the text as a HTML table. This is the default if running in a Jupyter environment.

    ``fmt`` Controls the format of each array cell. ``showindex`` is a flag to display indices as the first column.

    .. code:: python

        cfu.disp_array(edof, fmt=".0f", headers=["Element", "DOF1", "DOF2", "DOF3", "DOF4"])

    displays the following output in a console

    .. code:: python

        +-----------+--------+--------+--------+
        |   Element |   DOF1 |   DOF2 |   DOF3 |
        |-----------+--------+--------+--------|
        |         1 |      2 |      3 |      4 |
        |         3 |      4 |      5 |      6 |
        +-----------+--------+--------+--------+

    In a Jupyter environment it will render an HTML table.

