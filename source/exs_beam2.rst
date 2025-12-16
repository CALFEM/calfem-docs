exs_beam2
^^^^^^^^^

.. index:: exs_beam2

:Purpose:

    Analysis of a plane frame.

:Description:

    A frame consists of one horizontal and two vertical beams according to the figure.

    .. only:: html
        
        .. figure:: images/exs6_1.svg
            :align: center
            :width: 400px
    
    .. only:: latex
        
        .. figure:: images/exs6_1.svg
            :align: center
            :width: 70%

    **Material and geometric properties:**

    .. list-table::
       :widths: 20 10 30
       :header-rows: 0

       * - :math:`E`
         - :math:`=`
         - :math:`200` GPa
       * - :math:`A_1`
         - :math:`=`
         - :math:`2.0 \times 10^{-3}` m²
       * - :math:`I_1`
         - :math:`=`
         - :math:`1.6 \times 10^{-5}` m⁴
       * - :math:`A_2`
         - :math:`=`
         - :math:`6.0 \times 10^{-3}` m²
       * - :math:`I_2`
         - :math:`=`
         - :math:`5.4 \times 10^{-5}` m⁴
       * - :math:`P`
         - :math:`=`
         - :math:`2.0` kN
       * - :math:`q_0`
         - :math:`=`
         - :math:`10.0` kN/m

    The corresponding finite element model consists of three beam elements and twelve degrees of freedom.

    .. only:: html
        
        .. figure:: images/exs6_2.svg
            :align: center
            :width: 400px
    
    .. only:: latex
        
        .. figure:: images/exs6_2.svg
            :align: center
            :width: 70%

