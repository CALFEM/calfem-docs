.. _beam2gs:
.. index:: 
   single: beam2gs
   single: geometric nonlinear stress
   single: beam stress
   single: 2D beam stress
   single: nonlinear stress
   single: section forces
   pair: finite element; stress
   pair: geometric; nonlinear
   pair: beam; stress
   pair: 2D; stress
   pair: nonlinear; stress
   pair: section; forces

beam2gs
^^^^^^^

:Purpose:

    Compute section forces in a two dimensional nonlinear beam element with geometrical nonlinearity.

    .. figure:: images/beam2s.png
        :align: center
        :width: 70%

:Syntax:

.. only:: matlab

    .. code:: matlab

        [es, Qx] = beam2gs(ex, ey, ep, ed, Qx)
        [es, Qx] = beam2gs(ex, ey, ep, ed, Qx, eq)
        [es, Qx, edi] = beam2gs(ex, ey, ep, ed, Qx, eq, n)
        [es, Qx, edi, eci] = beam2gs(ex, ey, ep, ed, Qx, eq, n)

.. only:: python

    .. code-block:: python

        es, Qx = cfc.beam2gs(ex, ey, ep, ed, Qx)
        es, Qx = cfc.beam2gs(ex, ey, ep, ed, Qx, eq)
        es, Qx, edi = cfc.beam2gs(ex, ey, ep, ed, Qx, eq, n)
        es, Qx, edi, eci = cfc.beam2gs(ex, ey, ep, ed, Qx, eq, n)

:Description:

    :code:`beam2gs` computes the section forces and displacements in local directions along the geometric nonlinear beam element :code:`beam2ge`.

    The input variables :code:`ex`, :code:`ey`, :code:`ep`, :code:`Qx` and :code:`eq`, are described in :code:`beam2ge`. The element displacements, stored in :code:`ed`, are obtained by the function :code:`extract_ed`. If a distributed transversal load is applied to the element, the variable :code:`eq` must be included. The number of evaluation points for section forces and displacements are determined by :code:`n`. If :code:`n` is omitted, only the ends of the beam are evaluated.

    The output variable :code:`Qx` contains :math:`Q_{\bar{x}}` and the output variables

    :code:`es`:math:`= \begin{bmatrix}
    N(0) & V(0) & M(0) \\
    N(\bar{x}_2) & V(\bar{x}_2) & M(\bar{x}_2) \\
    \vdots & \vdots & \vdots \\
    N(\bar{x}_{n-1}) & V(\bar{x}_{n-1}) & M(\bar{x}_{n-1}) \\
    N(L) & V(L) & M(L)
    \end{bmatrix}`
    :math:`\quad`
    :code:`edi`:math:`= \begin{bmatrix}
    u(0) & v(0) \\
    u(\bar{x}_2) & v(\bar{x}_2) \\
    \vdots & \vdots \\
    u(\bar{x}_{n-1}) & v(\bar{x}_{n-1}) \\
    u(L) & v(L)
    \end{bmatrix}` 
    :math:`\quad` 
    :code:`eci`:math:`= \begin{bmatrix}
    0 \\
    \bar{x}_2 \\
    \vdots \\
    \bar{x}_{n-1} \\
    L
    \end{bmatrix}` 

    contain the section forces, the displacements, and the evaluation points on the local :math:`\bar{x}`-axis. :math:`L` is the length of the beam element.

