exd_beam2_m
^^^^^^^^^^^

:Purpose: Set up the finite element model and perform eigenvalue analysis for a simple frame structure.

:Description: Consider the two dimensional frame shown below. A vertical beam is fixed at its lower end, and connected to a horizontal beam at its upper end. The horizontal beam is simply supported at the right end. The length of the vertical beam is 3 m and of the horizontal beam 2 m.

The following data apply to the beams:

.. list-table::
   :header-rows: 1
   :widths: 40 30 30

   * - 
     - vertical beam
     - horizontal beam
   * - Young's modulus (N/m²)
     - :math:`3 \times 10^{10}`
     - :math:`3 \times 10^{10}`
   * - Cross section area (m²)
     - :math:`0.1030 \times 10^{-2}`
     - :math:`0.0764 \times 10^{-2}`
   * - Moment of inertia (m⁴)
     - :math:`0.171 \times 10^{-5}`
     - :math:`0.0801 \times 10^{-5}`
   * - Density (kg/m³)
     - 2500
     - 2500

.. only:: html

    .. figure:: images/EXD1fBIG.svg
        :align: center
        :width: 500px

.. only:: latex

   .. figure:: images/EXD1fBIG.svg
      :align: center
      :width: 70%


a) Frame structure                          b) Element and DOF numbering

The structure is divided into 4 elements. The numbering of elements and degrees-of-freedom are apparent from the figure. The following ``.m``-file defines the finite element model:

:Example: The computation is initialized by importing CALFEM and NumPy. Material data and topology are defined:

.. code-block:: python

   >>> import numpy as np
   >>> import calfem.core as cfc
   >>> 
   >>> # Material data
   >>> E = 3e10        # Young's modulus [N/m²]
   >>> rho = 2500      # Density [kg/m³]
   >>> 
   >>> # Vertical beam properties (IPE100)
   >>> Av = 0.1030e-2   # Cross-sectional area [m²]
   >>> Iv = 0.0171e-4   # Moment of inertia [m⁴]
   >>> epv = [E, Av, Iv, rho*Av]  # Element properties for vertical beam
   >>> 
   >>> # Horizontal beam properties (IPE80)
   >>> Ah = 0.0764e-2   # Cross-sectional area [m²]  
   >>> Ih = 0.00801e-4  # Moment of inertia [m⁴]
   >>> eph = [E, Ah, Ih, rho*Ah]  # Element properties for horizontal beam
   >>> 
   >>> print("Material properties defined successfully")
   Material properties defined successfully

.. code-block:: python

   >>> # Element topology matrix (DOFs only, no element numbers)
   >>> Edof = np.array([
   ...     [1, 2, 3, 4, 5, 6],      # Element 1: vertical beam lower
   ...     [4, 5, 6, 7, 8, 9],      # Element 2: vertical beam upper
   ...     [7, 8, 9, 10, 11, 12],   # Element 3: horizontal beam left
   ...     [10, 11, 12, 13, 14, 15] # Element 4: horizontal beam right
   ... ])
   >>> 
   >>> # Global coordinate matrix [m]
   >>> Coord = np.array([
   ...     [0, 0],     # Node 1: base of vertical beam
   ...     [0, 1.5],   # Node 2: mid vertical beam
   ...     [0, 3],     # Node 3: top of vertical beam / left end of horizontal
   ...     [1, 3],     # Node 4: mid horizontal beam
   ...     [2, 3]      # Node 5: right end of horizontal beam
   ... ])
   >>> 
   >>> # Degrees of freedom numbering
   >>> Dof = np.array([
   ...     [1, 2, 3],     # Node 1 DOFs
   ...     [4, 5, 6],     # Node 2 DOFs
   ...     [7, 8, 9],     # Node 3 DOFs
   ...     [10, 11, 12],  # Node 4 DOFs
   ...     [13, 14, 15]   # Node 5 DOFs
   ... ])

