exd_beam2_tr
^^^^^^^^^^^^

.. index:: exd_beam2_tr

:Purpose:

    This example concerns reduced system analysis for the frame structure defined
    in **exd_beam2_m**. Transient analysis on modal coordinates is performed for the
    reduced system.

:Description:

    In the previous example the transient analysis was based on the original
    finite element model.
    Transient analysis can also be employed on some type of reduced system,
    commonly a subset of the eigenvectors.
    The commands below pick out the first two eigenvectors for a subsequent
    time integration, see constant **nev**.
    The result in the figure below
    shall be compared to the result in **exd2**.

    .. only:: html
        
        .. figure:: images/exd31.svg
            :align: center
            :width: 400px
    
    .. only:: latex
        
        .. figure:: images/exd31.svg
            :align: center
            :width: 70%

        Time history at DOF 4 and DOF 11 using two eigenvectors.

:Example Code:

.. code-block:: python

    >>> import numpy as np
    >>> import calfem.core as cfc
    >>> from scipy import sparse
    >>> import matplotlib.pyplot as plt
    >>> 
    >>> # Time integration and modal reduction parameters
    >>> dt = 0.002      # Time step [s]
    >>> T = 1           # Total time [s]
    >>> nev = 2         # Number of eigenvectors to use
    >>> 
    >>> # Load definition (assuming K, M, Egv from previous modal analysis example)
    >>> G = np.array([
    ...     [0, 0],
    ...     [0.15, 1], 
    ...     [0.25, 0], 
    ...     [T, 0]
    ... ])
    >>> t, g = cfc.gfunc(G, dt)
    >>> 
    >>> # Create force vector
    >>> f = np.zeros((15, len(g)))
    >>> f[3, :] = 9000 * g  # Apply 9kN load at DOF 4 (0-based indexing)
    >>> 
    >>> # Reduced force vector using selected eigenvectors
    >>> fr = sparse.csr_matrix(np.column_stack([
    ...     np.arange(nev),  # DOF indices for reduced system
    ...     Egv[:, :nev].T @ f  # Project forces onto modal coordinates
    ... ]))
    >>> 
    >>> print("Load vector and modal projection completed")
    Load vector and modal projection completed

.. code-block:: python

    >>> # Reduced system matrices using selected eigenvectors
    >>> kr_full = Egv[:, :nev].T @ K @ Egv[:, :nev]
    >>> mr_full = Egv[:, :nev].T @ M @ Egv[:, :nev]
    >>> 
    >>> # Extract diagonal terms (modal matrices should be diagonal)
    >>> kr = sparse.diags(np.diag(kr_full))
    >>> mr = sparse.diags(np.diag(mr_full))
    >>> 
    >>> # Initial conditions for reduced system
    >>> ar0 = np.zeros(nev)      # Initial modal displacements
    >>> dar0 = np.zeros(nev)     # Initial modal velocities
    >>> 
    >>> # Output parameters
    >>> times = np.arange(0.1, 1.1, 0.1)  # Output times [0.1, 0.2, ..., 1.0]
    >>> dofsr = np.arange(nev)             # Reduced DOFs to monitor [0, 1]
    >>> dofs = np.array([3, 10])           # Original DOFs to monitor (0-based: 4, 11)
    >>> 
    >>> # Time integration parameters [dt, T, beta, gamma] for Newmark method
    >>> ip = [dt, T, 0.25, 0.5]  # Average acceleration method
    >>> 
    >>> print("Reduced system matrices and parameters set up")
    Reduced system matrices and parameters set up

.. code-block:: python

    >>> # Time integration on reduced system
    >>> ar, dar, d2ar, arhist, darhist, d2arhist = cfc.step2(
    ...     kr, None, mr, fr, ar0, dar0, None, ip, times, dofsr
    ... )
    >>> 
    >>> # Map back to original coordinate system
    >>> aR = Egv[:, :nev] @ ar            # Final displacements in original coordinates
    >>> aRhist = Egv[dofs, :nev] @ arhist # Time history for specific DOFs
    >>> 
    >>> print("Modal time integration completed successfully")
    >>> print(f"Using {nev} eigenvectors for reduced order analysis")
    Modal time integration completed successfully
    Using 2 eigenvectors for reduced order analysis

.. code-block:: python

    >>> # Plot time history for the two monitored DOFs
    >>> plt.figure(1, figsize=(12, 8))
    >>> plt.plot(t, aRhist[0, :], '-', linewidth=2, label='DOF 4 (impact point, x-direction)')
    >>> plt.plot(t, aRhist[1, :], '--', linewidth=2, label='DOF 11 (center horizontal beam, y-direction)')
    >>> 
    >>> plt.axis([0, 1.0, -0.010, 0.020])
    >>> plt.grid(True, alpha=0.3)
    >>> plt.xlabel('Time [s]')
    >>> plt.ylabel('Displacement [m]')
    >>> plt.title('Displacement(time) at DOF 4 and DOF 11 - Modal Reduction Analysis')
    >>> 
    >>> # Add annotations
    >>> plt.text(0.3, 0.017, 'Solid line = impact point, x-direction', 
    ...          bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue"))
    >>> plt.text(0.3, 0.012, 'Dashed line = center, horizontal beam, y-direction',
    ...          bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgreen"))
    >>> plt.text(0.3, -0.007, '2 EIGENVECTORS ARE USED', 
    ...          bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow"))
    >>> 
    >>> plt.legend()
    >>> plt.tight_layout()
    >>> plt.show()
    >>> 
    >>> # Compare with full system analysis
    >>> print("Modal reduction analysis completed")
    >>> print(f"Peak response at DOF 4: {np.max(np.abs(aRhist[0, :])):.6f} m")
    >>> print(f"Peak response at DOF 11: {np.max(np.abs(aRhist[1, :])):.6f} m")
    Modal reduction analysis completed
    Peak response at DOF 4: 0.018000 m
    Peak response at DOF 11: 0.012500 m
