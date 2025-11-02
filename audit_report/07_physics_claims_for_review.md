═══════════════════════════════════════════════════════════════
PHASE 8: EXTRACT DATA FOR EXPERT PHYSICS REVIEW
═══════════════════════════════════════════════════════════════
Ultra-Heavy Dark Matter Production in AGN Jets
Systematic Audit for Physics Expert Review
Generated: 2025-11-02

═══════════════════════════════════════════════════════════════
1. ALL PHYSICS CLAIMS
═══════════════════════════════════════════════════════════════

| Claim # | Claim Statement | Location in Paper | Supporting Calculation | Value/Range |
|---------|----------------|-------------------|----------------------|-------------|
| 1 | "Maximum electron Lorentz factor γ_e,max ~ 10^6-10^7" | Section 2.2.1, Eq. 6 | grmhd_acceleration.py, line 44 | γ_e,max = 10^6 - 10^7 |
| 2 | "Maximum proton Lorentz factor γ_p,max ~ 10^9-10^10" | Section 2.2.2, Eq. 8 | grmhd_acceleration.py, line 68 | γ_p,max = 10^9 - 10^10 |
| 3 | "Center-of-mass energies √s ~ 10^17-10^18 eV" | Section 2.3, Eq. 9 | Manuscript line 127 | √s_pp ≈ 1.9 × 10^18 eV |
| 4 | "EFT valid by factor 10^9" | Section 2.3, Eq. 11 | Manuscript line 143 | √s < 0.1M_Pl by 9 orders |
| 5 | "Blandford-Znajek power P_BZ ~ 10^45-10^47 erg/s" | Section 2.1, Eq. 2 | Manuscript line 70 | 10^45 - 10^47 erg/s |
| 6 | "MAD states achieve η ≈ 30% for a=0.5, η ≈ 140% for a=0.99" | Section 2.1 | Manuscript line 67 | η = 30% to 140% |
| 7 | "Production rates Ṅ_X ~ 10^10-10^15 s^-1 per AGN" | Section 5.1, Table 1 | Manuscript line 266-280 | 10^10 - 10^15 s^-1 |
| 8 | "Cosmic abundance Ω_X^AGN ≲ 10^-10 Ω_DM" | Section 5.2, Eq. 45 | Manuscript line 293 | ≲ 10^-10 Ω_DM |
| 9 | "Factor-of-10^3 systematic uncertainties" | Abstract, Section 5.5 | Manuscript line 23 | Factor of 1000 |
| 10 | "PDF corrections reduce rates by 30-100×" | Section 3.3, line 197 | pdf_integration.py, line 110 | Reduction: 30-100× |
| 11 | "Parton luminosity L_gg ≈ 10^-3-10^-4 at τ ~ 10^-2" | Section 2.3 | Manuscript line 138 | 10^-3 to 10^-4 |
| 12 | "TeV blazars require γ_e ≳ 3 × 10^5" | Section 2.2.1 | Manuscript line 102 (Fermi-LAT) | γ_e ≥ 3 × 10^5 |
| 13 | "UHECR maximum rigidities E_cut ≲ 5 EeV" | Section 2.2.2 | Manuscript line 120 (Auger) | ≤ 5 × 10^18 eV |
| 14 | "Magnetization parameter σ = 10-100" | Throughout | grmhd_acceleration.py, line 21 | σ = 10-100 |
| 15 | "Magnetic field B = 10^2-10^4 Gauss" | Section 2.1 | Throughout code | 100-10,000 G |
| 16 | "EFT cross section σ(s) ~ C_i^2 s^2/M_Pl^4" | Section 3.1, Eq. 14 | eft_cross_sections.py, line 59 | Eq. 14 |
| 17 | "EFT coupling C_i = 10^-3 to 1" | Section 3.4 | monte_carlo_sampling.py, line 49 | 0.001 - 1.0 |
| 18 | "AGN lifetime ~ 10^7 yr" | Section 5.2 | Manuscript line 290 | 10^7 years |
| 19 | "Cosmic AGN population ~ 10^6 sources" | Section 5.2 | Manuscript line 290 | 10^6 AGN |
| 20 | "UHDM optical depth τ_X ~ 10^-14 << 1" | Section 5.3, Eq. 47 | Manuscript line 305 | 10^-14 |
| 21 | "Escape velocity v_esc ~ 0.1c" | Section 5.3, Eq. 48 | Manuscript line 311 | 0.1c |
| 22 | "Thermalization time t_therm ~ 10^21 s >> t_cross ~ 10^6 s" | Section 5.3, Eq. 49 | Manuscript line 318 | 10^21 s vs 10^6 s |
| 23 | "CTA: ~10× improved sensitivity above 100 GeV" | Section 5.4.1 | Manuscript line 328 | 10× improvement |
| 24 | "IceCube-Gen2: ~10× neutrino sensitivity" | Section 5.4.1 | Manuscript line 330 | 10× improvement |
| 25 | "LISA detects ~100 SMBH mergers/year" | Section 5.4.2 | Manuscript line 332 | 100/year |
| 26 | "Burst production N_X^burst ~ 10^21" | Section 5.4.2, Eq. 50 | Manuscript line 336 | 10^21 particles |
| 27 | "Direct detection requires σ_X ≳ 3 × 10^-16 cm^2" | Section 5.4.3, Eq. 56 | Manuscript line 353 | ≥ 3 × 10^-16 cm^2 |
| 28 | "Energy budget constraint Ṅ_X < 6 × 10^17 s^-1" | Section 4.1, Eq. 36 | Manuscript line 236 | < 6 × 10^17 s^-1 |
| 29 | "IceCube limits blazars to ≤11-15% of diffuse ν flux" | Section 4.2 | Manuscript line 242 | 11-15% |
| 30 | "Photopion optical depth f_pγ < 0.01" | Section 4.2 | Manuscript line 248 | < 0.01 |

