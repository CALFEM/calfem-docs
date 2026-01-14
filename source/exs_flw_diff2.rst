exs_flw_diff2
^^^^^^^^^^^^^

:Purpose: 

   Show how to solve a two dimensional diffusion problem.

:Description: 

   Consider a filter paper of square shape. Three sides are in contact with pure water and the fourth side is in contact with a solution of concentration :math:`c=1.0 \cdot 10^{-3}` kg/m³. The length of each side is 0.100 m. Using symmetry, only half of the paper has to be analyzed. The paper and the corresponding finite element mesh are shown. The following boundary conditions are applied:

.. only:: html
    
    .. figure:: images/exs8f1.svg
        :align: center
        :width: 600px

.. only:: latex
    
    .. figure:: images/exs8f1.svg
        :align: center
        :width: 70%

:Example: 

   The computation is initialized by importing CALFEM and NumPy. The element topology matrix contains only the degrees of freedom for each quadrilateral element:

   .. code-block:: python

      import numpy as np
      import calfem.vis_mpl as cfv
      import calfem.core as cfc
      import calfem.utils as cfu

      edof = np.array([
         [1, 2, 5, 4],
         [2, 3, 6, 5],
         [4, 5, 8, 7],
         [5, 6, 9, 8],
         [7, 8, 11, 10],
         [8, 9, 12, 11],
         [10, 11, 14, 13],
         [11, 12, 15, 14],
      ])      

      coord = np.array([
         [0, 0],
         [0.025, 0],
         [0.05, 0],
         [0, 0.025],
         [0.025, 0.025],
         [0.05, 0.025],
         [0, 0.05],
         [0.025, 0.05],
         [0.05, 0.05],
         [0, 0.075],
         [0.025, 0.075],
         [0.05, 0.075],
         [0, 0.1],
         [0.025, 0.1],
         [0.05, 0.1],
      ])

      dofs = np.arange(1, coord.shape[0] + 1).reshape(coord.shape[0], 1)  

      ep = [1]

      D = np.array([
         [1, 0], 
         [0, 1]
      ])

      ex, ey = cfc.coordxtr(edof, coord, dofs)          


The global system matrices are initialized:

.. code-block:: python

   K = np.zeros((15, 15))  # Global conductivity matrix
   f = np.zeros((15, 1))   # Global source vector (no sources in this problem)

The global conductivity matrix is assembled by adding the element matrix computed with ``flw2qe()`` to each element location:

.. code-block:: python

   for elx, ely, etopo in zip(ex, ey, edof):
      Ke = cfc.flw2qe(elx, ely, ep, D)
      K = cfc.assem(etopo, K, Ke)

The boundary conditions are applied and the system is solved. The boundary condition at DOF 13 is set to 0.5×10⁻³ as an average of neighboring boundary concentrations:

.. code-block:: python

   bc_dofs = np.array([1, 2, 3, 4, 7, 10, 13, 14, 15])
   bc_vals = np.array([0, 0, 0, 0, 0, 0, 0.5e-3, 1e-3, 1e-3])

Solve for concentrations and boundary fluxes

.. tabs::

   .. tab:: Code

      .. code:: python

         a, r = cfc.solveq(K, f, bc_dofs, bc_vals)

         cfu.disp_h2("Concentration at nodes [kg/m^3]:")
         cfu.disp_array(a, ["a"])

         cfu.disp_h2("Boundary fluxes at nodes [kg/m^2/s)]:")
         cfu.disp_array(r, ["r"])

   .. tab:: Output

         .. code::

            ## Concentration at nodes [kg/m^3]:

            +------------+
            |          a |
            |------------|
            | 0.0000e+00 |
            | 0.0000e+00 |
            | 0.0000e+00 |
            | 0.0000e+00 |
            | 6.6176e-05 |
            | 9.3487e-05 |
            | 0.0000e+00 |
            | 1.7857e-04 |
            | 2.5000e-04 |
            | 0.0000e+00 |
            | 4.3382e-04 |
            | 5.4937e-04 |
            | 5.0000e-04 |
            | 1.0000e-03 |
            | 1.0000e-03 |
            +------------+

            ## Boundary fluxes at nodes [kg/m^2/s)]:

            +-------------+
            |           r |
            |-------------|
            | -1.6544e-05 |
            | -5.6460e-05 |
            | -3.9916e-05 |
            | -7.7731e-05 |
            |  0.0000e+00 |
            |  1.3553e-20 |
            | -2.1429e-04 |
            | -1.0842e-19 |
            |  0.0000e+00 |
            | -6.3655e-04 |
            | -1.0842e-19 |
            | -1.0842e-19 |
            |  1.6544e-05 |
            |  7.7075e-04 |
            |  2.5420e-04 |
            +-------------+            

