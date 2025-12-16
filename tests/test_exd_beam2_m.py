"""
Test script for exd_beam2_m example.
Eigenvalue analysis for a simple 2D frame structure.
"""

import numpy as np
import calfem.core as cfc

# Material data
E = 3e10        # Young's modulus [N/m²]
rho = 2500      # Density [kg/m³]

# Vertical beam properties (IPE100)
Av = 0.1030e-2   # Cross-sectional area [m²]
Iv = 0.0171e-4   # Moment of inertia [m⁴]
epv = [E, Av, Iv, rho*Av]  # Element properties for vertical beam

# Horizontal beam properties (IPE80)
Ah = 0.0764e-2   # Cross-sectional area [m²]  
Ih = 0.00801e-4  # Moment of inertia [m⁴]
eph = [E, Ah, Ih, rho*Ah]  # Element properties for horizontal beam

print("Material properties defined successfully")

# Element topology matrix (DOFs only, no element numbers)
Edof = np.array([
    [1, 2, 3, 4, 5, 6],      # Element 1: vertical beam lower
    [4, 5, 6, 7, 8, 9],      # Element 2: vertical beam upper
    [7, 8, 9, 10, 11, 12],   # Element 3: horizontal beam left
    [10, 11, 12, 13, 14, 15] # Element 4: horizontal beam right
])

# Global coordinate matrix [m]
Coord = np.array([
    [0, 0],     # Node 1: base of vertical beam
    [0, 1.5],   # Node 2: mid vertical beam
    [0, 3],     # Node 3: top of vertical beam / left end of horizontal
    [1, 3],     # Node 4: mid horizontal beam
    [2, 3]      # Node 5: right end of horizontal beam
])

# Degrees of freedom numbering
Dof = np.array([
    [1, 2, 3],     # Node 1 DOFs
    [4, 5, 6],     # Node 2 DOFs
    [7, 8, 9],     # Node 3 DOFs
    [10, 11, 12],  # Node 4 DOFs
    [13, 14, 15]   # Node 5 DOFs
])

# Initialize global matrices
K = np.zeros((15, 15))  # Global stiffness matrix
M = np.zeros((15, 15))  # Global mass matrix

# Extract element coordinates
Ex, Ey = cfc.coordxtr(Edof, Coord, Dof, 2)

# Assemble vertical beam elements (elements 1-2) with epv properties
for i in range(2):  # Elements 1 and 2 (vertical beam)
    k, m, c = cfc.beam2de(Ex[i], Ey[i], epv)
    K = cfc.assem(Edof[i], K, k)
    M = cfc.assem(Edof[i], M, m)

# Assemble horizontal beam elements (elements 3-4) with eph properties  
for i in range(2, 4):  # Elements 3 and 4 (horizontal beam)
    k, m, c = cfc.beam2de(Ex[i], Ey[i], eph)
    K = cfc.assem(Edof[i], K, k)
    M = cfc.assem(Edof[i], M, m)

print("Global stiffness and mass matrices assembled successfully")

# Boundary conditions (constrained DOFs)
b = np.array([1, 2, 3, 14])  # Fixed base and pinned right end

# Perform eigenvalue analysis
La, Egv = cfc.eigen(K, M, b)

# Calculate natural frequencies in Hz
Freq = np.sqrt(La) / (2 * np.pi)

print("Natural frequencies [Hz]:")
for i, f in enumerate(Freq):
    print(f"Mode {i+1}: {f:.4f} Hz")

# Extract first eigenmode for display
Edb = cfc.extract_ed(Edof, Egv[:, 0])  # First mode (index 0)
print(f"\nFirst eigenmode frequency: {Freq[0]:.2f} Hz")
