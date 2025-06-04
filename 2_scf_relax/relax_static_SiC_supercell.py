from ase.optimize import BFGS
from ase.io import write
from gpaw import restart
from gpaw.mpi import world
import numpy as np
import os

# Load from preconverged wavefunction
atoms, calc = restart('preconverged.gpw', txt='relax_log.txt')
atoms.calc = calc
atoms.wrap()

# Run optimization (with restart ability)
opt = BFGS(atoms, logfile='bfgs.log', trajectory='relax.traj', restart='bfgs.pckl')
opt.run(fmax=0.05, steps=50)

# Always compute energy and forces after relaxation
energy = atoms.get_potential_energy()
fmax = np.max(np.linalg.norm(atoms.get_forces(), axis=1))

# Only let rank 0 handle file writing
if world.rank == 0:
    print(f"\nFinal Energy: {energy:.6f} eV")
    print(f"Final max force: {fmax:.6f} eV/Å")

    if fmax < 0.05:
        print("✅ Converged: Saving relaxed structure and wavefunction.")
        calc.write('relaxed.gpw', mode='all')
        write('relaxed_positions_only.cif', atoms, format='cif', write_params={'sort': False})
        os.sync()
    else:
        print("⚠️ Not converged. Skipping save to avoid writing partial data.")
