.. _beam1ws:
.. index:: 
   single: beam1ws
   single: beam stress
   single: elastic support stress
   single: 1D beam stress
   single: foundation beam stress
   single: section forces
   pair: finite element; stress
   pair: beam; stress
   pair: elastic; support
   pair: foundation; stress
   pair: section; forces
   pair: 1D; stress

beam1ws
^^^^^^^

:Purpose:

    Compute section forces in a one dimensional beam element with elastic support.

    .. only:: html

        .. figure:: images/beam1s.svg
            :align: center
            :width: 400px

    .. only:: latex

        .. figure:: images/beam1s.svg
            :align: center
            :width: 70%

:Syntax:

.. only:: matlab

    .. code:: matlab

        es = beam1ws(ex, ep, ed)
        es = beam1ws(ex, ep, ed, eq)
        [es, edi, eci] = beam1ws(ex, ep, ed, eq, n)

.. only:: python

    .. code-block:: python

        es = cfc.beam1ws(ex, ep, ed)
        es = cfc.beam1ws(ex, ep, ed, eq)
        es, edi, eci = cfc.beam1ws(ex, ep, ed, eq, n)

:Description:

    :code:`beam1ws` computes the section forces and displacements in local directions
    along the beam element :code:`beam1we`.

    The input variables :code:`ex`, :code:`ep` and :code:`eq` are defined in
    :code:`beam1we`, and the element displacements, stored
    in :code:`ed`, are obtained by the function :code:`extract_ed`.
    If distributed loads are applied to the element, the variable :code:`eq` must be
    included.
    The number of evaluation points for section forces and displacements are
    determined by :code:`n`. If :code:`n` is omitted, only the ends of the
    beam are evaluated.

    The output variables

    :code:`es`:math:`= \begin{bmatrix}
    V(0)  & M(0) \\
    V(\bar{x}_{2}) & M(\bar{x}_{2})  \\
    \vdots & \vdots \\
    V(\bar{x}_{n-1}) & M(\bar{x}_{n-1})\\
    V(L) & M(L)
    \end{bmatrix}`
    :math:`\qquad`
    :code:`edi`:math:`= \begin{bmatrix}
    v(0)   \\
    v(\bar{x}_{2})   \\
    \vdots \\
    v(\bar{x}_{n-1})\\
    v(L)
    \end{bmatrix}` 
    :math:`\qquad` 
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

        \mathbf{\bar{a}}^e = \begin{bmatrix} \bar{u}_1 \\ \bar{u}_2 \\ \bar{u}_3 \\ \bar{u}_4 \end{bmatrix}

    where the transpose of :math:`\mathbf{a}^e` is stored in :code:`ed`.

    The displacement :math:`v(\bar{x})`, the bending moment :math:`M(\bar{x})` and the shear force :math:`V(\bar{x})` are computed from

    .. math::

        v(\bar{x}) = \mathbf{N} \mathbf{\bar{a}}^e + v_p(\bar{x})

    .. math::

        M(\bar{x}) = D_{EI} \mathbf{B} \mathbf{\bar{a}}^e + M_p(\bar{x})

    .. math::

        V(\bar{x}) = -D_{EI} \frac{d\mathbf{B}}{dx} \mathbf{\bar{a}}^e + V_p(\bar{x})

    where

    .. math::

        \mathbf{N} = \begin{bmatrix} 1 & \bar{x} & \bar{x}^2 & \bar{x}^3 \end{bmatrix} \mathbf{C}^{-1}

    .. math::

        \mathbf{B} = \begin{bmatrix} 0 & 0 & 2 & 6\bar{x} \end{bmatrix} \mathbf{C}^{-1}

    .. math::

        \frac{d\mathbf{B}}{dx} = \begin{bmatrix} 0 & 0 & 0 & 6 \end{bmatrix} \mathbf{C}^{-1}

    .. math::

        v_p(\bar{x}) = -\frac{k_{\bar{y}}}{D_{EI}}
        \begin{bmatrix}
        \frac{\bar{x}^4 - 2L\bar{x}^3 + L^2\bar{x}^2}{24} \\
        \frac{\bar{x}^5 - 3L^2\bar{x}^3 + 2L^3\bar{x}^2}{120} \\
        \frac{\bar{x}^6 - 4L^3\bar{x}^3 + 3L^4\bar{x}^2}{360} \\
        \frac{\bar{x}^7 - 5L^4\bar{x}^3 + 4L^5\bar{x}^2}{840}
        \end{bmatrix}^T \mathbf{C}^{-1} \mathbf{\bar{a}}^e
        + \frac{q_{\bar{y}}}{D_{EI}}\left(\frac{\bar{x}^4}{24} - \frac{L\bar{x}^3}{12} + \frac{L^2\bar{x}^2}{24}\right)

    .. math::

        M_p(\bar{x}) = -k_{\bar{y}}
        \begin{bmatrix}
        \frac{6\bar{x}^2 - 6L\bar{x} + L^2}{12} \\
        \frac{10\bar{x}^3 - 9L^2\bar{x} + 2L^3}{60} \\
        \frac{5\bar{x}^4 - 4L^3\bar{x} + L^4}{60} \\
        \frac{21\bar{x}^5 - 15L^4\bar{x} + 4L^5}{420}
        \end{bmatrix}^T \mathbf{C}^{-1} \mathbf{\bar{a}}^e
        + q_{\bar{y}}\left(\frac{\bar{x}^2}{2} - \frac{L\bar{x}}{2} + \frac{L^2}{12}\right)

    .. math::

        V_p(\bar{x}) = k_{\bar{y}}
        \begin{bmatrix}
        \frac{2\bar{x} - L}{2} \\
        \frac{10\bar{x}^2 - 3L^2}{20} \\
        \frac{5\bar{x}^3 - L^3}{15} \\
        \frac{7\bar{x}^4 - L^4}{28}
        \end{bmatrix}^T \mathbf{C}^{-1} \mathbf{\bar{a}}^e
        - q_{\bar{y}}\left(\bar{x} - \frac{L}{2}\right)

    in which :math:`D_{EI}`, :math:`k_{\bar{y}}`, :math:`L`, and :math:`q_{\bar{y}}`
    are defined in :code:`beam1we` and

    .. math::

        \mathbf{C}^{-1} =
        \begin{bmatrix}
        1 & 0 & 0 & 0 \\
        0 & 1 & 0 & 0 \\
        -\frac{3}{L^2} & -\frac{2}{L} & \frac{3}{L^2} & -\frac{1}{L} \\
        \frac{2}{L^3} & \frac{1}{L^2} & -\frac{2}{L^3} & \frac{1}{L^2}
        \end{bmatrix}