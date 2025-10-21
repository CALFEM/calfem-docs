.. _beam2ds:
.. index:: 
   single: beam2ds
   single: dynamic beam stress
   single: beam section forces
   single: 2D beam stress
   single: dynamic analysis
   single: section forces
   pair: finite element; stress
   pair: dynamic; beam
   pair: beam; stress
   pair: section; forces
   pair: 2D; stress
   pair: dynamic; analysis

beam2ds
^^^^^^^

:Purpose:

    Compute section forces for a two dimensional beam element in dynamic analysis.

    .. figure:: images/BEAM2S.png
        :align: center
        :width: 70%

:Syntax:

.. only:: matlab

    .. code-block:: matlab

    .. code:: matlab

        es = beam2ds(ex, ey, ep, ed, ev, ea)

.. only:: python

    .. code-block:: python

        es = cfc.beam2ds(ex, ey, ep, ed, ev, ea)

:Description:

    :code:`beam2ds` computes the section forces at the ends of the dynamic beam element :code:`beam2de`.

    The input variables :code:`ex`, :code:`ey` and :code:`ep` are defined in
    :code:`beam2de`. The element displacements, velocities, and accelerations, stored in :code:`ed`, :code:`ev`, and :code:`ea` respectively, are obtained by the function :code:`extract_ed`.

    The output variable :code:`es` contains the section forces at the ends of the beam:

    .. math::

        es = \begin{bmatrix}
        N_1 & V_1 & M_1 \\
        N_2 & V_2 & M_2
        \end{bmatrix}

:Theory:

    The section forces at the ends of the beam are obtained from the element force vector:

    .. math::

        \bar{\mathbf{P}} =
        \begin{bmatrix}
        -N_1 & -V_1 & -M_1 & N_2 & V_2 & M_2
        \end{bmatrix}^T

    computed according to:

    .. math::

        \bar{\mathbf{P}} =
            \bar{\mathbf{K}}^e \mathbf{G} \mathbf{a}^e
        + \bar{\mathbf{C}}^e \mathbf{G} \dot{\mathbf{a}}^e
        + \bar{\mathbf{M}}^e \mathbf{G} \ddot{\mathbf{a}}^e

    The matrices :math:`\bar{\mathbf{K}}^e` and :math:`\mathbf{G}` are described in :code:`beam2e`, and the matrices :math:`\bar{\mathbf{M}}^e` and :math:`\bar{\mathbf{C}}^e` are described in :code:`beam2d`.

    The nodal displacements:

    .. math::

        \mathbf{a}^e = \begin{bmatrix}
        u_1 & u_2 & u_3 & u_4 & u_5 & u_6
        \end{bmatrix}^T

    shown in :code:`beam2de` also define the directions of the nodal velocities:

    .. math::

        \dot{\mathbf{a}}^e = \begin{bmatrix}
        \dot{u}_1 & \dot{u}_2 & \dot{u}_3 & \dot{u}_4 & \dot{u}_5 & \dot{u}_6
        \end{bmatrix}^T

    and the nodal accelerations:

    .. math::

        \ddot{\mathbf{a}}^e = \begin{bmatrix}
        \ddot{u}_1 & \ddot{u}_2 & \ddot{u}_3 & \ddot{u}_4 & \ddot{u}_5 & \ddot{u}_6
        \end{bmatrix}^T

    Note that the transposes of :math:`\mathbf{a}^e`, :math:`\dot{\mathbf{a}}^e`, and :math:`\ddot{\mathbf{a}}^e` are stored in :code:`ed`, :code:`ev`, and :code:`ea` respectively.
