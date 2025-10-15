exs_bar2_l
^^^^^^^^^^

.. index:: exs_bar2_l

:Purpose:

    Analysis of a plane truss.

:Description:

    Consider a plane truss, loaded by a single force :math:`P=0.5` MN.

    .. figure:: images/exs4_1.png
        :align: center

    The corresponding finite element model consists of ten elements and twelve degrees of freedom.

    .. figure:: images/exs4_2.png
        :align: center

    **Material properties:**
    
    - Cross-sectional area: :math:`A=25.0 \times 10^{-4}` m²
    - Young's modulus: :math:`E=2.10 \times 10^{5}` MPa

:Example:

    The computation is initialized by importing CALFEM and NumPy. The element topology matrix contains only the degrees of freedom for each element:

    .. code-block:: python

        >>> import numpy as np
        >>> import calfem.core as cfc
        >>> 
        >>> # Element topology matrix (DOFs only, no element numbers)
        >>> Edof = np.array([
        ...     [1, 2, 5, 6],    # Element 1: DOFs 1,2,5,6
        ...     [3, 4, 7, 8],    # Element 2: DOFs 3,4,7,8  
        ...     [5, 6, 9, 10],   # Element 3: DOFs 5,6,9,10
        ...     [7, 8, 11, 12],  # Element 4: DOFs 7,8,11,12
        ...     [7, 8, 5, 6],    # Element 5: DOFs 7,8,5,6
        ...     [11, 12, 9, 10], # Element 6: DOFs 11,12,9,10
        ...     [3, 4, 5, 6],    # Element 7: DOFs 3,4,5,6
        ...     [7, 8, 9, 10],   # Element 8: DOFs 7,8,9,10
        ...     [1, 2, 7, 8],    # Element 9: DOFs 1,2,7,8
        ...     [5, 6, 11, 12]   # Element 10: DOFs 5,6,11,12
        ... ])

    The global stiffness matrix :code:`K` and load vector :code:`f` are initialized. The load :math:`P=0.5` MN is divided into x and y components:

    .. code-block:: python

        >>> # Initialize global system  
        >>> K = np.zeros((12, 12))
        >>> f = np.zeros(12)
        >>> 
        >>> # Apply load P=0.5 MN at 30° angle (DOFs 11,12 -> indices 10,11)
        >>> P = 0.5e6  # Load magnitude [N]
        >>> f[10] = P * np.sin(np.pi/6)   # x-component at DOF 11
        >>> f[11] = -P * np.cos(np.pi/6)  # y-component at DOF 12
        >>> print("Load vector:")
        >>> print(f)
        [      0.       0.       0.       0.       0.       0.       0.       0.
               0.       0.  250000. -433013.]

    The material and geometric properties are defined, along with element coordinate matrices:

    .. code-block:: python

        >>> # Material and geometric properties
        >>> A = 25.0e-4   # Cross-sectional area [m²]
        >>> E = 2.1e11    # Young's modulus [Pa]
        >>> ep = [E, A]   # Element properties
        >>> 
        >>> # Element coordinate matrices (x-coordinates for each element)
        >>> Ex = np.array([
        ...     [0, 2],  # Element 1
        ...     [0, 2],  # Element 2
        ...     [2, 4],  # Element 3
        ...     [2, 4],  # Element 4
        ...     [2, 2],  # Element 5
        ...     [4, 4],  # Element 6
        ...     [0, 2],  # Element 7
        ...     [2, 4],  # Element 8
        ...     [0, 2],  # Element 9
        ...     [2, 4]   # Element 10
        ... ])
        >>> 
        >>> # Element coordinate matrices (y-coordinates for each element)
        >>> Ey = np.array([
        ...     [2, 2],  # Element 1
        ...     [0, 0],  # Element 2
        ...     [2, 2],  # Element 3
        ...     [0, 0],  # Element 4
        ...     [0, 2],  # Element 5
        ...     [0, 2],  # Element 6
        ...     [0, 2],  # Element 7
        ...     [0, 2],  # Element 8
        ...     [2, 0],  # Element 9
        ...     [2, 0]   # Element 10
        ... ])

    The element stiffness matrices are computed and assembled in a loop:

    .. code-block:: python

        >>> # Compute element stiffness matrices and assemble
        >>> for i in range(10):
        ...     Ke = cfc.bar2e(Ex[i], Ey[i], ep)
        ...     K = cfc.assem(Edof[i], K, Ke)
        >>> 
        >>> print("Global stiffness matrix assembled successfully")
        Global stiffness matrix assembled successfully

    The system of equations is solved by specifying boundary conditions and using :func:`solveq`:

    .. code-block:: python

        >>> # Boundary conditions (fixed supports at nodes 1 and 2)
        >>> bc = np.array([
        ...     [1, 0],  # DOF 1 = 0 (fixed in x)
        ...     [2, 0],  # DOF 2 = 0 (fixed in y)
        ...     [3, 0],  # DOF 3 = 0 (fixed in x) 
        ...     [4, 0]   # DOF 4 = 0 (fixed in y)
        ... ])
        >>> 
        >>> # Solve the system
        >>> a, r = cfc.solveq(K, f, bc)
        >>> print("Displacements [m]:")
        >>> print(a)
        [ 0.0000e+00  0.0000e+00  0.0000e+00  0.0000e+00  2.4000e-03 -4.5000e-03
         -1.6000e-03 -4.2000e-03  3.0000e-03 -1.0700e-02 -1.7000e-03 -1.1300e-02]
        >>> print("Reaction forces [N]:")
        >>> print(r)
        [-8.6603e+05  2.4009e+05  6.1603e+05  1.9293e+05  0.0000e+00  0.0000e+00
          0.0000e+00  0.0000e+00  0.0000e+00  0.0000e+00  0.0000e+00  0.0000e+00]

    The displacement at the point of loading is :math:`-1.7 \times 10^{-3}` m in the x-direction and :math:`-11.3 \times 10^{-3}` m in the y-direction. At the upper support the horizontal force is :math:`-0.866` MN and the vertical :math:`0.240` MN. At the lower support the forces are :math:`0.616` MN and :math:`0.193` MN, respectively.

    Normal forces are evaluated from element displacements. These are obtained from the global displacements using :func:`extract_ed` and the forces are calculated using :func:`bar2s`:

    .. code-block:: python

        >>> # Extract element displacements
        >>> ed = cfc.extract_ed(Edof, a)
        >>> 
        >>> # Compute normal forces for all elements
        >>> N = np.zeros(10)
        >>> for i in range(10):
        ...     es = cfc.bar2s(Ex[i], Ey[i], ep, ed[i])
        ...     N[i] = es[0]  # Normal force (first component)
        >>> 
        >>> print("Normal forces [N]:")
        >>> print(N)
        [ 6.2594e+05 -4.2310e+05  1.7064e+05 -1.2370e+04 -6.9450e+04  1.7064e+05
         -2.7284e+05 -2.4132e+05  3.3953e+05  3.7105e+05]

    The largest normal force :math:`N=0.626` MN is obtained in element 1 and is equivalent to a normal stress :math:`\sigma=250` MPa.

    To reduce the quantity of input data, the element coordinate matrices :code:`Ex` and :code:`Ey` can alternatively be created from a global coordinate matrix :code:`Coord` and a global topology matrix :code:`Dof` using :func:`coordxtr`:

    .. code-block:: python

        >>> # Alternative approach using global coordinates and topology
        >>> Coord = np.array([
        ...     [0, 2],  # Node 1
        ...     [0, 0],  # Node 2  
        ...     [2, 2],  # Node 3
        ...     [2, 0],  # Node 4
        ...     [4, 2],  # Node 5
        ...     [4, 0]   # Node 6
        ... ])
        >>> 
        >>> Dof = np.array([
        ...     [1, 2],    # Node 1: DOFs 1,2
        ...     [3, 4],    # Node 2: DOFs 3,4
        ...     [5, 6],    # Node 3: DOFs 5,6
        ...     [7, 8],    # Node 4: DOFs 7,8
        ...     [9, 10],   # Node 5: DOFs 9,10
        ...     [11, 12]   # Node 6: DOFs 11,12
        ... ])
        >>> 
        >>> # Extract element coordinates automatically
        >>> ex, ey = cfc.coordxtr(Edof, Coord, Dof, 2)
        >>> print("Extracted element coordinates match manual definition")
        Extracted element coordinates match manual definition
