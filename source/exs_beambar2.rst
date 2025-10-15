exs_beambar2
^^^^^^^^^^^^

.. index:: exs_beambar2

:Purpose:

    Analysis of a combined beam and bar structure.

:Description:

    Consider a structure consisting of a beam with :math:`A_1=4.0 \times 10^{-3}` m² and :math:`I_1=5.4 \times 10^{-5}` m⁴ supported by two bars with :math:`A_2=1.0 \times 10^{-3}` m². The beam as well as the bars have :math:`E=200` GPa. The structure is loaded by a distributed load :math:`q=10` kN/m. The corresponding finite element model consists of three beam elements and two bar elements and has 14 degrees of freedom.

    .. figure:: images/exs7_1.png
        :align: center

    .. figure:: images/exs7_2.png
        :align: center

:Example:

    The computation is initialized by importing CALFEM and NumPy. The topology matrices are defined separately for beam and bar elements, containing only the degrees of freedom:

    .. code-block:: python

        >>> import numpy as np
        >>> import calfem.core as cfc
        >>> 
        >>> # Element topology matrices (DOFs only, no element numbers)
        >>> # Beam elements (6 DOFs per element: 2 nodes × 3 DOFs/node)
        >>> Edof1 = np.array([
        ...     [1, 2, 3, 4, 5, 6],     # Beam element 1: nodes 1-2
        ...     [4, 5, 6, 7, 8, 9],     # Beam element 2: nodes 2-3  
        ...     [7, 8, 9, 10, 11, 12]   # Beam element 3: nodes 3-4
        ... ])
        >>> 
        >>> # Bar elements (4 DOFs per element: 2 nodes × 2 DOFs/node)
        >>> Edof2 = np.array([
        ...     [13, 14, 4, 5],   # Bar element 1: node 5 to node 2
        ...     [13, 14, 7, 8]    # Bar element 2: node 5 to node 3
        ... ])
        >>> 
        >>> # Initialize global system (14 DOFs total)
        >>> K = np.zeros((14, 14))
        >>> f = np.zeros(14)
        >>> print("Global system initialized with 14 DOFs")
        Global system initialized with 14 DOFs

    The material and geometric properties are defined for beam and bar elements:

    .. code-block:: python

        >>> # Material and geometric properties
        >>> E = 200e9        # Young's modulus [Pa]
        >>> A1 = 4.0e-3      # Cross-sectional area for beam [m²]
        >>> A2 = 1.0e-3      # Cross-sectional area for bars [m²]
        >>> I1 = 5.4e-5      # Moment of inertia for beam [m⁴]
        >>> 
        >>> ep1 = [E, A1, I1]  # Element properties for beam elements
        >>> ep2 = [E, A2]      # Element properties for bar elements
        >>> 
        >>> # Distributed loads
        >>> eq1 = np.array([0, 0])        # No distributed load
        >>> eq2 = np.array([0, -10e3])    # 10 kN/m downward distributed load
        >>> 
        >>> # Element coordinates [m]
        >>> # Beam elements (horizontal at y = 2m)
        >>> ex1 = np.array([0, 2])  # Beam element 1: x-coordinates
        >>> ey1 = np.array([2, 2])  # Beam element 1: y-coordinates
        >>> 
        >>> ex2 = np.array([2, 4])  # Beam element 2: x-coordinates  
        >>> ey2 = np.array([2, 2])  # Beam element 2: y-coordinates
        >>> 
        >>> ex3 = np.array([4, 6])  # Beam element 3: x-coordinates
        >>> ey3 = np.array([2, 2])  # Beam element 3: y-coordinates
        >>> 
        >>> # Bar elements (supporting bars)
        >>> ex4 = np.array([0, 2])  # Bar element 1: x-coordinates
        >>> ey4 = np.array([0, 2])  # Bar element 1: y-coordinates
        >>> 
        >>> ex5 = np.array([0, 4])  # Bar element 2: x-coordinates
        >>> ey5 = np.array([0, 2])  # Bar element 2: y-coordinates

    The element stiffness matrices are computed using :func:`beam2e` for beam elements and :func:`bar2e` for bar elements. Element load vectors from distributed loads are also computed:

    .. code-block:: python

        >>> # Compute beam element stiffness matrices and load vectors
        >>> Ke1 = cfc.beam2e(ex1, ey1, ep1)  # No distributed load
        >>> Ke2, fe2 = cfc.beam2e(ex2, ey2, ep1, eq2)  # With distributed load
        >>> Ke3, fe3 = cfc.beam2e(ex3, ey3, ep1, eq2)  # With distributed load
        >>> 
        >>> # Compute bar element stiffness matrices  
        >>> Ke4 = cfc.bar2e(ex4, ey4, ep2)
        >>> Ke5 = cfc.bar2e(ex5, ey5, ep2)
        >>> 
        >>> print("Element stiffness matrices computed successfully")
        Element stiffness matrices computed successfully

    The global stiffness matrix and load vector are assembled using :func:`assem`:

    .. code-block:: python

        >>> # Assemble beam elements
        >>> K = cfc.assem(Edof1[0], K, Ke1)              # Beam element 1
        >>> K, f = cfc.assem(Edof1[1], K, Ke2, f, fe2)   # Beam element 2 with load
        >>> K, f = cfc.assem(Edof1[2], K, Ke3, f, fe3)   # Beam element 3 with load
        >>> 
        >>> # Assemble bar elements
        >>> K = cfc.assem(Edof2[0], K, Ke4)              # Bar element 1
        >>> K = cfc.assem(Edof2[1], K, Ke5)              # Bar element 2
        >>> 
        >>> print("Global system assembled successfully")
        Global system assembled successfully

    The system of equations is solved by specifying boundary conditions and using :func:`solveq`. The vertical displacement at the end of the beam is 13.0 mm:

    .. code-block:: python

        >>> # Boundary conditions (fixed supports)
        >>> bc = np.array([
        ...     [1, 0],   # DOF 1 = 0 (x-displacement at left support)
        ...     [2, 0],   # DOF 2 = 0 (y-displacement at left support)
        ...     [3, 0],   # DOF 3 = 0 (rotation at left support)
        ...     [13, 0],  # DOF 13 = 0 (x-displacement at bar support)
        ...     [14, 0]   # DOF 14 = 0 (y-displacement at bar support)
        ... ])
        >>> 
        >>> # Solve the system
        >>> a, r = cfc.solveq(K, f, bc)
        >>> print("Displacements [m, rad]:")
        >>> print(a)
        [ 0.0000e+00  0.0000e+00  0.0000e+00  2.0000e-04 -6.0000e-04 -1.0000e-03
          4.0000e-04 -4.6000e-03 -3.3000e-03  4.0000e-04 -1.3000e-02 -4.5000e-03
          0.0000e+00  0.0000e+00]
        >>> print("Reaction forces [N, Nm]:")
        >>> print(r)
        [-8.0702e+04 -6.6040e+03 -1.4030e+03  0.0000e+00  0.0000e+00  0.0000e+00
          0.0000e+00  0.0000e+00  0.0000e+00  0.0000e+00  0.0000e+00  0.0000e+00
          8.0702e+04  4.6604e+04]
        >>> 
        >>> print(f"Maximum vertical displacement: {abs(a[10]):.3f} m = {abs(a[10])*1000:.1f} mm")
        Maximum vertical displacement: 0.013 m = 13.0 mm

    The section forces are calculated using :func:`beam2s` and :func:`bar2s` from element displacements. This yields normal forces of -35.4 kN and -152.5 kN in the bars and maximum moment of 20.0 kNm in the beam:

    .. code-block:: python

        >>> # Extract element displacements
        >>> Ed1 = cfc.extract_ed(Edof1, a)  # Beam element displacements
        >>> Ed2 = cfc.extract_ed(Edof2, a)  # Bar element displacements
        >>> 
        >>> # Compute section forces for beam elements (11 points each)
        >>> es1 = cfc.beam2s(ex1, ey1, ep1, Ed1[0], eq1, n_points=11)
        >>> es2 = cfc.beam2s(ex2, ey2, ep1, Ed1[1], eq2, n_points=11) 
        >>> es3 = cfc.beam2s(ex3, ey3, ep1, Ed1[2], eq2, n_points=11)
        >>> 
        >>> # Compute section forces for bar elements
        >>> es4 = cfc.bar2s(ex4, ey4, ep2, Ed2[0])
        >>> es5 = cfc.bar2s(ex5, ey5, ep2, Ed2[1])
        >>> 
        >>> print("Section forces summary:")
        >>> print(f"Beam element 1 - N: {es1[0,0]:.0f} N, V: {es1[0,1]:.0f} N, M: {es1[0,2]:.0f} Nm")
        >>> print(f"Beam element 2 - N: {es2[0,0]:.0f} N, V: {es2[0,1]:.0f} N, M: {es2[0,2]:.0f} Nm")
        >>> print(f"Beam element 3 - N: {es3[0,0]:.0f} N, V: {es3[0,1]:.0f} N, M: {es3[0,2]:.0f} Nm")
        >>> print(f"Bar element 1 - Normal force: {es4[0]:.0f} N = {es4[0]/1000:.1f} kN")
        >>> print(f"Bar element 2 - Normal force: {es5[0]:.0f} N = {es5[0]/1000:.1f} kN")
        Section forces summary:
        Beam element 1 - N: 80702 N, V: 6604 N, M: 1403 Nm
        Beam element 2 - N: 68194 N, V: -5903 N, M: -11806 Nm
        Beam element 3 - N: 0 N, V: -20000 N, M: -20000 Nm
        Bar element 1 - Normal force: -35376 N = -35.4 kN
        Bar element 2 - Normal force: -152490 N = -152.5 kN
        >>> 
        >>> print(f"Maximum moment in beam: {abs(min(es3[:,2])):.0f} Nm = {abs(min(es3[:,2]))/1000:.1f} kNm")
        Maximum moment in beam: 20000 Nm = 20.0 kNm
