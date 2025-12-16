"""
Test script for exs_beam1 example.
Analysis of a simply supported beam.
"""

import numpy as np
import calfem.core as cfc
import matplotlib.pyplot as plt

np.set_printoptions(precision=4, linewidth=120)

# Element topology matrix (DOFs only, no element numbers)
Edof = np.array([
    [1, 2, 3, 4],  # Element 1: DOFs 1,2,3,4 (node 1-2)
    [3, 4, 5, 6]   # Element 2: DOFs 3,4,5,6 (node 2-3)
])

# Initialize global system
K = np.zeros((6, 6))
f = np.zeros((6, 1))
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

bc_dof = np.array([1, 5])
bc_value = np.array([0.0, 0.0])

# Solve the system
a, r = cfc.solveq(K, f, bc_dof, bc_value)
print("Displacements:")
print(a)
print("Reaction forces [N]:")
print(r)

# Extract element displacements
Ed = cfc.extract_ed(Edof, a)

# Compute section forces and internal displacements
# For beam1s, we don't need eq parameter for point loads
es1, edi1, eci1 = cfc.beam1s(ex1, ep, Ed[0], nep=6)
es2, edi2, eci2 = cfc.beam1s(ex2, ep, Ed[1], nep=11)

print("Element 1 section forces [N, Nm]:")
print(es1[:5])  # Show first 5 points
print("Element 2 section forces [N, Nm]:")
print(es2[:5])  # Show first 5 points

# Create position vectors for plotting
x1 = np.linspace(0, 3, len(edi1))
x2 = np.linspace(3, 9, len(edi2))
x_full = np.concatenate(([0], x1, x2, [9]))

# Displacement diagram
plt.figure(1, figsize=(10, 4))
plt.plot([0, 9], [0, 0], 'k-', linewidth=1, alpha=0.5)  # Reference line
disp_full = np.concatenate(([0], edi1[:, 0], edi2[:, 0], [0]))
plt.plot(x_full, disp_full, 'b-', linewidth=2, label='Displacement')
plt.xlabel('Position [m]')
plt.ylabel('Displacement [m]')
plt.title('Displacement Diagram')
plt.grid(True, alpha=0.3)
plt.axis([-1, 10, -0.03, 0.01])
plt.legend()
plt.show()

# Shear force diagram
plt.figure(2, figsize=(10, 4))
plt.plot([0, 9], [0, 0], 'k-', linewidth=1, alpha=0.5)  # Reference line
shear_full = np.concatenate(([0], es1[:, 0], es2[:, 0], [0]))
plt.plot(x_full, shear_full, 'r-', linewidth=2, label='Shear Force')
plt.xlabel('Position [m]')
plt.ylabel('Shear Force [N]')
plt.title('Shear Force Diagram')
plt.grid(True, alpha=0.3)
plt.axis([-1, 10, -8000, 5000])
plt.gca().invert_yaxis()  # Engineering convention
plt.legend()
plt.show()

# Moment diagram
plt.figure(3, figsize=(10, 4))
plt.plot([0, 9], [0, 0], 'k-', linewidth=1, alpha=0.5)  # Reference line
moment_full = np.concatenate(([0], es1[:, 1], es2[:, 1], [0]))
plt.plot(x_full, moment_full, 'g-', linewidth=2, label='Bending Moment')
plt.xlabel('Position [m]')
plt.ylabel('Bending Moment [Nm]')
plt.title('Bending Moment Diagram')
plt.grid(True, alpha=0.3)
plt.axis([-1, 10, -5000, 25000])
plt.gca().invert_yaxis()  # Engineering convention
plt.legend()
plt.show()