from ase.io import read, write
from ase.build import make_supercell
import numpy as np
import random
import os

# Step 1: Load CIF file (4H-SiC hexagonal)
base_structure = read("4H_SiC.cif")

# Step 2: Build 2x2x1 supercell (hexagonal directions)
P = np.diag([2, 2, 1])  # 2×2×1 supercell transformation matrix
supercell = make_supercell(base_structure, P)

# Step 3: Identify Carbon atoms
carbon_indices = [atom.index for atom in supercell if atom.symbol == 'C']

# Step 4: Randomly replace 2 Carbon atoms with Oxygen
o_indices = random.sample(carbon_indices, 2)
for idx in o_indices:
    supercell[idx].symbol = 'O'

# Step 5: Save the modified structure to CIF
output_cif = "SiC_2x2x1_O2_doped.cif"
write(output_cif, supercell)

output_cif  # Return path to saved CIF
