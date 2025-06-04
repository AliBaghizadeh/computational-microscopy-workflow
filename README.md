# Oxygen Diffusion in 4H-SiC via DFT and STEM Simulation

This project demonstrates how to model and simulate oxygen diffusion in 4H-SiC using **Computational Materials (with GPAW/ASE)** and simulate corresponding **atomic resolution STEM images using abTEM**.
The choice of oxygen diffusion in 4H-SiC is solely for semiconductor metrology, but the workflow can be used for many other materials. 

It is designed for educational use by junior researchers, and runs on:
- **Linux / WSL2 on Windows**
- **Google Colab (for abTEM image simulation)**

## 📊 Workflow Overview

1. **Build Supercell**: Start from a 4H-SiC CIF file and build a 2×2×1 supercell. Randomly replace two carbon atoms with oxygen atoms to simulate diffusion.  
   🔹 *Note:* The supercell size is critical. It depends on the intended zone axis for STEM simulation, the symmetry of the 4H-SiC lattice, and your available computational resources.

2. **Static SCF Calculation**: Perform a static self-consistent field (SCF) calculation using GPAW to pre-converge the charge density and wavefunctions.  
   🔹 *This step prepares the structure for faster relaxation by generating a `.gpw` file that includes preconverged states.*

3. **Geometry Relaxation**: Using the SCF results, relax atomic positions via force minimization (using BFGS optimizer).  
   🔹 *Note:* This is a simplified relaxation workflow. It does **not** optimize the unit cell dimensions or k-point mesh, and is **not intended** for high-accuracy total energy or band structure calculations. It's mainly designed to generate realistic atomic coordinates for image simulation.  
   🔹 For more accurate simulations, consult the [GPAW documentation](https://wiki.fysik.dtu.dk/gpaw/) and adjust cutoff energies, `kpts`, convergence thresholds, and relaxation strategies accordingly.

4. **Save Relaxed Structure**: After relaxation, the script automatically checks convergence and exports the relaxed atomic coordinates to `relaxed_positions_only.cif`.  
   🔹 *This file will be used in the STEM image simulation step.*

5. **Distance Analysis**: Analyze Si–Si interatomic distances using a simple script.  
   🔹 This helps verify that relaxation did not produce unphysical configurations.  
   🔹 You can extend this analysis to measure bond lengths, angular distortions, or compare pre/post-relaxation structures.

6. **Export to STEM Simulation**: Upload the relaxed CIF to Google Colab and open the abTEM simulation notebook.  
   🔹 In the notebook, align the structure along a chosen zone axis, expand it if necessary, and prepare it for image simulation.

7. **STEM Simulation (abTEM)**: Simulate ABF, MAADF, and HAADF contrast using abTEM in Colab.  
   abTEM supports two main approaches:  
   - **Flexible 4D-STEM Simulation**: Generates full diffraction patterns at each scan position and allows post-hoc integration over detector angles.  
   - **Direct STEM Simulation**: Uses pre-defined annular detectors for ABF or HAADF, suitable for fast, publication-ready images.  
   🔹 This notebook is GPU-accelerated using CuPy and runs efficiently in Colab.

---

## 🧰 Environment Setup

You must use Linux or WSL2 (Windows Subsystem for Linux). See [`setup/install_wsl_conda.md`](./setup/install_wsl_conda.md).

### Create Conda Environment

```bash
conda env create -f environment.yml
conda activate sic-dft
```

---

## ▶️ How to Run

### 1. Create Supercell

```bash
cd 1_structure
python create_SiC_222.py
```

### 2. Static and Relaxation Calculation

```bash
cd ../2_scf_relax
python static_SiC_222.py
python relax_static_SiC.py
```

### 3. Analyze Interatomic Distances

```bash
cd ../3_analysis
python interatomic_distances.py
```

### 📸 4. STEM Simulation in Google Colab

You can simulate STEM images using **abTEM in Google Colab**. Two standalone notebooks are provided:

#### ✅ Option 1: 4D-STEM with Flexible Detectors
- **File**: [`abTEM_4D_STEM_flexible_detectors.ipynb`](./4_stem_simulation/abTEM_4D_STEM_flexible_detectors.ipynb)
- Simulates full scattering using `FlexibleAnnularDetector`
- Performs radial integration to generate ABF, MAADF, HAADF images

#### ✅ Option 2: Fast Scan with Fixed Detectors
- **File**: [`abTEM_fast_scan.ipynb`](./4_stem_simulation/abTEM_fast_scan.ipynb)
- Uses `AnnularDetector` for faster, predefined ABF + HAADF scans

#### 🧪 To Use Either Notebook:
1. Open the notebook in [Google Colab](https://colab.research.google.com/)
2. Upload your **`relaxed_positions_only.cif`** file when prompted
3. Follow the step-by-step instructions inside the notebook:
   - Installs required packages
   - Builds zone-aligned structure
   - Sets up probe, scan, detectors
   - Simulates and visualizes images
   - Saves `.png` and `.npy` outputs

Each notebook is **self-contained**, **Colab-compatible**, and includes comments to guide new users.

---

## 📁 Folder Structure

- `1_structure/`: Builds doped SiC supercell
- `2_scf_relax/`: GPAW static and relaxed calculations
- `3_analysis/`: Post-analysis (interatomic distances)
- `4_stem_simulation/`: abTEM STEM simulation notebook
- `data/`: CIF files and relaxed output
- `setup/`: Guides for Windows/WSL users

---

## 📦 Requirements

See [`environment.yml`](./environment.yml) for all required packages (GPAW, ASE, NumPy, etc).

---

## 🧑‍🔬 Authors

This project was prepared for junior-level training in atomic-scale materials modeling.
