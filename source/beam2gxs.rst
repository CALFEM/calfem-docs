beam2gxs - Two dimensional geometric nonlinear exact beam element
-----------------------------------------------------------------

Purpose
^^^^^^^

Compute section forces in a two dimensional geometric nonlinear beam element with exact solution.

.. figure:: images/beam2s.png
    :align: center
    :alt: Two dimensional geometric nonlinear exact beam element

Syntax
^^^^^^

.. code-block:: matlab

    [es,Qx] = beam2gxs(ex, ey, ep, ed, Qx)
    [es,Qx] = beam2gxs(ex, ey, ep, ed, Qx, eq)
    [es,Qx,edi] = beam2gxs(ex, ey, ep, ed, Qx, eq, n)
    [es,Qx,edi,eci] = beam2gxs(ex, ey, ep, ed, Qx, eq, n)

Description
^^^^^^^^^^^

``beam2gxs`` computes the section forces and displacements in local directions along the geometric nonlinear beam element ``beam2gxe``.

The input variables ``ex``, ``ey``, ``ep``, ``Qx``, and ``eq`` are described in ``beam2gxe``. The element displacements, stored in ``ed``, are obtained by the function ``extract``. If a distributed transversal load is applied to the element, the variable ``eq`` must be included. The number of evaluation points for section forces and displacements are determined by ``n``. If ``n`` is omitted, only the ends of the beam are evaluated.

The output variable ``Qx`` contains :math:`Q_{\bar{x}}` and the output variables

.. math::

    \mathrm{es} =
    \begin{bmatrix}
     N(0) & V(0)  & M(0) \\
     N(\bar{x}_{2}) & V(\bar{x}_{2}) & M(\bar{x}_{2})  \\
     \vdots & \vdots & \vdots \\
     N(\bar{x}_{n-1}) & V(\bar{x}_{n-1}) & M(\bar{x}_{n-1})\\
     N(L) & V(L) & M(L)
    \end{bmatrix}

    \quad
    \mathrm{edi} =
    \begin{bmatrix}
     u(0) & v(0)   \\
     u(\bar{x}_{2}) & v(\bar{x}_{2})   \\
     \vdots & \vdots \\
     u(\bar{x}_{n-1}) & v(\bar{x}_{n-1})\\
     u(L) & v(L)
    \end{bmatrix}

    \quad
    \mathrm{eci} =
    \begin{bmatrix}
     0  \\
     \bar x_{2} \\
     \vdots   \\
     \bar x_{n-1} \\
     L
    \end{bmatrix}

contain the section forces, the displacements, and the evaluation points on the local :math:`\bar{x}`-axis. :math:`L` is the length of the beam element.

Theory
^^^^^^

The nodal displacements in local coordinates are given by

.. math::

    \mathbf{\bar{a}}^e =
    \begin{bmatrix}
    \bar{u}_1 \\ \bar{u}_2 \\ \bar{u}_3 \\ \bar{u}_4 \\ \bar{u}_5 \\ \bar{u}_6
    \end{bmatrix}
    = \mathbf{G} \mathbf{a}^e

where :math:`\mathbf{G}` is described in ``beam2ge`` and the transpose of :math:`\mathbf{a}^e` is stored in ``ed``. The displacements associated with bar action and beam action are determined as

.. math::

    \mathbf{\bar{a}}^e_{\text{bar}} =
    \begin{bmatrix}
    \bar{u}_1 \\
    \bar{u}_4
    \end{bmatrix}
    ; \quad
    \mathbf{\bar{a}}^e_{\text{beam}} =
    \begin{bmatrix}
    \bar{u}_2 \\ \bar{u}_3 \\ \bar{u}_5 \\ \bar{u}_6
    \end{bmatrix}

The displacement :math:`u(\bar{x})` is computed from

.. math::

    u(\bar{x}) = \mathbf{N}_{\text{bar}} \mathbf{\bar{a}}^e_{\text{bar}}

where

.. math::

    \mathbf{N}_{\text{bar}} =
    \begin{bmatrix}
    1 & \bar{x}
    \end{bmatrix}
    \mathbf{C}^{-1}_{\text{bar}} =
    \begin{bmatrix}
    1-\frac{\bar{x}}{L} & \frac{\bar{x}}{L}
    \end{bmatrix}

where :math:`L` is defined in ``beam2gxe`` and

.. math::

    \mathbf{C}^{-1}_{\text{bar}} =
    \begin{bmatrix}
    1 & 0 \\
    -\frac{1}{L} & \frac{1}{L}
    \end{bmatrix}

The displacement :math:`v(\bar{x})`, the rotation :math:`\theta(\bar{x})`, the bending moment :math:`M(\bar{x})` and the shear force :math:`V(\bar{x})` are computed from

.. math::

    v(\bar{x}) = \mathbf{N}_{\text{beam}} \mathbf{\bar{a}}^e_{\text{beam}} + v_p(\bar{x})

