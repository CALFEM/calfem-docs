beam2ws
^^^^^^^

:Purpose:

    Compute section forces in a two dimensional beam element with elastic support.

    .. figure:: images/beam2s.png
        :align: center
        :width: 70%

:Syntax:

    .. code:: matlab

        es = beam2ws(ex, ey, ep, ed)
        es = beam2ws(ex, ey, ep, ed, eq)
        es, edi, eci = beam2ws(ex, ey, ep, ed, eq, n)

:Description:

    :code:`beam2ws` computes the section forces and displacements in local directions
    along the beam element :code:`beam2we`.

    The input variables :code:`ex`, :code:`ey`, :code:`ep` and :code:`eq` are defined in
    :code:`beam2we`, and the element displacements, stored
    in :code:`ed`, are obtained by the function :code:`extract_ed`.
    If distributed loads are applied to the element, the variable :code:`eq` must be
    included.
    The number of evaluation points for section forces and displacements are
    determined by :code:`n`. If :code:`n` is omitted, only the ends of the
    beam are evaluated.

    The output variables

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

    contain the section forces, the displacements, and the evaluation points on the local :math:`\bar{x}`-axis.
    :math:`L` is the length of the beam element.

:Theory:

    The nodal displacements in local coordinates are given by

    .. math::

        \bar{\mathbf{a}}^e =
        \begin{bmatrix}
        \bar{u}_1 \\ \bar{u}_2 \\ \bar{u}_3 \\ \bar{u}_4 \\ \bar{u}_5 \\ \bar{u}_6
        \end{bmatrix}
        = \mathbf{G} \mathbf{a}^e

    where :math:`\mathbf{G}` is described in :code:`beam2we`
    and the transpose of :math:`\mathbf{a}^e` is stored in :code:`ed`.
    The displacements associated with bar action and beam action are determined as

    .. math::

        \bar{\mathbf{a}}^e_{\text{bar}} =
        \begin{bmatrix}
        \bar{u}_1 \\
        \bar{u}_4
        \end{bmatrix}
        \qquad
        \bar{\mathbf{a}}^e_{\text{beam}} =
        \begin{bmatrix}
        \bar{u}_2 \\ \bar{u}_3 \\ \bar{u}_5 \\ \bar{u}_6
        \end{bmatrix}

    The displacement :math:`u(\bar{x})` and the normal force :math:`N(\bar{x})` are computed from

    .. math::

        u(\bar{x}) = \mathbf{N}_{\text{bar}} \bar{\mathbf{a}}^e_{\text{bar}} + u_p(\bar{x})

    .. math::

        N(\bar{x}) = D_{EA} \mathbf{B}_{\text{bar}} \bar{\mathbf{a}}^e + N_p(\bar{x})

    where

    .. math::

        \mathbf{N}_{\text{bar}} = \begin{bmatrix} 1 & \bar{x} \end{bmatrix} \mathbf{C}^{-1}_{\text{bar}} = \begin{bmatrix} 1-\frac{\bar{x}}{L} & \frac{\bar{x}}{L} \end{bmatrix}

    .. math::

        \mathbf{B}_{\text{bar}} = \begin{bmatrix} 0 & 1 \end{bmatrix} \mathbf{C}^{-1}_{\text{bar}} = \begin{bmatrix} -\frac{1}{L} & \frac{1}{L} \end{bmatrix}

    .. math::

        u_p(\bar{x}) = \frac{k_{\bar{x}}}{D_{EA}}
        \begin{bmatrix}
        \frac{\bar{x}^2-L\bar{x}}{2} & \frac{\bar{x}^3-L^2\bar{x}}{6}
        \end{bmatrix}
        \mathbf{C}^{-1}_{\text{bar}} \bar{\mathbf{a}}^e_{\text{bar}}
        - \frac{q_{\bar{x}}}{D_{EA}}\left(\frac{\bar{x}^2}{2}-\frac{L\bar{x}}{2}\right)

    .. math::

        N_p(\bar{x}) = k_{\bar{x}}
        \begin{bmatrix}
        \frac{2\bar{x}-L}{2} & \frac{3\bar{x}^2-L^2}{6}
        \end{bmatrix}
        \mathbf{C}^{-1}_{\text{bar}} \bar{\mathbf{a}}^e_{\text{bar}}
        - q_{\bar{x}}\left(\bar{x}-\frac{L}{2}\right)

    in which :math:`D_{EA}`, :math:`k_{\bar{x}}`, :math:`L`, and :math:`q_{\bar{x}}`
    are defined in :code:`beam2we` and

    .. math::

        \mathbf{C}^{-1}_{\text{bar}} =
        \begin{bmatrix}
        1 & 0 \\
        -\frac{1}{L} & \frac{1}{L}
        \end{bmatrix}

    The displacement :math:`v(\bar{x})`, the bending moment :math:`M(\bar{x})` and the shear force :math:`V(\bar{x})` are computed from

    .. math::

        v(\bar{x}) = \mathbf{N}_{\text{beam}} \bar{\mathbf{a}}^e_{\text{beam}} + v_p(\bar{x})

    .. math::

        M(\bar{x}) = D_{EI} \mathbf{B}_{\text{beam}} \bar{\mathbf{a}}^e_{\text{beam}} + M_p(\bar{x})

    .. math::

        V(\bar{x}) = -D_{EI} \frac{d\mathbf{B}_{\text{beam}}}{dx} \bar{\mathbf{a}}^e_{\text{beam}} + V_p(\bar{x})

    where

    .. math::

        \mathbf{N}_{\text{beam}} = \begin{bmatrix} 1 & \bar{x} & \bar{x}^2 & \bar{x}^3 \end{bmatrix} \mathbf{C}^{-1}_{\text{beam}}

    .. math::

        \mathbf{B}_{\text{beam}} = \begin{bmatrix} 0 & 0 & 2 & 6\bar{x} \end{bmatrix} \mathbf{C}^{-1}_{\text{beam}}

    .. math::

        \frac{d\mathbf{B}_{\text{beam}}}{dx} = \begin{bmatrix} 0 & 0 & 0 & 6 \end{bmatrix} \mathbf{C}^{-1}_{\text{beam}}

    .. math::

        v_p(\bar{x}) = -\frac{k_{\bar{y}}}{D_{EI}}
        \begin{bmatrix}
        \frac{\bar{x}^4-2L\bar{x}^3+L^2\bar{x}^2}{24} \\
        \frac{\bar{x}^5-3L^2\bar{x}^3+2L^3\bar{x}^2}{120} \\
        \frac{\bar{x}^6-4L^3\bar{x}^3+3L^4\bar{x}^2}{360} \\
        \frac{\bar{x}^7-5L^4\bar{x}^3+4L^5\bar{x}^2}{840}
        \end{bmatrix}^T
        \mathbf{C}^{-1}_{\text{beam}} \bar{\mathbf{a}}^e_{\text{beam}}
        + \frac{q_{\bar{y}}}{D_{EI}}\left(\frac{\bar{x}^4}{24}-\frac{L\bar{x}^3}{12}+\frac{L^2\bar{x}^2}{24}\right)

    .. math::

        M_p(\bar{x}) = -k_{\bar{y}}
        \begin{bmatrix}
        \frac{6\bar{x}^2-6L\bar{x}+L^2}{12} \\
        \frac{10\bar{x}^3-9L^2\bar{x}+2L^3}{60} \\
        \frac{5\bar{x}^4-4L^3\bar{x}+L^4}{60} \\
        \frac{21\bar{x}^5-15L^4\bar{x}+4L^5}{420}
        \end{bmatrix}^T
        \mathbf{C}^{-1}_{\text{beam}} \bar{\mathbf{a}}^e_{\text{beam}}
        + q_{\bar{y}}\left(\frac{\bar{x}^2}{2}-\frac{L\bar{x}}{2}+\frac{L^2}{12}\right)

    .. math::

        V_p(\bar{x}) = k_{\bar{y}}
        \begin{bmatrix}
        \frac{2\bar{x}-L}{2} \\
        \frac{10\bar{x}^2-3L^2}{20} \\
        \frac{5\bar{x}^3-L^3}{15} \\
        \frac{7\bar{x}^4-L^4}{28}
        \end{bmatrix}^T
        \mathbf{C}^{-1}_{\text{beam}} \bar{\mathbf{a}}^e_{\text{beam}}
        - q_{\bar{y}}\left(\bar{x}-\frac{L}{2}\right)

    in which :math:`D_{EI}`, :math:`k_{\bar{y}}`, :math:`L`, and :math:`q_{\bar{y}}`
    are defined in :code:`beam2we` and

    .. math::

        \mathbf{C}^{-1}_{\text{beam}} =
        \begin{bmatrix}
        1 & 0 & 0 & 0 \\
        0 & 1 & 0 & 0 \\
        -\frac{3}{L^2} & -\frac{2}{L} & \frac{3}{L^2} & -\frac{1}{L} \\
        \frac{2}{L^3} & \frac{1}{L^2} & -\frac{2}{L^3} & \frac{1}{L^2}
        \end{bmatrix}
