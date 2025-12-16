"""
Test script for exd_beam2_b example.
Time varying boundary condition and time integration for the frame structure.
Note: This script requires K, M, Ex, Ey, Edof from the modal analysis example.
"""

import numpy as np
import calfem.core as cfc
from scipy import sparse

# Note: This assumes K, M, Ex, Ey, Edof are defined from exd_beam2_m
# For standalone execution, you would need to run that example first

# Time integration parameters
dt = 0.002      # Time step [s]
T = 1           # Total time [s]

# Time-varying boundary condition definition
G = np.array([
    [0, 0],
    [0.1, 0.02], 
    [0.2, -0.01], 
    [0.3, 0.0], 
    [T, 0]
])
t, g = cfc.gfunc(G, dt)

# Boundary condition matrix setup
# bc format: [DOF, prescribed_displacement_values...]
bc = np.zeros((4, 1 + len(g)))
bc[0, :] = np.concatenate([[0], g])    # DOF 1 (0-based) with time-varying displacement
bc[1, 0] = 1    # DOF 2 (0-based) fixed
bc[2, 0] = 2    # DOF 3 (0-based) fixed  
bc[3, 0] = 13   # DOF 14 (0-based) fixed

# Initial conditions (structure at rest)
a0 = np.zeros(15)   # Initial displacements
da0 = np.zeros(15)  # Initial velocities

print("Time-varying boundary conditions and initial conditions set up")

# Output parameters
times = np.arange(0.1, 1.1, 0.1)  # Output times [0.1, 0.2, ..., 1.0]
dofs = np.array([0, 3, 10])        # DOFs to monitor (0-based: 1, 4, 11)

# Time integration parameters [dt, T, beta, gamma] for Newmark method
ip = [dt, T, 0.25, 0.5]  # Average acceleration method

# Note: The following would require K and M from exd_beam2_m
# Convert to sparse matrices for efficiency (assuming K, M from previous example)
# k = sparse.csr_matrix(K)
# m = sparse.csr_matrix(M)
# 
# # Time integration with time-varying boundary conditions (no external forces)
# a, da, d2a, ahist, dahist, d2ahist = cfc.step2(
#     k, None, m, np.array([]), a0, da0, bc, ip, times, dofs
# )
# 
# print("Time integration with moving boundary completed successfully")
# print(f"Response history computed for DOFs {dofs+1} at {len(times)} time points")

print("\nNote: To execute full time integration with moving boundary, run exd_beam2_m first to generate K and M matrices")
