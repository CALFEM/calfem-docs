.. _secforce2:
.. index:: 
   single: secforce2
   single: section force diagram
   single: force diagram
   single: beam force visualization
   single: 2D force diagram
   pair: visualization; forces
   pair: section; forces
   pair: force; diagram
   pair: beam; forces
   pair: 2D; visualization

secforce2
^^^^^^^^^

:Purpose:
    Draw the section force diagrams of a two dimensional bar or beam element in its global position.

:Syntax:
.. only:: matlab

    .. code-block:: matlab

        secforce2(ex, ey, es, plotpar, sfac)
        secforce2(ex, ey, es, plotpar, sfac, eci)
        [sfac] = secforce2(ex, ey, es)
        [sfac] = secforce2(ex, ey, es, plotpar)

.. only:: python

    .. code-block:: python

        cfv.secforce2(ex, ey, es, plotpar, sfac)
        cfv.secforce2(ex, ey, es, plotpar, sfac, eci)
        sfac = cfv.secforce2(ex, ey, es)
        sfac = cfv.secforce2(ex, ey, es, plotpar)

:Description:
    The input variables :code:`ex` and :code:`ey` are defined in :code:`bar2e` or :code:`beam2e`. The input variable

    :code:`es`:math:`= \begin{bmatrix} S_1 \\ S_2 \\ \vdots \\ S_n \end{bmatrix}`

    consists of a column matrix that contains section forces. The values in :code:`es` are computed in, e.g., :code:`bar2s` or :code:`beam2s`.

    The variable :code:`plotpar` sets plot parameters for the diagram:

    :code:`plotpar`:math:`= [\, \text{linecolor} \;\; \text{elementcolor} \,]`

    where

    .. list-table::
        :widths: 20 30 20 30
        :header-rows: 1

        * - linecolor
          - color
          - elementcolor
          - color
        * - 1
          - black
          - 1
          - black
        * - 2
          - blue
          - 2
          - blue
        * - 3
          - magenta
          - 3
          - magenta
        * - 4
          - red
          - 4
          - red

    The scale factor :code:`sfac` is a scalar that the section forces are multiplied with to get a suitable graphical representation. If :code:`sfac` is omitted in the input list, the scale factor is set automatically.

    The input variable

    :code:`eci`:math:`= \begin{bmatrix} \bar{x}_1 \\ \bar{x}_2 \\ \vdots \\ \bar{x}_n \end{bmatrix}`

    specifies the local :math:`\bar{x}`-coordinates of the quantities in :code:`es`. If :code:`eci` is not given, uniform distance is assumed.