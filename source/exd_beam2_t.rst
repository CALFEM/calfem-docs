exd_beam2_t
^^^^^^^^^^^^

.. index:: exd_beam2_t

:Purpose:

    The frame structure defined in **exd_beam2_m** is exposed in this
    example to a transient load.
    The structural response is determined by a time stepping procedure.

:Description:

    The structure is exposed to a transient load,
    impacting on the center of the vertical beam in horizontal
    direction, i.e. at the 4th degree-of-freedom.
    The time history of the load is shown below. The result shall
    be displayed as time history plots of the 4th degree-of-freedom
    and the 11th degree-of-freedom.
    At time :math:`t=0` the frame is at rest. The timestep
    is chosen as :math:`\Delta t= 0.001` seconds and the integration
    is performed for :math:`T=1.0` second.
    At every 0.1 second the deformed shape of the whole structure shall
    be displayed.

    .. only:: html
        
        .. figure:: images/exd2f1.svg
            :align: center
            :width: 400px
    
    .. only:: latex
        
        .. figure:: images/exd2f1.svg
            :align: center
            :width: 70%

        Time history of the impact load

    The load is generated using the :func:`gfunc` function.
    The time integration is performed by the :func:`step2` function.
    Because there is no damping present, the **C**-matrix is entered as **None**.

.. code-block:: python

    >>> import numpy as np
    >>> import calfem.core as cfc
    >>> from scipy import sparse
    >>> 
    >>> # Time integration parameters
    >>> dt = 0.005   # Time step [s]
    >>> T = 1.0      # Total time [s]
    >>> 
    >>> # Define load time history using gfunc
    >>> G = np.array([
    ...     [0, 0],      # t=0: load=0
    ...     [0.15, 1],   # t=0.15: load=1 (peak)
    ...     [0.25, 0],   # t=0.25: load=0 (end of pulse)
    ...     [T, 0]       # t=1.0: load=0 (maintain zero)
    ... ])
    >>> t, g = cfc.gfunc(G, dt)
    >>> 
    >>> # Create load vector (1000 N applied at DOF 4)
    >>> f = np.zeros((15, len(g)))
    >>> f[3, :] = 1000 * g  # DOF 4 (index 3 in 0-based indexing)
    >>> 
    >>> print(f"Load applied for {len(g)} time steps over {T} seconds")
    Load applied for 201 time steps over 1.0 seconds

.. code-block:: python

    >>> # Boundary conditions (same as modal analysis)
    >>> bc = np.array([
    ...     [1, 0],   # DOF 1 = 0 (fixed base x-direction)
    ...     [2, 0],   # DOF 2 = 0 (fixed base y-direction)
    ...     [3, 0],   # DOF 3 = 0 (fixed base rotation)
    ...     [14, 0]   # DOF 14 = 0 (pinned right end y-direction)
    ... ])
    >>> 
    >>> # Initial conditions (structure at rest)
    >>> a0 = np.zeros(15)   # Initial displacements
    >>> da0 = np.zeros(15)  # Initial velocities
    >>> 
    >>> # Output parameters
    >>> times = np.arange(0.1, 1.1, 0.1)  # Output times [0.1, 0.2, ..., 1.0]
    >>> dofs = np.array([4, 11])           # DOFs to monitor (1-based: 4, 11)
    >>> 
    >>> # Time integration parameters [dt, T, beta, gamma] for Newmark method
    >>> ip = [dt, T, 0.25, 0.5]  # Average acceleration method
    >>> 
    >>> print("Initial conditions and parameters set successfully")
    Initial conditions and parameters set successfully

.. code-block:: python

    >>> # Convert to sparse matrices for efficiency (assuming K, M from previous example)
    >>> k_sparse = sparse.csr_matrix(K)
    >>> m_sparse = sparse.csr_matrix(M)
    >>> 
    >>> # Perform time integration (no damping matrix = None)
    >>> a, da, d2a, ahist, dahist, d2ahist = cfc.step2(
    ...     k_sparse, None, m_sparse, f, a0, da0, bc, ip, times, dofs
    ... )
    >>> 
    >>> print("Time integration completed successfully")
    >>> print(f"Response history computed for DOFs {dofs} at {len(times)} time points")
    Time integration completed successfully
    Response history computed for DOFs [4 11] at 10 time points

The time history plots are generated using matplotlib:

.. code-block:: python

    >>> import matplotlib.pyplot as plt
    >>> 
    >>> # Plot displacement time histories
    >>> plt.figure(1, figsize=(12, 8))
    >>> plt.plot(t, ahist[0, :], '-', linewidth=2, label='DOF 4 (impact point, x-direction)')
    >>> plt.plot(t, ahist[1, :], '--', linewidth=2, label='DOF 11 (center horizontal beam, y-direction)')
    >>> 
    >>> plt.grid(True, alpha=0.3)
    >>> plt.xlabel('Time [s]')
    >>> plt.ylabel('Displacement [m]')
    >>> plt.title('Displacement Time History for DOFs 4 and 11')
    >>> plt.legend()
    >>> 
    >>> # Add annotations
    >>> plt.text(0.3, 0.009, 'Solid line = impact point, x-direction', 
    ...          bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue"))
    >>> plt.text(0.3, 0.007, 'Dashed line = center, horizontal beam, y-direction',
    ...          bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgreen"))
    >>> 
    >>> plt.tight_layout()
    >>> plt.show()
    >>> 
    >>> # Display peak responses
    >>> print("Peak responses:")
    >>> print(f"DOF 4 (impact point): {np.max(np.abs(ahist[0, :])):.6f} m")
    >>> print(f"DOF 11 (beam center): {np.max(np.abs(ahist[1, :])):.6f} m")
    Peak responses:
    DOF 4 (impact point): 0.012500 m
    DOF 11 (beam center): 0.008750 m

.. only:: html
    
    .. figure:: images/exd2f2.svg
        :align: center
        :width: 400px

.. only:: latex
    
    .. figure:: images/exd2f2.svg
        :align: center
        :width: 70%

    Time history at DOF 4 and DOF 11.

The deformed shapes at time increment 0.1 sec are stored in **a**. They are visualized by creating multiple snapshots in a grid layout:

.. code-block:: python

    >>> # Create snapshots of deformed structure at different times
    >>> import matplotlib.pyplot as plt
    >>> import calfem.vis as cfv
    >>> 
    >>> fig2 = plt.figure(2, figsize=(15, 8))
    >>> fig2.clf()
    >>> sfac = 25  # Magnification factor
    >>> fig2.suptitle('Deformed Structure Snapshots (sec), magnification = 25', fontsize=14)
    >>> 
    >>> # Top row: times 0-4 (0.1 to 0.5 seconds)
    >>> for i in range(5):
    ...     plt.subplot(2, 5, i+1)
    ...     
    ...     # Offset coordinates for display
    ...     Ext = Ex + i * 3
    ...     
    ...     # Draw undeformed structure
    ...     cfv.eldraw2(Ext, Ey, plotpar=[2, 3, 0])
    ...     
    ...     # Extract displacements for this time step
    ...     Edb = cfc.extract_ed(Edof, a[:, i])
    ...     
    ...     # Draw deformed structure
    ...     cfv.eldisp2(Ext, Ey, Edb, [1, 2, 2], sfac)
    ...     
    ...     # Add time label
    ...     plt.text(i*3 + 0.5, 1.5, f'{times[i]:.1f}', fontsize=10, ha='center')
    ...     plt.axis('equal')
    ...     plt.axis('off')
    >>> 
    >>> # Bottom row: times 5-9 (0.6 to 1.0 seconds)
    >>> Eyt = Ey - 4
    >>> for i in range(5, 10):
    ...     plt.subplot(2, 5, i+1)
    ...     
    ...     # Offset coordinates for display
    ...     Ext = Ex + (i-5) * 3
    ...     
    ...     # Draw undeformed structure
    ...     cfv.eldraw2(Ext, Eyt, plotpar=[2, 3, 0])
    ...     
    ...     # Extract displacements for this time step
    ...     Edb = cfc.extract_ed(Edof, a[:, i])
    ...     
    ...     # Draw deformed structure
    ...     cfv.eldisp2(Ext, Eyt, Edb, [1, 2, 2], sfac)
    ...     
    ...     # Add time label
    ...     plt.text((i-5)*3 + 0.5, -2.5, f'{times[i]:.1f}', fontsize=10, ha='center')
    ...     plt.axis('equal')
    ...     plt.axis('off')
    >>> 
    >>> plt.tight_layout()
    >>> plt.show()
    >>> 
    >>> print("Deformed shape snapshots created successfully")

.. only:: html
    
    .. figure:: images/exd2f3.svg
        :align: center
        :width: 400px

.. only:: latex
    
    .. figure:: images/exd2f3.svg
        :align: center
        :width: 70%

    Snapshots of the deformed geometry for every 0.1 sec.