The element flux vectors are calculated from element concentrations using :func:`flw2qs`:

.. code-block:: python

   ed = cfc.extract_eldisp(edof, a)

Compute element flux vectors for all elements.

.. tabs::

   .. tab:: Code

      .. code-block:: python

         es = np.zeros((8, 2))
         el_idx = 0

         for elx, ely, eld in zip(ex, ey, ed):
            es_el, t = cfc.flw2qs(elx, ely, ep, D, eld)
            es[el_idx] = es_el

            el_idx += 1

            cfu.disp_h2(f"Element flux vectors [kg/m^2/s]:")
            cfu.disp_array(es, headers=["qx", "qy"])

            cfu.disp_h2("Concentration field [×10⁻³ kg/m³]:")
            cfu.disp("Pure water boundaries (DOFs 1-4,7,10): 0.000")
            cfu.disp(f"Internal concentrations:")

            a_dofs = [5, 6, 8, 9, 11, 12]
            a_internal = a[a_dofs - np.ones(len(a_dofs), dtype=int)]
            a_table = np.hstack((np.array(a_dofs, dtype=int).reshape(-1, 1), a_internal.reshape(-1, 1)))

            cfu.disp_array(a_table, headers=["DOF", "Concentration"])

            cfu.disp(f"Solution boundaries (DOFs 14,15): 1.000")

   .. tab:: Output

      .. code::

         ## Element flux vectors [kg/m^2/s]:

         +-------------+-------------+
         |          qx |          qy |
         |-------------+-------------|
         | -1.3235e-03 | -1.3235e-03 |
         | -5.4622e-04 | -3.1933e-03 |
         | -4.8950e-03 | -2.2479e-03 |
         | -1.9748e-03 | -5.3782e-03 |
         | -1.2248e-02 | -5.1050e-03 |
         | -3.7395e-03 | -1.1092e-02 |
         | -1.8676e-02 | -2.1324e-02 |
         | -2.3109e-03 | -2.0336e-02 |
         +-------------+-------------+

         ## Concentration field [×10⁻³ kg/m³]:

         Pure water boundaries (DOFs 1-4,7,10): 0.000
         Internal concentrations:
         +------------+-----------------+
         |        DOF |   Concentration |
         |------------+-----------------|
         | 5.0000e+00 |      6.6176e-05 |
         | 6.0000e+00 |      9.3487e-05 |
         | 8.0000e+00 |      1.7857e-04 |
         | 9.0000e+00 |      2.5000e-04 |
         | 1.1000e+01 |      4.3382e-04 |
         | 1.2000e+01 |      5.4937e-04 |
         +------------+-----------------+
         Solution boundaries (DOFs 14,15): 1.000     

.. code-block:: python

   import calfem.vis_mpl as cfv
   import calfem.core as cfc
   import calfem.utils as cfu

Visualization can be created using CALFEM's visualization functions:

.. code-block:: python

   >>> cfv.eldraw2(ex, ey, [1, 2, 1], range(1, ex.shape[0] + 1))
   >>> cfv.eliso2_mpl(ex, ey, ed)
   >>> cfv.show_and_wait()

.. only:: html
    
    .. figure:: images/exs8f2.svg
        :align: center
        :width: 600px

.. only:: latex
    
    .. figure:: images/exs8f2.svg
        :align: center
        :width: 70%

   Flux vectors

.. only:: html
    
    .. figure:: images/exs8f3.svg
        :align: center
        :width: 600px

.. only:: latex
    
    .. figure:: images/exs8f3.svg
        :align: center
        :width: 70%

   Contour lines

.. note::

    Two comments concerning the contour lines:

    In the upper left corner, the contour lines should physically have met at the corner point. However, the drawing of the contour lines for the quadrilateral element follows the numerical approximation along the element boundaries, i.e. a linear variation. A finer element mesh will bring the contour lines closer to the corner point.

    Along the symmetry line, the contour lines should physically be perpendicular to the boundary. This will also be improved with a finer element mesh.

