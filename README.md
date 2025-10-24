# Ultra-Heavy Dark Matter Production in AGN Jets

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
[![arXiv](https://img.shields.io/badge/arXiv-2410.XXXXX-b31b1b.svg)](https://arxiv.org/abs/2410.XXXXX)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Authors:** Kirti Patidar
**Affiliation:** Department of Physics and Astronomy, [Institution]
**Contact:** kirti.patidar@institution.edu
**Version:** 2.0-FINAL
**Last Updated:** October 24, 2025

---

## 📄 Abstract

This repository contains the complete research package for **"Ultra-Heavy Dark Matter Production in Active Galactic Nucleus Jets: A Falsifiable Multi-Messenger Framework"**.

We investigate whether AGN jets can produce ultra-heavy dark matter (UHDM) with masses $10^{15}$--$10^{19}$ eV through Standard Model particle collisions at center-of-mass energies $\sqrt{s} \sim 10^{17}$--$10^{18}$ eV. Using GRMHD simulations, effective field theory parametrization, and multi-messenger observations (Fermi-LAT, IceCube, Pierre Auger), we predict production rates $\dot{N}_X \sim 10^{10}$--$10^{15}$ s$^{-1}$ per AGN with factor-of-$10^3$ systematic uncertainties.

**Key Finding:** AGN jets contribute $\Omega_X^{\rm AGN} \lesssim 10^{-10}\Omega_{\rm DM}$---subdominant to primordial mechanisms but exhibiting unique spatial clustering and kinematic signatures testable by next-generation experiments (CTA, IceCube-Gen2, LISA).

---

## 📂 Repository Structure

```
UHDM_AGN_Paper_Final/
├── manuscript/
│   ├── manuscript_final.tex          # LaTeX source (RevTeX4-2 format)
│   ├── manuscript_final.pdf          # Compiled PDF
│   ├── references.bib                # BibTeX bibliography
│   └── supplementary_material.pdf    # MCMC diagnostics (Figure S1)
├── figures/
│   ├── fig1_eft_validity_corrected.pdf    # EFT cutoff plot (regenerated)
│   ├── fig2_gamma_max.pdf                 # Max Lorentz factors
│   ├── fig3_production_rate.pdf           # Production rates vs mass
│   ├── fig4_constraints.pdf               # Multi-messenger constraints
│   └── figS1_mcmc_diagnostics.pdf         # Convergence diagnostics
├── code/
│   ├── grmhd_acceleration.py         # Lorentz factor calculations
│   ├── eft_cross_sections.py         # EFT production cross sections
│   ├── monte_carlo_sampling.py       # MCMC parameter scan (emcee)
│   ├── pdf_integration.py            # CT18 NNLO parton luminosity
│   ├── observational_constraints.py  # Fermi/IceCube/Auger limits
│   └── requirements.txt              # Python dependencies
├── data/
│   ├── fermi_lat_3fhl_catalog.fits   # Fermi-LAT source catalog
│   ├── icecube_neutrino_limits.csv   # IceCube stacking analysis
│   ├── auger_uhecr_spectrum.dat      # Pierre Auger UHECR data
│   └── mc_posterior_samples.h5       # Monte Carlo output (10^6 samples)
├── workflow/
│   ├── Dockerfile                    # Reproducibility container
│   ├── run_analysis.sh               # Master execution script
│   └── environment.yml               # Conda environment
├── docs/
│   ├── README.md                     # Detailed documentation
│   ├── metadata.json                 # Project metadata (Zenodo/arXiv)
│   ├── submission_checklist.txt      # Pre-submission validation
│   └── peer_review_response.txt      # Response to reviewer comments
└── LICENSE                           # MIT License
```

---

## 🚀 Quick Start

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

# Monte Carlo scan (WARNING: takes 8-12 hours!)
python code/monte_carlo_sampling.py

# Observational constraints
python code/observational_constraints.py
```

---

## 📊 Key Results

- **Maximum Lorentz factors**: $\gamma_{e,\rm max} \sim 10^6$--$10^7$ (electrons), $\gamma_{p,\rm max} \sim 10^9$--$10^{10}$ (protons)
- **Center-of-mass energies**: $\sqrt{s} \sim 10^{17}$--$10^{18}$ eV (within EFT regime by $10^9$)
- **Production rates**: $\dot{N}_X \sim 10^{10}$--$10^{15}$ s$^{-1}$ per AGN (factor-of-$10^3$ uncertainty)
- **Cosmic abundance**: $\Omega_X^{\rm AGN} \lesssim 10^{-10}\Omega_{\rm DM}$ (subdominant)
- **Multi-messenger constraints**: All current data (Fermi-LAT, IceCube, UHECR) allow predicted rates

---

## 🔬 Code Modules

### 1. GRMHD Acceleration (`grmhd_acceleration.py`)
Calculates maximum Lorentz factors from:
- Magnetic reconnection in σ >> 1 jets
- Relativistic shock acceleration
- **Generates Figure 2**

### 2. EFT Cross Sections (`eft_cross_sections.py`)
Computes production cross sections using:
- Contact interaction operators
- EFT validity analysis
- **Generates Figures 1 & 3**

### 3. PDF Integration (`pdf_integration.py`)
Integrates parton luminosities:
- CT18 NNLO parton distribution functions
- Hadronic cross section convolution

### 4. Monte Carlo Sampling (`monte_carlo_sampling.py`)
Bayesian parameter inference:
- emcee affine-invariant sampler
- 10^6 posterior samples across 5 chains
- Random seeds: {42, 137, 271, 314, 628} for reproducibility
- **Generates Figure S1** (diagnostics)

### 5. Observational Constraints (`observational_constraints.py`)
Multi-messenger limits:
- Fermi-LAT 3FHL catalog (1,556 sources)
- IceCube neutrino stacking (1,163 AGN)
- Pierre Auger UHECR spectrum
- **Generates Figure 4**

---

## 📈 Figures

All figures are generated programmatically from code:

- **Figure 1**: EFT validity regions (corrected)
- **Figure 2**: Maximum Lorentz factors vs magnetization
- **Figure 3**: Production rates vs UHDM mass
- **Figure 4**: Multi-messenger constraints summary
- **Figure S1**: MCMC convergence diagnostics

Figures are saved in `figures/` as vector PDFs (300 dpi).

---

## 🔄 Reproducibility

### Computational Requirements
- **MCMC scan**: ~8-12 hours on 16 cores (10^6 samples)
- **Memory**: ~8 GB RAM
- **Storage**: ~500 MB for MCMC output

### Random Seeds
All random number generators are seeded for bit-exact reproducibility:
```python
np.random.seed(42)  # NumPy operations
# emcee chains use seeds: {42, 137, 271, 314, 628}
```

### Docker Container
Fully containerized environment ensures platform-independent reproducibility:
```bash
docker run -it uhdm-agn bash workflow/run_analysis.sh
```

### Validation Checklist
Before submission, verify:
- [x] All figures regenerate from code
- [x] MCMC converges (R-hat < 1.01)
- [x] Manuscript compiles without errors
- [x] Data provenance documented
- [x] Random seeds set for reproducibility
- [x] Docker image builds successfully

See `docs/submission_checklist.txt` for full checklist.

---

## 📚 Citation

If you use this code or data, please cite:

```bibtex
@article{patidar2025uhdm,
  author = {Patidar, Kirti},
  title = {Ultra-Heavy Dark Matter Production in Active Galactic Nucleus Jets:
           A Falsifiable Multi-Messenger Framework},
  journal = {[Journal Name]},
  year = {2025},
  eprint = {arXiv:2410.XXXXX},
  doi = {10.XXXX/XXXXX}
}
```

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Fermi-LAT Collaboration for gamma-ray data
- IceCube Collaboration for neutrino limits
- Pierre Auger Collaboration for UHECR data
- CT18 PDF collaboration (CTEQ-TEA) for parton distributions
- emcee developers for MCMC framework

---

## 📧 Contact

**Kirti Patidar**
Department of Physics and Astronomy
Email: kirti.patidar@institution.edu

For questions or issues:
- Open an issue on GitHub
- Email the author directly

---

## 📝 Documentation

For detailed documentation, see:
- [`docs/README.md`](docs/README.md) - Comprehensive technical documentation
- [`docs/metadata.json`](docs/metadata.json) - Project metadata for Zenodo/arXiv
- [`docs/submission_checklist.txt`](docs/submission_checklist.txt) - Pre-submission validation
- [`manuscript/`](manuscript/) - LaTeX source and compiled PDF

---

**Status**: Ready for Submission
**Version**: 2.0-FINAL
**arXiv**: arXiv:2410.XXXXX
**Zenodo DOI**: 10.5281/zenodo.XXXXXXX
**Last Updated**: October 24, 2025
