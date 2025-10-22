platrs
^^^^^^

:Purpose:
    Compute section forces in a rectangular plate element.

    .. only:: html
        
        .. figure:: images/PLATRS.svg
            :align: center
            :width: 400px
    
    .. only:: latex
        
        .. figure:: images/PLATRS.svg
            :align: center
            :width: 70%

:Syntax:
    .. code:: matlab

        [es,et]=platrs(ex,ey,ep,D,ed)

:Description:
    :math:`\mathtt{platrs}` computes the section forces :math:`\mathtt{es}` and the curvature matrix :math:`\mathtt{et}` in a rectangular plate element.
    The section forces and the curvatures are computed at the center of the element.

    The input variables :math:`\mathbf{ex}`, :math:`\mathbf{ey}`, :math:`\mathbf{ep}` and :math:`\mathbf{D}` are defined in :math:`\mathtt{platre}`.
    The vector :math:`\mathbf{ed}` contains the nodal displacements :math:`\mathbf{a}^e` of the element and is obtained by the function :math:`\mathtt{extract}` as

    .. math::

        \mathbf{ed} = (\mathbf{a}^e)^T = [\,u_1\;\; u_2\;\; \ldots \;\; u_{12}\;]

    The output variables

    .. math::

        \mathtt{es} = \left[\,\mathbf{M}^T\; \mathbf{V}^T\,\right] = \left[\, M_{xx}\; M_{yy}\; M_{xy}\; V_{xz}\; V_{yz}\; \right]

    .. math::

        \mathtt{et} = \boldsymbol{\kappa}^T = \left[\, \kappa_{xx}\; \kappa_{yy}\; \kappa_{xy}\; \right]

    contain the section forces and curvatures in global directions.

:Theory:
    The curvatures and the section forces are computed according to

    .. math::

        \boldsymbol{\kappa} = \left[
        \begin{array}{c}
        \kappa_{xx} \\
        \kappa_{yy} \\
        \kappa_{xy}
        \end{array}
        \right] =
        \bar{\mathbf{B}}\,\mathbf{C}^{-1}\,\mathbf{a}^e

    .. math::

        \mathbf{M} =
        \left[
        \begin{array}{c}
        M_{xx} \\
        M_{yy} \\
        M_{xy}
        \end{array}
        \right] =
        \tilde{\mathbf{D}}\,\boldsymbol{\kappa}

    .. math::

        \mathbf{V} =
        \left[
        \begin{array}{c}
        V_{xz} \\
        V_{yz}
        \end{array}
        \right] =
        \tilde{\nabla}\,\mathbf{M}

    where the matrices :math:`\tilde{\mathbf{D}}`, :math:`\bar{\mathbf{B}}`, :math:`\mathbf{C}` and :math:`\mathbf{a}^e` are described in :math:`\mathtt{platre}`, and where

    .. math::

        \tilde{\nabla} = \left[
        \begin{array}{ccc}
        \dfrac{\partial}{\partial x} & 0 & \dfrac{\partial}{\partial y} \\
        0 & \dfrac{\partial}{\partial y} & \dfrac{\partial}{\partial x}
        \end{array}
        \right]
