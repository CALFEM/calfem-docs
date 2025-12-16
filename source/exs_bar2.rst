exs_bar2
^^^^^^^^

.. index:: exs_bar2

:Purpose:

    Analysis of a plane truss.

:Description:

    Consider a plane truss consisting of three bars with the properties :math:`E=200` GPa, :math:`A_1=6.0 \times 10^{-4}` m², :math:`A_2=3.0 \times 10^{-4}` m² and :math:`A_3=10.0 \times 10^{-4}` m², and loaded by a single force :math:`P=80` kN. The corresponding finite element model consists of three elements and eight degrees of freedom.

    .. only:: html
        
        .. figure:: images/exs3.svg
            :align: center
            :width: 400px
    
    .. only:: latex
        
        .. figure:: images/exs3.svg
            :align: center
            :width: 70%

:Example:

    The computation is initialized by importing CALFEM and NumPy. The element topology matrix contains only the degrees of freedom for each element:

    .. code-block:: python

        >>> import numpy as np
        >>> import calfem.core as cfc

        >>> # Element topology matrix (DOFs only, no element numbers)  
        >>> Edof = np.array([
        ...     [1, 2, 5, 6],  # Element 1: DOFs 1,2,5,6
        ...     [5, 6, 7, 8],  # Element 2: DOFs 5,6,7,8
        ...     [3, 4, 5, 6]   # Element 3: DOFs 3,4,5,6
        ... ])

    The global stiffness matrix :code:`K` and the load vector :code:`f` are initialized. The load of 80 kN is applied in the negative y-direction at DOF 6:

    .. code-block:: python

        >>> # Initialize global system
        >>> K = np.zeros((8, 8))
        >>> f = np.zeros((8, 1))
        >>> f[5] = -80e3  # Load at DOF 6 (index 5 in 0-based indexing)
        >>> print("Load vector:")
        >>> print(f)
        [[     0.]
         [     0.]
         [     0.]
         [     0.]
         [     0.]
         [-80000.]
         [     0.]
         [     0.]]

    The material and geometric properties are defined for each element:

    .. code-block:: python

        >>> # Material and geometric properties
        >>> E = 2.0e11  # Young's modulus [Pa]
        >>> A1 = 6.0e-4   # Cross-sectional area element 1 [m²]
        >>> A2 = 3.0e-4   # Cross-sectional area element 2 [m²]  
        >>> A3 = 10.0e-4  # Cross-sectional area element 3 [m²]
        >>> 
        >>> ep1 = [E, A1]  # Element properties for element 1
        >>> ep2 = [E, A2]  # Element properties for element 2
        >>> ep3 = [E, A3]  # Element properties for element 3

    The element coordinates are defined for each element (x and y coordinates of start and end nodes):

    .. code-block:: python

        >>> # Element coordinates [m]
        >>> ex1 = np.array([0, 1.6])    # Element 1 x-coordinates
        >>> ey1 = np.array([0, 0])      # Element 1 y-coordinates
        >>> 
        >>> ex2 = np.array([1.6, 1.6])  # Element 2 x-coordinates  
        >>> ey2 = np.array([0, 1.2])    # Element 2 y-coordinates
        >>> 
        >>> ex3 = np.array([0, 1.6])    # Element 3 x-coordinates
        >>> ey3 = np.array([1.2, 0])    # Element 3 y-coordinates

    The element stiffness matrices :code:`Ke1`, :code:`Ke2` and :code:`Ke3` are computed using :code:`bar2e`:

    .. code-block:: python




    The element stiffness matrices are computed and assembled into the global stiffness matrix:

    .. code-block:: python

        >>> # Compute element stiffness matrices 
        >>> Ke1 = cfc.bar2e(ex1, ey1, ep1)
        >>> print(Ke1)
        [[ 75000000.         0. -75000000.         0.]
         [        0.         0.         0.         0.]
         [-75000000.         0.  75000000.         0.]
         [        0.         0.         0.         0.]]
        >>> Ke2 = cfc.bar2e(ex2, ey2, ep2)  
        >>> print(Ke2)
        [[        0.         0.         0.         0.]
         [        0.  50000000.         0. -50000000.]
         [        0.         0.         0.         0.]
         [        0. -50000000.         0.  50000000.]]
        >>> Ke3 = cfc.bar2e(ex3, ey3, ep3)
        >>> print(Ke3)        
        [[ 64000000. -48000000. -64000000.  48000000.]
         [-48000000.  36000000.  48000000. -36000000.]
         [-64000000.  48000000.  64000000. -48000000.]
         [ 48000000. -36000000. -48000000.  36000000.]]        
        >>> # Assemble global stiffness matrix
        >>> K = cfc.assem(Edof[0], K, Ke1)
        >>> K = cfc.assem(Edof[1], K, Ke2)
        >>> K = cfc.assem(Edof[2], K, Ke3)        
        >>> print("Global stiffness matrix K:")
        >>> print(K)
        [[ 7.50e+07  0.00e+00  0.00e+00  0.00e+00 -7.50e+07  0.00e+00  0.00e+00  0.00e+00]
         [ 0.00e+00  0.00e+00  0.00e+00  0.00e+00  0.00e+00  0.00e+00  0.00e+00  0.00e+00]
         [ 0.00e+00  0.00e+00  6.40e+07 -4.80e+07 -6.40e+07  4.80e+07  0.00e+00  0.00e+00]
         [ 0.00e+00  0.00e+00 -4.80e+07  3.60e+07  4.80e+07 -3.60e+07  0.00e+00  0.00e+00]
         [-7.50e+07  0.00e+00 -6.40e+07  4.80e+07  1.39e+08 -4.80e+07  0.00e+00  0.00e+00]
         [ 0.00e+00  0.00e+00  4.80e+07 -3.60e+07 -4.80e+07  8.60e+07  0.00e+00 -5.00e+07]
         [ 0.00e+00  0.00e+00  0.00e+00  0.00e+00  0.00e+00  0.00e+00  0.00e+00  0.00e+00]
         [ 0.00e+00  0.00e+00  0.00e+00  0.00e+00  0.00e+00 -5.00e+07  0.00e+00  5.00e+07]]

    The system of equations :math:`\boldsymbol{Ka}=\boldsymbol{f}` is solved by specifying the boundary conditions and using :func:`solveq`:

    .. code-block:: python

        >>> # Boundary conditions (DOF, prescribed value)
        >>> bc_dof = np.array([1, 2, 3, 4, 5, 6, 7, 8])
        >>> bc_value = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
        >>> 
        >>> # Solve the system
        >>> a, r = cfc.solveq(K, f, bc_dof, bc_value)
        >>> print("Displacements [m]:")
        >>> print(a)
        [[ 0.    ]
         [ 0.    ]
         [ 0.    ]
         [ 0.    ]
         [-0.0004]
         [-0.0012]
         [ 0.    ]
         [ 0.    ]]
        >>> print("Reaction forces [N]:")
        >>> print(r)
        [[ 29844.5596]
         [     0.    ]
         [-29844.5596]
         [ 22383.4197]
         [     0.    ]
         [     0.    ]
         [     0.    ]
         [ 57616.5803]]

    The vertical displacement at the point of loading is 1.15 mm. The element forces are calculated by extracting element displacements and computing stresses:

    .. code-block:: python

        >>> # Extract element displacements and compute forces
        >>> ed1 = cfc.extract_ed(Edof[0], a)
        >>> es1 = cfc.bar2s(ex1, ey1, ep1, ed1)
        >>> print(f"Element 1 forces [N]: {es1[0]}")
        Element 1 forces [N]: [-29844.5596]
        >>> 
        >>> ed2 = cfc.extract_ed(Edof[1], a) 
        >>> es2 = cfc.bar2s(ex2, ey2, ep2, ed2)
        >>> print(f"Element 2 forces [N]: {es2[0]}")
        Element 2 forces [N]: [57616.5803]
        >>> 
        >>> ed3 = cfc.extract_ed(Edof[2], a)
        >>> es3 = cfc.bar2s(ex3, ey3, ep3, ed3)  
        >>> print(f"Element 3 forces [N]: {es3[0]}")
        Element 3 forces [N]: [37305.6995]

    The normal forces are :math:`N_1=-29.84` kN (compression), :math:`N_2=57.62` kN (tension) and :math:`N_3=37.31` kN (tension).

    Visualization of the results can be performed using CALFEM's visualization functions:

    .. code-block:: python

        >>> import calfem.vis_mpl as cfv
        >>> import matplotlib.pyplot as plt
        >>> 
        >>> # Create displacement diagram
        >>> cfv.figure(1)
        >>> 
        >>> # Draw undeformed structure
        >>> plotpar = [2, 1, 0]  # Line style, marker, color
        >>> cfv.eldraw2(ex1, ey1, plotpar)
        >>> cfv.eldraw2(ex2, ey2, plotpar)
        >>> cfv.eldraw2(ex3, ey3, plotpar)
        >>> 
        >>> # Calculate scale factor and draw deformed structure
        >>> sfac = cfv.scalfact2(ex1, ey1, ed1, 0.1)
        >>> plotpar = [1, 2, 1]  # Line style, marker, color for deformed shape
        >>> cfv.eldisp2(ex1, ey1, ed1, plotpar, sfac)
        >>> cfv.eldisp2(ex2, ey2, ed2, plotpar, sfac)
        >>> cfv.eldisp2(ex3, ey3, ed3, plotpar, sfac)
        >>> 
        >>> plt.axis([-0.4, 2.0, -0.4, 1.4])
        >>> cfv.scalgraph2(sfac, [1e-3, 0, -0.3])
        >>> plt.title('Displacements')
        >>> plt.show()
        >>> 
        >>> # Create normal force diagram  
        >>> cfv.figure(2)
        >>> plotpar = [2, 1]  # Line style, marker
        >>> sfac = cfv.scalfact2(ex1, ey1, es2[:, 0], 0.1)
        >>> cfv.secforce2(ex1, ey1, es1[:, 0], plotpar, sfac)
        >>> cfv.secforce2(ex2, ey2, es2[:, 0], plotpar, sfac)
        >>> cfv.secforce2(ex3, ey3, es3[:, 0], plotpar, sfac)
        >>> 
        >>> plt.axis([-0.4, 2.0, -0.4, 1.4])
        >>> cfv.scalgraph2(sfac, [5e4, 0, -0.3])
        >>> plt.title('Normal force')
        >>> plt.show()

    .. only:: html
        
        .. figure:: images/exs3_1.svg
            :align: center
            :width: 400px
    
    .. only:: latex
        
        .. figure:: images/exs3_1.svg
            :align: center
            :width: 70%
        
        Displacement diagram

    .. only:: html
        
        .. figure:: images/exs3_2.svg
            :align: center
            :width: 400px
    
    .. only:: latex
        
        .. figure:: images/exs3_2.svg
            :align: center
            :width: 70%
        
        Normal force diagram