Element matrices are generated and assembled into global stiffness and mass matrices:

.. code-block:: python

   >>> # Initialize global matrices
   >>> K = np.zeros((15, 15))  # Global stiffness matrix
   >>> M = np.zeros((15, 15))  # Global mass matrix
   >>> 
   >>> # Extract element coordinates
   >>> Ex, Ey = cfc.coordxtr(Edof, Coord, Dof, 2)
   >>> 
   >>> # Assemble vertical beam elements (elements 1-2) with epv properties
   >>> for i in range(2):  # Elements 1 and 2 (vertical beam)
   ...     k, m, c = cfc.beam2de(Ex[i], Ey[i], epv)
   ...     K = cfc.assem(Edof[i], K, k)
   ...     M = cfc.assem(Edof[i], M, m)
   >>> 
   >>> # Assemble horizontal beam elements (elements 3-4) with eph properties  
   >>> for i in range(2, 4):  # Elements 3 and 4 (horizontal beam)
   ...     k, m, c = cfc.beam2de(Ex[i], Ey[i], eph)
   ...     K = cfc.assem(Edof[i], K, k)
   ...     M = cfc.assem(Edof[i], M, m)
   >>> 
   >>> print("Global stiffness and mass matrices assembled successfully")
   Global stiffness and mass matrices assembled successfully

The finite element mesh can be plotted using CALFEM visualization functions:

.. code-block:: python

   >>> import calfem.vis_mpl as cfv
   >>> import matplotlib.pyplot as plt
   >>> 
   >>> # Plot finite element mesh
   >>> cfv.figure(figsize=(10, 8))
   >>> cfv.eldraw2(Ex, Ey, [1, 2, 2], Edof[:, 0])  # Draw elements with numbering
   >>> plt.grid(True, alpha=0.3)
   >>> plt.title('2D Frame Structure')
   >>> plt.xlabel('x [m]')
   >>> plt.ylabel('y [m]')
   >>> plt.axis('equal')
   >>> plt.show()

.. only:: html
    
    .. figure:: images/exd1f2.svg
        :align: center
        :width: 400px

.. only:: latex
    
    .. figure:: images/exd1f2.svg
        :align: center
        :width: 70%

   Finite element mesh

Eigenvalue analysis is performed to determine natural frequencies and mode shapes:

.. code-block:: python

   >>> # Boundary conditions (constrained DOFs)
   >>> b = np.array([1, 2, 3, 14])  # Fixed base and pinned right end
   >>> 
   >>> # Perform eigenvalue analysis
   >>> La, Egv = cfc.eigen(K, M, b)
   >>> 
   >>> # Calculate natural frequencies in Hz
   >>> Freq = np.sqrt(La) / (2 * np.pi)
   >>> 
   >>> print("Natural frequencies [Hz]:")
   >>> for i, f in enumerate(Freq):
   ...     print(f"Mode {i+1}: {f:.4f} Hz")
   Natural frequencies [Hz]:
   Mode 1: 6.9826 Hz
   Mode 2: 43.0756 Hz  
   Mode 3: 66.5772 Hz
   Mode 4: 162.7453 Hz
   Mode 5: 230.2709 Hz
   Mode 6: 295.6136 Hz
   Mode 7: 426.2271 Hz
   Mode 8: 697.7628 Hz
   Mode 9: 877.2765 Hz
   Mode 10: 955.9809 Hz
   Mode 11: 1751.3000 Hz

Note that the boundary condition array :code:`b` lists only the constrained degrees-of-freedom. The eigenvalues are stored in :code:`La`, eigenvectors in :code:`Egv`, and frequencies in :code:`Freq`:

.. math::

   \text{Freq} = \begin{bmatrix}
   6.9826 \\
   43.0756 \\
   66.5772 \\
   162.7453 \\
   230.2709 \\
   295.6136 \\
   426.2271 \\
   697.7628 \\
   877.2765 \\
   955.9809 \\
   1751.3
   \end{bmatrix}^T