═══════════════════════════════════════════════════════════════
2. KEY EQUATIONS (LaTeX with Full Context)
═══════════════════════════════════════════════════════════════

**EQUATION 1: Blandford-Znajek Power**
```latex
P_{\rm BZ} = \frac{\kappa \Omega_H^2 \Phi_{\rm BH}^2}{4\pi c} f(\Omega_H)
```
- **Equation Number**: Eq. 1 (line 63)
- **Purpose**: Calculate electromagnetic power extracted from rotating black hole
- **Input Parameters**:
  - κ ≈ 0.053 (split monopole geometry)
  - Ω_H = ac/(2r_H) (horizon angular frequency)
  - a = 0.9 (spin parameter, typical)
  - Φ_BH: magnetic flux threading horizon
- **Output Values**: P_BZ ~ 10^45 - 10^47 erg/s
- **Literature Source**: Blandford & Znajek (1977), MNRAS, 179, 433

---

**EQUATION 6: Maximum Electron Lorentz Factor**
```latex
\gamma_{e,\rm max} \approx \left( \frac{3 e E_\parallel}{4\sigma_T (U_B + U_{\rm rad,eff})} \right)^{1/2}
```
- **Equation Number**: Eq. 6 (line 91)
- **Purpose**: Calculate maximum electron Lorentz factor balancing acceleration vs cooling
- **Input Parameters**:
  - e = 4.803×10^-10 esu (elementary charge)
  - E_∥: parallel electric field
  - σ_T = 6.65×10^-25 cm^2 (Thomson cross section)
  - U_B = B^2/(8π) (magnetic energy density)
  - B = 10^3 G (typical)
  - η_e = 0.1 (electron acceleration efficiency)
- **Output Values**: γ_e,max ~ 10^6 - 10^7
- **Supporting Physics**: Synchrotron + IC + curvature cooling (Eqs. 3-5)
- **Code Location**: grmhd_acceleration.py:44-66

---

**EQUATION 7: Hillas Criterion (Protons)**
```latex
\gamma_{p,\rm max} = \frac{eBR}{m_p c^2} \approx 10^{18} \left(\frac{B}{100 \text{ G}}\right) \left(\frac{R}{10^{18} \text{ cm}}\right)
```
- **Equation Number**: Eq. 7 (line 109)
- **Purpose**: Maximum proton Lorentz factor from Hillas criterion
- **Input Parameters**:
  - B = 100-10,000 G (magnetic field range)
  - R = 10^15 - 10^17 cm (acceleration region size)
  - m_p = 1.673×10^-24 g (proton mass)
- **Output Values**: γ_p,max ~ 10^9 - 10^10
- **Literature Source**: Hillas (1984), ARA&A, 22, 425
- **Observational Constraint**: Consistent with Auger UHECR cutoff at ~5 EeV

---

**EQUATION 9: Center-of-Mass Energy (pp collisions)**
```latex
\sqrt{s}_{pp} \approx 2\gamma_p m_p c^2 \sim 1.9 \times 10^{18} \text{ eV}
```
- **Equation Number**: Eq. 9 (line 127)
- **Purpose**: Calculate collision energy for head-on proton-proton collisions
- **Input Parameters**:
  - γ_p = 10^9 (from Eq. 7)
  - m_p c^2 = 938 MeV (proton rest mass)
- **Output Values**: √s_pp ≈ 1.9 × 10^18 eV
- **Comparison**: 10^5 times higher than LHC (√s = 14 TeV)

---

**EQUATION 11: EFT Validity Check**
```latex
\sqrt{s}_{pp} \sim 2 \times 10^{18} \text{ eV} < 0.1M_{\rm Pl} = 1.22 \times 10^{27} \text{ eV}
```
- **Equation Number**: Eq. 11 (line 143)
- **Purpose**: Verify collision energies lie within EFT validity regime
- **Result**: Valid by **9 orders of magnitude**
- **Critical Note**: Paper emphasizes this as justification for EFT approach
- **Planck Scale**: M_Pl = 1.22 × 10^19 GeV = 1.22 × 10^28 eV

---

**EQUATION 12: EFT Lagrangian**
```latex
\mathcal{L}_{\rm eff} = \mathcal{L}_{\rm SM} + \sum_{i} \frac{C_i}{\Lambda^2} \mathcal{O}_i^{(6)} + \mathcal{O}\left(\frac{1}{\Lambda^4}\right)
```
- **Equation Number**: Eq. 12 (line 157)
- **Purpose**: Parametrize new physics via dimension-6 operators
- **Input Parameters**:
  - Λ ~ M_Pl = 1.22 × 10^19 GeV (cutoff scale)
  - C_i = 10^-3 to 1 (Wilson coefficients)
- **Operators**: Vector/axial-vector, gluon G^μν G_μν, Higgs portal
- **Literature Source**: Grzadkowski et al. (2010), JHEP, 10, 085

---

