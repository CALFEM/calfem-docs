"""
Test script for exs_bar2_l example.
Analysis of a plane truss with ten elements.
"""

import numpy as np
import calfem.core as cfc

# Element topology matrix (DOFs only, no element numbers)
Edof = np.array([
    [1, 2, 5, 6],    # Element 1: DOFs 1,2,5,6
    [3, 4, 7, 8],    # Element 2: DOFs 3,4,7,8  
    [5, 6, 9, 10],   # Element 3: DOFs 5,6,9,10
    [7, 8, 11, 12],  # Element 4: DOFs 7,8,11,12
    [7, 8, 5, 6],    # Element 5: DOFs 7,8,5,6
    [11, 12, 9, 10], # Element 6: DOFs 11,12,9,10
    [3, 4, 5, 6],    # Element 7: DOFs 3,4,5,6
    [7, 8, 9, 10],   # Element 8: DOFs 7,8,9,10
    [1, 2, 7, 8],    # Element 9: DOFs 1,2,7,8
    [5, 6, 11, 12]   # Element 10: DOFs 5,6,11,12
])

# Initialize global system  
K = np.zeros((12, 12))
f = np.zeros(12)

# Apply load P=0.5 MN at 30° angle (DOFs 11,12 -> indices 10,11)
P = 0.5e6  # Load magnitude [N]
f[10] = P * np.sin(np.pi/6)   # x-component at DOF 11
f[11] = -P * np.cos(np.pi/6)  # y-component at DOF 12
print("Load vector:")
print(f)

# Material and geometric properties
A = 25.0e-4   # Cross-sectional area [m²]
E = 2.1e11    # Young's modulus [Pa]
ep = [E, A]   # Element properties

# Element coordinate matrices (x-coordinates for each element)
Ex = np.array([
    [0, 2],  # Element 1
    [0, 2],  # Element 2
    [2, 4],  # Element 3
    [2, 4],  # Element 4
    [2, 2],  # Element 5
    [4, 4],  # Element 6
    [0, 2],  # Element 7
    [2, 4],  # Element 8
    [0, 2],  # Element 9
    [2, 4]   # Element 10
])

# Element coordinate matrices (y-coordinates for each element)
Ey = np.array([
    [2, 2],  # Element 1
    [0, 0],  # Element 2
    [2, 2],  # Element 3
    [0, 0],  # Element 4
    [0, 2],  # Element 5
    [0, 2],  # Element 6
    [0, 2],  # Element 7
    [0, 2],  # Element 8
    [2, 0],  # Element 9
    [2, 0]   # Element 10
])

# Compute element stiffness matrices and assemble
for i in range(10):
    Ke = cfc.bar2e(Ex[i], Ey[i], ep)
    K = cfc.assem(Edof[i], K, Ke)

print("Global stiffness matrix assembled successfully")

# Boundary conditions (fixed supports at nodes 1 and 2)
bc = np.array([
    [1, 0],  # DOF 1 = 0 (fixed in x)
    [2, 0],  # DOF 2 = 0 (fixed in y)
    [3, 0],  # DOF 3 = 0 (fixed in x) 
    [4, 0]   # DOF 4 = 0 (fixed in y)
])

# Solve the system
a, r = cfc.solveq(K, f, bc)
print("Displacements [m]:")
print(a)
print("Reaction forces [N]:")
print(r)

# Extract element displacements
ed = cfc.extract_ed(Edof, a)

# Compute normal forces for all elements
N = np.zeros(10)
for i in range(10):
    es = cfc.bar2s(Ex[i], Ey[i], ep, ed[i])
    N[i] = es[0]  # Normal force (first component)

print("Normal forces [N]:")
print(N)

# Alternative approach using global coordinates and topology
Coord = np.array([
    [0, 2],  # Node 1
    [0, 0],  # Node 2  
    [2, 2],  # Node 3
    [2, 0],  # Node 4
    [4, 2],  # Node 5
    [4, 0]   # Node 6
])

Dof = np.array([
    [1, 2],    # Node 1: DOFs 1,2
    [3, 4],    # Node 2: DOFs 3,4
    [5, 6],    # Node 3: DOFs 5,6
    [7, 8],    # Node 4: DOFs 7,8
    [9, 10],   # Node 5: DOFs 9,10
    [11, 12]   # Node 6: DOFs 11,12
])

# Extract element coordinates automatically
ex, ey = cfc.coordxtr(Edof, Coord, Dof, 2)
print("Extracted element coordinates match manual definition")
