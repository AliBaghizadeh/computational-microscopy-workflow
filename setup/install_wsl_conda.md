# Installing WSL2 + Conda on Windows

This guide helps you set up a Linux (Ubuntu) environment inside Windows to run GPAW and Python-based DFT simulations.

---

## 🖥️ Step 1: Install WSL2 and Ubuntu

Open PowerShell **as Administrator** and run:

```powershell
wsl --install
```

Reboot if prompted. This installs:
- WSL2 backend
- Ubuntu as the default Linux distro

Once done, launch **Ubuntu** from Start Menu.

---

## 🐍 Step 2: Install Miniconda inside WSL

```bash
cd /tmp
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

Accept the license and set up `conda`.

---

## ⚙️ Step 3: Create Environment

From your WSL terminal:

```bash
conda env create -f environment.yml
conda activate sic-dft
```

You’re now ready to run the DFT scripts.