**EQUATION 14: EFT Cross Section Scaling**
```latex
\sigma(s) \sim \frac{C_i^2}{\Lambda^4} s^2 = C_i^2 \frac{s^2}{M_{\rm Pl}^4}
```
- **Equation Number**: Eq. 14 (line 166)
- **Purpose**: Production cross section for UHDM via contact operators
- **Input Parameters**:
  - C_i = 1 (order-1 coupling)
  - s = (10^18 eV)^2 (collision energy squared)
  - M_Pl = 1.22 × 10^19 GeV
- **Output**: σ ~ 10^-72 cm^2 (contact operator estimate)
- **Code Location**: eft_cross_sections.py:23-60

---

**EQUATION 17: Spatially-Integrated Production Rate**
```latex
\dot{N}_X = \int_{r_{\rm min}}^{r_{\rm max}} \int_0^{2\pi} \int_0^{\theta_{\rm jet}} n_1(r) n_2(r) \sigma(r) v r^2 \sin\theta \, dr\, d\theta\, d\phi
```
- **Equation Number**: Eq. 17 (line 175)
- **Purpose**: Spatial integration accounting for radial stratification
- **Critical Improvement**: Replaces single-zone approximation (Issue 2.1 from review)
- **Input Parameters**:
  - r_min = 10 r_g (innermost stable orbit)
  - r_max = 1 pc
  - n_p(r) = n_p,0 (r/r_0)^-2 (mass continuity)
  - B(r) = B_0 (r/r_0)^-5/4 (McKinney 2007)
- **Output**: Integrated production rate accounts for radial profile

---

**EQUATION 19: Parton Luminosity**
```latex
\frac{d\mathcal{L}_{gg}}{d\tau} = \int_{\tau}^{1} \frac{dx}{x} g(x, Q^2) g(\tau/x, Q^2)
```
- **Equation Number**: Eq. 19 (line 193)
- **Purpose**: Calculate gluon-gluon luminosity using CT18 NNLO PDFs
- **Input Parameters**:
  - τ = 4m_X^2/s_pp ≈ 10^-2 (for m_X = 10^17 eV)
  - Q^2 ~ (10^17 eV)^2 (factorization scale)
  - g(x, Q^2): gluon PDF from CT18NNLO
- **Output**: L_gg(τ) ≈ 10^-3 - 10^-4
- **Critical Finding**: Reduces naive estimates by 30-100× (Issue 2.2)
- **Literature Source**: Hou et al. (2019), Phys. Rev. D, 103, 014013
- **Code Location**: pdf_integration.py:74-111

---

**EQUATION 45: Cosmic UHDM Abundance**
```latex
\Omega_X^{\rm AGN} \sim \frac{\dot{N}_X \times t_{\rm AGN} \times N_{\rm AGN} \times m_X}{\rho_{\rm crit}} \lesssim 10^{-10} \Omega_{\rm DM}
```
- **Equation Number**: Eq. 45 (line 293)
- **Purpose**: Calculate cosmic abundance of AGN-produced UHDM
- **Input Parameters**:
  - Ṅ_X ~ 10^12 s^-1 (median production rate)
  - t_AGN ~ 10^7 yr (AGN lifetime)
  - N_AGN ~ 10^6 (cosmic AGN population)
  - m_X = 10^17 eV (UHDM mass)
  - ρ_crit = 9.47 × 10^-30 g/cm^3
- **Output**: Ω_X^AGN ≲ 10^-10 Ω_DM
- **Interpretation**: Subdominant to primordial UHDM

---

**EQUATION 47: UHDM Optical Depth**
```latex
\tau_X = n_p \sigma_X L_{\rm jet} \sim 10^{-14} \ll 1
```
- **Equation Number**: Eq. 47 (line 305)
- **Purpose**: Verify UHDM escapes jet without re-scattering
- **Input Parameters**:
  - n_p ~ 10^3 cm^-3 (proton density in jet)
  - σ_X ~ 10^-37 cm^2 (EFT cross section)
  - L_jet ~ 10^17 cm (jet length scale)
- **Output**: τ_X ~ 10^-14 << 1
- **Conclusion**: Optically thin, UHDM escapes freely

═══════════════════════════════════════════════════════════════
3. NOVEL CONTRIBUTIONS
═══════════════════════════════════════════════════════════════

**What This Paper Claims to Do That's NEW:**

1. **First Systematic Framework for AGN Jets as UHDM Production Sites**
   - Location: Section 1.1, lines 38-51
   - Claim: "Extensive literature searches found no established work on AGN jets as primary production sites for UHDM"
   - Distinction: Previous work studied UHDM *detection/scattering* in jets (Gorchtein 2010, Wang 2024), NOT production
   - **Novel Element**: Calculating production rates from SM particle collisions in AGN jets

2. **Energy-Loss-Corrected Maximum Lorentz Factors**
   - Location: Section 2.2, Eqs. 3-6
   - Claim: Include Klein-Nishina suppression in IC cooling + curvature radiation
   - **Novel Element**: Previous estimates neglected KN regime at γ > 10^6
   - Result: More conservative γ_max predictions

3. **Spatially-Integrated Production Rates (Not Single-Zone)**
   - Location: Section 3.2, Eq. 17
   - Claim: First radial integration of production rate accounting for n(r), B(r), γ_max(r)
   - **Novel Element**: Replaces standard single-zone approximation
   - Impact: More realistic estimates (addresses peer review Issue 2.1)

4. **PDF-Corrected Gluon Fusion Rates at Ultra-High Energies**
   - Location: Section 3.3, Eq. 19
   - Claim: Apply CT18 NNLO PDFs at √s ~ 10^18 eV with proper τ integration
   - **Novel Element**: First time CT18 NNLO used at AGN jet energies
   - Result: 30-100× reduction in previous estimates

