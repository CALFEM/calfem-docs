eldraw2
^^^^^^^

:Purpose:
    Draw the undeformed mesh for a two dimensional structure.


:Syntax:
    .. code:: matlab

        eldraw2(Ex, Ey)
        eldraw2(Ex, Ey, plotpar)
        eldraw2(Ex, Ey, plotpar, elnum)

:Description:
    :math:`\texttt{eldraw2}` displays the undeformed mesh for a two dimensional structure.

    Input variables are the coordinate matrices :math:`\texttt{Ex}` and :math:`\texttt{Ey}` formed by the function :math:`\texttt{coordxtr}`.

    The variable :math:`\texttt{plotpar}` sets plot parameters for linetype, linecolor and node marker:

    .. math::

        \texttt{plotpar} = [\, \text{linetype} \;\; \text{linecolor} \;\; \text{nodemark} \,]

    +----------------+----------------+----------------+-----------+
    | linetype       | meaning        | linecolor      | meaning   |
    +================+================+================+===========+
    | 1              | solid line     | 1              | black     |
    +----------------+----------------+----------------+-----------+
    | 2              | dashed line    | 2              | blue      |
    +----------------+----------------+----------------+-----------+
    | 3              | dotted line    | 3              | magenta   |
    +----------------+----------------+----------------+-----------+
    |                |                | 4              | red       |
    +----------------+----------------+----------------+-----------+

    +----------------+----------------+
    | nodemark       | meaning        |
    +================+================+
    | 1              | circle         |
    +----------------+----------------+
    | 2              | star           |
    +----------------+----------------+
    | 0              | no mark        |
    +----------------+----------------+

    Default is solid black lines with circles at nodes.

    Element numbers can be displayed at the center of the element if a column vector :math:`\texttt{elnum}` with the element numbers is supplied. This column vector can be derived from the element topology matrix :math:`\texttt{Edof}`:

    .. math::

        \texttt{elnum} = \texttt{Edof}(:,1)

    i.e. the first column of the topology matrix.

:Limitations:
    Supported elements are bar, beam, triangular three node, and quadrilateral four node elements.