.. math::

    \theta(\bar{x}) = \frac{d\mathbf{N}_{\text{beam}}}{dx} \mathbf{\bar{a}}^e_{\text{beam}} + \theta_p(\bar{x})

.. math::

    M(\bar{x}) = D_{EI} \mathbf{B}_{\text{beam}} \mathbf{\bar{a}}^e_{\text{beam}} + M_p(\bar{x})

.. math::

    V(\bar{x}) = -D_{EI} \frac{d\mathbf{B}_{\text{beam}}}{dx} \mathbf{\bar{a}}^e_{\text{beam}} + V_p(\bar{x})

For an axial compressive force (:math:`Q_{\bar{x}} < 0`) we have

.. math::

    \mathbf{N}_{\text{beam}} =
    \begin{bmatrix}
    1 & \bar{x} & \cos k \bar{x} & \sin k \bar{x}
    \end{bmatrix}
    \mathbf{C}^{-1}_{\text{beam}}

.. math::

    \frac{d\mathbf{N}_{\text{beam}}}{dx} =
    \begin{bmatrix}
    0 & 1 & -k \sin k \bar{x} & k \cos k \bar{x}
    \end{bmatrix}
    \mathbf{C}^{-1}_{\text{beam}}

.. math::

    \mathbf{B}_{\text{beam}} =
    \begin{bmatrix}
    0 & 0 & -k^2 \cos k \bar{x} & -k^2 \sin k \bar{x}
    \end{bmatrix}
    \mathbf{C}^{-1}_{\text{beam}}

.. math::

    \frac{d\mathbf{B}_{\text{beam}}}{dx} =
    \begin{bmatrix}
    0 & 0 & k^3 \sin k \bar{x} & -k^3 \cos k \bar{x}
    \end{bmatrix}
    \mathbf{C}^{-1}_{\text{beam}}

.. math::

    v_p(\bar{x}) =
    \frac{q_{\bar{y}}L^4}{2D_{EI}}
    \left[
        \frac{1 + \cos kL}{(kL)^3 \sin kL}(-1 + \cos k \bar{x})
        -\frac{1}{(kL)^3} \sin k \bar{x}
        + \frac{1}{(kL)^2} \left(\frac{\bar{x}^2}{L^2}-\frac{\bar{x}}{L}\right)
    \right]

.. math::

    \theta_p(\bar{x}) =
    \frac{q_{\bar{y}}L^3}{2D_{EI}}
    \left[
        -\frac{1 + \cos kL}{(kL)^2 \sin kL} \sin k \bar{x}
        -\frac{1}{(kL)^2} \cos k \bar{x}
        + \frac{1}{(kL)^2} \left(\frac{2\bar{x}}{L}-1\right)
    \right]

.. math::

    M_p(\bar{x}) =
    \frac{q_{\bar{y}}L^2}{2}
    \left[
        -\frac{1 + \cos kL}{(kL) \sin kL} \cos k \bar{x}
        +\frac{1}{(kL)} \sin k \bar{x}
        + \frac{2}{(kL)^2}
    \right]

.. math::

    V_p(\bar{x}) = Q_{\bar{x}}
    \begin{bmatrix}
    0 \\
    0 \\
    2\bar{x} - L \\
    3\bar{x}^2 - \frac{9L^2}{10}
    \end{bmatrix}^T
    \mathbf{C}^{-1}_{\text{beam}}
    \mathbf{\bar{a}}^e_{\text{beam}}
    - q_{\bar{y}}\left(\bar{x} - \frac{L}{2}\right)

in which :math:`D_{EI}`, :math:`L`, and :math:`q_{\bar{y}}` are defined in ``beam2gxe`` and

.. math::

    \mathbf{C}^{-1}_{\text{beam}} =
    \begin{bmatrix}
    k (kL \sin kL+\cos kL-1) & -kL \cos kL+\sin kL & -k (1-\cos kL) & -\sin kL+kL \\
    - k^2  \sin kL & -k (1-\cos kL) &  k^2  \sin kL & -k (1-\cos kL) \\
    -k(1-\cos kL) & kL \cos kL-\sin kL & k (1-\cos kL) & \sin kL-kL \\
    k\sin kL & kL \sin kL+\cos kL-1 & -k \sin kL & 1-\cos kL
    \end{bmatrix}

An updated value of the axial force is computed as

.. math::

    Q_{\bar{x}} = D_{EA}
    \begin{bmatrix}
    0 & 1
    \end{bmatrix}
    \mathbf{C}^{-1}_{\text{bar}}
    \mathbf{\bar{a}}^e_{\text{bar}}

The normal force :math:`N(\bar{x})` is then computed as

.. math::

    N(\bar{x}) = Q_{\bar{x}} + \theta(\bar{x}) V(\bar{x})