5. **Multi-Messenger Falsifiable Predictions**
   - Location: Section 4, Table 1
   - Claim: Simultaneous constraints from Fermi-LAT + IceCube + Auger
   - **Novel Element**: Integrated multi-messenger framework for UHDM production
   - Testability: Predictions for CTA, IceCube-Gen2, LISA

6. **LISA-Correlated UHDM Burst Signals**
   - Location: Section 5.4.2, Eq. 50
   - Claim: GW-triggered jet formation → time-correlated UHDM production
   - **Novel Element**: No previous work connecting LISA GW events to UHDM
   - Smoking Gun: Primordial UHDM has NO GW correlation

7. **Quantitative Systematic Uncertainty Analysis**
   - Location: Section 5.5
   - Claim: Factor-of-10^3 uncertainties explicitly quantified and propagated
   - **Novel Element**: Most papers hide uncertainties; this paper emphasizes them
   - Philosophy: "Improvability over precision"

═══════════════════════════════════════════════════════════════
4. OBSERVATIONAL CONSTRAINTS USED
═══════════════════════════════════════════════════════════════

| Dataset | Values Used | Source Paper | How Applied in This Work |
|---------|-------------|--------------|--------------------------|
| **Fermi-LAT 3FHL** | γ-ray flux limit F_γ < 10^-11 erg/cm²/s | Ajello et al. (2017), ApJS, 232, 18 | Energy budget constraint: Ṅ_X < ε_γ P_BZ / m_X (Eq. 36) |
| **Fermi-LAT TeV Blazars** | γ_e ≳ 3 × 10^5 required | Ajello et al. (2017), ApJS, 232, 18 | Validates γ_e,max predictions (Section 2.2.1) |
| **IceCube Stacking** | Blazars contribute ≤11-15% of diffuse ν flux | IceCube Collab. (2024), arXiv:2410.18184 | Constrains photopion optical depth f_pγ < 0.01 (Eq. 40) |
| **IceCube Neutrino Limit** | F_ν < 10^-6 ν/cm²/s (E_ν > 1 TeV) | IceCube Collab. (2024), arXiv:2410.18184 | Upper limit on hadronic processes (Section 4.2) |
| **Pierre Auger UHECR** | GZK suppression above E_GZK ≈ 5×10^19 eV | Auger Collab. (2020), Phys. Rev. D, 102, 062005 | Validates γ_p,max ~ 10^9-10^10 (Section 2.2.2) |
| **Auger Composition** | Light → heavy transition above 10^18 eV | Aab et al. (2017), Science, 357, 1266 | Requires Z=26 (Fe) to reach 10^20 eV (Section 4.3) |
| **Auger Photon Limits** | τ_X > few × 10^21 years for hadronic SHDM | Auger Collab. (2019), Phys. Rev. D, 99, 082002 | Lifetime constraint on UHDM decay (Section 1, line 35) |
| **GRMHD Simulations (MAD)** | η ≈ 30% (a=0.5), η ≈ 140% (a=0.99) | Tchekhovskoy et al. (2010), ApJ, 711, 50 | P_BZ power extraction efficiency (Section 2.1) |
| **CT18 NNLO PDFs** | L_gg(τ=10^-2) ≈ 10^-3 - 10^-4 | Hou et al. (2019), Phys. Rev. D, 103, 014013 | Parton luminosity reduction factor (Section 3.3) |
| **McKinney+ GRMHD** | B(r) ∝ r^-5/4 scaling | McKinney et al. (2012), MNRAS, 423, 3083 | Radial magnetic field profile (Eq. 18) |

═══════════════════════════════════════════════════════════════
5. NUMERICAL RESULTS SUMMARY
═══════════════════════════════════════════════════════════════

**Production Rates (Table 1, Section 5.1):**

| m_X [eV] | Median Ṅ_X [s^-1] | 16th Percentile | 84th Percentile | Uncertainty |
|----------|------------------|-----------------|-----------------|-------------|
| 10^15 | 8 × 10^12 | 2 × 10^10 | 4 × 10^15 | Factor of 250 |
| 10^16 | 2 × 10^10 | 5 × 10^7 | 1 × 10^13 | Factor of 200 |
| 10^17 | 5 × 10^7 | 1 × 10^5 | 3 × 10^10 | Factor of 300 |
| 10^18 | 1 × 10^5 | 2 × 10^2 | 6 × 10^7 | Factor of 300 |

**Maximum Lorentz Factors:**
- Electrons: γ_e,max = 10^6 - 10^7
- Protons: γ_p,max = 10^9 - 10^10

**Collision Energies:**
- √s_pp = 1.9 × 10^18 eV (for γ_p = 10^9)
- √s_ee = 1 × 10^12 eV (for γ_e = 10^6)

**EFT Validity:**
- √s / (0.1 M_Pl) ~ 10^-9 (valid by 9 orders of magnitude)

**Cosmic Abundance:**
- Ω_X^AGN ≲ 10^-10 Ω_DM (subdominant)

**Magnetic Fields:**
- B = 100 - 10,000 Gauss (range explored)

**Magnetization:**
- σ = 10 - 100 (typical values)

**Jet Parameters:**
- Opening angle θ_jet = 0.01 - 0.5 radians
- Bulk Lorentz factor Γ_bulk ~ 10
- Length scale L_jet ~ 10^17 cm (1 pc)

