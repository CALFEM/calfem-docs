disp_h[1-3]
^^^^^^^^^^^

:Purpose:
    Display text heading in either markdown or HTML, depending if running in a console or in a Jupyter environment (HTML).

:Syntax:

    .. code-block:: python

        cfu.disp_h1(msg)
        cfu.disp_h2(msg)
        cfu.disp_h3(msg)


:Description:
    :code:`disp_h1` displays ``msg`` as a heading in markdown if running in a console or as a HTML heading if running in a Jupyter environment. The following code
    
    .. code:: python

        cfu.disp_h1("Element 1 stiffness matrix:")

    displays the following output in a console

    .. code:: python

        # Element 1 stiffness matrix:

    and

    .. code:: html

        <h1>Element 1 stiffness matrix:</h1>

    When running in a Jupyter environment, but will be rendered as a section header.


