# Oxygen Diffusion in 4H-SiC via DFT and STEM Simulation

This project demonstrates how to model and simulate oxygen diffusion in 4H-SiC using **Computational Materials (with GPAW/ASE)** and simulate corresponding **atomic resolution STEM images using abTEM**.
The choice of oxygen diffusion in 4H-SiC is solely for semiconductor metrology, but the workflow can be used for many other materials. 

It is designed for educational use by junior researchers, and runs on:
- **Linux / WSL2 on Windows**
- **Google Colab (for abTEM image simulation)**

## 🧠 Why This Project Matters

Microscopy-based defect characterization increasingly demands synergy between **atomic-scale simulations** and **experimental STEM imaging**. However, junior researchers often encounter major barriers when trying to bridge DFT and microscopy.

### 🔧 Pain Points in the Field

- ⚙️ **Heavyweight DFT tools vs practical needs**: While high-accuracy DFT codes like VASP or Wien2k are standard in academia, they are computationally intensive and often overkill for generating atomic models used in microscopy image                simulations. In contrast, GPAW/ASE provides a Python-based, lightweight alternative with sufficient accuracy for many practical defect studies, and supports scripting for automated exploration of multiple defect configurations.
- 📦 **Limited support for batch STEM simulations**: Many STEM simulation packages—especially closed-source or GUI-driven ones—lack automation capabilities for high-throughput simulations. abTEM, being open-source and Python-native, enables            flexible, scriptable workflows to simulate large sets of images under varying conditions (defocus, aberrations, zone axis, thickness, etc.).
- 📉 **Limited examples for defect modeling + STEM**: There is a shortage of beginner-friendly, end-to-end examples that walk users through the full process: from structure setup → DFT relaxation → STEM image generation. This project fills            that gap.
- 💻 **Complex environments**: Installing and configuring GPAW, especially on Windows, is error-prone without HPC experience.
- ❓ **Lack of reproducible starter projects**: Most DFT + STEM workflows are either highly customized or too abstract for newcomers to replicate on a laptop or in Google Colab. This project is designed to be fully reproducible on modest             computing setups with annotated scripts and notebooks.

### ✅ What This Project Offers

This project was designed specifically to help newcomers overcome those challenges:

- 🔁 **End-to-end reproducibility**: Includes every step from structure setup to image generation, with working input/output files.
- 🧪 **Realistic but simplified modeling**: Focuses on meaningful yet computationally affordable simulations.
- 🧑‍🏫 **Educational clarity**: Modular scripts, in-code comments, and clearly documented workflows suitable for courses and research training.
- 💡 **Cross-platform setup**: Runs on Linux or WSL2 + Google Colab, so anyone can get started — even without HPC access.
- 🔄 **Extendable design**: Easily adapted for different dopants, host materials, or imaging geometries.

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
   - Installs required packages (then restart session)
   - Builds zone-aligned structure
   - Sets up probe, scan, and detectors
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

This project was prepared for junior-level training as a guideline on how to model defects in materials using computational approaches and how to simulate microscopy images at the atomic scale.

## 📚 References

This project makes use of the following key scientific software:

- **GPAW** – A Python-based DFT code using real-space grids and PAW formalism  
  *Jens Jørgen Mortensen, Ask Hjorth Larsen, Mikael Kuisma et al. GPAW: An open Python package for electronic structure calculations featured, J. Chem. Phys. 160, 092503 (2024)*  
  [https://wiki.fysik.dtu.dk/gpaw/](https://wiki.fysik.dtu.dk/gpaw/)

- **ASE (Atomic Simulation Environment)** – Python tools for setting up, running, and analyzing atomistic simulations  
  *Ask Hjorth Larsen et al, The Atomic Simulation Environment—A Python library for working with atoms, J. Phys.: Condens. Matter Vol. 29 273002, 2017*  
  [https://wiki.fysik.dtu.dk/ase/](https://wiki.fysik.dtu.dk/ase/)

- **abTEM** – A transmission electron microscopy simulation code based on the multislice algorithm  
  *Jacob Madsen and Toma Susi. The abTEM code: transmission electron microscopy from first principles. Open Research Europe 1:24, 2021.*  
  [https://abtem.readthedocs.io](https://abtem.readthedocs.io)

Please cite these tools appropriately in your own publications if you build on this workflow.
