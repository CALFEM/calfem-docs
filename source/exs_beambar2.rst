exs_beambar2
^^^^^^^^^^^^

.. index:: exs_beambar2

:Purpose:

    Analysis of a combined beam and bar structure.

:Description:

    Consider a structure consisting of a beam with :math:`A_1=4.0 \times 10^{-3}` m² and :math:`I_1=5.4 \times 10^{-5}` m⁴ supported by two bars with :math:`A_2=1.0 \times 10^{-3}` m². The beam as well as the bars have :math:`E=200` GPa. The structure is loaded by a distributed load :math:`q=10` kN/m. The corresponding finite element model consists of three beam elements and two bar elements and has 14 degrees of freedom.

    .. only:: html
        
        .. figure:: images/exs7_1.svg
            :align: center
            :width: 400px
    
    .. only:: latex
        
        .. figure:: images/exs7_1.svg
            :align: center
            :width: 70%

    .. only:: html
        
        .. figure:: images/exs7_2.svg
            :align: center
            :width: 400px
    
    .. only:: latex
        
        .. figure:: images/exs7_2.svg
            :align: center
            :width: 70%

:Example:

    The computation is initialized by importing CALFEM and NumPy. The topology matrices are defined separately for beam and bar elements, containing only the degrees of freedom:

    .. code-block:: python

        >>> import numpy as np
        >>> import calfem.core as cfc
        >>> import calfem.utils as cfu
        >>> 
        >>> edof1 = np.array([
        ...     [1, 2, 3, 4, 5, 6],     # Beam element 1: nodes 1-2
        ...     [4, 5, 6, 7, 8, 9],     # Beam element 2: nodes 2-3  
        ...     [7, 8, 9, 10, 11, 12]   # Beam element 3: nodes 3-4
        ... ])
        >>> 
        >>> edof2 = np.array([
        ...     [13, 14, 4, 5],   # Bar element 1: node 5 to node 2
        ...     [13, 14, 7, 8]    # Bar element 2: node 5 to node 3
        ... ])
        >>> 
        >>> K = np.zeros((14, 14))
        >>> f = np.zeros((14, 1)

    The material and geometric properties are defined for beam and bar elements:

    .. code-block:: python

        >>> E = 200e9        # Young's modulus [Pa]
        >>> A1 = 4.0e-3      # Cross-sectional area for beam [m²]
        >>> A2 = 1.0e-3      # Cross-sectional area for bars [m²]
        >>> I1 = 5.4e-5      # Moment of inertia for beam [m⁴]
        >>> 
        >>> ep1 = [E, A1, I1]  # Element properties for beam elements
        >>> ep2 = [E, A2]      # Element properties for bar elements
        >>> 
        >>> eq1 = np.array([0, 0])        # No distributed load
        >>> eq2 = np.array([0, -10e3])    # 10 kN/m downward distributed load
        >>> 
        >>> ex1 = np.array([0, 2])  # Beam element 1: x-coordinates
        >>> ey1 = np.array([2, 2])  # Beam element 1: y-coordinates
        >>> 
        >>> ex2 = np.array([2, 4])  # Beam element 2: x-coordinates  
        >>> ey2 = np.array([2, 2])  # Beam element 2: y-coordinates
        >>> 
        >>> ex3 = np.array([4, 6])  # Beam element 3: x-coordinates
        >>> ey3 = np.array([2, 2])  # Beam element 3: y-coordinates
        >>> 
        >>> ex4 = np.array([0, 2])  # Bar element 1: x-coordinates
        >>> ey4 = np.array([0, 2])  # Bar element 1: y-coordinates
        >>> 
        >>> ex5 = np.array([0, 4])  # Bar element 2: x-coordinates
        >>> ey5 = np.array([0, 2])  # Bar element 2: y-coordinates

    The element stiffness matrices are computed using :func:`beam2e` for beam elements and :func:`bar2e` for bar elements. Element load vectors from distributed loads are also computed:

    .. code-block:: python

        >>> Ke1 = cfc.beam2e(ex1, ey1, ep1)  # No distributed load
        >>> Ke2, fe2 = cfc.beam2e(ex2, ey2, ep1, eq2)  # With distributed load
        >>> Ke3, fe3 = cfc.beam2e(ex3, ey3, ep1, eq2)  # With distributed load
        >>> 
        >>> Ke4 = cfc.bar2e(ex4, ey4, ep2)
        >>> Ke5 = cfc.bar2e(ex5, ey5, ep2)

    The global stiffness matrix and load vector are assembled using :func:`assem`:

    .. code-block:: python

        >>> K = cfc.assem(edof1[0, :], K, Ke1)
        >>> K, f = cfc.assem(edof1[1, :], K, Ke2, f, fe2)
        >>> K, f = cfc.assem(edof1[2, :], K, Ke3, f, fe3)
        >>> K = cfc.assem(edof2[0, :], K, Ke4)
        >>> K = cfc.assem(edof2[1, :], K, Ke5)
        >>> 
        >>> K = cfc.assem(edof2[0], K, Ke4)              # Bar element 1
        >>> K = cfc.assem(edof2[1], K, Ke5)              # Bar element 2

    The system of equations is solved by specifying boundary conditions and using :func:`solveq`. The vertical displacement at the end of the beam is 13.0 mm:

    .. code-block:: python

        >>> bc = np.array([1, 2, 3, 13, 14])
        >>> a, r = cfc.solveq(K, f, bc)
        >>> 
        >>> print("Displacements [m, rad]:")
        >>> print(a)
        Displacements [m, rad]:
        [[ 0.        ]
         [ 0.        ]
         [ 0.        ]
         [ 0.00020112]
         [-0.00030208]
         [-0.00053629]
         [ 0.0003844 ]
         [-0.00281787]
         [-0.0023903 ]
         [ 0.0003844 ]
         [-0.00945033]
         [-0.00362487]
         [ 0.        ]
         [ 0.        ]]        
        >>> print("Reaction forces [N, Nm]:")
        >>> print(r)
        Reaction forces [N, Nm]:
        [[-8.04490636e+04]
         [-3.79407610e+03]
         [-8.98127126e+02]
         [ 0.00000000e+00]
         [-7.27595761e-12]
         [ 1.36424205e-12]
         [-5.82076609e-11]
         [ 0.00000000e+00]
         [ 1.45519152e-11]
         [ 0.00000000e+00]
         [ 1.45519152e-11]
         [-5.00222086e-12]
         [ 8.04490636e+04]
         [ 4.37940761e+04]]        
        >>> print(f"Maximum vertical displacement: {abs(a[10]):.3f} m = {abs(a[10])*1000:.1f} mm")
        Maximum vertical displacement: 0.009 m = 9.5 mm

    The section forces are calculated using :func:`beam2s` and :func:`bar2s` from element displacements. This yields normal forces of -35.4 kN and -152.5 kN in the bars and maximum moment of 20.0 kNm in the beam:

    .. code-block:: python

        >>> ed1 = cfc.extract_ed(edof1, a)  # Beam element displacements
        >>> ed2 = cfc.extract_ed(edof2, a)  # Bar element displacements
        >>> 
        >>> es1, _, _ = cfc.beam2s(ex1, ey1, ep1, ed1[0], eq1, nep=11)
        >>> es2, _, _ = cfc.beam2s(ex2, ey2, ep1, ed1[1], eq2, nep=11) 
        >>> es3, _, _ = cfc.beam2s(ex3, ey3, ep1, ed1[2], eq2, nep=11)
        >>> 
        >>> es4, _, _ = cfc.bar2s(ex4, ey4, ep2, ed2[0], nep=11)
        >>> es5, _, _ = cfc.bar2s(ex5, ey5, ep2, ed2[1], nep=11)

        >>> cfu.disp_h2("es1 = ")
        ## es1 =

        >>> cfu.disp_array(es1, headers=["N", "V", "M"])
        +------------+------------+-------------+
        |          N |          V |           M |
        |------------+------------+-------------|
        | 8.0449e+04 | 3.7941e+03 |  8.9813e+02 |
        | 8.0449e+04 | 3.7941e+03 |  1.3931e+02 |
        | 8.0449e+04 | 3.7941e+03 | -6.1950e+02 |
        | 8.0449e+04 | 3.7941e+03 | -1.3783e+03 |
        | 8.0449e+04 | 3.7941e+03 | -2.1371e+03 |
        | 8.0449e+04 | 3.7941e+03 | -2.8959e+03 |
        | 8.0449e+04 | 3.7941e+03 | -3.6548e+03 |
        | 8.0449e+04 | 3.7941e+03 | -4.4136e+03 |
        | 8.0449e+04 | 3.7941e+03 | -5.1724e+03 |
        | 8.0449e+04 | 3.7941e+03 | -5.9312e+03 |
        | 8.0449e+04 | 3.7941e+03 | -6.6900e+03 |
        +------------+------------+-------------+        
        >>> cfu.disp_h2("es2 = ")
        ## es2 =

        >>> cfu.disp_array(es2, headers=["N", "V", "M"])

        +------------+-------------+-------------+
        |          N |           V |           M |
        |------------+-------------+-------------|
        | 7.3310e+04 | -3.3450e+03 | -6.6900e+03 |
        | 7.3310e+04 | -1.3450e+03 | -6.2210e+03 |
        | 7.3310e+04 |  6.5499e+02 | -6.1520e+03 |
        | 7.3310e+04 |  2.6550e+03 | -6.4830e+03 |
        | 7.3310e+04 |  4.6550e+03 | -7.2140e+03 |
        | 7.3310e+04 |  6.6550e+03 | -8.3450e+03 |
        | 7.3310e+04 |  8.6550e+03 | -9.8760e+03 |
        | 7.3310e+04 |  1.0655e+04 | -1.1807e+04 |
        | 7.3310e+04 |  1.2655e+04 | -1.4138e+04 |
        | 7.3310e+04 |  1.4655e+04 | -1.6869e+04 |
        | 7.3310e+04 |  1.6655e+04 | -2.0000e+04 |
        +------------+-------------+-------------+        
        >>> cfu.disp_h2("es3 = ")
        ## es3 =

        >>> cfu.disp_array(es3, headers=["N", "V", "M"])
        +------------+-------------+-------------+
        |          N |           V |           M |
        |------------+-------------+-------------|
        | 0.0000e+00 | -2.0000e+04 | -2.0000e+04 |
        | 0.0000e+00 | -1.8000e+04 | -1.6200e+04 |
        | 0.0000e+00 | -1.6000e+04 | -1.2800e+04 |
        | 0.0000e+00 | -1.4000e+04 | -9.8000e+03 |
        | 0.0000e+00 | -1.2000e+04 | -7.2000e+03 |
        | 0.0000e+00 | -1.0000e+04 | -5.0000e+03 |
        | 0.0000e+00 | -8.0000e+03 | -3.2000e+03 |
        | 0.0000e+00 | -6.0000e+03 | -1.8000e+03 |
        | 0.0000e+00 | -4.0000e+03 | -8.0000e+02 |
        | 0.0000e+00 | -2.0000e+03 | -2.0000e+02 |
        | 0.0000e+00 |  2.3419e-12 |  1.1124e-11 |
        +------------+-------------+-------------+        
        >>> cfu.disp_h2("es4 = ")
        ## es4 =

        >>> cfu.disp_array(es4, headers=["N"])
        +-------------+
        |           N |
        |-------------|
        | -5.0481e+03 |
        | -5.0481e+03 |
        | -5.0481e+03 |
        | -5.0481e+03 |
        | -5.0481e+03 |
        | -5.0481e+03 |
        | -5.0481e+03 |
        | -5.0481e+03 |
        | -5.0481e+03 |
        | -5.0481e+03 |
        | -5.0481e+03 |
        +-------------+        
        >>> cfu.disp_h2("es5 = ")
        ## es5 =

        >>> cfu.disp_array(es5, headers=["N"])       
        +-------------+
        |           N |
        |-------------|
        | -4.0982e+04 |
        | -4.0982e+04 |
        | -4.0982e+04 |
        | -4.0982e+04 |
        | -4.0982e+04 |
        | -4.0982e+04 |
        | -4.0982e+04 |
        | -4.0982e+04 |
        | -4.0982e+04 |
        | -4.0982e+04 |
        | -4.0982e+04 |
        +-------------+         
