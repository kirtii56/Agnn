# Methods Documentation

Technical notes on the physics models and parameterisations used in the
UHDM AGN production analysis.  These notes supplement the manuscript and
explain choices made in the code where the full derivation or data source
is not included in the repository.

---

## 1. EFT Cross Section Formula

### Lagrangian

We use a dimension-6 contact interaction between Standard Model quarks
and the UHDM scalar X:

    L_eff = (1 / Lambda^2) (q-bar q)(X-bar X)

where Lambda is the EFT cutoff scale.

### Partonic cross section

The tree-level q qbar -> X Xbar cross section from this operator is:

    sigma_hat(s) = (s / Lambda^4) * (1 / (16 pi)) * beta(s, m_X)

where

    beta = sqrt(1 - 4 m_X^2 / s)

is the final-state velocity factor, and s is the partonic centre-of-mass
energy squared.

### Derivation sketch

Starting from the dimension-6 operator with coupling 1/Lambda^2, the
squared amplitude is |M|^2 ~ s / Lambda^4 (by dimensional analysis,
since the operator has mass dimension 6).  The two-body phase space in
d = 4 gives a factor 1/(8 pi) * beta / (2s), and including colour/spin
averaging for a single quark flavour yields the 1/(16 pi) prefactor.

### EFT validity

The effective description is valid only when the partonic energy is below
the cutoff:

    sqrt(s) < Lambda

Above this scale, the contact interaction must be UV-completed by a
mediator, and the cross section formula is no longer reliable.

### Units

The code returns cross sections in cm^2 using the conversion
1 GeV^{-2} = 3.894 x 10^{-28} cm^2.

---

## 2. GRMHD Parameter Choices

### Magnetic field strength:  B = 0.1 -- 100 G

This range corresponds to AGN jet environments at distances ~0.1--10 pc
from the central engine.  Observational constraints come from:

- Faraday rotation measure gradients across jets
  (Zavala & Taylor 2005, ApJ 626, L73)
- Jet power arguments equating Poynting flux to observed luminosity
  (Zamaninasab et al. 2014, Nature 510, 126)
- Core-shift measurements in VLBI-resolved jets
  (Lobanov 1998, A&A 330, 79)

Values above ~100 G are relevant only very close to the black hole
(< 10 R_g) and are not representative of the extended acceleration zone.

### Magnetization parameter:  sigma = 10 -- 1000

GRMHD simulations of magnetically arrested disks (MAD) produce jets with
sigma >> 1 near the jet base, decreasing with distance.  Key references:

- Tchekhovskoy et al. 2011, MNRAS 418, L79
  (MAD jets with sigma ~ 10--100 at launch)
- McKinney et al. 2012, MNRAS 423, 3083
  (sigma up to ~1000 in the jet spine)

The sigma >> 1 regime is where magnetic reconnection dominates particle
acceleration over shock acceleration.

### Jet radius:  R_jet = 10^14 -- 10^16 cm

This covers the range from ~0.003 pc to ~0.3 pc:

- 10^14 cm:  inner jet / blazar-zone scale
- 10^15 cm:  typical reconnection / acceleration region
- 10^16 cm:  transition to large-scale jet (~pc)

These scales are set by the jet opening angle (~1/Gamma_bulk) and the
distance from the central engine.

### Electron acceleration:  gamma_e_max = eta * sigma

In the sigma >> 1 regime, PIC simulations show that magnetic reconnection
accelerates electrons to Lorentz factors proportional to the magnetization:

    gamma_e_max = eta * sigma

with eta ~ 0.1--0.3 (Sironi & Spitkovsky 2014, ApJ 783, L21; Werner et
al. 2016, ApJ 816, L8).  The efficiency eta encapsulates the fraction of
magnetic energy converted to the highest-energy particles.

### Proton acceleration:  gamma_p_max = e B R_jet / (m_p c^2)

