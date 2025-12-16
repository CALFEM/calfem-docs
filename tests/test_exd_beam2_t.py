"""
Test script for exd_beam2_t example.
Transient load analysis for the frame structure defined in exd_beam2_m.
Note: This script requires K, M, Ex, Ey, Edof from the modal analysis example.
"""

import numpy as np
import calfem.core as cfc
from scipy import sparse

# Note: This assumes K, M, Ex, Ey, Edof are defined from exd_beam2_m
# For standalone execution, you would need to run that example first or include the setup

# Time integration parameters
dt = 0.005   # Time step [s]
T = 1.0      # Total time [s]

# Define load time history using gfunc
G = np.array([
    [0, 0],      # t=0: load=0
    [0.15, 1],   # t=0.15: load=1 (peak)
    [0.25, 0],   # t=0.25: load=0 (end of pulse)
    [T, 0]       # t=1.0: load=0 (maintain zero)
])
t, g = cfc.gfunc(G, dt)

# Create load vector (1000 N applied at DOF 4)
f = np.zeros((15, len(g)))
f[3, :] = 1000 * g  # DOF 4 (index 3 in 0-based indexing)

print(f"Load applied for {len(g)} time steps over {T} seconds")

# Boundary conditions (same as modal analysis)
bc = np.array([
    [1, 0],   # DOF 1 = 0 (fixed base x-direction)
    [2, 0],   # DOF 2 = 0 (fixed base y-direction)
    [3, 0],   # DOF 3 = 0 (fixed base rotation)
    [14, 0]   # DOF 14 = 0 (pinned right end y-direction)
])

# Initial conditions (structure at rest)
a0 = np.zeros(15)   # Initial displacements
da0 = np.zeros(15)  # Initial velocities

# Output parameters
times = np.arange(0.1, 1.1, 0.1)  # Output times [0.1, 0.2, ..., 1.0]
dofs = np.array([4, 11])           # DOFs to monitor (1-based: 4, 11)

# Time integration parameters [dt, T, beta, gamma] for Newmark method
ip = [dt, T, 0.25, 0.5]  # Average acceleration method

print("Initial conditions and parameters set successfully")

# Note: The following would require K and M from exd_beam2_m
# Convert to sparse matrices for efficiency (assuming K, M from previous example)
# k_sparse = sparse.csr_matrix(K)
# m_sparse = sparse.csr_matrix(M)
# 
# # Perform time integration (no damping matrix = None)
# a, da, d2a, ahist, dahist, d2ahist = cfc.step2(
#     k_sparse, None, m_sparse, f, a0, da0, bc, ip, times, dofs
# )
# 
# print("Time integration completed successfully")
# print(f"Response history computed for DOFs {dofs} at {len(times)} time points")

print("\nNote: To execute full time integration, run exd_beam2_m first to generate K and M matrices")
