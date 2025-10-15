beam3s
^^^^^^

:Purpose:

    Compute section forces in a three dimensional beam element.

    .. figure:: images/BEAM3S.png
        :align: center
        :width: 70%

:Syntax:

.. only:: matlab

    .. code-block:: matlab

        es = beam3s(ex, ey, ez, eo, ep, ed)
        es = beam3s(ex, ey, ez, eo, ep, ed, eq)
        [es, edi] = beam3s(ex, ey, ez, eo, ep, ed, eq, n)
        [es, edi, eci] = beam3s(ex, ey, ez, eo, ep, ed, eq, n)

.. only:: python

    .. code-block:: python

        es = cfc.beam3s(ex, ey, ez, eo, ep, ed)
        es = cfc.beam3s(ex, ey, ez, eo, ep, ed, eq)
        es, edi = cfc.beam3s(ex, ey, ez, eo, ep, ed, eq, n)
        es, edi, eci = cfc.beam3s(ex, ey, ez, eo, ep, ed, eq, n)

:Description:

    :code:`beam3s` computes the section forces and displacements in local directions along the beam element :code:`beam3e`.

    The input variables :code:`ex`, :code:`ey`, :code:`ez`, :code:`eo`, :code:`ep` and :code:`eq` are defined in :code:`beam3e`.

    The element displacements, stored in :code:`ed`, are obtained by the function :code:`extract_ed`. If a distributed load is applied to the element, the variable :code:`eq` must be included. The number of evaluation points for section forces and displacements are determined by :code:`n`. If :code:`n` is omitted, only the ends of the beam are evaluated.

    The output variables:

    :code:`es`:math:`= \begin{bmatrix}
    N(0) & V_{\bar{y}}(0)  & V_{\bar{z}}(0)  & T(0)  & M_{\bar{y}}(0) & M_{\bar{z}}(0) \\
    N(\bar{x}_{2}) & V_{\bar{y}}(\bar{x}_{2}) & V_{\bar{z}}(\bar{x}_{2}) & T(\bar{x}_{2}) & M_{\bar{y}}(\bar{x}_{2}) & M_{\bar{z}}(\bar{x}_{2}) \\
    N(\bar{x}_{n-1}) & V_{\bar{y}}(\bar{x}_{n-1}) & V_{\bar{z}}(\bar{x}_{n-1}) & T(\bar{x}_{n-1}) & M_{\bar{y}}(\bar{x}_{n-1}) & M_{\bar{z}}(\bar{x}_{n-1}) \\
    N(L) & V_{\bar{y}}(L) & V_{\bar{z}}(L) & T(\bar{x}_{n-1}) & M_{\bar{y}}(L) & M_{\bar{z}}(L)
    \end{bmatrix}`

    :code:`edi`:math:`= \begin{bmatrix}
    u(0) & v(0) & w(0)  & \varphi(0) \\
    u(\bar{x}_{2}) & v(\bar{x}_{2}) & w(\bar{x}_{2})  & \varphi(\bar{x}_{2})    \\
    \vdots & \vdots & \vdots & \vdots \\
    u(\bar{x}_{n-1}) & v(\bar{x}_{n-1}) & w(\bar{x}_{n-1}) & \varphi(\bar{x}_{n-1})\\
    u(L) & v(L) & w(L) & \varphi(L)
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

        \mathbf{\bar{a}}^e=
        \begin{bmatrix}
        \bar{u}_1 \\ \bar{u}_2 \\ \bar{u}_3 \\ \bar{u}_4 \\ \bar{u}_5 \\
        \bar{u}_6 \\ \bar{u}_7 \\ \bar{u}_8 \\ \bar{u}_9 \\ \bar{u}_{10} \\ \bar{u}_{11} \\
        \bar{u}_{12}
        \end{bmatrix}
        = \mathbf{G} \mathbf{a}^e

    where :math:`\mathbf{G}` is described in :code:`beam3e` and the transpose of :math:`\mathbf{a}^e` is stored in :code:`ed`.

    The displacements associated with bar action, beam action in the :math:`\bar{x}\bar{y}`-plane, beam action in the :math:`\bar{x}\bar{z}`-plane, and torsion are determined as

    .. math::

        \mathbf{\bar{a}}^e_{\text{bar}}=
        \begin{bmatrix}
        \bar{u}_1 \\
        \bar{u}_7
        \end{bmatrix};
        \quad
        \mathbf{\bar{a}}^e_{\text{beam},\bar{z}}=
        \begin{bmatrix}
        \bar{u}_2 \\ \bar{u}_6 \\ \bar{u}_8 \\ \bar{u}_{12}
        \end{bmatrix};
        \quad
        \mathbf{\bar{a}}^e_{\text{beam},\bar{y}}=
        \begin{bmatrix}
        \bar{u}_3 \\ -\bar{u}_5 \\ \bar{u}_9 \\ -\bar{u}_{11}
        \end{bmatrix};
        \quad
        \mathbf{\bar{a}}^e_{\text{torsion}}=
        \begin{bmatrix}
        \bar{u}_4 \\
        \bar{u}_{10}
        \end{bmatrix}

    The displacement :math:`u(\bar{x})` and the normal force :math:`N(\bar{x})` are computed from

    .. math::

        u(\bar{x}) = \mathbf{N}_{\text{bar}} \mathbf{\bar{a}}^e_{\text{bar}} + u_p(\bar{x})

    .. math::

        N(\bar{x}) = D_{EA} \mathbf{B}_{\text{bar}} \mathbf{\bar{a}}^e + N_p(\bar{x})

    where

    .. math::

        \mathbf{N}_{\text{bar}} = \begin{bmatrix} 1 & \bar{x} \end{bmatrix} \mathbf{C}^{-1}_{\text{bar}} = \begin{bmatrix} 1-\frac{\bar{x}}{L} & \frac{\bar{x}}{L} \end{bmatrix}

    .. math::

        \mathbf{B}_{\text{bar}} = \begin{bmatrix} 0 & 1 \end{bmatrix} \mathbf{C}^{-1}_{\text{bar}} = \begin{bmatrix} -\frac{1}{L} & \frac{1}{L} \end{bmatrix}

    .. math::

        u_p(\bar{x}) = -\frac{q_{\bar{x}}}{D_{EA}}\left(\frac{\bar{x}^2}{2}-\frac{L\bar{x}}{2}\right)

    .. math::

        N_p(\bar{x}) = -q_{\bar{x}}\left(\bar{x}-\frac{L}{2}\right)

    in which :math:`D_{EA}`, :math:`L`, and :math:`q_{\bar{x}}` are defined in :code:`beam3e` and

    .. math::

        \mathbf{C}^{-1}_{\text{bar}} =
        \begin{bmatrix}
        1 & 0 \\
        -\frac{1}{L} & \frac{1}{L}
        \end{bmatrix}

    The displacement :math:`v(\bar{x})`, the bending moment :math:`M_{\bar{z}}(\bar{x})` and the shear force :math:`V_{\bar{y}}(\bar{x})` are computed from

    .. math::

        v(\bar{x}) = \mathbf{N}_{\text{beam}} \mathbf{\bar{a}}^e_{\text{beam},\bar{z}} + v_p(\bar{x})

    .. math::

        M_{\bar{z}}(\bar{x}) = D_{EI_{\bar{z}}} \mathbf{B}_{\text{beam}} \mathbf{\bar{a}}^e_{\text{beam},\bar{z}} + M_{\bar{z},p}(\bar{x})

    .. math::

        V_{\bar{y}}(\bar{x}) = -D_{EI_{\bar{z}}} \frac{d\mathbf{B}_{\text{beam}}}{dx} \mathbf{\bar{a}}^e_{\text{beam},\bar{z}} + V_{\bar{y},p}(\bar{x})

    where

    .. math::

        \mathbf{N}_{\text{beam}} = \begin{bmatrix} 1 & \bar{x} & \bar{x}^2 & \bar{x}^3 \end{bmatrix} \mathbf{C}^{-1}_{\text{beam}}

    .. math::

        \mathbf{B}_{\text{beam}} = \begin{bmatrix} 0 & 0 & 2 & 6\bar{x} \end{bmatrix} \mathbf{C}^{-1}_{\text{beam}}

    .. math::

        \frac{d\mathbf{B}_{\text{beam}}}{dx} = \begin{bmatrix} 0 & 0 & 0 & 6 \end{bmatrix} \mathbf{C}^{-1}_{\text{beam}}

    .. math::

        v_p(\bar{x}) = \frac{q_{\bar{y}}}{D_{EI_{\bar{z}}}}\left(\frac{\bar{x}^4}{24}-\frac{L \bar{x}^3}{12}+\frac{L^2 \bar{x}^2}{24}\right)

    .. math::

        M_{\bar{z},p}(\bar{x}) = q_{\bar{y}}\left(\frac{\bar{x}^2}{2}-\frac{L \bar{x}}{2}+\frac{L^2}{12}\right)

    .. math::

        V_{\bar{y},p}(\bar{x}) = -q_{\bar{y}}\left(\bar{x}-\frac{L}{2}\right)

    in which :math:`D_{EI_{\bar{z}}}`, :math:`L`, and :math:`q_{\bar{y}}` are defined in :code:`beam3e` and

    .. math::

        \mathbf{C}^{-1}_{\text{beam}} =
        \begin{bmatrix}
        1 & 0 & 0 & 0 \\
        0 & 1 & 0 & 0 \\
        -\frac{3}{L^2} & -\frac{2}{L} & \frac{3}{L^2} & -\frac{1}{L} \\
        \frac{2}{L^3} & \frac{1}{L^2} & -\frac{2}{L^3} & \frac{1}{L^2}
        \end{bmatrix}

    The displacement :math:`w(\bar{x})`, the bending moment :math:`M_{\bar{y}}(\bar{x})` and the shear force :math:`V_{\bar{z}}(\bar{x})` are computed from

    .. math::

        w(\bar{x}) = \mathbf{N}_{\text{beam}} \mathbf{\bar{a}}^e_{\text{beam},\bar{y}} + w_p(\bar{x})

    .. math::

        M_{\bar{y}}(\bar{x}) = -D_{EI_{\bar{y}}} \mathbf{B}_{\text{beam}} \mathbf{\bar{a}}^e_{\text{beam},\bar{y}} + M_{\bar{y},p}(\bar{x})

    .. math::

        V_{\bar{z}}(\bar{x}) = -D_{EI_{\bar{y}}} \frac{d\mathbf{B}_{\text{beam}}}{dx} \mathbf{\bar{a}}^e_{\text{beam},\bar{y}} + V_{\bar{z},p}(\bar{x})

    where

    .. math::

        w_p(\bar{x}) = \frac{q_{\bar{z}}}{D_{EI_{\bar{y}}}}\left(\frac{\bar{x}^4}{24}-\frac{L \bar{x}^3}{12}+\frac{L^2 \bar{x}^2}{24}\right)

    .. math::

        M_{\bar{y},p}(\bar{x}) = -q_{\bar{z}}\left(\frac{\bar{x}^2}{2}-\frac{L \bar{x}}{2}+\frac{L^2}{12}\right)

    .. math::

        V_{\bar{z},p}(\bar{x}) = -q_{\bar{z}}\left(\bar{x}-\frac{L}{2}\right)

    in which :math:`D_{EI_{\bar{y}}}`, :math:`L`, and :math:`q_{\bar{z}}` are defined in :code:`beam3e` and :math:`\mathbf{N}_{\text{beam}}`, :math:`\mathbf{B}_{\text{beam}}`, and :math:`\frac{d\mathbf{B}_{\text{beam}}}{dx}` are given above.

    The displacement :math:`\varphi(\bar{x})` and the torque :math:`T(\bar{x})` are computed from

    .. math::

        \varphi(\bar{x}) = \mathbf{N}_{\text{torsion}} \mathbf{\bar{a}}^e_{\text{torsion}} + \varphi_p(\bar{x})

    .. math::

        T(\bar{x}) = D_{GK} \mathbf{B}_{\text{torsion}} \mathbf{\bar{a}}^e + T_p(\bar{x})

    where

    .. math::

        \mathbf{N}_{\text{torsion}} = \mathbf{N}_{\text{bar}}

    .. math::

        \mathbf{B}_{\text{torsion}} = \mathbf{B}_{\text{bar}}

    .. math::

        \varphi_p(\bar{x}) = -\frac{q_{\omega}}{D_{GK}}\left(\frac{\bar{x}^2}{2}-\frac{L\bar{x}}{2}\right)

    .. math::

        T_p(\bar{x}) = -q_{\omega}\left(\bar{x}-\frac{L}{2}\right)

    in which :math:`D_{GK}`, :math:`L`, and :math:`q_{\omega}` are defined in :code:`beam3e`.
