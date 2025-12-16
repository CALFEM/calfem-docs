"""
Test script for exs_spring example.
Demonstrates the basic steps in a finite element calculation using a system of three linear elastic springs.
"""

import numpy as np
import calfem.core as cfc

# Element topology matrix (no element numbers, just DOFs)
Edof = np.array([
    [1, 2],  # Element 1: DOF 1 to DOF 2
    [2, 3],  # Element 2: DOF 2 to DOF 3  
    [2, 3]   # Element 3: DOF 2 to DOF 3
])

K = np.zeros((3,3))
f = np.zeros((3,1))
print(K)
print(f)

f[1] = 100.0  # Load at DOF 2 (index 1 in 0-based indexing)
print(f)

k = 1500
ep1 = k      # Spring stiffness for elements 2
ep2 = 2 * k  # Spring stiffness for elements 1 and 3

Ke1 = cfc.spring1e(ep1)
print("Ke1 (k=1500):")
print(Ke1)

Ke2 = cfc.spring1e(ep2)
print("Ke2 (k=3000):")
print(Ke2)

# Assemble element 1 (uses Ke2 with stiffness 3000)
K = cfc.assem(Edof[0, :], K, Ke2)
print("After assembling element 1:")
print(K)

# Assemble element 2 (uses Ke1 with stiffness 1500)
K = cfc.assem(Edof[1, :], K, Ke1)
print("After assembling element 2:")
print(K)

# Assemble element 3 (uses Ke2 with stiffness 3000)
K = cfc.assem(Edof[2, :], K, Ke2)
print("After assembling element 3:")
print(K)

bc_index = np.array([1, 3])
bc_value = np.array([0.0, 0.0])
a, r = cfc.solveq(K, f, bc_index, bc_value)
print("Displacements:")
print(a)
print("Reaction forces:")
print(r)

# Extract displacements for each element
ed1 = cfc.extract_ed(Edof[0, :], a)  # Element 1
ed2 = cfc.extract_ed(Edof[1, :], a)  # Element 2  
ed3 = cfc.extract_ed(Edof[2, :], a)  # Element 3

print("Element displacements:")
print("Element 1:", ed1)
print("Element 2:", ed2)
print("Element 3:", ed3)

# Calculate element forces
es1 = cfc.spring1s(ep2, ed1)  # Element 1 uses ep2 (3000)
es2 = cfc.spring1s(ep1, ed2)  # Element 2 uses ep1 (1500)
es3 = cfc.spring1s(ep2, ed3)  # Element 3 uses ep2 (3000)

print("Spring forces:")
print("Element 1 force:", es1)
print("Element 2 force:", es2) 
print("Element 3 force:", es3)
