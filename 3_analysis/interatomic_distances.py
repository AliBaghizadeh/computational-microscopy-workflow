from ase.io import read
from scipy.spatial.distance import pdist, squareform
import numpy as np

atoms = read('relaxed_positions_only.cif')
positions = [atom.position for atom in atoms if atom.symbol == 'Si']
dist_matrix = squareform(pdist(positions))

# Print nearest distances
for i in range(len(positions)):
    closest = np.partition(dist_matrix[i], 1)[1]  # exclude self (0.0)
    print(f'Si atom {i}: nearest neighbor = {closest:.3f} Å')