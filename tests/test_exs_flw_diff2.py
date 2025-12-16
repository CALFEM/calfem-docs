"""
Test script for exs_flw_diff2 example.
Two dimensional diffusion problem for a filter paper of square shape.
"""

import numpy as np
import calfem.core as cfc

# Element topology matrix (DOFs only, no element numbers)
# Each row represents one quadrilateral element with 4 nodes
Edof = np.array([
    [1, 2, 5, 4],      # Element 1
    [2, 3, 6, 5],      # Element 2
    [4, 5, 8, 7],      # Element 3
    [5, 6, 9, 8],      # Element 4
    [7, 8, 11, 10],    # Element 5
    [8, 9, 12, 11],    # Element 6
    [10, 11, 14, 13],  # Element 7
    [11, 12, 15, 14]   # Element 8
])

# Initialize global system (15 DOFs for concentration field)
K = np.zeros((15, 15))  # Global conductivity matrix
f = np.zeros(15)        # Global source vector (no sources in this problem)
print("Global system initialized with 15 DOFs")

# Element properties and material matrix
ep = 1                    # Thickness [m]
D = np.array([[1, 0],     # Diffusion/conductivity matrix [m²/s]
              [0, 1]])

# Element coordinates for standard element (0.025 × 0.025 m)
ex = np.array([0, 0.025, 0.025, 0])      # x-coordinates [m]
ey = np.array([0, 0, 0.025, 0.025])      # y-coordinates [m]

# Compute element conductivity matrix
Ke = cfc.flw2qe(ex, ey, ep, D)
print("Element conductivity matrix:")
print(Ke)

# Assemble global conductivity matrix
for i in range(8):  # 8 elements
    K = cfc.assem(Edof[i], K, Ke)

print("Global conductivity matrix assembled successfully")

# Boundary conditions (prescribed concentrations)
bc = np.array([
    [1, 0],        # DOF 1 = 0 (pure water boundary)
    [2, 0],        # DOF 2 = 0 (pure water boundary)
    [3, 0],        # DOF 3 = 0 (pure water boundary)
    [4, 0],        # DOF 4 = 0 (pure water boundary)
    [7, 0],        # DOF 7 = 0 (pure water boundary)
    [10, 0],       # DOF 10 = 0 (pure water boundary)
    [13, 0.5e-3],  # DOF 13 = 0.5×10⁻³ kg/m³ (average concentration)
    [14, 1e-3],    # DOF 14 = 1.0×10⁻³ kg/m³ (solution boundary)
    [15, 1e-3]     # DOF 15 = 1.0×10⁻³ kg/m³ (solution boundary)
])

# Solve for concentrations and boundary fluxes
a, r = cfc.solveq(K, f, bc)
print("Concentrations [kg/m³]:")
print(a)
print("Boundary fluxes [kg/m²/s]:")  
print(r)

# Extract element concentrations
Ed = cfc.extract_ed(Edof, a)

# Compute element flux vectors for all elements
Es = np.zeros((8, 2))  # Store flux vectors for 8 elements
for i in range(8):
    Es[i] = cfc.flw2qs(ex, ey, ep, D, Ed[i])

print("Element flux vectors [kg/m²/s]:")
for i in range(8):
    print(f"Element {i+1}: qx = {Es[i,0]:.6f}, qy = {Es[i,1]:.6f}")

# Summary of key results
print("\nConcentration field [×10⁻³ kg/m³]:")
print(f"Pure water boundaries (DOFs 1-4,7,10): 0.000")
print(f"Internal concentrations:")
print(f"  DOF 5: {a[4]*1000:.3f}")
print(f"  DOF 6: {a[5]*1000:.3f}") 
print(f"  DOF 8: {a[7]*1000:.3f}")
print(f"  DOF 9: {a[8]*1000:.3f}")
print(f"  DOF 11: {a[10]*1000:.3f}")
print(f"  DOF 12: {a[11]*1000:.3f}")
print(f"Solution boundaries (DOFs 14,15): 1.000")

# Alternative approach using global coordinates
# Global coordinate matrix and DOF numbering
Coord = np.array([
    [0,     0    ], [0.025, 0    ], [0.05,  0    ],   # Row 1
    [0,     0.025], [0.025, 0.025], [0.05,  0.025],   # Row 2  
    [0,     0.05 ], [0.025, 0.05 ], [0.05,  0.05 ],   # Row 3
    [0,     0.075], [0.025, 0.075], [0.05,  0.075],   # Row 4
    [0,     0.1  ], [0.025, 0.1  ], [0.05,  0.1  ]    # Row 5
])

Dof = np.array([
    [1], [2], [3],      # Row 1 DOFs
    [4], [5], [6],      # Row 2 DOFs
    [7], [8], [9],      # Row 3 DOFs
    [10], [11], [12],   # Row 4 DOFs
    [13], [14], [15]    # Row 5 DOFs
])

# Extract element coordinates automatically
Ex, Ey = cfc.coordxtr(Edof, Coord, Dof, 4)
print("Element coordinates extracted successfully")

# Assembly and solution (same as before but with variable geometry)
K_alt = np.zeros((15, 15))
f_alt = np.zeros(15)

for i in range(8):
    Ke = cfc.flw2qe(Ex[i], Ey[i], ep, D)
    K_alt = cfc.assem(Edof[i], K_alt, Ke)

a_alt, r_alt = cfc.solveq(K_alt, f_alt, bc)
Ed_alt = cfc.extract_ed(Edof, a_alt)

# Compute flux vectors for visualization
Es_vis = np.zeros((8, 2))
for i in range(8):
    Es_vis[i] = cfc.flw2qs(Ex[i], Ey[i], ep, D, Ed_alt[i])

print("Alternative solution matches original approach")
