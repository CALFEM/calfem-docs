beam2s - Two Dimensional Beam Element
-------------------------------------

.. index:: beam2s

.. header::
    :left: **beam2s**
    :right: **Two dimensional beam element**

.. header::
    :left: **Two dimensional beam element**
    :right: **beam2s**

Purpose
^^^^^^^

Compute section forces in a two-dimensional beam element.

.. figure:: images/beam2s.png
    :align: center
    :width: 70%

Syntax
^^^^^^ 

.. code-block:: none

    [es] = beam2s(ex, ey, ep, ed)
    [es] = beam2s(ex, ey, ep, ed, eq)
    [es, edi] = beam2s(ex, ey, ep, ed, eq, n)
    [es, edi, eci] = beam2s(ex, ey, ep, ed, eq, n)

Description
^^^^^^^^^^^

**beam2s** computes the section forces and displacements in local directions along the beam element **beam2e**.

The input variables **ex**, **ey**, **ep**, and **eq** are defined in **beam2e**.

The element displacements, stored in **ed**, are obtained by the function **extract**. If a distributed load is applied to the element, the variable **eq** must be included. The number of evaluation points for section forces and displacements is determined by **n**. If **n** is omitted, only the ends of the beam are evaluated.

The output variables:

.. math::

    es =
    \begin{bmatrix}
    N(0) & V(0) & M(0) \\
    N(\bar{x}_2) & V(\bar{x}_2) & M(\bar{x}_2) \\
    \vdots & \vdots & \vdots \\
    N(\bar{x}_{n-1}) & V(\bar{x}_{n-1}) & M(\bar{x}_{n-1}) \\
    N(L) & V(L) & M(L)
    \end{bmatrix}

    edi =
    \begin{bmatrix}
    u(0) & v(0) \\
    u(\bar{x}_2) & v(\bar{x}_2) \\
    \vdots & \vdots \\
    u(\bar{x}_{n-1}) & v(\bar{x}_{n-1}) \\
    u(L) & v(L)
    \end{bmatrix}

    eci =
    \begin{bmatrix}
    0 \\
    \bar{x}_2 \\
    \vdots \\
    \bar{x}_{n-1} \\
    L
    \end{bmatrix}

contain the section forces, the displacements, and the evaluation points on the local :math:`\bar{x}`-axis. :math:`L` is the length of the beam element.

Theory
^^^^^^

The nodal displacements in local coordinates are given by:

.. math::

    \mathbf{\bar{a}}^e =
    \begin{bmatrix}
    \bar{u}_1 \\
    \bar{u}_2 \\
    \bar{u}_3 \\
    \bar{u}_4 \\
    \bar{u}_5 \\
    \bar{u}_6
    \end{bmatrix}
    = \mathbf{G} \mathbf{a}^e

where :math:`\mathbf{G}` is described in **beam2e** and the transpose of :math:`\mathbf{a}^e` is stored in **ed**.

The displacements associated with bar action and beam action are determined as:

.. math::

    \mathbf{\bar{a}}^e_{\text{bar}} =
    \begin{bmatrix}
    \bar{u}_1 \\
    \bar{u}_4
    \end{bmatrix},
    \quad
    \mathbf{\bar{a}}^e_{\text{beam}} =
    \begin{bmatrix}
    \bar{u}_2 \\
    \bar{u}_3 \\
    \bar{u}_5 \\
    \bar{u}_6
    \end{bmatrix}

The displacement :math:`u(\bar{x})` and the normal force :math:`N(\bar{x})` are computed from:

.. math::

    u(\bar{x}) = \mathbf{N}_{\text{bar}} \mathbf{\bar{a}}^e_{\text{bar}} + u_p(\bar{x})

.. math::

    N(\bar{x}) = D_{EA} \mathbf{B}_{\text{bar}} \mathbf{\bar{a}}^e + N_p(\bar{x})

where:

.. math::

    \mathbf{N}_{\text{bar}} =
    \begin{bmatrix}
    1 & \bar{x}
    \end{bmatrix}
    \mathbf{C}^{-1}_{\text{bar}} =
    \begin{bmatrix}
    1 - \frac{\bar{x}}{L} & \frac{\bar{x}}{L}
    \end{bmatrix}

.. math::

    \mathbf{B}_{\text{bar}} =
    \begin{bmatrix}
    0 & 1
    \end{bmatrix}
    \mathbf{C}^{-1}_{\text{bar}} =
    \begin{bmatrix}
    -\frac{1}{L} & \frac{1}{L}
    \end{bmatrix}

.. math::

    u_p(\bar{x}) = -\frac{q_{\bar{x}}}{D_{EA}}
    \left(\frac{\bar{x}^2}{2} - \frac{L \bar{x}}{2}\right)

.. math::

    N_p(\bar{x}) = -q_{\bar{x}}
    \left(\bar{x} - \frac{L}{2}\right)

where :math:`D_{EA}`, :math:`L`, and :math:`q_{\bar{x}}` are defined in **beam2e**, and:

.. math::

    \mathbf{C}^{-1}_{\text{bar}} =
    \begin{bmatrix}
    1 & 0 \\
    -\frac{1}{L} & \frac{1}{L}
    \end{bmatrix}

The displacement :math:`v(\bar{x})`, the bending moment :math:`M(\bar{x})`, and the shear force :math:`V(\bar{x})` are computed from:

.. math::

    v(\bar{x}) = \mathbf{N}_{\text{beam}} \mathbf{\bar{a}}^e_{\text{beam}} + v_p(\bar{x})

.. math::

    M(\bar{x}) = D_{EI} \mathbf{B}_{\text{beam}} \mathbf{\bar{a}}^e_{\text{beam}} + M_p(\bar{x})

.. math::

    V(\bar{x}) = -D_{EI} \frac{d\mathbf{B}_{\text{beam}}}{d\bar{x}} \mathbf{\bar{a}}^e_{\text{beam}} + V_p(\bar{x})

where:

.. math::

    \mathbf{N}_{\text{beam}} =
    \begin{bmatrix}
    1 & \bar{x} & \bar{x}^2 & \bar{x}^3
    \end{bmatrix}
    \mathbf{C}^{-1}_{\text{beam}}

.. math::

    \mathbf{B}_{\text{beam}} =
    \begin{bmatrix}
    0 & 0 & 2 & 6\bar{x}
    \end{bmatrix}
    \mathbf{C}^{-1}_{\text{beam}}

.. math::

    \frac{d\mathbf{B}_{\text{beam}}}{d\bar{x}} =
    \begin{bmatrix}
    0 & 0 & 0 & 6
    \end{bmatrix}
    \mathbf{C}^{-1}_{\text{beam}}

.. math::

    v_p(\bar{x}) = \frac{q_{\bar{y}}}{D_{EI}}
    \left(\frac{\bar{x}^4}{24} - \frac{L \bar{x}^3}{12} + \frac{L^2 \bar{x}^2}{24}\right)

.. math::

    M_p(\bar{x}) = q_{\bar{y}}
    \left(\frac{\bar{x}^2}{2} - \frac{L \bar{x}}{2} + \frac{L^2}{12}\right)

.. math::

    V_p(\bar{x}) = -q_{\bar{y}}
    \left(\bar{x} - \frac{L}{2}\right)

where :math:`D_{EI}`, :math:`L`, and :math:`q_{\bar{y}}` are defined in **beam2e**, and:

.. math::

    \mathbf{C}^{-1}_{\text{beam}} =
    \begin{bmatrix}
    1 & 0 & 0 & 0 \\
    0 & 1 & 0 & 0 \\
    -\frac{3}{L^2} & -\frac{2}{L} & \frac{3}{L^2} & -\frac{1}{L} \\
    \frac{2}{L^3} & \frac{1}{L^2} & -\frac{2}{L^3} & \frac{1}{L^2}
    \end{bmatrix}