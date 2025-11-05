# Ultra-High-Density Matter in Active Galactic Nuclei

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

This repository contains the complete analysis pipeline for our study of ultra-high-density matter (UHDM) production in active galactic nucleus (AGN) jets using multi-messenger astronomy constraints.

**Key Results:**
- GRMHD simulations predict maximum Lorentz factors γ_max ~ 10^6-10^7 in magnetically-dominated jets
- EFT calculations constrain production cross sections for UHDM with masses 100 GeV - 100 TeV
- Multi-messenger constraints from Fermi-LAT, IceCube, and Pierre Auger Observatory exclude large regions of parameter space
- Bayesian MCMC analysis (10^6 samples) maps allowed parameter regions

## Repository Structure

```
UHDM_AGN_Paper_Final/
├── manuscript/          # LaTeX manuscript and bibliography
├── figures/            # Publication-quality PDF figures
├── code/               # Python analysis scripts
├── data/               # Observational data and MCMC outputs
├── workflow/           # Docker and automation scripts
├── docs/               # Documentation and metadata
└── LICENSE             # MIT License
```

## Quick Start

### Installation

**Option 1: Conda (Recommended)**
```bash
conda env create -f workflow/environment.yml
conda activate uhdm-agn
```

**Option 2: pip**
```bash
pip install -r code/requirements.txt
```

**Option 3: Docker**
```bash
docker build -t uhdm-agn -f workflow/Dockerfile .
docker run -it -v $(pwd):/workspace uhdm-agn
```

### Running the Analysis

Execute the complete pipeline:
```bash
bash workflow/run_analysis.sh
```

Or run individual modules:
```bash
# GRMHD acceleration
python code/grmhd_acceleration.py

# EFT cross sections
python code/eft_cross_sections.py

# Monte Carlo scan (WARNING: slow!)
python code/monte_carlo_sampling.py

# Observational constraints
python code/observational_constraints.py
```

## Code Modules

### 1. GRMHD Acceleration (`grmhd_acceleration.py`)
Calculates maximum Lorentz factors from:
- Magnetic reconnection in σ >> 1 jets
- Relativistic shock acceleration
- Generates **Figure 2**

### 2. EFT Cross Sections (`eft_cross_sections.py`)
Computes production cross sections using:
- Contact interaction operators
- EFT validity analysis
- Generates **Figures 1 & 3**

### 3. PDF Integration (`pdf_integration.py`)
Integrates parton luminosities:
- CT18 NNLO parton distribution functions
- Hadronic cross section convolution

### 4. Monte Carlo Sampling (`monte_carlo_sampling.py`)
Bayesian parameter inference:
- emcee affine-invariant sampler
- 10^6 posterior samples
- Generates **Figure S1** (diagnostics)

### 5. Observational Constraints (`observational_constraints.py`)
Multi-messenger limits:
- Fermi-LAT 3FHL catalog
- IceCube neutrino stacking
- Pierre Auger UHECR spectrum
- Generates **Figure 4**

## Data Requirements

Download observational data:

```bash
# Fermi-LAT 3FHL Catalog
wget https://fermi.gsfc.nasa.gov/ssc/data/access/lat/3FHL/gll_psch_v13.fit \
  -O data/fermi_lat_3fhl_catalog.fits

# IceCube and Auger data
# See data/README_data.txt for details
```

Or use built-in parameterizations (less accurate).

## Reproducibility

### Dependencies
- Python 3.9+
- NumPy, SciPy, Matplotlib
- emcee, corner (MCMC)
- h5py, pandas, astropy
- Optional: LHAPDF (for CT18 PDFs)
- LaTeX (for manuscript compilation)

### Computational Requirements
- **MCMC scan**: ~8-12 hours on 16 cores (10^6 samples)
- **Memory**: ~8 GB RAM
- **Storage**: ~500 MB for MCMC output

### Random Seeds
All random number generators are seeded for reproducibility:
```python
np.random.seed(42)
emcee uses deterministic initialization
```

### Docker Container
Fully containerized environment ensures bit-for-bit reproducibility:
```bash
docker run -it uhdm-agn bash workflow/run_analysis.sh
```

## Figures

All figures are generated programmatically from code:

- **Figure 1**: EFT validity regions (corrected)
- **Figure 2**: Maximum Lorentz factors vs magnetization
- **Figure 3**: Production rates vs UHDM mass
- **Figure 4**: Multi-messenger constraints summary
- **Figure S1**: MCMC convergence diagnostics

Figures are saved in `figures/` as vector PDFs (300 dpi).

## Citation

If you use this code or data, please cite:

```bibtex
@article{patidar2025uhdm,
  author = {Patidar, Kirti},
  title = {Ultra-Heavy Dark Matter Production in Active Galactic Nucleus Jets:
           A Falsifiable Multi-Messenger Framework},
  year = {2025},
  note = {Preprint available at https://github.com/kirtii56/Agnn}
}
```

## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

## Acknowledgments

- Fermi-LAT Collaboration for gamma-ray data
- IceCube Collaboration for neutrino limits
- Pierre Auger Collaboration for UHECR data
- CT18 PDF collaboration for parton distributions

## Contact

For questions or issues:
- Open an issue on GitHub
- Email: [contact email]

## Validation Checklist

Before submission, verify:

- [ ] All figures regenerate from code
- [ ] MCMC converges (R-hat < 1.1)
- [ ] Unit tests pass: `pytest tests/`
- [ ] Manuscript compiles without errors
- [ ] Data provenance documented
- [ ] Random seeds set for reproducibility
- [ ] Docker image builds successfully

See `docs/submission_checklist.txt` for full checklist.

---

**Status**: ArXiv Preprint Ready
**Version**: 2.0-FINAL
**Last Updated**: November 3, 2025