**MCMC Diagnostics:**
- Total samples: N = 5 × 10^6 (5 chains × 10^6 each)
- Gelman-Rubin: R̂ < 1.01 (converged)
- Effective sample size: N_eff > 10^4
- Autocorrelation time: τ < 100
- Random seeds: {42, 137, 271, 314, 628}

**Observational Limits:**
- Fermi-LAT: F_γ < 10^-11 erg/cm²/s
- IceCube: F_ν < 10^-6 ν/cm²/s (E > 1 TeV)
- Auger: E_cut ≲ 5 EeV

**UHDM Escape:**
- Optical depth: τ_X ~ 10^-14 << 1
- Escape velocity: v_esc ~ 0.1c
- UHDM velocity: v_X ~ c
- Thermalization time: t_therm ~ 10^21 s >> t_cross ~ 10^6 s

**Next-Generation Sensitivities:**
- CTA: 10× improvement above 100 GeV
- IceCube-Gen2: 10× neutrino sensitivity
- LISA: ~100 SMBH mergers/year

═══════════════════════════════════════════════════════════════
6. ASSUMPTIONS & APPROXIMATIONS
═══════════════════════════════════════════════════════════════

**CRITICAL ASSUMPTIONS:**

1. **"AGN jets are magnetically dominated (σ >> 1)"**
   - Location: Section 2, throughout
   - Justification: GRMHD simulations show MAD states achieve σ = 10-100
   - Literature: Tchekhovskoy et al. (2010, 2011)
   - Standard in field? YES - MAD models are widely accepted
   - What if wrong? If σ < 1, acceleration less efficient → lower γ_max → lower production rates

2. **"Contact interaction operators are adequate for EFT"**
   - Location: Section 3.1, Eq. 12
   - Justification: Dimension-6 operators dominate at √s << Λ
   - Standard in field? YES - standard SMEFT approach
   - What if wrong? Specific UV completions (SUSY, extra dimensions) give different C_i values

3. **"Parton-level processes dominate UHDM production"**
   - Location: Section 3.3
   - Justification: Highest energy collisions occur at parton level
   - Standard in field? YES - collider physics standard
   - What if wrong? Nuclear coherence effects could enhance cross sections

4. **"Jets are optically thin to UHDM (τ_X << 1)"**
   - Location: Section 5.3, Eq. 47
   - Justification: Calculated τ_X ~ 10^-14 for EFT cross sections
   - Standard in field? N/A - first calculation
   - What if wrong? UHDM could thermalize → different kinematics

5. **"Head-on collisions maximize production"**
   - Location: Section 2.3, Eq. 9
   - Justification: Worst-case (best-case?) for highest √s
   - Standard in field? YES - conservative estimate
   - What if wrong? Realistic angular distribution → lower average √s

6. **"AGN lifetimes ~ 10^7 years"**
   - Location: Section 5.2
   - Justification: Typical quasar duty cycle
   - Standard in field? YES - observational consensus
   - What if wrong? Longer lifetimes → higher integrated production

7. **"Cosmic AGN population ~ 10^6"**
   - Location: Section 5.2
   - Justification: Integration of AGN luminosity function
   - Standard in field? YES - consistent with surveys
   - What if wrong? Uncertainties < factor of 10

8. **"EFT cutoff Λ ~ M_Pl"**
   - Location: Section 3.1
   - Justification: Gravitational interactions expected at Planck scale
   - Standard in field? YES - minimal assumption
   - What if wrong? Lower Λ → EFT breaks down earlier

9. **"Wilson coefficients C_i = 10^-3 to 1"**
   - Location: Section 3.4, MCMC
   - Justification: Logarithmic prior spanning plausible range
   - Standard in field? YES - agnostic approach without UV completion
   - What if wrong? Specific models predict definite C_i values

10. **"Synchrotron + IC + curvature cooling dominate electrons"**
    - Location: Section 2.2.1, Eqs. 3-5
    - Justification: Standard radiative processes for relativistic electrons
    - Standard in field? YES - textbook physics (Rybicki & Lightman)
    - What if wrong? Additional cooling → lower γ_e,max

11. **"Magnetic reconnection efficiency η ~ 0.1"**
    - Location: Section 2.2, grmhd_acceleration.py
    - Justification: PIC simulations in relativistic regime
    - Standard in field? DEBATABLE - ranges from 0.01 to 0.5 in literature
    - What if wrong? Factor of 50 uncertainty in acceleration power

12. **"UHDM is stable on cosmological timescales"**
    - Location: Implicit throughout
    - Justification: Auger limits give τ_X > 10^21 yr
    - Standard in field? YES for superheavy DM
    - What if wrong? Decay products would be observable

13. **"Black hole spin a = 0.9 (typical)"**
    - Location: Section 2.1
    - Justification: Observational measurements of AGN BH spins
    - Standard in field? YES - typical range 0.7-0.99
    - What if wrong? Lower a → lower P_BZ → lower production rates

14. **"Radial profiles: n_p ∝ r^-2, B ∝ r^-5/4"**
    - Location: Section 3.2, Eq. 18
    - Justification: Mass continuity + GRMHD simulations (McKinney+ 2012)
    - Standard in field? YES for jet models
    - What if wrong? Different profiles → different integrated rates

15. **"We neglect bremsstrahlung cooling"**
    - Location: Implicit (not mentioned in cooling equations)
    - Justification: Negligible compared to synchrotron at γ > 10^6
    - Standard in field? YES - subdominant for ultra-relativistic particles
    - What if wrong? Minimal impact (bremsstrahlung ∝ γ vs synchrotron ∝ γ^2)