:Example:

    The computation is initialized by importing CALFEM and NumPy. The element topology matrix contains only the degrees of freedom for each element:

    .. code-block:: python

        >>> import numpy as np
        >>> import calfem.core as cfc
        >>> 
        >>> # Element topology matrix (DOFs only, no element numbers)
        >>> Edof = np.array([
        ...     [4, 5, 6, 1, 2, 3],    # Element 1: left column (node 2-1)
        ...     [7, 8, 9, 10, 11, 12], # Element 2: right column (node 3-4)
        ...     [4, 5, 6, 7, 8, 9]     # Element 3: horizontal beam (node 2-3)
        ... ])

    The global stiffness matrix :code:`K` and load vector :code:`f` are initialized. The point load P = 2000 N is applied at DOF 4:

    .. code-block:: python

        >>> # Initialize global system
        >>> K = np.zeros((12, 12))
        >>> f = np.zeros((12, 1))
        >>> f[3] = 2e3  # Load at DOF 4 (index 3 in 0-based indexing)
        >>> print("Load vector:")
        >>> print(f)
        [[   0.]
         [   0.]
         [   0.]
         [2000.]
         [   0.]
         [   0.]
         [   0.]
         [   0.]
         [   0.]
         [   0.]
         [   0.]
         [   0.]]

    The material and geometric properties are defined for each element type:

    .. code-block:: python

        >>> # Material and geometric properties
        >>> E = 200e9        # Young's modulus [Pa]
        >>> A1 = 2e-3       # Cross-sectional area for columns [m²]
        >>> A2 = 6e-3       # Cross-sectional area for beam [m²]
        >>> I1 = 1.6e-5     # Moment of inertia for columns [m⁴]
        >>> I2 = 5.4e-5     # Moment of inertia for beam [m⁴]
        >>> 
        >>> ep1 = [E, A1, I1]  # Element properties for columns
        >>> ep2 = [E, A2, I2]  # Element properties for horizontal beam
        >>> 
        >>> # Element coordinates [m]
        >>> ex1 = np.array([0, 0])  # Element 1: left column x-coordinates
        >>> ex2 = np.array([6, 6])  # Element 2: right column x-coordinates  
        >>> ex3 = np.array([0, 6])  # Element 3: horizontal beam x-coordinates
        >>> ey1 = np.array([4, 0])  # Element 1: left column y-coordinates
        >>> ey2 = np.array([4, 0])  # Element 2: right column y-coordinates
        >>> ey3 = np.array([4, 4])  # Element 3: horizontal beam y-coordinates
        >>> 
        >>> # Distributed loads (only on horizontal beam)
        >>> eq1 = np.array([0, 0])      # No distributed load on left column
        >>> eq2 = np.array([0, 0])      # No distributed load on right column  
        >>> eq3 = np.array([0, -10e3])  # 10 kN/m downward on horizontal beam

    The element stiffness matrices and load vectors are computed and assembled:

    .. code-block:: python

        >>> # Compute element stiffness matrices
        >>> Ke1 = cfc.beam2e(ex1, ey1, ep1)
        >>> Ke2 = cfc.beam2e(ex2, ey2, ep1)  # Same properties as element 1
        >>> Ke3, fe3 = cfc.beam2e(ex3, ey3, ep2, eq3)  # With distributed load
        >>> 
        >>> # Assemble global stiffness matrix and load vector
        >>> K = cfc.assem(edof[0, :], K, Ke1)
        >>> K = cfc.assem(edof[1, :], K, Ke2)
        >>> K, f = cfc.assem(edof[2, :], K, Ke3, f, fe3)
        >>> 
        >>> print("Global system assembled successfully")
        Global system assembled successfully

    The system of equations is solved by specifying boundary conditions and using :func:`solveq`:

    .. code-block:: python

        >>> # Boundary conditions (fixed supports at base of columns)
        >>> bc_dof = np.array([1, 2, 3, 10, 11])
        >>> bc_value = np.array([0.0, 0.0, 0.0, 0.0, 0.0])
        >>> 
        >>> # Solve the system
        >>> a, r = cfc.solveq(K, f, bc)
        >>> print("Displacements [m, rad]:")
        >>> print(a)
        [[ 0.    ]
         [ 0.    ]
         [ 0.    ]
         [ 0.0075]
         [-0.0003]
         [-0.0054]
         [ 0.0075]
         [-0.0003]
         [ 0.0047]
         [ 0.    ]
         [ 0.    ]
         [-0.0052]]
        >>> print("Reaction forces [N, Nm]:")
        >>> print(r)
        [[ 1.9268e+03]
         [ 2.8741e+04]
         [ 0.0000e+00]
         [-7.2760e-12]
         [-3.9268e+03]
         [ 3.1259e+04]
         [ 0.0000e+00]]

    The element displacements are extracted and section forces are computed along each element:

    .. code-block:: python

        >>> # Extract element displacements
        >>> Ed = cfc.extract_ed(Edof, a)
        >>> 
        >>> # Compute section forces and internal displacements (21 points each)
        >>> es1, edi1, ec1 = cfc.beam2s(ex1, ey1, ep1, ed[0, :], eq1, nep=21)
        >>> es2, edi2, ec2 = cfc.beam2s(ex2, ey2, ep1, ed[1, :], eq2, nep=21)
        >>> es3, edi3, ec3 = cfc.beam2s(ex3, ey3, ep2, ed[2, :], eq3, nep=21)
        >>> 
        >>> print("Element 1 (left column) section forces [N, N, Nm]:")
        >>> print("N =", es1[0, 0], "V =", es1[0, 1], "M =", es1[0, 2])
        Element 1 (left column) section forces [N, N, Nm]:
        N = -28740.878321063385 V = 1926.7601159371466 M = 8152.31039012879
        >>> 
        >>> print("Element 2 (right column) section forces [N, N, Nm]:")
        >>> print("N =", es2[0, 0], "V =", es2[0, 1], "M =", es2[0, 2])
        Element 2 (right column) section forces [N, N, Nm]:
        N = -31259.121678936615 V = -3926.760115937116 M = -15707.040463748464
        >>> 
        >>> print("Element 3 (horizontal beam) section forces [N, N, Nm]:")
        >>> print("N =", es3[0, 0], "V =", es3[0, 1], "M =", es3[0, 2])
        Element 3 (horizontal beam) section forces [N, N, Nm]:
        N = -3926.760115937226 V = -28740.87832106339 M = -8152.310390128787

    Visualization of the frame analysis results using CALFEM's visualization functions:

    .. code-block:: python

        >>> import calfem.vis_mpl as cfv
        >>> import matplotlib.pyplot as plt
        >>> 
        >>> # Displacement diagram
        >>> cfv.figure(1, figsize=(10, 8))
        >>> 
        >>> # Draw undeformed structure
        >>> plotpar = [2, 1, 0]  # Line style, marker, color
        >>> cfv.eldraw2(ex1, ey1, plotpar)
        >>> cfv.eldraw2(ex2, ey2, plotpar)  
        >>> cfv.eldraw2(ex3, ey3, plotpar)
        >>> 
        >>> # Calculate scale factor and draw deformed structure
        >>> sfac = cfv.scalfact2(ex3, ey3, Ed[2], 0.1)
        >>> plotpar = [1, 2, 1]  # Line style, marker, color for deformed shape
        >>> cfv.dispbeam2(ex1, ey1, edi1, plotpar, sfac)
        >>> cfv.dispbeam2(ex2, ey2, edi2, plotpar, sfac)
        >>> cfv.dispbeam2(ex3, ey3, edi3, plotpar, sfac)
        >>> 
        >>> plt.axis([-1.5, 7.5, -0.5, 5.5])
        >>> cfv.scalgraph2(sfac, [1e-2, 0.5, 0])
        >>> plt.title('Displacements')
        >>> plt.xlabel('x [m]')
        >>> plt.ylabel('y [m]')
        >>> plt.grid(True, alpha=0.3)
        >>> plt.show()
        >>> 
        >>> # Normal force diagram
        >>> cfv.figure(2, figsize=(10, 8))
        >>> plotpar = [2, 1]  # Line style, marker
        >>> sfac = cfv.scalfact2(ex1, ey1, es1[:, 0], 0.2)
        >>> cfv.secforce2(ex1, ey1, es1[:, 0], plotpar, sfac)
        >>> cfv.secforce2(ex2, ey2, es2[:, 0], plotpar, sfac)
        >>> cfv.secforce2(ex3, ey3, es3[:, 0], plotpar, sfac)
        >>> 
        >>> plt.axis([-1.5, 7.5, -0.5, 5.5])
        >>> cfv.scalgraph2(sfac, [3e4, 1.5, 0])
        >>> plt.title('Normal Force')
        >>> plt.xlabel('x [m]')
        >>> plt.ylabel('y [m]')
        >>> plt.grid(True, alpha=0.3)
        >>> plt.show()
        >>> 
        >>> # Shear force diagram
        >>> cfv.figure(3, figsize=(10, 8))
        >>> plotpar = [2, 1]
        >>> sfac = cfv.scalfact2(ex3, ey3, es3[:, 1], 0.2)
        >>> cfv.secforce2(ex1, ey1, es1[:, 1], plotpar, sfac)
        >>> cfv.secforce2(ex2, ey2, es2[:, 1], plotpar, sfac)
        >>> cfv.secforce2(ex3, ey3, es3[:, 1], plotpar, sfac)
        >>> 
        >>> plt.axis([-1.5, 7.5, -0.5, 5.5])
        >>> cfv.scalgraph2(sfac, [3e4, 0.5, 0])
        >>> plt.title('Shear Force')
        >>> plt.xlabel('x [m]')
        >>> plt.ylabel('y [m]')
        >>> plt.grid(True, alpha=0.3)
        >>> plt.show()
        >>> 
        >>> # Moment diagram
        >>> cfv.figure(4, figsize=(10, 8))
        >>> plotpar = [2, 1]
        >>> sfac = cfv.scalfact2(ex3, ey3, es3[:, 2], 0.2)
        >>> cfv.secforce2(ex1, ey1, es1[:, 2], plotpar, sfac)
        >>> cfv.secforce2(ex2, ey2, es2[:, 2], plotpar, sfac)
        >>> cfv.secforce2(ex3, ey3, es3[:, 2], plotpar, sfac)
        >>> 
        >>> plt.axis([-1.5, 7.5, -0.5, 5.5])
        >>> cfv.scalgraph2(sfac, [3e4, 0.5, 0])
        >>> plt.title('Bending Moment')
        >>> plt.xlabel('x [m]')
        >>> plt.ylabel('y [m]')
        >>> plt.grid(True, alpha=0.3)
        >>> plt.show()

    .. only:: html
        
        .. figure:: images/exs6_3.svg
            :align: center
            :width: 400px
    
    .. only:: latex
        
        .. figure:: images/exs6_3.svg
            :align: center
            :width: 70%
        
        Displacement diagram

    .. only:: html
        
        .. figure:: images/exs6_4.svg
            :align: center
            :width: 400px
    
    .. only:: latex
        
        .. figure:: images/exs6_4.svg
            :align: center
            :width: 70%
        
        Normal force diagram

    .. only:: html
        
        .. figure:: images/exs6_5.svg
            :align: center
            :width: 400px
    
    .. only:: latex
        
        .. figure:: images/exs6_5.svg
            :align: center
            :width: 70%
        
        Shear force diagram

    .. only:: html
        
        .. figure:: images/exs6_6.svg
            :align: center
            :width: 400px
    
    .. only:: latex
        
        .. figure:: images/exs6_6.svg
            :align: center
            :width: 70%
        
        Moment diagram
