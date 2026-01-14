exn_bar2g
^^^^^^^^^

.. index:: exn_bar2g

:Purpose:

    Plane truss considering geometric nonlinearity.

:Description:

    Consider a plane truss consisting of two bars with the properties :math:`E=200` GPa, :math:`A_1=6.0 \times 10^{-4}` m², and :math:`A_2=3.0 \times 10^{-4}` m². The truss is loaded by a force :math:`P=10` MN to the left and a force :math:`F=0.2` MN downwards. The corresponding finite element model consists of two elements and six degrees of freedom.

    .. only:: html
        
        .. figure:: images/exn1.svg
            :align: center
            :width: 700px
    
    .. only:: latex
        
        .. figure:: images/exn1.svg
            :align: center
            :width: 70%

:Example:

    The computation is initialized by defining the topology matrix :code:`Edof`, containing element numbers and global element degrees of freedom. The element property vectors :code:`ep1` and :code:`ep2` and the element coordinate vectors :code:`ex1`, :code:`ex2`, :code:`ey1`, and :code:`ey2` are also defined:

    .. code-block:: python

        import numpy as np
        import calfem.core as cfc
        import calfem.utils as cfu        

        edof = np.array([[1, 2, 5, 6], [3, 4, 5, 6]])        
        E = 10e9
        A1 = 4e-2
        A2 = 1e-2
        ep1 = np.array([E, A1])
        ep2 = np.array([E, A2])

        ex1 = np.array([0.0, 1.6])
        ey1 = np.array([0.0, 0.0])
        ex2 = np.array([0.0, 1.6])
        ey2 = np.array([1.2, 0])

    The bar element function considering geometric nonlinearity :code:`bar2ge` requires the value of axial force :math:`Q_{\bar{x}}`. Since the axial forces are a result of the computation, the computation procedure is iterative. Initially, the axial forces are set to zero, i.e. :math:`Q_{\bar{x}}^{(1)}=0` and :math:`Q_{\bar{x}}^{(2)}=0` which are stored in :code:`QX1` and :code:`QX2`. This means that the first iteration is equivalent to a linear analysis using :code:`bar2e`. To make sure that the first iteration is performed, the scalar used for storing the previous axial force in element 1 :code:`QX01` is set to 1. To avoid dividing by 0 in the second convergence check, a nonzero but small value is assumed for the initial axial force in Element 1, i.e. :math:`Q_{\bar{x}, 0}^{(1)}=0.0001`. In each iteration the axial forces :code:`QX1` and :code:`QX2` are updated according to the computational result. The iterations continue until the difference in axial force :code:`QX1` of the two latest iterations is less than an accepted error :code:`eps` chosen as :math:`1.0 \times 10^{-6}` (:code:`QX1` - :code:`QX01`) / :code:`QX01` :math:`<` :code:`eps`:

    .. code-block:: python

        eps = 1e-6  # Error norm
        QX1 = 0.01
        QX2 = 0
        # Initial axial forces
        QX01 = 1  # Axial force of the initial former iteration
        n = 0  # Iteration counter	


    In each iteration the global stiffness matrix :code:`K` (6×6) and the load vector :code:`f` (6×1) is initially filled with zeros. The nodal loads of 10.0 MN and 0.2 MN acting at lower right corner of the frame are placed in position 5 and 6 of the load vector, respectively. Element stiffness matrices are computed by :code:`bar2ge` and assembled using :code:`assem`, after which the system of equations is solved using :code:`solveq`. Based on the computed displacements :code:`a`, new values of section forces and axial forces are computed by :code:`bar2gs`. If :code:`QX1` does not converge in 20 iterations the analysis is interrupted:

    .. code-block:: python

        while abs((QX1 - QX01) / QX01) > eps:

            n += 1

            K = np.zeros((6, 6))
            f = np.zeros((6, 1))
            f[4] = -10e6
            f[5] = -0.2e6

            Ke1 = cfc.bar2ge(ex1, ey1, ep1, QX1)
            Ke2 = cfc.bar2ge(ex2, ey2, ep2, QX2)
            K = cfc.assem(edof[0, :], K, Ke1)
            K = cfc.assem(edof[1, :], K, Ke2)
            bc = np.array([1, 2, 3, 4])
            a, r = cfc.solveq(K, f, bc)

            Ed = cfc.extract_ed(edof, a)

            QX01 = QX1
            es1, QX1 = cfc.bar2gs(ex1, ey1, ep1, Ed[0, :])
            es2, QX2 = cfc.bar2gs(ex2, ey2, ep2, Ed[1, :])

            if n > 20:
                print("The solution does not converge")
                break

    After 7 iterations the computation has converged and the axial forces are:

    .. code-block:: python

        # Displacements:

        +-------------+
        |  0.0000e+00 |
        |  0.0000e+00 |
        |  0.0000e+00 |
        |  0.0000e+00 |
        | -4.4544e-02 |
        | -1.0884e-01 |
        +-------------+

        # Normal forces:

        [-11135997.48710512]
        [1483293.2117848]

    The displacements according to the linear analysis and the analysis considering geometric nonlinearity are respectively:

    .. code-block:: python

        a =                         a =

                 0                           0
                 0                           0
                 0                           0
                 0                           0
           -0.0411                     -0.0445
           -0.0659                     -0.1088

    The vertical displacement at the node to the right is 108.8 mm, which is 1.6 times larger than the result from a linear computation according to the first iteration. The axial force in Element 2 is 1.483 kN, which is 4.5 times larger than the value obtained in the linear computation.
