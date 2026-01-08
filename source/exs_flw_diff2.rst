exs_flw_diff2
^^^^^^^^^^^^^

:Purpose: Show how to solve a two dimensional diffusion problem.

:Description: Consider a filter paper of square shape. Three sides are in contact with pure water and the fourth side is in contact with a solution of concentration :math:`c=1.0 \cdot 10^{-3}` kg/m³. The length of each side is 0.100 m. Using symmetry, only half of the paper has to be analyzed. The paper and the corresponding finite element mesh are shown. The following boundary conditions are applied:

.. only:: html
    
    .. figure:: images/exs8f1.svg
        :align: center
        :width: 400px

.. only:: latex
    
    .. figure:: images/exs8f1.svg
        :align: center
        :width: 70%

:Example: The computation is initialized by importing CALFEM and NumPy. The element topology matrix contains only the degrees of freedom for each quadrilateral element:

.. code-block:: python

   >>> import numpy as np
   >>> import calfem.core as cfc
   >>> import calfem.utils as cfu
   >>> 
   >>> # Element topology matrix (DOFs only, no element numbers)
   >>> # Each row represents one quadrilateral element with 4 nodes
   >>> edof = np.array([
   ...     [1, 2, 5, 4],      # Element 1
   ...     [2, 3, 6, 5],      # Element 2
   ...     [4, 5, 8, 7],      # Element 3
   ...     [5, 6, 9, 8],      # Element 4
   ...     [7, 8, 11, 10],    # Element 5
   ...     [8, 9, 12, 11],    # Element 6
   ...     [10, 11, 14, 13],  # Element 7
   ...     [11, 12, 15, 14]   # Element 8
   ... ])

The global system matrices are initialized:

.. code-block:: python

   >>> K = np.zeros((15, 15))  # Global conductivity matrix
   >>> f = np.zeros((15, 1))   # Global source vector (no sources in this problem)

Because all elements have the same geometry, orientation, and material properties, only one element conductivity matrix needs to be computed using :func:`flw2qe`:

Element properties and material matrix

.. code-block:: python

   >>> ep = [1]                    # Thickness [m]
   >>> D = np.array([[1, 0],     # Diffusion/conductivity matrix [m²/s]
   ...               [0, 1]])

Element coordinates for standard element (0.025 × 0.025 m)

.. code:: python

   >>> ex = np.array([0, 0.025, 0.025, 0])      # x-coordinates [m]
   >>> ey = np.array([0, 0, 0.025, 0.025])      # y-coordinates [m]
   >>> 

Compute element conductivity matrix.

.. code:: python

   >>> Ke = cfc.flw2qe(ex, ey, ep, D)
   >>> print("Element conductivity matrix:")
   >>> print(Ke)
   [[ 0.75  -0.25  -0.25  -0.25]
    [-0.25   0.75  -0.25  -0.25]
    [-0.25  -0.25   0.75  -0.25]
    [-0.25  -0.25  -0.25   0.75]]

The global conductivity matrix is assembled by adding the element matrix to each element location:

.. code-block:: python

   >>> for i in range(8):  # 8 elements
   ...     K = cfc.assem(edof[i], K, Ke)

The boundary conditions are applied and the system is solved. The boundary condition at DOF 13 is set to 0.5×10⁻³ as an average of neighboring boundary concentrations:

.. code-block:: python

   >>> bc_dofs = np.array([1, 2, 3, 4, 7, 10, 13, 14, 15])
   >>> bc_values = np.array([0, 0, 0, 0, 0, 0, 0.5e-3, 1e-3, 1e-3])
   >>> 

Solve for concentrations and boundary fluxes

