exs_beam1
^^^^^^^^^

.. index:: exs_beam1

:Purpose:

    Analysis of a simply supported beam.

:Description:

    Consider a beam with the length :math:`9.0` m. The beam is simply supported and loaded by a point load :math:`P=10000` N applied at a point :math:`3.0` m from the left support. The corresponding computational model has six degrees of freedom and consists of two beam elements with four degrees of freedom. The beam has Young's modulus :math:`E=210` GPa and moment of inertia :math:`I=2510 \times 10^{-8}` m⁴.

    .. only:: html
        
        .. figure:: images/exs5_1.svg
            :align: center
            :width: 400px
    
    .. only:: latex
        
        .. figure:: images/exs5_1.svg
            :align: center
            :width: 70%

    .. only:: html
        
        .. figure:: images/exs5_2.svg
            :align: center
            :width: 400px
    
    .. only:: latex
        
        .. figure:: images/exs5_2.svg
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
        ...     [1, 2, 3, 4],  # Element 1: DOFs 1,2,3,4 (node 1-2)
        ...     [3, 4, 5, 6]   # Element 2: DOFs 3,4,5,6 (node 2-3)
        ... ])

    The global stiffness matrix :code:`K` and load vector :code:`f` are initialized. The point load P = 10000 N is applied at DOF 3:

    .. code-block:: python

        >>> # Initialize global system
        >>> K = np.zeros((6, 6))
        >>> f = np.zeros((6, 1))
        >>> f[2] = -10000  # Load at DOF 3 (index 2 in 0-based indexing)
        >>> print("Load vector:")
        >>> print(f)
        [[     0.]
         [     0.]
         [-10000.]
         [     0.]
         [     0.]
         [     0.]]

    The material and geometric properties are defined, along with element coordinates and stiffness matrices:

    .. code-block:: python

        >>> # Material and geometric properties
        >>> E = 210e9      # Young's modulus [Pa]
        >>> I = 2510e-8    # Moment of inertia [m⁴]
        >>> ep = [E, I]    # Element properties
        >>> 
        >>> # Element coordinates [m]
        >>> ex1 = np.array([0, 3])  # Element 1: from x=0 to x=3
        >>> ex2 = np.array([3, 9])  # Element 2: from x=3 to x=9
        >>> 
        >>> # Compute element stiffness matrices
        >>> Ke1 = cfc.beam1e(ex1, ep)
        >>> print("Element 1 stiffness matrix:")
        >>> print(Ke1)
        [[ 2342666.6667  3514000.     -2342666.6667  3514000.    ]
         [ 3514000.      7028000.     -3514000.      3514000.    ]
         [-2342666.6667 -3514000.      2342666.6667 -3514000.    ]
         [ 3514000.      3514000.     -3514000.      7028000.    ]]
        >>> 
        >>> Ke2 = cfc.beam1e(ex2, ep)
        >>> print("Element 2 stiffness matrix:")
        >>> print(Ke2)
        [[ 292833.3333  878500.     -292833.3333  878500.    ]
         [ 878500.     3514000.     -878500.     1757000.    ]
         [-292833.3333 -878500.      292833.3333 -878500.    ]
         [ 878500.     1757000.     -878500.     3514000.    ]]

    The element stiffness matrices are assembled into the global stiffness matrix:

    .. code-block:: python

        >>> # Assemble global stiffness matrix
        >>> K = cfc.assem(Edof[0], K, Ke1)
        >>> K = cfc.assem(Edof[1], K, Ke2)
        >>> print("Global stiffness matrix assembled successfully")
        Global stiffness matrix assembled successfully

    The system of equations is solved by defining boundary conditions and using :func:`solveq`:

    .. code-block:: python

        >>> # Boundary conditions (simply supported beam)
        >>> bc_dof = np.array([1, 5])
        >>> bc_value = np.array([0.0, 0.0])
        >>> 
        >>> # Solve the system
        >>> a, r = cfc.solveq(K, f, bc)
        >>> print("Displacements:")
        >>> print(a)
        [[ 0.    ]
         [-0.0095]
         [-0.0228]
         [-0.0038]
         [ 0.    ]
         [ 0.0076]]
        >>> print("Reaction forces [N]:")
        >>> print(r)
        [[ 6.6667e+03]
         [ 0.0000e+00]
         [ 9.0949e-12]
         [-1.0914e-11]
         [ 3.3333e+03]
         [ 0.0000e+00]]

    The section forces and element displacements are calculated from global displacements:

    .. code-block:: python

        >>> # Extract element displacements
        >>> Ed = cfc.extract_ed(Edof, a)
        >>> 
        >>> # Compute section forces and internal displacements
        >>> # For beam1s, we don't need eq parameter for point loads
        >>> es1, edi1 = cfc.beam1s(ex1, ep, Ed[0], n_points=6)
        >>> es2, edi2 = cfc.beam1s(ex2, ep, Ed[1], n_points=11)
        >>> 
        >>> print("Element 1 section forces [N, Nm]:")
        >>> print(es1[:5])  # Show first 5 points
        [[-6.6667e+03  9.1437e-12]
         [-6.6667e+03  4.0000e+03]
         [-6.6667e+03  8.0000e+03]
         [-6.6667e+03  1.2000e+04]
         [-6.6667e+03  1.6000e+04]]        
        >>> print("Element 2 section forces [N, Nm]:")
        >>> print(es2[:5])  # Show first 5 points
        [[ 3333.3333 20000.    ]
         [ 3333.3333 18000.    ]
         [ 3333.3333 16000.    ]
         [ 3333.3333 14000.    ]
         [ 3333.3333 12000.    ]]        

    **Results:**

    The solution shows the expected behavior for a simply supported beam with a point load:

    - **Maximum deflection**: 22.8 mm at the loading point (DOF 3)
    - **Support reactions**: 6667 N at left support, 3333 N at right support  
    - **Maximum shear force**: 6667 N (in element 1)
    - **Maximum moment**: 20000 Nm (at the loading point)

    Visualization of the results using matplotlib:

    .. code-block:: python

        >>> import matplotlib.pyplot as plt
        >>> 
        >>> # Create position vectors for plotting
        >>> x1 = np.linspace(0, 3, len(edi1))
        >>> x2 = np.linspace(3, 9, len(edi2))
        >>> x_full = np.concatenate(([0], x1, x2, [9]))
        >>> 
        >>> # Displacement diagram
        >>> plt.figure(1, figsize=(10, 4))
        >>> plt.plot([0, 9], [0, 0], 'k-', linewidth=1, alpha=0.5)  # Reference line
        >>> disp_full = np.concatenate(([0], edi1[:, 0], edi2[:, 0], [0]))
        >>> plt.plot(x_full, disp_full, 'b-', linewidth=2, label='Displacement')
        >>> plt.xlabel('Position [m]')
        >>> plt.ylabel('Displacement [m]')
        >>> plt.title('Displacement Diagram')
        >>> plt.grid(True, alpha=0.3)
        >>> plt.axis([-1, 10, -0.03, 0.01])
        >>> plt.legend()
        >>> plt.show()
        >>> 
        >>> # Shear force diagram
        >>> plt.figure(2, figsize=(10, 4))
        >>> plt.plot([0, 9], [0, 0], 'k-', linewidth=1, alpha=0.5)  # Reference line
        >>> shear_full = np.concatenate(([0], es1[:, 0], es2[:, 0], [0]))
        >>> plt.plot(x_full, shear_full, 'r-', linewidth=2, label='Shear Force')
        >>> plt.xlabel('Position [m]')
        >>> plt.ylabel('Shear Force [N]')
        >>> plt.title('Shear Force Diagram')
        >>> plt.grid(True, alpha=0.3)
        >>> plt.axis([-1, 10, -8000, 5000])
        >>> plt.gca().invert_yaxis()  # Engineering convention
        >>> plt.legend()
        >>> plt.show()
        >>> 
        >>> # Moment diagram
        >>> plt.figure(3, figsize=(10, 4))
        >>> plt.plot([0, 9], [0, 0], 'k-', linewidth=1, alpha=0.5)  # Reference line
        >>> moment_full = np.concatenate(([0], es1[:, 1], es2[:, 1], [0]))
        >>> plt.plot(x_full, moment_full, 'g-', linewidth=2, label='Bending Moment')
        >>> plt.xlabel('Position [m]')
        >>> plt.ylabel('Bending Moment [Nm]')
        >>> plt.title('Bending Moment Diagram')
        >>> plt.grid(True, alpha=0.3)
        >>> plt.axis([-1, 10, -5000, 25000])
        >>> plt.gca().invert_yaxis()  # Engineering convention
        >>> plt.legend()
        >>> plt.show()

    .. only:: html
        
        .. figure:: images/exs5_3.svg
            :align: center
            :width: 400px
    
    .. only:: latex
        
        .. figure:: images/exs5_3.svg
            :align: center
            :width: 70%
        
        Displacement diagram

    .. only:: html
        
        .. figure:: images/exs5_4.svg
            :align: center
            :width: 400px
    
    .. only:: latex
        
        .. figure:: images/exs5_4.svg
            :align: center
            :width: 70%
        
        Shear force diagram

    .. only:: html
        
        .. figure:: images/exs5_5.svg
            :align: center
            :width: 400px
    
    .. only:: latex
        
        .. figure:: images/exs5_5.svg
            :align: center
            :width: 70%
        
        Moment diagram