═══════════════════════════════════════════════════════════════
7. COMPARISON TO LITERATURE
═══════════════════════════════════════════════════════════════

**Direct Comparisons Made in Paper:**

1. **"γ_e,max consistent with Fermi-LAT TeV blazars"**
   - Location: Section 2.2.1, line 102
   - Comparison: "Our γ_e,max ~ 10^6-10^7 vs Fermi requires γ_e ≳ 3×10^5"
   - Agreement: YES - predictions consistent
   - Reference: Ajello et al. (2017), ApJS, 232, 18

2. **"γ_p,max consistent with UHECR observations"**
   - Location: Section 2.2.2, line 120
   - Comparison: "Our γ_p,max ~ 10^9-10^10 gives E_p ~ 10^18-10^19 eV vs Auger GZK cutoff at 5 EeV"
   - Agreement: YES - consistent with GZK regime
   - Reference: Auger Collaboration (2020), Phys. Rev. D, 102, 062005

3. **"EFT validity vastly satisfied"**
   - Location: Section 2.3, line 143
   - Comparison: "√s ~ 10^18 eV vs 0.1 M_Pl = 1.22×10^27 eV → valid by 10^9"
   - Agreement: YES - well within validity
   - Distinguishes from trans-Planckian scenarios

4. **"PDF corrections reduce naive estimates"**
   - Location: Section 3.3, line 197
   - Comparison: "CT18 NNLO gives L_gg ~ 10^-3-10^-4, reducing rates by 30-100×"
   - Agreement with CT18: YES
   - Previous work: Many studies used naive parton approximations without PDF integration
   - Reference: Hou et al. (2019), Phys. Rev. D, 103, 014013

5. **"IceCube neutrino limits consistent"**
   - Location: Section 4.2, line 242
   - Comparison: "IceCube limits blazars to ≤11-15% of diffuse flux vs our predictions"
   - Agreement: YES - predictions below limits
   - Reference: IceCube Collaboration (2024), arXiv:2410.18184

6. **"Distinguished from UHDM detection studies"**
   - Location: Section 1.1, line 51
   - Comparison: "This work calculates PRODUCTION vs Gorchtein+ (2010) & Wang+ (2024) study SCATTERING"
   - Agreement: N/A - different physics
   - References: Gorchtein & Kopp (2010), Phys. Rev. D, 82, 055014; Wang et al. (2024)

**Literature Gaps Identified:**

- "No previous work on AGN jets as PRIMARY production sites" (line 51)
- "First multi-messenger framework for UHDM production" (implicit throughout Section 4)
- "First LISA-correlated UHDM burst prediction" (Section 5.4.2)

═══════════════════════════════════════════════════════════════
8. UNCERTAINTY QUANTIFICATION
═══════════════════════════════════════════════════════════════

**How Uncertainties Are Calculated:**

1. **Monte Carlo Parameter Scan (Primary Method)**
   - Tool: emcee (affine-invariant MCMC)
   - Samples: 5 chains × 10^6 samples = 5×10^6 total
   - Parameters varied: M_X, C_i, σ, θ_jet, B
   - Priors: Logarithmic (Jeffreys) for scale-invariance
   - Convergence: Gelman-Rubin R̂ < 1.01
   - Uncertainty bands: 16th-84th percentiles (68% CI)
   - Code: monte_carlo_sampling.py

2. **Statistical Errors**
   - MCMC sampling uncertainty: Quantified via posterior width
   - Example: For m_X = 10^17 eV, Ṅ_X spans 10^5 to 10^10 (5 orders)
   - Quoted as 68% confidence intervals

3. **Systematic Errors**
   - **Magnetic field uncertainty**: B = 100-10,000 G → factor of 100
   - **PDF uncertainties**: CT18 error bands → factor of 3-10 at high x
   - **Magnetization σ**: Range 10-100 → factor of 10
   - **Reconnection efficiency η**: Literature range 0.01-0.5 → factor of 50
   - **EFT coupling C_i**: Range 10^-3 to 1 → factor of 1000 in σ ∝ C_i^2
   - **Jet geometry**: θ_jet = 0.01-0.5 rad → factor of 50 in solid angle

4. **Total Systematic Uncertainty**
   - Quoted as "factor-of-10^3" throughout paper
   - Dominated by: EFT coupling (×10^3), magnetic field (×100), reconnection efficiency (×50)
   - Propagated through MCMC by sampling all parameters simultaneously

5. **Parameter Scan Ranges (MCMC Priors)**
   - log₁₀(M_X/GeV) ~ U(2, 5) → 100 GeV to 100 TeV
   - log₁₀(g_eff) ~ U(-2, 1) → 0.01 to 10
   - log₁₀(σ) ~ U(-1, 2) → 0.1 to 100
   - θ_jet ~ U(0.01, 0.5) radians
   - Code: monte_carlo_sampling.py, lines 40-56

6. **Observational Constraint Uncertainties**
   - Fermi-LAT flux: ±30% typical systematic (catalog uncertainties)
   - IceCube neutrino: ±20-50% depending on energy
   - Auger UHECR: ±15% energy scale uncertainty

**Sources of Uncertainty Listed in Paper (Section 5.5):**

1. Multi-zone approximation: Factor of 3
2. PDF uncertainties at x ~ 10^-2: Factor of 3
3. EFT coupling uncertainty: Factor of 10^3 (in rate ∝ C_i^2)
4. Jet microphysics (η): Factor of 50
5. UV completion unknown: Cannot predict definite C_i values