.. code-block:: python

   >>> a, r = cfc.solveq(K, f, bc)
   >>> print("Concentrations [kg/m³]:")
   >>> print(a)
   >>> print("Boundary fluxes [kg/m²/s]:")  
   >>> print(r)
   Concentrations [kg/m³]:
   [[0.00000000e+00]
    [0.00000000e+00]
    [0.00000000e+00]
    [0.00000000e+00]
    [6.61764706e-05]
    [9.34873950e-05]
    [0.00000000e+00]
    [1.78571429e-04]
    [2.50000000e-04]
    [0.00000000e+00]
    [4.33823529e-04]
    [5.49369748e-04]
    [5.00000000e-04]
    [1.00000000e-03]
    [1.00000000e-03]]
   Boundary fluxes [kg/m²/s]:
   [[-1.65441176e-05]
    [-5.64600840e-05]
    [-3.99159664e-05]
    [-7.77310924e-05]
    [ 0.00000000e+00]
    [-1.35525272e-20]
    [-2.14285714e-04]
    [ 5.42101086e-20]
    [ 5.42101086e-20]
    [-6.36554622e-04]
    [ 0.00000000e+00]
    [ 2.16840434e-19]
    [ 1.65441176e-05]
    [ 7.70745798e-04]
    [ 2.54201681e-04]]   

The element flux vectors are calculated from element concentrations using :func:`flw2qs`:

.. code-block:: python

   >>> ed = cfc.extract_ed(edof, a)

Compute element flux vectors for all elements.

.. code-block:: python

   >>> es = np.zeros((8, 2))  # Store flux vectors for 8 elements
   >>> for i in range(8):
   >>>    es[i], _ = cfc.flw2qs(ex, ey, ep, D, ed[i])
   >>> 
   >>> print("Element flux vectors [kg/m²/s]:")
   >>> for i, ees in enumerate(es):
   >>>    print(f"Element {i+1}: qx = {ees[0]:.6f}, qy = {ees[1]:.6f}")

**Results:**

The solution demonstrates the expected concentration distribution and flux patterns:

.. code-block:: text

   Element flux vectors [kg/m²/s]:
   Element 1: qx = -0.001324, qy = -0.001324
   Element 2: qx = -0.000546, qy = -0.003193
   Element 3: qx = -0.004895, qy = -0.002248
   Element 4: qx = -0.001975, qy = -0.005378
   Element 5: qx = -0.012248, qy = -0.005105
   Element 6: qx = -0.003739, qy = -0.011092
   Element 7: qx = -0.018676, qy = -0.021324
   Element 8: qx = -0.002311, qy = -0.020336   

.. code-block:: python

   >>> # Summary of key results
   >>> print("\\nConcentration field [×10⁻³ kg/m³]:")
   >>> print(f"Pure water boundaries (DOFs 1-4,7,10): 0.000")
   >>> print(f"Internal concentrations:")
   >>> print(f"  DOF 5: {a[4]*1000:.3f}")
   >>> print(f"  DOF 6: {a[5]*1000:.3f}") 
   >>> print(f"  DOF 8: {a[7]*1000:.3f}")
   >>> print(f"  DOF 9: {a[8]*1000:.3f}")
   >>> print(f"  DOF 11: {a[10]*1000:.3f}")
   >>> print(f"  DOF 12: {a[11]*1000:.3f}")
   >>> print(f"Solution boundaries (DOFs 14,15): 1.000")
   
.. code-block:: text

   Concentration field [×10⁻³ kg/m³]:
   Pure water boundaries (DOFs 1-4,7,10): 0.000
   Internal concentrations:
     DOF 5: 0.066
     DOF 6: 0.093
     DOF 8: 0.179
     DOF 9: 0.250
     DOF 11: 0.434
     DOF 12: 0.549
   Solution boundaries (DOFs 14,15): 1.000

An alternative approach using global coordinates and automatic mesh generation, with visualization of flux vectors and contour lines:

.. code-block:: python

   import calfem.vis_mpl as cfv
   import calfem.core as cfc
   import calfem.utils as cfu

Create system matrices system matrices, coord and dof matrices.

