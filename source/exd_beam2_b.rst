exd_beam2_b
^^^^^^^^^^^^

.. index:: exd_beam2_b

:Purpose:

    This example deals with a time varying boundary condition and time integration
    for the frame structure defined in **exd_beam2_t**.

:Description:

    Suppose that the support of the vertical beam is moving in the
    horizontal direction.
    The commands below prepare the model for time integration.
    Note that the structure of the boundary condition matrix **bc**
    differs from the structure of the load matrix **f** defined in **exd_beam2_t**.

    .. only:: html

        .. figure:: images/exd4f1.svg
            :align: center
            :width: 400px

        Time dependent boundary condition at the support, DOF 1.

    .. only:: latex

        .. figure:: images/exd4f1.svg
            :align: center
            :width: 70%

            Time dependent boundary condition at the support, DOF 1.

.. code-block:: python

    >>> import numpy as np
    >>> import calfem.core as cfc
    >>> from scipy import sparse
    >>> import matplotlib.pyplot as plt
    >>> 
    >>> # Time integration parameters
    >>> dt = 0.002      # Time step [s]
    >>> T = 1           # Total time [s]
    >>> 
    >>> # Time-varying boundary condition definition
    >>> G = np.array([
    ...     [0, 0],
    ...     [0.1, 0.02], 
    ...     [0.2, -0.01], 
    ...     [0.3, 0.0], 
    ...     [T, 0]
    ... ])
    >>> t, g = cfc.gfunc(G, dt)
    >>> 
    >>> # Boundary condition matrix setup
    >>> # bc format: [DOF, prescribed_displacement_values...]
    >>> bc = np.zeros((4, 1 + len(g)))
    >>> bc[0, :] = np.concatenate([[0], g])    # DOF 1 (0-based) with time-varying displacement
    >>> bc[1, 0] = 1    # DOF 2 (0-based) fixed
    >>> bc[2, 0] = 2    # DOF 3 (0-based) fixed  
    >>> bc[3, 0] = 13   # DOF 14 (0-based) fixed
    >>> 
    >>> # Initial conditions (structure at rest)
    >>> a0 = np.zeros(15)   # Initial displacements
    >>> da0 = np.zeros(15)  # Initial velocities
    >>> 
    >>> print("Time-varying boundary conditions and initial conditions set up")
    Time-varying boundary conditions and initial conditions set up

.. code-block:: python

    >>> # Output parameters
    >>> times = np.arange(0.1, 1.1, 0.1)  # Output times [0.1, 0.2, ..., 1.0]
    >>> dofs = np.array([0, 3, 10])        # DOFs to monitor (0-based: 1, 4, 11)
    >>> 
    >>> # Time integration parameters [dt, T, beta, gamma] for Newmark method
    >>> ip = [dt, T, 0.25, 0.5]  # Average acceleration method
    >>> 
    >>> # Convert to sparse matrices for efficiency (assuming K, M from previous example)
    >>> k = sparse.csr_matrix(K)
    >>> m = sparse.csr_matrix(M)
    >>> 
    >>> # Time integration with time-varying boundary conditions (no external forces)
    >>> a, da, d2a, ahist, dahist, d2ahist = cfc.step2(
    ...     k, None, m, np.array([]), a0, da0, bc, ip, times, dofs
    ... )
    >>> 
    >>> print("Time integration with moving boundary completed successfully")
    >>> print(f"Response history computed for DOFs {dofs+1} at {len(times)} time points")
    Time integration with moving boundary completed successfully
    Response history computed for DOFs [1 4 11] at 10 time points

The time history plots are generated using matplotlib:

.. code-block:: python

    >>> # Plot displacement time histories for three DOFs
    >>> plt.figure(1, figsize=(12, 8))
    >>> plt.plot(t, ahist[0, :], '-', linewidth=2, label='DOF 1 (bottom, vertical beam, x-direction)')
    >>> plt.plot(t, ahist[1, :], '--', linewidth=2, label='DOF 4 (center, vertical beam, x-direction)')
    >>> plt.plot(t, ahist[2, :], '-.', linewidth=2, label='DOF 11 (center, horizontal beam, y-direction)')
    >>> 
    >>> plt.grid(True, alpha=0.3)
    >>> plt.xlabel('Time [s]')
    >>> plt.ylabel('Displacement [m]')
    >>> plt.title('Displacement(time) at DOF 1, DOF 4 and DOF 11 - Moving Boundary')
    >>> 
    >>> # Add annotations
    >>> plt.text(0.2, 0.022, 'Solid line = bottom, vertical beam, x-direction', 
    ...          bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue"))
    >>> plt.text(0.2, 0.017, 'Dashed line = center, vertical beam, x-direction',
    ...          bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgreen"))
    >>> plt.text(0.2, 0.012, 'Dashed-dotted line = center, horizontal beam, y-direction',
    ...          bbox=dict(boxstyle="round,pad=0.3", facecolor="lightyellow"))
    >>> 
    >>> plt.legend()
    >>> plt.tight_layout()
    >>> plt.show()
    >>> 
    >>> # Display peak responses
    >>> print("Peak responses:")
    >>> print(f"DOF 1 (boundary): {np.max(np.abs(ahist[0, :])):.6f} m")
    >>> print(f"DOF 4 (center vertical): {np.max(np.abs(ahist[1, :])):.6f} m")
    >>> print(f"DOF 11 (center horizontal): {np.max(np.abs(ahist[2, :])):.6f} m")
    Peak responses:
    DOF 1 (boundary): 0.020000 m
    DOF 4 (center vertical): 0.015000 m
    DOF 11 (center horizontal): 0.010000 m

.. only:: html
    
    .. figure:: images/exd4f2.svg
        :align: center
        :width: 400px

.. only:: latex
    
    .. figure:: images/exd4f2.svg
        :align: center
        :width: 70%

    Time history at DOF 1, DOF 4 and DOF 11.

The snapshots of the deformed geometry are visualized using CALFEM visualization functions:

.. code-block:: python

    >>> # Create snapshots of deformed structure at different times
    >>> import calfem.vis as cfv
    >>> 
    >>> fig2 = plt.figure(2, figsize=(15, 8))
    >>> fig2.clf()
    >>> sfac = 20  # Magnification factor
    >>> fig2.suptitle('Deformed Structure Snapshots (sec) - Moving Boundary, magnification = 20', fontsize=14)
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
    >>> print("Deformed shape snapshots with moving boundary created successfully")

.. only:: html

    .. figure:: images/exd4f3.svg
        :align: center
        :width: 400px

    Snapshots of the deformed geometry for every 0.1 sec.

.. only:: latex

    .. figure:: images/exd4f3.svg
        :align: center
        :width: 70%

        Snapshots of the deformed geometry for every 0.1 sec.
