"""
Test script for exs_flw_temp1 example.
Analysis of one-dimensional heat flow through a wall built up of concrete and thermal insulation.
"""

import numpy as np
import calfem.core as cfc

# Element topology matrix (DOFs only, no element numbers)
Edof = np.array([
    [1, 2],  # Element 1: DOF 1 to DOF 2
    [2, 3],  # Element 2: DOF 2 to DOF 3
    [3, 4],  # Element 3: DOF 3 to DOF 4
    [4, 5],  # Element 4: DOF 4 to DOF 5
    [5, 6]   # Element 5: DOF 5 to DOF 6
])

# Initialize global stiffness matrix and load vector
K = np.zeros((6, 6))
f = np.zeros(6)
f[3] = 10  # Heat source at DOF 4 (index 3 in 0-based indexing)
print("Load vector f:")
print(f)

# Thermal conductance values for each element
ep1 = 25.0    # Element 1: 1/0.04 = 25.0 W/K
ep2 = 24.3    # Element 2: 1.7/0.070 = 24.3 W/K  
ep3 = 0.4     # Element 3: 0.040/0.100 = 0.4 W/K
ep4 = 17.0    # Element 4: 1.7/0.100 = 17.0 W/K
ep5 = 7.7     # Element 5: 1/0.13 = 7.7 W/K

# Compute element stiffness matrices
Ke1 = cfc.spring1e(ep1)
Ke2 = cfc.spring1e(ep2)
Ke3 = cfc.spring1e(ep3)
Ke4 = cfc.spring1e(ep4)
Ke5 = cfc.spring1e(ep5)

# Assemble global stiffness matrix
K = cfc.assem(Edof[0, :], K, Ke1)  # Element 1
K = cfc.assem(Edof[1, :], K, Ke2)  # Element 2
K = cfc.assem(Edof[2, :], K, Ke3)  # Element 3
K = cfc.assem(Edof[3, :], K, Ke4)  # Element 4
K = cfc.assem(Edof[4, :], K, Ke5)  # Element 5

# Boundary conditions: DOF 1 = -17°C, DOF 6 = 20°C

bc_index = np.array([1, 6])  # DOF indices for boundary conditions
bc_value = np.array([-17.0, 20.0])  # Corresponding

# Solve system of equations
a, r = cfc.solveq(K, f, bc_index, bc_value)

print("Temperatures at nodes:")
print(a)

print("Reaction forces (boundary heat flows):")
print(r)

# Extract element displacements (temperature differences)
ed1 = cfc.extract_ed(Edof[0, :], a)  # Element 1
ed2 = cfc.extract_ed(Edof[1, :], a)  # Element 2
ed3 = cfc.extract_ed(Edof[2, :], a)  # Element 3
ed4 = cfc.extract_ed(Edof[3, :], a)  # Element 4
ed5 = cfc.extract_ed(Edof[4, :], a)  # Element 5

# Calculate heat flows through each element
q1 = cfc.spring1s(ep1, ed1)
q2 = cfc.spring1s(ep2, ed2)
q3 = cfc.spring1s(ep3, ed3)
q4 = cfc.spring1s(ep4, ed4)
q5 = cfc.spring1s(ep5, ed5)

print("Heat flows through elements:")
print(f"Element 1: {q1[0]:.1f} W/m²")
print(f"Element 2: {q2[0]:.1f} W/m²")
print(f"Element 3: {q3[0]:.1f} W/m²")
print(f"Element 4: {q4[0]:.1f} W/m²")
print(f"Element 5: {q5[0]:.1f} W/m²")
