bar1s - One dimensional bar element
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index:: bar1s

**Purpose**

Compute normal force in a one dimensional bar element.

.. figure:: images/bar1s.png
    :align: center
    :width: 70%

**Syntax**

.. code-block:: matlab

    es = bar1s(ex, ep, ed)
    es = bar1s(ex, ep, ed, eq)
    [es, edi] = bar1s(ex, ep, ed, eq, n)
    [es, edi, eci] = bar1s(ex, ep, ed, eq, n)

**Description**

``bar1s`` computes the normal force in the one dimensional bar element ``bar1e``.

The input variables ``ex`` and ``ep`` are defined in ``bar1e`` and the element nodal displacements, stored in ``ed``, are obtained by the function ``extract``. If distributed load is applied to the element, the variable ``eq`` must be included.

The number of evaluation points for normal force and displacement are determined by ``n``. If ``n`` is omitted, only the ends of the bar are evaluated.

The output variables

.. math::

    \mathrm{es} =
    \begin{bmatrix}
    N(0) \\
    N(\bar{x}_2) \\
    \vdots \\
    N(\bar{x}_{n-1}) \\
    N(L)
    \end{bmatrix}
    \qquad
    \mathrm{edi} =
    \begin{bmatrix}
    u(0) \\
    u(\bar{x}_2) \\
    \vdots \\
    u(\bar{x}_{n-1}) \\
    u(L)
    \end{bmatrix}
    \qquad
    \mathrm{eci} =
    \begin{bmatrix}
    0 \\
    \bar{x}_2 \\
    \vdots \\
    \bar{x}_{n-1} \\
    L
    \end{bmatrix}

contain the normal force, the displacement, and the evaluation points on the local :math:`\bar{x}`-axis. :math:`L` is the length of the bar element.

**Theory**

The nodal displacements in local coordinates are given by

.. math::

    \mathbf{\bar{a}}^e = \begin{bmatrix} \bar{u}_1 \\ \bar{u}_2 \end{bmatrix}

The transpose of :math:`\mathbf{\bar{a}}^e` is stored in ``ed``.

The displacement :math:`u(\bar{x})` and the normal force :math:`N(\bar{x})` are computed from

.. math::

    u(\bar{x}) = \mathbf{N} \mathbf{\bar{a}}^e + u_p(\bar{x})

.. math::

    N(\bar{x}) = D_{EA} \mathbf{B} \mathbf{\bar{a}}^e + N_p(\bar{x})

where

.. math::

    \mathbf{N} = \begin{bmatrix} 1 & \bar{x} \end{bmatrix} \mathbf{C}^{-1} = \begin{bmatrix} 1 - \frac{\bar{x}}{L} & \frac{\bar{x}}{L} \end{bmatrix}

.. math::

    \mathbf{B} = \begin{bmatrix} 0 & 1 \end{bmatrix} \mathbf{C}^{-1} = \frac{1}{L} \begin{bmatrix} -1 & 1 \end{bmatrix}

.. math::

    u_p(\bar{x}) = -\frac{q_{\bar{x}}}{D_{EA}} \left( \frac{\bar{x}^2}{2} - \frac{L\bar{x}}{2} \right)

.. math::

    N_p(\bar{x}) = -q_{\bar{x}} \left( \bar{x} - \frac{L}{2} \right)

in which :math:`D_{EA}`, :math:`L`, and :math:`q_{\bar{x}}` are defined in ``bar1e`` and

.. math::

    \mathbf{C}^{-1} = \begin{bmatrix} 1 & 0 \\ -\frac{1}{L} & \frac{1}{L} \end{bmatrix}