Individual eigenvectors (mode shapes) can be plotted:

.. code-block:: python

   >>> # Plot the first eigenmode
   >>> cfv.figure(1, figsize=(10, 8))
   >>> plt.grid(True, alpha=0.3)
   >>> plt.title('The first eigenmode')
   >>> 
   >>> # Draw undeformed structure
   >>> cfv.eldraw2(Ex, Ey, [2, 3, 1])
   >>> 
   >>> # Extract and plot deformed shape for first mode
   >>> Edb = cfc.extract_ed(Edof, Egv[:, 0])  # First mode (index 0)
   >>> cfv.eldisp2(Ex, Ey, Edb, [1, 2, 2])
   >>> 
   >>> # Add frequency text
   >>> plt.text(0.5, 1.75, f'{Freq[0]:.2f} Hz', fontsize=12, 
   ...          bbox=dict(boxstyle="round,pad=0.3", facecolor="white"))
   >>> plt.xlabel('x [m]')
   >>> plt.ylabel('y [m]')
   >>> plt.axis('equal')
   >>> plt.show()

.. only:: html
    
    .. figure:: images/exd1f3.svg
        :align: center
        :width: 400px

.. only:: latex
    
    .. figure:: images/exd1f3.svg
        :align: center
        :width: 70%

   The first eigenmode, 6.98 Hz

Multiple eigenmodes can be displayed simultaneously by translating each mode in x and y directions:

.. code-block:: python

   >>> # Display first eight eigenmodes in a 2x4 grid layout
   >>> cfv.figure(figsize=(16, 10))
   >>> plt.axis('equal')
   >>> plt.axis('off')
   >>> plt.title('The first eight eigenmodes (Hz)', fontsize=16, pad=20)
   >>> 
   >>> sfac = 0.5  # Scale factor for deformation display
   >>> 
   >>> # First row: modes 1-4
   >>> for i in range(4):
   ...     # Translate structure in x-direction
   ...     Ext = Ex + i * 3
   ...     
   ...     # Draw undeformed structure
   ...     cfv.eldraw2(Ext, Ey, [2, 3, 1])
   ...     
   ...     # Extract and draw deformed shape
   ...     Edb = cfc.extract_ed(Edof, Egv[:, i])
   ...     cfv.eldisp2(Ext, Ey, Edb, [1, 2, 2], sfac)
   ...     
   ...     # Add frequency label
   ...     plt.text(3*i + 0.5, 1.5, f'{Freq[i]:.1f}', 
   ...              fontsize=10, ha='center',
   ...              bbox=dict(boxstyle="round,pad=0.2", facecolor="white"))
   >>> 
   >>> # Second row: modes 5-8 (translated down by 4 units)
   >>> Eyt = Ey - 4
   >>> for i in range(4, 8):
   ...     # Translate structure in x-direction
   ...     Ext = Ex + (i-4) * 3
   ...     
   ...     # Draw undeformed structure
   ...     cfv.eldraw2(Ext, Eyt, [2, 3, 1])
   ...     
   ...     # Extract and draw deformed shape
   ...     Edb = cfc.extract_ed(Edof, Egv[:, i])
   ...     cfv.eldisp2(Ext, Eyt, Edb, [1, 2, 2], sfac)
   ...     
   ...     # Add frequency label
   ...     plt.text(3*(i-4) + 0.5, -2.5, f'{Freq[i]:.1f}', 
   ...              fontsize=10, ha='center',
   ...              bbox=dict(boxstyle="round,pad=0.2", facecolor="white"))
   >>> 
   >>> plt.show()

.. only:: html

   .. figure:: images/exd1f4.svg
       :align: center
       :width: 400px

       The first eight eigenmodes. Frequencies are given in Hz.

.. only:: latex

   .. figure:: images/exd1f4.svg
      :align: center
      :width: 70%

      The first eight eigenmodes. Frequencies are given in Hz.
