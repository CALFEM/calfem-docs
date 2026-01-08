"""
Test script for exs_beambar2 example.
Analysis of a combined beam and bar structure.
"""

import numpy as np
import calfem.core as cfc
import calfem.utils as cfu

# Element topology matrices (DOFs only, no element numbers)
# Beam elements (6 DOFs per element: 2 nodes × 3 DOFs/node)
edof1 = np.array([
    [1, 2, 3, 4, 5, 6],     # Beam element 1: nodes 1-2
    [4, 5, 6, 7, 8, 9],     # Beam element 2: nodes 2-3  
    [7, 8, 9, 10, 11, 12]   # Beam element 3: nodes 3-4
])

# Bar elements (4 DOFs per element: 2 nodes × 2 DOFs/node)
edof2 = np.array([
    [13, 14, 4, 5],   # Bar element 1: node 5 to node 2
    [13, 14, 7, 8]    # Bar element 2: node 5 to node 3
])

# Initialize global system (14 DOFs total)
K = np.zeros((14, 14))
f = np.zeros((14, 1))
print("Global system initialized with 14 DOFs")

# Material and geometric properties
E = 200e9        # Young's modulus [Pa]
A1 = 4.0e-3      # Cross-sectional area for beam [m²]
A2 = 1.0e-3      # Cross-sectional area for bars [m²]
I1 = 5.4e-5      # Moment of inertia for beam [m⁴]

ep1 = [E, A1, I1]  # Element properties for beam elements
ep2 = [E, A2]      # Element properties for bar elements

# Distributed loads
eq1 = np.array([0, 0])        # No distributed load
eq2 = np.array([0, -10e3])    # 10 kN/m downward distributed load

# Element coordinates [m]
# Beam elements (horizontal at y = 2m)
ex1 = np.array([0, 2])  # Beam element 1: x-coordinates
ey1 = np.array([2, 2])  # Beam element 1: y-coordinates

ex2 = np.array([2, 4])  # Beam element 2: x-coordinates  
ey2 = np.array([2, 2])  # Beam element 2: y-coordinates

ex3 = np.array([4, 6])  # Beam element 3: x-coordinates
ey3 = np.array([2, 2])  # Beam element 3: y-coordinates

# Bar elements (supporting bars)
ex4 = np.array([0, 2])  # Bar element 1: x-coordinates
ey4 = np.array([0, 2])  # Bar element 1: y-coordinates

ex5 = np.array([0, 4])  # Bar element 2: x-coordinates
ey5 = np.array([0, 2])  # Bar element 2: y-coordinates

# Compute beam element stiffness matrices and load vectors
Ke1 = cfc.beam2e(ex1, ey1, ep1)  # No distributed load
Ke2, fe2 = cfc.beam2e(ex2, ey2, ep1, eq2)  # With distributed load
Ke3, fe3 = cfc.beam2e(ex3, ey3, ep1, eq2)  # With distributed load

# Compute bar element stiffness matrices  
Ke4 = cfc.bar2e(ex4, ey4, ep2)
Ke5 = cfc.bar2e(ex5, ey5, ep2)

print("Element stiffness matrices computed successfully")

# Assemble beam elements
K = cfc.assem(edof1[0, :], K, Ke1)
K, f = cfc.assem(edof1[1, :], K, Ke2, f, fe2)
K, f = cfc.assem(edof1[2, :], K, Ke3, f, fe3)
K = cfc.assem(edof2[0, :], K, Ke4)
K = cfc.assem(edof2[1, :], K, Ke5)

# Assemble bar elements
K = cfc.assem(edof2[0], K, Ke4)              # Bar element 1
K = cfc.assem(edof2[1], K, Ke5)              # Bar element 2

print("Global system assembled successfully")

# Boundary conditions (fixed supports)
bc = np.array([1, 2, 3, 13, 14])

# Solve the system
a, r = cfc.solveq(K, f, bc)

print("Displacements [m, rad]:")
print(a)
print("Reaction forces [N, Nm]:")
print(r)

print(f"Maximum vertical displacement: {abs(a[10, 0]):.3f} m = {abs(a[10, 0])*1000:.1f} mm")

# Extract element displacements
ed1 = cfc.extract_ed(edof1, a)  # Beam element displacements
ed2 = cfc.extract_ed(edof2, a)  # Bar element displacements

# Compute section forces for beam elements (11 points each)
es1, _, _ = cfc.beam2s(ex1, ey1, ep1, ed1[0], eq1, nep=11)
es2, _, _ = cfc.beam2s(ex2, ey2, ep1, ed1[1], eq2, nep=11) 
es3, _, _ = cfc.beam2s(ex3, ey3, ep1, ed1[2], eq2, nep=11)

# Compute section forces for bar elements
es4, _, _ = cfc.bar2s(ex4, ey4, ep2, ed2[0], nep=11)
es5, _, _ = cfc.bar2s(ex5, ey5, ep2, ed2[1], nep=11)

cfu.disp_h2("es1 = ")
cfu.disp_array(es1, headers=["N", "V", "M"])
cfu.disp_h2("es2 = ")
cfu.disp_array(es2, headers=["N", "V", "M"])
cfu.disp_h2("es3 = ")
cfu.disp_array(es3, headers=["N", "V", "M"])
cfu.disp_h2("es4 = ")
cfu.disp_array(es4, headers=["N"])
cfu.disp_h2("es5 = ")
cfu.disp_array(es5, headers=["N"])
