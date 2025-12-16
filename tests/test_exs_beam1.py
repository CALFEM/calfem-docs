"""
Test script for exs_beam1 example.
Analysis of a simply supported beam.
"""

import numpy as np
import calfem.core as cfc

# Element topology matrix (DOFs only, no element numbers)
Edof = np.array([
    [1, 2, 3, 4],  # Element 1: DOFs 1,2,3,4 (node 1-2)
    [3, 4, 5, 6]   # Element 2: DOFs 3,4,5,6 (node 2-3)
])

# Initialize global system
K = np.zeros((6, 6))
f = np.zeros(6)
f[2] = -10000  # Load at DOF 3 (index 2 in 0-based indexing)
print("Load vector:")
print(f)

# Material and geometric properties
E = 210e9      # Young's modulus [Pa]
I = 2510e-8    # Moment of inertia [m⁴]
ep = [E, I]    # Element properties

# Element coordinates [m]
ex1 = np.array([0, 3])  # Element 1: from x=0 to x=3
ex2 = np.array([3, 9])  # Element 2: from x=3 to x=9

# Compute element stiffness matrices
Ke1 = cfc.beam1e(ex1, ep)
print("Element 1 stiffness matrix:")
print(Ke1)

Ke2 = cfc.beam1e(ex2, ep)
print("Element 2 stiffness matrix:")
print(Ke2)

# Assemble global stiffness matrix
K = cfc.assem(Edof[0], K, Ke1)
K = cfc.assem(Edof[1], K, Ke2)
print("Global stiffness matrix assembled successfully")

# Boundary conditions (simply supported beam)
bc = np.array([
    [1, 0],  # DOF 1 = 0 (vertical displacement at left support)
    [5, 0]   # DOF 5 = 0 (vertical displacement at right support)
])

# Solve the system
a, r = cfc.solveq(K, f, bc)
print("Displacements:")
print(a)
print("Reaction forces [N]:")
print(r)

# Extract element displacements
Ed = cfc.extract_ed(Edof, a)

# Compute section forces and internal displacements
# For beam1s, we don't need eq parameter for point loads
es1, edi1 = cfc.beam1s(ex1, ep, Ed[0], n_points=6)
es2, edi2 = cfc.beam1s(ex2, ep, Ed[1], n_points=11)

print("Element 1 section forces [N, Nm]:")
print(es1[:5])  # Show first 5 points
print("Element 2 section forces [N, Nm]:")
print(es2[:5])  # Show first 5 points
