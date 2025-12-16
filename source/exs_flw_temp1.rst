exs_flw_temp1
^^^^^^^^^^^^^

.. index:: exs_flw_temp1

:Purpose:

    Analysis of one-dimensional heat flow.

:Description:

    Consider a wall built up of concrete and thermal insulation. The outdoor temperature is :math:`-17°\text{C}` and the temperature inside is :math:`20°\text{C}`. At the inside of the thermal insulation there is a heat source yielding :math:`10` W/m².

    .. only:: html
        
        .. figure:: images/exs2_1.svg
            :align: center
            :width: 400px
    
    .. only:: latex
        
        .. figure:: images/exs2_1.svg
            :align: center
            :width: 70%

    .. only:: html
        
        .. figure:: images/exs2_2.svg
            :align: center
            :width: 400px
    
    .. only:: latex
        
        .. figure:: images/exs2_2.svg
            :align: center
            :width: 70%

    The wall is subdivided into five elements and the one-dimensional spring (analogy) element :code:`spring1e` is used. Equivalent spring stiffnesses are :math:`k_i=\lambda A/L` for thermal conductivity and :math:`k_i=A/R` for thermal surface resistance. Corresponding spring stiffnesses per m² of the wall are:

    .. list-table::
       :widths: 20 30 10 20 20
       :header-rows: 0

       * - :math:`k_1 =`
         - :math:`1/0.04`
         - :math:`=`
         - :math:`25.0`
         - W/K
       * - :math:`k_2 =`
         - :math:`1.7/0.070`
         - :math:`=`
         - :math:`24.3`
         - W/K
       * - :math:`k_3 =`
         - :math:`0.040/0.100`
         - :math:`=`
         - :math:`0.4`
         - W/K
       * - :math:`k_4 =`
         - :math:`1.7/0.100`
         - :math:`=`
         - :math:`17.0`
         - W/K
       * - :math:`k_5 =`
         - :math:`1/0.13`
         - :math:`=`
         - :math:`7.7`
         - W/K