═══════════════════════════════════════════════════════════════
9. RED FLAGS FOR PHYSICS REVIEW
═══════════════════════════════════════════════════════════════

**SUSPICIOUS / POTENTIALLY PROBLEMATIC ITEMS:**

🚩 **RED FLAG 1: EFT Efficiency >100%**
- Location: Section 2.1, line 67
- Claim: "η ≈ 140% for a=0.99"
- Issue: How can efficiency exceed 100%?
- Explanation: Paper cites Tchekhovskoy+ (2010) - likely refers to ratio of jet power to accretion power (not BH rotational energy)
- **NEEDS CLARIFICATION**: Is this a misstatement or genuine >100% extraction relative to accretion power?

🚩 **RED FLAG 2: Factor-of-10^3 Uncertainty Span**
- Location: Throughout (Abstract, Section 5.5)
- Claim: "Factor-of-10^3 systematic uncertainties"
- Issue: With 3 orders of magnitude uncertainty, are predictions meaningful?
- Defense: Paper explicitly acknowledges this and emphasizes "improvability over precision"
- **QUESTION**: Is this honest transparency or admission of non-falsifiability?

🚩 **RED FLAG 3: PDF Extrapolation to 10^18 eV**
- Location: Section 3.3, line 197
- Claim: "CT18 NNLO PDFs applied at √s ~ 10^18 eV"
- Issue: CT18 NNLO fitted to collider data up to √s ~ 10^4 GeV (LHC)
- Extrapolation: 14 orders of magnitude beyond training data!
- **MAJOR CONCERN**: Are PDF predictions reliable at 10^14× higher energies?
- Paper's Defense: Uses conservative estimates and propagates uncertainties

🚩 **RED FLAG 4: Cosmic Abundance "Subdominant by 10^10"**
- Location: Section 5.2, Eq. 45
- Claim: "Ω_X^AGN ≲ 10^-10 Ω_DM"
- Issue: If AGN contribution is 10^-10 of DM, why does this matter?
- Defense: Paper emphasizes unique observational signatures (spatial clustering, GW correlation)
- **QUESTION**: Is 10^-10 contribution detectable in practice?

🚩 **RED FLAG 5: No Direct Detection Possible**
- Location: Section 5.4.3, Eq. 56
- Claim: "Detection requires σ_X ≳ 3×10^-16 cm^2, 14 orders above weak scale"
- Issue: If undetectable, how is this falsifiable?
- Defense: Paper emphasizes indirect tests via multi-messenger signals
- **QUESTION**: Are indirect tests truly constraining?

🚩 **RED FLAG 6: Head-On Collision Assumption**
- Location: Section 2.3, Eq. 9
- Claim: √s calculated for head-on collisions
- Issue: Realistic angular distribution → much lower average √s
- Paper's Defense: Provides upper limit on production rates
- **QUESTION**: Should paper quote realistic angle-averaged rates?

🚩 **RED FLAG 7: Single-Zone → Multi-Zone "Improvement"**
- Location: Section 3.2, Eq. 17
- Claim: Spatial integration "improves" single-zone estimate
- Issue: Does integration actually change rates significantly?
- **QUESTION**: What's the quantitative difference between single-zone and integrated results?
- Paper doesn't explicitly show comparison

🚩 **RED FLAG 8: Magnetization σ = 10-100 Range**
- Location: Throughout
- Claim: "σ >> 1 jets from GRMHD simulations"
- Issue: σ = 10 is only moderately >> 1
- Literature Check: Some jets may have σ ~ 1 or even σ < 1
- **QUESTION**: Are all AGN jets magnetically dominated?

🚩 **RED FLAG 9: No Comparison to Primordial UHDM Production**
- Location: Section 5.2
- Claim: AGN production is "subdominant" to primordial
- Issue: No quantitative comparison to gravitational production rates from inflation
- **MISSING**: Expected Ω_X from gravitational particle creation for comparison

🚩 **RED FLAG 10: MCMC Priors May Bias Results**
- Location: Section 3.4, monte_carlo_sampling.py
- Claim: Jeffreys (log-uniform) priors for scale invariance
- Issue: Log priors strongly favor smaller values
- Example: log₁₀(C_i) ~ U(-3, 0) → median C_i ~ 10^-1.5 ≈ 0.03
- **QUESTION**: Do prior choices bias production rate estimates low?

**INTERNAL CONSISTENCY CHECKS:**

✓ **Units Check**: All equations dimensionally correct (checked against submission checklist)
✓ **Cross-References**: Equation numbers, figure references all resolve
❓ **Numerical Consistency**: Table 1 production rates vs Eq. 45 cosmic abundance - need to verify calculation
❓ **Figure-Text Agreement**: Do figures show the claimed ranges? (Figures not generated yet)

═══════════════════════════════════════════════════════════════
10. QUESTIONS FOR EXPERT REVIEW
═══════════════════════════════════════════════════════════════

**ASTROPHYSICS & JET PHYSICS:**

1. **Is a magnetization parameter σ = 10-100 reasonable for ALL AGN jets?**
   - What fraction of AGN jets are truly magnetically dominated?
   - Could σ < 1 jets contribute? How would that change results?

2. **Is the magnetic field range B = 100-10,000 G justified?**
   - What observational constraints exist on B in AGN jet bases?
   - How does B vary with jet type (radio-loud vs radio-quiet, FRI vs FRII)?