:Theory:

    The nodal displacements in local coordinates are given by

    .. math::

        \mathbf{\bar{a}}^e =
        \begin{bmatrix}
        \bar{u}_1 \\ \bar{u}_2 \\ \bar{u}_3 \\ \bar{u}_4 \\ \bar{u}_5 \\ \bar{u}_6
        \end{bmatrix}
        = \mathbf{G} \mathbf{a}^e

    where :math:`\mathbf{G}` is described in :code:`beam2ge` and the transpose of :math:`\mathbf{a}^e` is stored in :code:`ed`.

    The displacements associated with bar action and beam action are determined as

    .. math::

        \mathbf{\bar{a}}^e_{\mathrm{bar}} =
        \begin{bmatrix}
        \bar{u}_1 \\
        \bar{u}_4
        \end{bmatrix};
        \qquad
        \mathbf{\bar{a}}^e_{\mathrm{beam}} =
        \begin{bmatrix}
        \bar{u}_2 \\ \bar{u}_3 \\ \bar{u}_5 \\ \bar{u}_6
        \end{bmatrix}

    The displacement :math:`u(\bar{x})` is computed from

    .. math::

        u(\bar{x}) = \mathbf{N}_{\mathrm{bar}} \mathbf{\bar{a}}^e_{\mathrm{bar}}

    where

    .. math::

        \mathbf{N}_{\mathrm{bar}} = \begin{bmatrix} 1 & \bar{x} \end{bmatrix} \mathbf{C}^{-1}_{\mathrm{bar}} = \begin{bmatrix} 1-\frac{\bar{x}}{L} & \frac{\bar{x}}{L} \end{bmatrix}

    where :math:`L` is defined in :code:`beam2ge` and

    .. math::

        \mathbf{C}^{-1}_{\mathrm{bar}} =
        \begin{bmatrix}
        1 & 0 \\
        -\frac{1}{L} & \frac{1}{L}
        \end{bmatrix}

    The displacement :math:`v(\bar{x})`, the rotation :math:`\theta(\bar{x})`, the bending moment :math:`M(\bar{x})` and the shear force :math:`V(\bar{x})` are computed from

    .. math::

        v(\bar{x}) = \mathbf{N}_{\mathrm{beam}} \mathbf{\bar{a}}^e_{\mathrm{beam}} + v_p(\bar{x})

    .. math::

        \theta(\bar{x}) = \frac{d\mathbf{N}_{\mathrm{beam}}}{dx} \mathbf{\bar{a}}^e_{\mathrm{beam}} + \theta_p(\bar{x})

    .. math::

        M(\bar{x}) = D_{EI} \mathbf{B}_{\mathrm{beam}} \mathbf{\bar{a}}^e_{\mathrm{beam}} + M_p(\bar{x})

    .. math::

        V(\bar{x}) = -D_{EI} \frac{d\mathbf{B}_{\mathrm{beam}}}{dx} \mathbf{\bar{a}}^e_{\mathrm{beam}} + V_p(\bar{x})

    where

    .. math::

        \mathbf{N}_{\mathrm{beam}} = \begin{bmatrix} 1 & \bar{x} & \bar{x}^2 & \bar{x}^3 \end{bmatrix} \mathbf{C}^{-1}_{\mathrm{beam}}

    .. math::

        \frac{d\mathbf{N}_{\mathrm{beam}}}{dx} = \begin{bmatrix} 0 & 1 & 2\bar{x} & 3\bar{x}^2 \end{bmatrix} \mathbf{C}^{-1}_{\mathrm{beam}}

    .. math::

        \mathbf{B}_{\mathrm{beam}} = \begin{bmatrix} 0 & 0 & 2 & 6\bar{x} \end{bmatrix} \mathbf{C}^{-1}_{\mathrm{beam}}

    .. math::

        \frac{d\mathbf{B}_{\mathrm{beam}}}{dx} = \begin{bmatrix} 0 & 0 & 0 & 6 \end{bmatrix} \mathbf{C}^{-1}_{\mathrm{beam}}

    .. math::

        v_p(\bar{x}) =
        -\frac{Q_{\bar{x}}}{D_{EI}}
        \begin{bmatrix}
        0 \\
        0 \\
        \frac{\bar{x}^4}{12}-\frac{L \bar{x}^3}{6}+\frac{L^2 \bar{x}^2}{12} \\
        \frac{\bar{x}^5}{20}-\frac{3L^2 \bar{x}^3}{20}+\frac{L^3 \bar{x}^2}{10}
        \end{bmatrix}^T
        \mathbf{C}^{-1}_{\mathrm{beam}} \mathbf{\bar{a}}^e_{\mathrm{beam}}
        + \frac{q_{\bar{y}}}{D_{EI}}\left(\frac{\bar{x}^4}{24}-\frac{L \bar{x}^3}{12}+\frac{L^2 \bar{x}^2}{24}\right)

    .. math::

        \theta_p(\bar{x}) =
        -\frac{Q_{\bar{x}}}{D_{EI}}
        \begin{bmatrix}
        0 \\
        0 \\
        \frac{\bar{x}^3}{3}-\frac{L \bar{x}^2}{2}+\frac{L^2 \bar{x}}{6} \\
        \frac{\bar{x}^4}{4}-\frac{9L^2 \bar{x}^2}{20}+\frac{L^3 \bar{x}}{5}
        \end{bmatrix}^T
        \mathbf{C}^{-1}_{\mathrm{beam}} \mathbf{\bar{a}}^e_{\mathrm{beam}}
        + \frac{q_{\bar{y}}}{D_{EI}}\left(\frac{\bar{x}^3}{6}-\frac{L \bar{x}^2}{4}+\frac{L^2 \bar{x}}{12}\right)

    .. math::

        M_p(\bar{x}) =
        -Q_{\bar{x}}
        \begin{bmatrix}
        0 \\
        0 \\
        \bar{x}^2 - L\bar{x} + \frac{L^2}{6} \\
        \bar{x}^3 - \frac{9L^2 \bar{x}}{10} + \frac{L^3}{5}
        \end{bmatrix}^T
        \mathbf{C}^{-1}_{\mathrm{beam}} \mathbf{\bar{a}}^e_{\mathrm{beam}}
        + q_{\bar{y}}\left(\frac{\bar{x}^2}{2}-\frac{L \bar{x}}{2}+\frac{L^2}{12}\right)

    .. math::

        V_p(\bar{x}) =
        Q_{\bar{x}}
        \begin{bmatrix}
        0 \\
        0 \\
        2\bar{x} - L \\
        3\bar{x}^2 - \frac{9L^2}{10}
        \end{bmatrix}^T
        \mathbf{C}^{-1}_{\mathrm{beam}} \mathbf{\bar{a}}^e_{\mathrm{beam}}
        - q_{\bar{y}}\left(\bar{x} - \frac{L}{2}\right)

    in which :math:`D_{EI}`, :math:`L`, and :math:`q_{\bar{y}}` are defined in :code:`beam2ge` and

    .. math::

        \mathbf{C}^{-1}_{\mathrm{beam}} =
        \begin{bmatrix}
        1 & 0 & 0 & 0 \\
        0 & 1 & 0 & 0 \\
        -\frac{3}{L^2} & -\frac{2}{L} & \frac{3}{L^2} & -\frac{1}{L} \\
        \frac{2}{L^3} & \frac{1}{L^2} & -\frac{2}{L^3} & \frac{1}{L^2}
        \end{bmatrix}

    An updated value of the axial force is computed as

    .. math::

        Q_{\bar{x}} = D_{EA} \begin{bmatrix} 0 & 1 \end{bmatrix} \mathbf{C}^{-1}_{\mathrm{bar}} \mathbf{\bar{a}}^e_{\mathrm{bar}}

    The normal force :math:`N(\bar{x})` is then computed as

    .. math::

        N(\bar{x}) = Q_{\bar{x}} + \theta(\bar{x}) V(\bar{x})