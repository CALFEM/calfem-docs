"""
Test script for exs_bar2 example.
Analysis of a plane truss consisting of three bars.
"""

import numpy as np
import calfem.core as cfc

np.set_printoptions(precision=4, linewidth=120)

# Element topology matrix (DOFs only, no element numbers)  
Edof = np.array([
    [1, 2, 5, 6],  # Element 1: DOFs 1,2,5,6
    [5, 6, 7, 8],  # Element 2: DOFs 5,6,7,8
    [3, 4, 5, 6]   # Element 3: DOFs 3,4,5,6
])

# Initialize global system
K = np.zeros((8, 8))
f = np.zeros((8, 1))
f[5] = -80e3  # Load at DOF 6 (index 5 in 0-based indexing)
print("Load vector:")
print(f)

# Material and geometric properties
E = 2.0e11  # Young's modulus [Pa]
A1 = 6.0e-4   # Cross-sectional area element 1 [m²]
A2 = 3.0e-4   # Cross-sectional area element 2 [m²]  
A3 = 10.0e-4  # Cross-sectional area element 3 [m²]

ep1 = [E, A1]  # Element properties for element 1
ep2 = [E, A2]  # Element properties for element 2
ep3 = [E, A3]  # Element properties for element 3

# Element coordinates [m]
ex1 = np.array([0, 1.6])    # Element 1 x-coordinates
ey1 = np.array([0, 0])      # Element 1 y-coordinates

ex2 = np.array([1.6, 1.6])  # Element 2 x-coordinates  
ey2 = np.array([0, 1.2])    # Element 2 y-coordinates

ex3 = np.array([0, 1.6])    # Element 3 x-coordinates
ey3 = np.array([1.2, 0])    # Element 3 y-coordinates

# Compute element stiffness matrices

Ke1 = cfc.bar2e(ex1, ey1, ep1)
print(Ke1)

Ke2 = cfc.bar2e(ex2, ey2, ep2)  
print(Ke2)

Ke3 = cfc.bar2e(ex3, ey3, ep3)
print(Ke3)

# Assemble global stiffness matrix

K = cfc.assem(Edof[0], K, Ke1)
K = cfc.assem(Edof[1], K, Ke2)
K = cfc.assem(Edof[2], K, Ke3)

print("Global stiffness matrix K:")
print(K)

# Boundary conditions (DOF, prescribed value)

bc_dof = np.array([1, 2, 3, 4, 7, 8])  # DOFs with boundary conditions
bc_value = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

# Solve the system
a, r = cfc.solveq(K, f, bc_dof, bc_value)
print("Displacements [m]:")
print(a)
print("Reaction forces [N]:")
print(r)

# Extract element displacements and compute forces
ed1 = cfc.extract_ed(Edof[0], a)
es1 = cfc.bar2s(ex1, ey1, ep1, ed1)
print(f"Element 1 forces [N]: {es1[0]}")

ed2 = cfc.extract_ed(Edof[1], a) 
es2 = cfc.bar2s(ex2, ey2, ep2, ed2)
print(f"Element 2 forces [N]: {es2[0]}")

ed3 = cfc.extract_ed(Edof[2], a)
es3 = cfc.bar2s(ex3, ey3, ep3, ed3)  
print(f"Element 3 forces [N]: {es3[0]}")
