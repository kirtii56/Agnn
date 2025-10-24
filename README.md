# UHDM AGN Paper - Final Repository

[![arXiv](https://img.shields.io/badge/arXiv-XXXX.XXXXX-b31b1b.svg)](https://arxiv.org/abs/XXXX.XXXXX)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Ultra-High-Density Matter in Active Galactic Nuclei: Constraints from Multi-Messenger Observations

This repository contains the complete code, data, and analysis for our study on UHDM production in AGN jets using multi-messenger constraints.

**Full documentation**: See [`docs/README.md`](docs/README.md)

## Quick Start

```bash
# Clone repository
git clone https://github.com/username/UHDM_AGN_Paper_Final.git
cd UHDM_AGN_Paper_Final

# Set up environment
conda env create -f workflow/environment.yml
conda activate uhdm-agn

# Run full analysis pipeline
bash workflow/run_analysis.sh
```

## Repository Structure

```
├── manuscript/          # LaTeX manuscript + bibliography
├── figures/            # Publication figures (PDF)
├── code/               # Python analysis scripts
├── data/               # Observational data + MCMC output
├── workflow/           # Docker, environment, run scripts
├── docs/               # Documentation
└── LICENSE             # MIT License
```

## Key Features

- **GRMHD Simulations**: Lorentz factor calculations in magnetically-dominated jets
- **EFT Cross Sections**: Production rates with validity analysis
- **Bayesian MCMC**: Parameter space exploration (10^6 samples via emcee)
- **Multi-Messenger Constraints**: Fermi-LAT, IceCube, Pierre Auger
- **Fully Reproducible**: Docker container + automation scripts

## Citation

```bibtex
@article{uhdm_agn_2024,
  author = {[Authors]},
  title = {Ultra-High-Density Matter in Active Galactic Nuclei},
  journal = {[Journal]},
  year = {2024},
  eprint = {arXiv:XXXX.XXXXX}
}
```

## License

MIT License - see [LICENSE](LICENSE) for details

## Contact

For questions: [email] or open an issue on GitHub
