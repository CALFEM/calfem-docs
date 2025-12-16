"""
Test script for exs_beam2 example
Extracted from exs_beam2.rst documentation
"""

import numpy as np
import matplotlib.pyplot as plt

import calfem.core as cfc
import calfem.vis_mpl as cfv

np.set_printoptions(precision=4, linewidth=120)

# Element topology matrix (DOFs only, no element numbers)
edof = np.array([
    [4, 5, 6, 1, 2, 3], 
    [7, 8, 9, 10, 11, 12], 
    [4, 5, 6, 7, 8, 9]
])

# Initialize global system
K = np.zeros((12, 12))
f = np.zeros((12, 1))
f[3] = 2e3  # Load at DOF 4 (index 3 in 0-based indexing)
print("Load vector:")
print(f)

# Material and geometric properties
E = 200e9        # Young's modulus [Pa]
A1 = 2e-3       # Cross-sectional area for columns [m²]
A2 = 6e-3       # Cross-sectional area for beam [m²]
I1 = 1.6e-5     # Moment of inertia for columns [m⁴]
I2 = 5.4e-5     # Moment of inertia for beam [m⁴]

ep1 = [E, A1, I1]  # Element properties for columns
ep2 = [E, A2, I2]  # Element properties for horizontal beam

# Element coordinates [m]
ex1 = np.array([0, 0])  # Element 1: left column x-coordinates
ex2 = np.array([6, 6])  # Element 2: right column x-coordinates  
ex3 = np.array([0, 6])  # Element 3: horizontal beam x-coordinates
ey1 = np.array([4, 0])  # Element 1: left column y-coordinates
ey2 = np.array([4, 0])  # Element 2: right column y-coordinates
ey3 = np.array([4, 4])  # Element 3: horizontal beam y-coordinates

# Distributed loads (only on horizontal beam)
eq1 = np.array([0, 0])      # No distributed load on left column
eq2 = np.array([0, 0])      # No distributed load on right column  
eq3 = np.array([0, -10e3])  # 10 kN/m downward on horizontal beam

# Compute element stiffness matrices
Ke1 = cfc.beam2e(ex1, ey1, ep1)
Ke2 = cfc.beam2e(ex2, ey2, ep1)  # Same properties as element 1
Ke3, fe3 = cfc.beam2e(ex3, ey3, ep2, eq3)  # With distributed load

# Assemble global stiffness matrix and load vector
K = cfc.assem(edof[0, :], K, Ke1)
K = cfc.assem(edof[1, :], K, Ke2)
K, f = cfc.assem(edof[2, :], K, Ke3, f, fe3)

print("Global system assembled successfully")

# Boundary conditions (fixed supports at base of columns)

bc_dof = np.array([1, 2, 3, 10, 11])
bc_value = np.array([0.0, 0.0, 0.0, 0.0, 0.0])

# Solve the system
a, r = cfc.solveq(K, f, bc_dof, bc_value)
print("Displacements [m, rad]:")
print(a)
print("Reaction forces [N, Nm]:")
print(r)

# Extract element displacements
ed = cfc.extract_ed(edof, a)

# Compute section forces and internal displacements (21 points each)
es1, edi1, ec1 = cfc.beam2s(ex1, ey1, ep1, ed[0, :], eq1, nep=21)
es2, edi2, ec2 = cfc.beam2s(ex2, ey2, ep1, ed[1, :], eq2, nep=21)
es3, edi3, ec3 = cfc.beam2s(ex3, ey3, ep2, ed[2, :], eq3, nep=21)

print("Element 1 (left column) section forces [N, N, Nm]:")
print("N =", es1[0, 0], "V =", es1[0, 1], "M =", es1[0, 2])

print("Element 2 (right column) section forces [N, N, Nm]:")
print("N =", es2[0, 0], "V =", es2[0, 1], "M =", es2[0, 2])

print("Element 3 (horizontal beam) section forces [N, N, Nm]:")
print("N =", es3[0, 0], "V =", es3[0, 1], "M =", es3[0, 2])

# ----- Draw deformed frame ---------------------------------------

plotpar = [2, 1, 0]
sfac = cfv.scalfact2(ex3, ey3, edi3, 0.1)
print("sfac=")
print(sfac)

cfv.figure(1)
cfv.eldraw2(ex1, ey1, plotpar)
cfv.eldraw2(ex2, ey2, plotpar)
cfv.eldraw2(ex3, ey3, plotpar)

plotpar = [1, 2, 1]
cfv.dispbeam2(ex1, ey1, edi1, plotpar, sfac)
cfv.dispbeam2(ex2, ey2, edi2, plotpar, sfac)
cfv.dispbeam2(ex3, ey3, edi3, plotpar, sfac)
cfv.axis([-1.5, 7.5, -0.5, 5.5])
plotpar1 = 2
cfv.scalgraph2(sfac, [1e-2, 0.5, 0], plotpar1)
cfv.title("Displacements")

# ----- Draw normal force diagram --------------------------------

plotpar = [2, 1]
sfac = cfv.scalfact2(ex1, ey1, es1[:, 0], 0.2)
cfv.figure(2)
cfv.secforce2(ex1, ey1, es1[:, 0], plotpar, sfac)
cfv.secforce2(ex2, ey2, es2[:, 0], plotpar, sfac)
cfv.secforce2(ex3, ey3, es3[:, 0], plotpar, sfac)
cfv.axis([-1.5, 7.5, -0.5, 5.5])
cfv.scalgraph2(sfac, [3e4, 1.5, 0], plotpar1)
cfv.title("Normal force")

# ----- Draw shear force diagram ---------------------------------

plotpar = [2, 1]
sfac = cfv.scalfact2(ex3, ey3, es3[:, 1], 0.2)
cfv.figure(3)
cfv.secforce2(ex1, ey1, es1[:, 1], plotpar, sfac)
cfv.secforce2(ex2, ey2, es2[:, 1], plotpar, sfac)
cfv.secforce2(ex3, ey3, es3[:, 1], plotpar, sfac)
cfv.axis([-1.5, 7.5, -0.5, 5.5])
cfv.scalgraph2(sfac, [3e4, 0.5, 0], plotpar1)
cfv.title("Shear force")

# ----- Draw moment diagram --------------------------------------

plotpar = [2, 1]
sfac = cfv.scalfact2(ex3, ey3, es3[:, 2], 0.2)
print("sfac=")
print(sfac)

cfv.figure(4)
cfv.secforce2(ex1, ey1, es1[:, 2], plotpar, sfac)
cfv.secforce2(ex2, ey2, es2[:, 2], plotpar, sfac)
cfv.secforce2(ex3, ey3, es3[:, 2], plotpar, sfac)
cfv.axis([-1.5, 7.5, -0.5, 5.5])
cfv.scalgraph2(sfac, [3e4, 0.5, 0], plotpar1)
cfv.title("Moment")

cfv.show_and_wait()