.. code-block:: python

   >>> K = np.zeros((15, 15))
   >>> f = np.zeros((15, 1))
   >>> 
   >>> coord = np.array([
   ... [0, 0],
   ... [0.025, 0],
   ... [0.05, 0],
   ... [0, 0.025],
   ... [0.025, 0.025],
   ... [0.05, 0.025],
   ... [0, 0.05],
   ... [0.025, 0.05],
   ... [0.05, 0.05],
   ... [0, 0.075],
   ... [0.025, 0.075],
   ... [0.05, 0.075],
   ... [0, 0.1],
   ... [0.025, 0.1],
   ... [0.05, 0.1]
   ... ])
   >>> dof = np.arange(1, 16).reshape((15, 1))

Element properties, topology and coordinates.

.. code-block:: python

   >>> ep = np.array([1])
   >>> D = np.array([[1, 0], [0, 1]])
   >>> edof = np.array([
   ...   [1, 2, 5, 4],
   ...   [2, 3, 6, 5],
   ...   [4, 5, 8, 7],
   ...   [5, 6, 9, 8],
   ...   [7, 8, 11, 10],
   ...   [8, 9, 12, 11],
   ...   [10, 11, 14, 13],
   ...   [11, 12, 15, 14],
   ...   ])  

Extract element coordinates automatically.

.. code-block:: python

   >>> ex, ey = cfc.coordxtr(edof, coord, dof)

Assembly and solution (same as before but with variable geometry).

.. code-block:: python

   >>> for i in range(8):
   >>>    Ke = cfc.flw2qe(ex[i], ey[i], ep, D)
   >>>    K = cfc.assem(edof[i], K, Ke)

Solve equation system.   
      
.. code-block:: python

   >>> bc_prescr = np.array([1, 2, 3, 4, 7, 10, 13, 14, 15])
   >>> bc_val = np.array([0, 0, 0, 0, 0, 0, 0.5e-3, 1e-3, 1e-3])
   >>> a, r = cfc.solveq(K, f, bc_prescr, bc_val)

Compute element flux vectors and contour lines.

.. code-block:: python

   >>> ed = cfc.extractEldisp(edof, a)
   >>> es = np.zeros((8, 2))
   >>> for i in range(8):
   >>>     es[i], Et = cfc.flw2qs(ex[i], ey[i], ep, D, ed[i])

Visualization can be created using CALFEM's visualization functions:

.. code-block:: python

   >>> cfv.eldraw2(ex, ey, [1, 2, 1], range(1, ex.shape[0] + 1))
   >>> cfv.eliso2_mpl(ex, ey, ed)
   >>> cfv.show_and_wait()

.. only:: html
    
    .. figure:: images/exs8f2.svg
        :align: center
        :width: 400px

.. only:: latex
    
    .. figure:: images/exs8f2.svg
        :align: center
        :width: 70%

   Flux vectors

.. only:: html
    
    .. figure:: images/exs8f3.svg
        :align: center
        :width: 400px

.. only:: latex
    
    .. figure:: images/exs8f3.svg
        :align: center
        :width: 70%

   Contour lines

.. note::

    Two comments concerning the contour lines:

    In the upper left corner, the contour lines should physically have met at the corner point. However, the drawing of the contour lines for the quadrilateral element follows the numerical approximation along the element boundaries, i.e. a linear variation. A finer element mesh will bring the contour lines closer to the corner point.

    Along the symmetry line, the contour lines should physically be perpendicular to the boundary. This will also be improved with a finer element mesh.

    A color plot of the concentrations can be created using matplotlib:

    .. code-block:: python

        >>> # Color-filled contour plot
        >>> plt.figure(figsize=(10, 8))
        >>> 
        >>> # Create filled contours
        >>> for i in range(8):
        ...     plt.fill(Ex[i], Ey[i], Ed_alt[i], alpha=0.8, cmap='jet')
        >>> 
        >>> plt.colorbar(label='Concentration [kg/m³]')
        >>> plt.title('Concentration Distribution')
        >>> plt.xlabel('x [m]')
        >>> plt.ylabel('y [m]')
        >>> plt.axis('equal')
        >>> plt.grid(True, alpha=0.3)
        >>> plt.show()
