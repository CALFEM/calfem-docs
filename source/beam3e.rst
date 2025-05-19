beam3e - Three dimensional beam element
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Purpose**

Compute element stiffness matrix for a three dimensional beam element.

.. figure:: images/BEAM3E.png
    :align: center
    :width: 70%

**Syntax**

.. code-block:: matlab

    Ke = beam3e(ex, ey, ez, eo, ep)
    [Ke, fe] = beam3e(ex, ey, ez, eo, ep, eq)

**Description**

``beam3e`` provides the global element stiffness matrix ``Ke`` for a three dimensional beam element.

The input variables

.. math::

    \begin{aligned}
    \mathrm{ex} &= [x_1 \;\; x_2] \\
    \mathrm{ey} &= [y_1 \;\; y_2] \\
    \mathrm{ez} &= [z_1 \;\; z_2]
    \end{aligned}
    \qquad
    \mathrm{eo} = [x_{\bar{z}} \;\; y_{\bar{z}} \;\; z_{\bar{z}}]

supply the element nodal coordinates :math:`x_1`, :math:`y_1`, etc. as well as the direction of the local beam coordinate system :math:`(\bar{x}, \bar{y}, \bar{z})`. By giving a global vector :math:`(x_{\bar{z}}, y_{\bar{z}}, z_{\bar{z}})` parallel with the positive local :math:`\bar{z}` axis of the beam, the local beam coordinate system is defined.

The variable

.. math::

    \mathrm{ep} = [E \;\; G \;\; A \;\; I_{\bar{y}} \;\; I_{\bar{z}} \;\; K_v]

supplies the modulus of elasticity :math:`E`, the shear modulus :math:`G`, the cross section area :math:`A`, the moment of inertia with respect to the :math:`\bar{y}` axis :math:`I_{\bar{y}}`, the moment of inertia with respect to the :math:`\bar{z}` axis :math:`I_{\bar{z}}`, and St. Venant torsion constant :math:`K_v`.

The element load vector ``fe`` can also be computed if uniformly distributed loads are applied to the element. The optional input variable

.. math::

    \mathrm{eq} = [q_{\bar{x}} \;\; q_{\bar{y}} \;\; q_{\bar{z}} \;\; q_{\bar{\omega}}]

then contains the distributed loads. The positive directions of :math:`q_{\bar{x}}`, :math:`q_{\bar{y}}`, and :math:`q_{\bar{z}}` follow the local beam coordinate system. The distributed torque :math:`q_{\bar{\omega}}` is positive if directed in the local :math:`\bar{x}`-direction, i.e. from local :math:`\bar{y}` to local :math:`\bar{z}`. All the loads are per unit length.

**Theory**

The element stiffness matrix :math:`\mathbf{K}^e` is computed according to

.. math::

    \mathbf{K}^e = \mathbf{G}^T \bar{\mathbf{K}}^e \mathbf{G}

where

.. math::

    \bar{\mathbf{K}}^e = \left[
    \begin{array}{cccccccccccc}
    \frac{D_{EA}}{L} & 0 & 0 & 0 & 0 & 0 & -\frac{D_{EA}}{L} & 0 & 0 & 0 & 0 & 0 \\
    0 & \frac{12D_{EI_{\bar z}}}{L^3} & 0 & 0 & 0 & \frac{6D_{EI_{\bar z}}}{L^2} & 0 & -\frac{12D_{EI_{\bar z}}}{L^3} & 0 & 0 & 0 & \frac{6D_{EI_{\bar z}}}{L^2} \\
    0 & 0 & \frac{12D_{EI_{\bar y}}}{L^3} & 0 & -\frac{6D_{EI_{\bar y}}}{L^2} & 0 & 0 & 0 & -\frac{12D_{EI_{\bar y}}}{L^3} & 0 & -\frac{6D_{EI_{\bar y}}}{L^2} & 0 \\
    0 & 0 & 0 & \frac{D_{GK}}{L} & 0 & 0 & 0 & 0 & 0 & -\frac{D_{GK}}{L} & 0 & 0 \\
    0 & 0 & -\frac{6D_{EI_{\bar y}}}{L^2} & 0 & \frac{4D_{EI_{\bar y}}}{L} & 0 & 0 & 0 & \frac{6D_{EI_{\bar y}}}{L^2} & 0 & \frac{2D_{EI_{\bar y}}}{L} & 0 \\
    0 & \frac{6D_{EI_{\bar z}}}{L^2} & 0 & 0 & 0 & \frac{4D_{EI_{\bar z}}}{L} & 0 & -\frac{6D_{EI_{\bar z}}}{L^2} & 0 & 0 & 0 & \frac{2D_{EI_{\bar z}}}{L} \\
    -\frac{D_{EA}}{L} & 0 & 0 & 0 & 0 & 0 & \frac{D_{EA}}{L} & 0 & 0 & 0 & 0 & 0 \\
    0 & -\frac{12D_{EI_{\bar z}}}{L^3} & 0 & 0 & 0 & -\frac{6D_{EI_{\bar z}}}{L^2} & 0 & \frac{12D_{EI_{\bar z}}}{L^3} & 0 & 0 & 0 & -\frac{6D_{EI_{\bar z}}}{L^2} \\
    0 & 0 & -\frac{12D_{EI_{\bar y}}}{L^3} & 0 & \frac{6D_{EI_{\bar y}}}{L^2} & 0 & 0 & 0 & \frac{12D_{EI_{\bar y}}}{L^3} & 0 & \frac{6D_{EI_{\bar y}}}{L^2} & 0 \\
    0 & 0 & 0 & -\frac{D_{GK}}{L} & 0 & 0 & 0 & 0 & 0 & \frac{D_{GK}}{L} & 0 & 0 \\
    0 & 0 & -\frac{6D_{EI_{\bar y}}}{L^2} & 0 & \frac{2D_{EI_{\bar y}}}{L} & 0 & 0 & 0 & \frac{6D_{EI_{\bar y}}}{L^2} & 0 & \frac{4D_{EI_{\bar y}}}{L} & 0 \\
    0 & \frac{6D_{EI_{\bar z}}}{L^2} & 0 & 0 & 0 & \frac{2D_{EI_{\bar z}}}{L} & 0 & -\frac{6D_{EI_{\bar z}}}{L^2} & 0 & 0 & 0 & \frac{4D_{EI_{\bar z}}}{L}
    \end{array}
    \right]