:Example:

    The computation is initialized by importing CALFEM and NumPy. A global system matrix :code:`K` and a heat flow vector :code:`f` are defined. The heat source inside the wall is considered by setting :math:`f_4=10`. The element matrices :code:`Ke` are computed using :code:`cfc.spring1e`, and the function :code:`cfc.assem` assembles the global stiffness matrix.

    .. code-block:: python

        >>> import numpy as np
        >>> import calfem.core as cfc

        >>> # Element topology matrix (DOFs only, no element numbers)
        >>> Edof = np.array([
        ...     [1, 2],  # Element 1: DOF 1 to DOF 2
        ...     [2, 3],  # Element 2: DOF 2 to DOF 3
        ...     [3, 4],  # Element 3: DOF 3 to DOF 4
        ...     [4, 5],  # Element 4: DOF 4 to DOF 5
        ...     [5, 6]   # Element 5: DOF 5 to DOF 6
        ... ])

        >>> # Initialize global stiffness matrix and load vector
        >>> K = np.zeros((6, 6))
        >>> f = np.zeros((6, 1))
        >>> f[3] = 10  # Heat source at DOF 4 (index 3 in 0-based indexing)
        >>> print("Load vector f:")
        >>> print(f)
        [[ 0.]
         [ 0.]
         [ 0.]
         [10.]
         [ 0.]
         [ 0.]]

    The thermal conductance values for each element are defined, and element stiffness matrices are computed:

    .. code-block:: python

        >>> # Thermal conductance values for each element
        >>> ep1 = 25.0    # Element 1: 1/0.04 = 25.0 W/K
        >>> ep2 = 24.3    # Element 2: 1.7/0.070 = 24.3 W/K  
        >>> ep3 = 0.4     # Element 3: 0.040/0.100 = 0.4 W/K
        >>> ep4 = 17.0    # Element 4: 1.7/0.100 = 17.0 W/K
        >>> ep5 = 7.7     # Element 5: 1/0.13 = 7.7 W/K

        >>> # Compute element stiffness matrices
        >>> Ke1 = cfc.spring1e(ep1)
        >>> Ke2 = cfc.spring1e(ep2)
        >>> Ke3 = cfc.spring1e(ep3)
        >>> Ke4 = cfc.spring1e(ep4)
        >>> Ke5 = cfc.spring1e(ep5)

    The element stiffness matrices are assembled into the global stiffness matrix:

    .. code-block:: python

        >>> # Assemble global stiffness matrix
        >>> K = cfc.assem(Edof[0, :], K, Ke1)  # Element 1
        >>> K = cfc.assem(Edof[1, :], K, Ke2)  # Element 2
        >>> K = cfc.assem(Edof[2, :], K, Ke3)  # Element 3
        >>> K = cfc.assem(Edof[3, :], K, Ke4)  # Element 4
        >>> K = cfc.assem(Edof[4, :], K, Ke5)  # Element 5

    The system of equations is solved using :code:`cfc.solveq` with boundary conditions. The prescribed temperatures are :math:`T_1=-17°\text{C}` and :math:`T_6=20°\text{C}`:

    .. code-block:: python

        >>> # Boundary conditions: DOF 1 = -17°C, DOF 6 = 20°C
        >>> bc_index = np.array([1, 6])  # DOF indices for boundary conditions
        >>> bc_value = np.array([-17.0, 20.0])  # Corresponding
        >>> # Solve system of equations
        >>> a, r = cfc.solveq(K, f, bc)
        >>> 
        >>> print("Temperatures at nodes:")
        >>> print(a)
        [[-17.        ]
         [-16.43842455]
         [-15.86067203]
         [ 19.23779344]
         [ 19.47540439]
         [ 20.        ]]        
        >>> print("Reaction forces (boundary heat flows):")
        >>> print(r)
        [[-1.40393862e+01]
         [ 0.00000000e+00]
         [ 0.00000000e+00]
         [ 0.00000000e+00]
         [ 5.68434189e-14]
         [ 4.03938619e+00]]

    The temperature values :math:`a_i` at the node points are given in the vector :code:`a` and the boundary heat flows in the vector :code:`r`.

    After solving the system of equations, the heat flow through each element is computed using :code:`cfc.extract_ed` and :code:`cfc.spring1s`:

    .. code-block:: python

        >>> # Extract element displacements (temperature differences)
        >>> ed1 = cfc.extract_ed(Edof[0, :], a)  # Element 1
        >>> ed2 = cfc.extract_ed(Edof[1, :], a)  # Element 2
        >>> ed3 = cfc.extract_ed(Edof[2, :], a)  # Element 3
        >>> ed4 = cfc.extract_ed(Edof[3, :], a)  # Element 4
        >>> ed5 = cfc.extract_ed(Edof[4, :], a)  # Element 5

        >>> # Calculate heat flows through each element
        >>> q1 = cfc.spring1s(ep1, ed1)
        >>> q2 = cfc.spring1s(ep2, ed2)
        >>> q3 = cfc.spring1s(ep3, ed3)
        >>> q4 = cfc.spring1s(ep4, ed4)
        >>> q5 = cfc.spring1s(ep5, ed5)

        >>> print("Heat flows through elements:")
        >>> print(f"Element 1: {q1[0]:.1f} W/m²")
        Element 1: 14.0 W/m²
        >>> print(f"Element 2: {q2[0]:.1f} W/m²")
        Element 2: 14.0 W/m²
        >>> print(f"Element 3: {q3[0]:.1f} W/m²")
        Element 3: 14.0 W/m²
        >>> print(f"Element 4: {q4[0]:.1f} W/m²")
        Element 4: 4.0 W/m²
        >>> print(f"Element 5: {q5[0]:.1f} W/m²")
        Element 5: 4.0 W/m²

    The heat flow through the wall is :math:`q=14.0` W/m² in the part of the wall to the left of the heat source (elements 1-3), and :math:`q=4.0` W/m² in the part to the right of the heat source (elements 4-5). This demonstrates how the internal heat source affects the heat flow distribution through the wall.