3. **Is magnetic reconnection efficiency η = 0.1 a good estimate?**
   - What do PIC simulations actually predict for relativistic reconnection?
   - Could η be as low as 0.01 or as high as 0.5? Impact on γ_max?

4. **Are the Lorentz factor predictions γ_e ~ 10^6-10^7, γ_p ~ 10^9-10^10 realistic?**
   - Do Fermi-LAT and Auger observations truly require these values?
   - Alternative acceleration mechanisms (shear, turbulence)?

5. **Is the Blandford-Znajek mechanism the dominant power source?**
   - Contribution from accretion disk vs BH spin extraction?
   - How does this vary with BH mass and accretion rate?

6. **Is η ≈ 140% for a=0.99 a typo or genuine?**
   - What does >100% efficiency mean physically?
   - Is this jet power / accretion power (not BH rotation power)?

7. **Are AGN lifetimes ~ 10^7 years accurate?**
   - Difference between quasar lifetimes and radio AGN?
   - Duty cycle vs. total lifetime?

8. **Is the radial scaling B(r) ∝ r^-5/4 robust?**
   - Do all GRMHD simulations agree on this power law?
   - Alternatives: r^-1 (monopole), r^-2 (dipole)?

**PARTICLE PHYSICS & EFT:**

9. **Is the EFT cutoff scale Λ ~ M_Pl justified for UHDM?**
   - Could Λ be much lower (e.g., string scale ~ 10^16 GeV)?
   - How would lower Λ affect EFT validity?

10. **Are dimension-6 contact operators adequate?**
    - Should dimension-8 operators be included at √s ~ 10^18 eV?
    - When do higher-order terms become important?

11. **Is the Wilson coefficient range C_i = 10^-3 to 1 reasonable?**
    - What do specific UV completions (SUSY, extra dimensions, string theory) predict?
    - Could C_i be much smaller (e.g., 10^-6) or larger (e.g., 10)?

12. **Is gluon-gluon fusion the dominant channel?**
    - Quark-antiquark annihilation contribution?
    - Photon-photon fusion at high energies?

13. **Are CT18 NNLO PDFs reliable at √s ~ 10^18 eV?**
    - What's the expected uncertainty from extrapolating 14 orders of magnitude?
    - Alternative: Use DGLAP evolution to predict PDFs at ultra-high Q^2?

14. **Should synchrotron cooling of produced UHDM be considered?**
    - Even if weakly coupled, do magnetic fields affect UHDM trajectories?

**COSMOLOGY & DARK MATTER:**

15. **Is Ω_X^AGN ~ 10^-10 Ω_DM detectable?**
    - What's the expected spatial distribution?
    - Concentrated around massive galaxies - observable in structure?

16. **How does AGN-produced UHDM compare to primordial gravitational production?**
    - What's the expected Ω_X from inflation for m_X = 10^15-10^18 eV?
    - Ratio of astrophysical to primordial?

17. **Could AGN-produced UHDM have different velocity distribution?**
    - Higher velocity dispersion due to recent production?
    - Impact on direct detection (if cross sections were higher)?

18. **Are there other astrophysical production sites?**
    - Supernovae? Gamma-ray bursts? Neutron star mergers?
    - How do AGN jets compare?

**OBSERVATIONAL TESTS:**

19. **Are the Fermi-LAT energy budget constraints accurate?**
    - How much energy can be diverted to UHDM production vs observed γ-rays?
    - Is f_budget = 0.01 (1%) a reasonable limit?

20. **Can IceCube-Gen2 actually constrain these models?**
    - What's the expected neutrino signal from UHDM production/decay?
    - Correlated with AGN positions?

21. **Is the LISA-GW correlation signal realistic?**
    - Do SMBH mergers actually trigger AGN jets?
    - Time delay between GW and jet formation?
    - N_X^burst ~ 10^21 particles - how would this manifest?

22. **What would CTA observations tell us?**
    - Can CTA constrain γ_e,max to factor-of-3 as claimed?
    - Distinguishing UHDM production from standard blazar emission?

**METHODOLOGY & STATISTICS:**

23. **Is factor-of-10^3 uncertainty acceptable for a physics prediction?**
    - At what point does a prediction become non-falsifiable?
    - Paper emphasizes "improvability" - is this sufficient?

24. **Are the MCMC priors appropriate?**
    - Do log-uniform priors bias results toward small C_i?
    - Alternative: Uniform priors in C_i (not log C_i)?

25. **Is spatial integration (multi-zone vs single-zone) significant?**
    - What's the quantitative difference in production rates?
    - Paper doesn't show explicit comparison - should it?

26. **Are there missing physics effects?**
    - Photon-photon pair production background?
    - Bethe-Heitler pair production?
    - Plasma effects at high density?

**VALIDITY & FALSIFIABILITY:**

27. **Is this framework truly falsifiable?**
    - With 10^3 uncertainties and no direct detection, what observation could disprove it?
    - Or is this more of an exploratory framework?

28. **What specific prediction is most testable?**
    - LISA-GW correlation?
    - Spatial clustering around massive galaxies?
    - CTA γ-ray limits?

29. **How does this compare to WIMP searches?**
    - WIMPs have null results after decades - could this be similar?
    - What's the discovery timeline if this is correct?

30. **What's the "smoking gun" for astrophysical UHDM production?**
    - Time-correlated GW+UHDM signal?
    - Spatial correlation with AGN?
    - Kinematic signatures?

═══════════════════════════════════════════════════════════════
END OF PHYSICS CLAIMS FOR REVIEW
═══════════════════════════════════════════════════════════════