and

.. math::

    \mathbf{G} = \left[
    \begin{array}{cccccccccccc}
    n_{x\bar{x}} & n_{y\bar{x}} & n_{z\bar{x}} & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
    n_{x\bar{y}} & n_{y\bar{y}} & n_{z\bar{y}} & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
    n_{x\bar{z}} & n_{y\bar{z}} & n_{z\bar{z}} & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & n_{x\bar{x}} & n_{y\bar{x}} & n_{z\bar{x}} & 0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & n_{x\bar{y}} & n_{y\bar{y}} & n_{z\bar{y}} & 0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & n_{x\bar{z}} & n_{y\bar{z}} & n_{z\bar{z}} & 0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & n_{x\bar{x}} & n_{y\bar{x}} & n_{z\bar{x}} & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & n_{x\bar{y}} & n_{y\bar{y}} & n_{z\bar{y}} & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & n_{x\bar{z}} & n_{y\bar{z}} & n_{z\bar{z}} & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & n_{x\bar{x}} & n_{y\bar{x}} & n_{z\bar{x}} \\
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & n_{x\bar{y}} & n_{y\bar{y}} & n_{z\bar{y}} \\
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & n_{x\bar{z}} & n_{y\bar{z}} & n_{z\bar{z}}
    \end{array}
    \right]

where the axial stiffness :math:`D_{EA}`, the bending stiffness :math:`D_{EI_{\bar z}}`, the bending stiffness :math:`D_{EI_{\bar y}}`, and the St. Venant torsion stiffness :math:`D_{GK}` are given by

.. math::

    D_{EA} = EA; \quad D_{EI_{\bar z}} = EI_{\bar z}; \quad D_{EI_{\bar y}} = EI_{\bar y}; \quad D_{GK} = GK_v

The length :math:`L` is given by

.. math::

    L = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}

The transformation matrix :math:`\mathbf{G}` contains direction cosines computed as

.. math::

    \begin{aligned}
    n_{x\bar{x}} &= \frac{x_2 - x_1}{L} \qquad n_{y\bar{x}} = \frac{y_2 - y_1}{L} \qquad n_{z\bar{x}} = \frac{z_2 - z_1}{L} \\
    n_{x\bar{z}} &= \frac{x_{\bar{z}}}{L_{\bar{z}}} \qquad n_{y\bar{z}} = \frac{y_{\bar{z}}}{L_{\bar{z}}} \qquad n_{z\bar{z}} = \frac{z_{\bar{z}}}{L_{\bar{z}}} \\
    n_{x\bar{y}} &= n_{y\bar{z}} n_{z\bar{x}} - n_{z\bar{z}} n_{y\bar{x}} \\
    n_{y\bar{y}} &= n_{z\bar{z}} n_{x\bar{x}} - n_{x\bar{z}} n_{z\bar{x}} \\
    n_{z\bar{y}} &= n_{x\bar{z}} n_{y\bar{x}} - n_{y\bar{z}} n_{x\bar{x}}
    \end{aligned}

where

.. math::

    L_{\bar{z}} = \sqrt{x_{\bar{z}}^2 + y_{\bar{z}}^2 + z_{\bar{z}}^2}

The element load vector :math:`\mathbf{f}_l^e`, stored in ``fe``, is computed according to

.. math::

    \mathbf{f}_l^e = \mathbf{G}^T \bar{\mathbf{f}}_l^e

where

.. math::

    \bar{\mathbf{f}}_l^e =
    \begin{bmatrix}
    \dfrac{q_{\bar{x}}L}{2} \\
    \dfrac{q_{\bar{y}}L}{2} \\
    \dfrac{q_{\bar{z}}L}{2} \\
    \dfrac{q_{\bar{\omega}}L}{2} \\
    -\dfrac{q_{\bar{z}}L^2}{12} \\
    \dfrac{q_{\bar{y}}L^2}{12} \\
    \dfrac{q_{\bar{x}}L}{2} \\
    \dfrac{q_{\bar{y}}L}{2} \\
    \dfrac{q_{\bar{z}}L}{2} \\
    \dfrac{q_{\bar{\omega}}L}{2} \\
    \dfrac{q_{\bar{z}}L^2}{12} \\
    -\dfrac{q_{\bar{y}}L^2}{12}
    \end{bmatrix}
