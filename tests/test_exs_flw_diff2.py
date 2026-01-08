"""
Test script for exs_flw_diff2 example.
Two dimensional diffusion problem for a filter paper of square shape.
"""

import numpy as np
import calfem.core as cfc
import calfem.utils as cfu
import calfem.vis_mpl as cfv

# Element topology matrix (DOFs only, no element numbers)
# Each row represents one quadrilateral element with 4 nodes
edof = np.array([
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
f = np.zeros((15, 1))        # Global source vector (no sources in this problem)
print("Global system initialized with 15 DOFs")

# Element properties and material matrix
ep = [1]                    # Thickness [m]
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
for etopo in edof:  # 8 elements
    K = cfc.assem(etopo, K, Ke)

print("Global conductivity matrix assembled successfully")

# Boundary conditions (prescribed concentrations)

bc_dofs = np.array([1, 2, 3, 4, 7, 10, 13, 14, 15])
bc_values = np.array([0, 0, 0, 0, 0, 0, 0.5e-3, 1e-3, 1e-3])

# Solve for concentrations and boundary fluxes
a, r = cfc.solveq(K, f, bc_dofs, bc_values)
print("Concentrations [kg/m³]:")
print(a)
print("Boundary fluxes [kg/m²/s]:")  
print(r)

# Extract element concentrations
ed = cfc.extract_ed(edof, a)

# Compute element flux vectors for all elements
es = np.zeros((8, 2))  # Store flux vectors for 8 elements
for i in range(8):
    es[i], _ = cfc.flw2qs(ex, ey, ep, D, ed[i])

print("Element flux vectors [kg/m²/s]:")
for i, ees in enumerate(es):
    print(f"Element {i+1}: qx = {ees[0]:.6f}, qy = {ees[1]:.6f}")

# Summary of key results
print("\nConcentration field [×10⁻³ kg/m³]:")
print(f"Pure water boundaries (DOFs 1-4,7,10): 0.000")
print(f"Internal concentrations:")
print(f"  DOF 5: {a[4, 0]*1000:.3f}")
print(f"  DOF 6: {a[5, 0]*1000:.3f}") 
print(f"  DOF 8: {a[7, 0]*1000:.3f}")
print(f"  DOF 9: {a[8, 0]*1000:.3f}")
print(f"  DOF 11: {a[10, 0]*1000:.3f}")
print(f"  DOF 12: {a[11, 0]*1000:.3f}")
print(f"Solution boundaries (DOFs 14,15): 1.000")

# Alternative approach using global coordinates
# Global coordinate matrix and DOF numbering

K = np.zeros((15, 15))
f = np.zeros((15, 1))

coord = np.array([
        [0, 0],
        [0.025, 0],
        [0.05, 0],
        [0, 0.025],
        [0.025, 0.025],
        [0.05, 0.025],
        [0, 0.05],
        [0.025, 0.05],
        [0.05, 0.05],
        [0, 0.075],
        [0.025, 0.075],
        [0.05, 0.075],
        [0, 0.1],
        [0.025, 0.1],
        [0.05, 0.1]
])

dof = np.arange(1, 16).reshape((15, 1))

# ----- Element properties, topology and coordinates -----

ep = np.array([1])
D = np.array([[1, 0], [0, 1]])
edof = np.array(
    [
        [1, 2, 5, 4],
        [2, 3, 6, 5],
        [4, 5, 8, 7],
        [5, 6, 9, 8],
        [7, 8, 11, 10],
        [8, 9, 12, 11],
        [10, 11, 14, 13],
        [11, 12, 15, 14],
    ]
)
ex, ey = cfc.coordxtr(edof, coord, dof)

# ----- Generate FE-mesh -----

# clf; eldraw2(Ex,Ey,[1 3 0],Edof(:,1));
# disp('PRESS ENTER TO CONTINUE'); pause; clf;

# ----- Create and assemble element matrices -----

for i in range(8):
    Ke = cfc.flw2qe(ex[i], ey[i], ep, D)
    K = cfc.assem(edof[i], K, Ke)

# ----- Solve equation system -----

bc_prescr = np.array([1, 2, 3, 4, 7, 10, 13, 14, 15])
bc_val = np.array([0, 0, 0, 0, 0, 0, 0.5e-3, 1e-3, 1e-3])
a, r = cfc.solveq(K, f, bc_prescr, bc_val)

# ----- Compute element flux vector -----

ed = cfc.extractEldisp(edof, a)
es = np.zeros((8, 2))
for i in range(8):
    es[i], Et = cfc.flw2qs(ex[i], ey[i], ep, D, ed[i])

# ----- Draw flux vectors and contourlines -----

cfu.disp_h2("ex")
cfu.disp_array(ex, headers=["x0", "x1", "x2", "x3"])
cfu.disp_h2("ey")
cfu.disp_array(ey, headers=["x0", "x1", "x2", "x3"])
cfu.disp_h2("a")
cfu.disp_array(a)
cfu.disp_h2("ed")
cfu.disp_array(ed, headers=["ed0", "ed1", "ed2", "ed3"])

cfv.eldraw2(ex, ey, [1, 2, 1], range(1, ex.shape[0] + 1))
cfv.eliso2_mpl(ex, ey, ed)
cfv.show_and_wait()
