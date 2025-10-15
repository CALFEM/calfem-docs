exs_beam1
^^^^^^^^^

.. index:: exs_beam1

:Purpose:

    Analysis of a simply supported beam.

:Description:

    Consider a beam with the length :math:`9.0` m. The beam is simply supported and loaded by a point load :math:`P=10000` N applied at a point :math:`3.0` m from the left support. The corresponding computational model has six degrees of freedom and consists of two beam elements with four degrees of freedom. The beam has Young's modulus :math:`E=210` GPa and moment of inertia :math:`I=2510 \times 10^{-8}` m⁴.

    .. figure:: images/exs5_1.png
        :align: center

    .. figure:: images/exs5_2.png
        :align: center

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
        >>> f = np.zeros(6)
        >>> f[2] = -10000  # Load at DOF 3 (index 2 in 0-based indexing)
        >>> print("Load vector:")
        >>> print(f)
        [     0.      0. -10000.      0.      0.      0.]

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
        [[ 2.3427e+06  3.5140e+06 -2.3427e+06  3.5140e+06]
         [ 3.5140e+06  7.0280e+06 -3.5140e+06  3.5140e+06]
         [-2.3427e+06 -3.5140e+06  2.3427e+06 -3.5140e+06]
         [ 3.5140e+06  3.5140e+06 -3.5140e+06  7.0280e+06]]
        >>> 
        >>> Ke2 = cfc.beam1e(ex2, ep)
        >>> print("Element 2 stiffness matrix:")
        >>> print(Ke2)
        [[ 2.9279e+05  8.7836e+05 -2.9279e+05  8.7836e+05]
         [ 8.7836e+05  3.5135e+06 -8.7836e+05  1.7567e+06]
         [-2.9279e+05 -8.7836e+05  2.9279e+05 -8.7836e+05]
         [ 8.7836e+05  1.7567e+06 -8.7836e+05  3.5135e+06]]

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
        >>> bc = np.array([
        ...     [1, 0],  # DOF 1 = 0 (vertical displacement at left support)
        ...     [5, 0]   # DOF 5 = 0 (vertical displacement at right support)
        ... ])
        >>> 
        >>> # Solve the system
        >>> a, r = cfc.solveq(K, f, bc)
        >>> print("Displacements:")
        >>> print(a)
        [ 0.0000e+00 -9.5000e-03 -2.2800e-02 -3.8000e-03  0.0000e+00  7.6000e-03]
        >>> print("Reaction forces [N]:")
        >>> print(r)
        [ 6667.   0.   0.   0.   3333.   0.]

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
        >>> print("Element 2 section forces [N, Nm]:")
        >>> print(es2[:5])  # Show first 5 points

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

    .. figure:: images/exs5_3.png
        :align: center
        
        Displacement diagram

    .. figure:: images/exs5_4.png
        :align: center
        
        Shear force diagram

    .. figure:: images/exs5_5.png
        :align: center
        
        Moment diagram