The Hillas criterion (Hillas 1984, ARA&A 22, 425) gives the maximum
energy a proton can reach while its Larmor radius fits inside the
acceleration region:

    E_max = e B R_jet
    gamma_p_max = E_max / (m_p c^2)

For B = 10 G and R_jet = 10^15 cm this gives gamma_p ~ 3 x 10^9,
consistent with UHECR energies.

---

## 3. Observational Limit Parameterisations

Since the full Fermi-LAT, IceCube, and Auger data files are not included
in this repository, the code uses parameterised upper limits drawn from
published results.  These are sufficient for the order-of-magnitude
predictions in this analysis.

### Fermi-LAT (3FHL catalog)

- **Observable**: point-source sensitivity in E^2 dN/dE
- **Limit used**: E^2 dN/dE < 10^{-12} erg cm^{-2} s^{-1}
- **Energy range**: 10 GeV -- 2 TeV
- **Basis**: Ajello et al. 2017, ApJS 232, 18 (3FHL catalog)
- **Notes**: The 3FHL sensitivity varies across the sky; we use the
  median sensitivity as a representative upper limit.  For specific AGN,
  one should use the per-source upper limit from the catalog.

### IceCube (AGN neutrino stacking)

- **Observable**: per-AGN muon-neutrino flux
- **Limit used**: phi_nu < 10^{-18} GeV cm^{-2} s^{-1} sr^{-1}
- **Energy range**: 1 TeV -- 10 PeV
- **Basis**: IceCube Collaboration (Abbasi et al.) 2023, ApJ 954, 75
- **Notes**: This is the stacking limit from ~1000 gamma-ray-selected
  AGN.  Individual bright sources (e.g. NGC 1068) have tighter
  constraints.  The limit assumes an E^{-2} neutrino spectrum.

### Pierre Auger (UHECR spectrum)

- **Observable**: integral cosmic-ray flux above threshold energy
- **Threshold**: E > 10^{19.5} eV (31.6 EeV)
- **Basis**: Pierre Auger Collaboration 2020, PRL 125, 121106
- **Notes**: The Auger constraint is parameterised as a simple integral
  flux limit above the energy threshold.  In practice, the composition-
  sensitive observables (X_max distributions) provide additional
  constraints on UHDM decay products.  The code uses an approximate
  limit that is conservative (i.e. weaker than the actual data).

---

## 4. MCMC Parameter Scan

### Sampler

We use the emcee affine-invariant ensemble sampler (Foreman-Mackey et al.
2013, PASP 125, 306).  The algorithm requires nwalkers >= 2 * ndim; with
ndim = 4 parameters we use nwalkers = 10.

### Parameters and priors

All parameters have log-uniform (flat in log10) priors:

| Parameter | Symbol | Prior range |
|-----------|--------|-------------|
| EFT cutoff | log10(Lambda/GeV) | [8, 11] |
| UHDM mass | log10(m_X/GeV) | [6, 10] |
| Magnetization | log10(sigma_jet) | [1, 3] |
| B-field | log10(B_jet/G) | [-1, 2] |

### Likelihood

The likelihood is a one-sided Gaussian penalty:

    log L = -0.5 * sum_i [ max(0, F_pred_i - F_lim_i)^2 / sigma_i^2 ]

where the sum runs over the three messenger channels (gamma-ray,
neutrino, cosmic ray), and sigma_i = 0.5 * F_lim_i represents a 50%
systematic uncertainty on the limit.

### Convergence diagnostics

- **Acceptance fraction**: target 0.2--0.5 (achieved: ~0.39)
- **Autocorrelation time**: estimated via emcee.autocorr.integrated_time
- **Split R-hat**: Gelman-Rubin statistic computed by treating each
  walker as an independent chain, splitting in half, and computing
  between/within-chain variance.  R-hat < 1.1 indicates convergence.
  With only 10^3 samples R-hat will typically be > 1.1; this is expected
  for the fast demonstration and improves with longer chains.
