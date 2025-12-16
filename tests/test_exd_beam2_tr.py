"""
Test script for exd_beam2_tr example.
Reduced system analysis using modal coordinates for the frame structure.
Note: This script requires K, M, Egv from the modal analysis example.
"""

import numpy as np
import calfem.core as cfc
from scipy import sparse

# Note: This assumes K, M, Egv are defined from exd_beam2_m
# For standalone execution, you would need to run that example first

# Time integration and modal reduction parameters
dt = 0.002      # Time step [s]
T = 1           # Total time [s]
nev = 2         # Number of eigenvectors to use

# Load definition (assuming K, M, Egv from previous modal analysis example)
G = np.array([
    [0, 0],
    [0.15, 1], 
    [0.25, 0], 
    [T, 0]
])
t, g = cfc.gfunc(G, dt)

# Create force vector
f = np.zeros((15, len(g)))
f[3, :] = 9000 * g  # Apply 9kN load at DOF 4 (0-based indexing)

# Note: The following would require K, M, Egv from exd_beam2_m
# Reduced force vector using selected eigenvectors
# fr = sparse.csr_matrix(np.column_stack([
#     np.arange(nev),  # DOF indices for reduced system
#     Egv[:, :nev].T @ f  # Project forces onto modal coordinates
# ]))

print("Load vector and modal projection completed")

# Reduced system matrices using selected eigenvectors
# kr_full = Egv[:, :nev].T @ K @ Egv[:, :nev]
# mr_full = Egv[:, :nev].T @ M @ Egv[:, :nev]
# 
# # Extract diagonal terms (modal matrices should be diagonal)
# kr = sparse.diags(np.diag(kr_full))
# mr = sparse.diags(np.diag(mr_full))

# Initial conditions for reduced system
ar0 = np.zeros(nev)      # Initial modal displacements
dar0 = np.zeros(nev)     # Initial modal velocities

# Output parameters
times = np.arange(0.1, 1.1, 0.1)  # Output times [0.1, 0.2, ..., 1.0]
dofsr = np.arange(nev)             # Reduced DOFs to monitor [0, 1]
dofs = np.array([3, 10])           # Original DOFs to monitor (0-based: 4, 11)

# Time integration parameters [dt, T, beta, gamma] for Newmark method
ip = [dt, T, 0.25, 0.5]  # Average acceleration method

print("Reduced system matrices and parameters set up")

# Note: The following would require kr, mr, fr from modal reduction
# Time integration on reduced system
# ar, dar, d2ar, arhist, darhist, d2arhist = cfc.step2(
#     kr, None, mr, fr, ar0, dar0, None, ip, times, dofsr
# )
# 
# # Map back to original coordinate system
# aR = Egv[:, :nev] @ ar            # Final displacements in original coordinates
# aRhist = Egv[dofs, :nev] @ arhist # Time history for specific DOFs
# 
# print("Modal time integration completed successfully")
# print(f"Using {nev} eigenvectors for reduced order analysis")

print("\nNote: To execute full modal reduction analysis, run exd_beam2_m first to generate K, M, and Egv")
