# Oxygen Diffusion in 4H-SiC via DFT and STEM Simulation

This project demonstrates how to model and simulate oxygen diffusion in 4H-SiC using **Computational Materials (with GPAW/ASE)** and simulate corresponding **atomic resolution STEM images using abTEM**.
The choice of oxygen diffusion in 4H-SiC is solely for semiconductor metrology, but the workflow can be used for many other materials. 

It is designed for educational use by junior researchers, and runs on:
- **Linux / WSL2 on Windows**
- **Google Colab (for abTEM image simulation)**

## 📊 Workflow Overview

1. **Build Supercell**: Start from 4H-SiC CIF, build 2x2x1 supercell, introduce O dopants.    
   The size of the supercell is very important, and depends on factors like the zone axis for image simulation, the symmetry of the lattice, and of course, your computational resources.
2. **SCF + Relaxation**: Perform static and relaxed DFT calculations using GPAW.     
   This approach is just a demo. It does not optimize lattice parameters, and it is not intended to relax atomic positions for the purpose of electronic structure or very high-accuracy coordinate calculations.      
   The best strategy is to read the manual of the GPAW for the possible choices of parameters to reduce or increase the accuracy of the final results. Again, mind your computation resources.     
3. **Distance Analysis**: Analyze Si–Si interatomic distances.
   This is just a short script allowing analyzing the intratomic distances. The analysis can be expanded to other things like comparing original and relaxed cif files, too.
4. **STEM Simulation**: Simulate ABF, MAADF, HAADF contrast with abTEM in Colab.  
   The **abTEM** package supports two main approaches for STEM image simulation:

   - **Flexible (4D-STEM-like) Simulation**:  
     This comprehensive method simulates the full diffraction pattern at each probe position and allows **post-acquisition integration** of signals over any detector angles. It’s similar to 4D-STEM and ideal for exploring how different angular       ranges affect image contrast.  
     In this project, we use this to generate **ABF, MAADF, and HAADF** contrast maps by integrating over selected annular angle ranges.

   - **Direct (Single-Detector) Simulation**:  
     This more traditional method simulates STEM images by scanning a probe across the sample and collecting signal using predefined detector geometries (like fixed ABF or HAADF detectors).  
     This is faster and commonly used for generating reproducible, publication-style images with specific detector settings.

   The simulation is done in **Google Colab** to take advantage of GPU acceleration (via CuPy) and avoid local hardware limitations. Just upload the `relaxed_positions_only.cif` file and run the notebook step-by-step.

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
