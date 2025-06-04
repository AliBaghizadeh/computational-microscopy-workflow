# Oxygen Diffusion in 4H-SiC via DFT and STEM Simulation

This project demonstrates how to model and simulate oxygen diffusion in 4H-SiC using **DFT (with GPAW/ASE)** and simulate corresponding **STEM images using abTEM**.

It is designed for educational use by junior researchers, and runs on:
- **Linux / WSL2 on Windows**
- **Google Colab (for abTEM image simulation)**

## 📊 Workflow Overview

1. **Build Supercell**: Start from 4H-SiC CIF, build 2x2x1 supercell, introduce O dopants.
2. **SCF + Relaxation**: Perform static and relaxed DFT calculations using GPAW.
3. **Distance Analysis**: Analyze Si–Si interatomic distances.
4. **STEM Simulation**: Simulate ABF, MAADF, HAADF contrast with abTEM in Colab.

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

### 4. STEM Simulation in Colab

Open [`abTEM_image_simulation_SiC_ver2.ipynb`](./4_stem_simulation/abTEM_image_simulation_SiC_ver2.ipynb) in [Google Colab](https://colab.research.google.com), upload `relaxed_positions_only.cif` and follow notebook instructions.

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
