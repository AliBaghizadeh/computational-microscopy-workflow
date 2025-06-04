from ase.io import read
from gpaw import GPAW
import random
import pickle
import numpy as np
from gpaw.mpi import world

# Read doped supercell
atoms = read('SiC_2x2x1_O2_doped.cif')

# Log dopant info
c_indices = [atom.index for atom in atoms if atom.symbol == 'C']
o_indices = [atom.index for atom in atoms if atom.symbol == 'O']
print(f"Remaining Carbon atoms: {len(c_indices)}, Doped Oxygen atoms: {len(o_indices)}")

# Static SCF calculation
calc = GPAW(
    mode='lcao',
    basis='dzp',
    xc='PBE',
    kpts=(1, 1, 1),
    convergence={'energy': 1e-5, 'density': 1e-3, 'eigenstates': 1e-8},
    txt='scf_log.txt'
)

atoms.calc = calc
energy = atoms.get_potential_energy()
print("SCF energy:", energy)
print("SCF steps:", calc.get_number_of_iterations())

calc.write('preconverged.gpw')
