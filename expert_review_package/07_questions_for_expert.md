# QUESTIONS FOR EXPERT PHYSICS REVIEW
**30 Critical Questions Requiring Domain Expertise**
**Generated: 2025-11-02**

---

## CATEGORY 1: ASTROPHYSICS & JET PHYSICS (Questions 1-8)

### Q1: Is magnetization parameter σ = 10-100 reasonable for ALL AGN jets?
**Context**: Paper assumes σ = 10-100 throughout, citing GRMHD MAD simulations.

**Specific sub-questions**:
- What fraction of AGN jets are in MAD (magnetically arrested disk) state?
- Do FRI (low-power) and FRII (high-power) jets have different σ?
- Could σ < 1 jets (magnetically weak) also contribute? How would results change?
- Observational constraints on σ for individual AGN?

**Why this matters**: If only 20% of AGN are MAD, cosmic production rates drop by factor of 5.

---

### Q2: Is magnetic field range B = 100-10,000 G observationally justified?
**Context**: Paper scans B = 10^2 - 10^4 G in MCMC.

**Specific sub-questions**:
- What are typical B values near jet base (r ~ 10-100 r_g)?
- How is B measured? (Synchrotron self-absorption? VLBI Faraday rotation?)
- Does B vary by AGN class (blazars vs radio galaxies)?
- Could B be systematically lower/higher than this range?

**Why this matters**: γ_max ∝ B^-1 (synchrotron cooling), so B uncertainty propagates directly to production rates.

---

### Q3: Is magnetic reconnection efficiency η = 0.1 accurate?
**Context**: Paper uses η ~ 0.1 for particle acceleration efficiency, with literature range 0.01-0.5.

**Specific sub-questions**:
- What do PIC (particle-in-cell) simulations predict for relativistic reconnection with σ >> 1?
- Does η depend on σ (magnetization), guide field, or other parameters?
- Observational constraints on η from jet observations?
- Could η be much lower (~0.01) or higher (~0.5)? Impact on γ_max?

**Why this matters**: Factor-of-50 uncertainty in η → factor-of-50 in acceleration power → huge uncertainty in rates.

---

### Q4: Are Lorentz factor predictions γ_e ~ 10^6-10^7, γ_p ~ 10^9-10^10 realistic?
**Context**: Paper calculates these from GRMHD + cooling balance.

**Specific sub-questions**:
- Do Fermi-LAT TeV blazar observations truly require γ_e ≳ 10^6?
- Do UHECR observations from Auger require γ_p ~ 10^9-10^10?
- Alternative acceleration mechanisms: Shear? Turbulence? Stochastic? How do they compare?
- Could γ_max be systematically lower due to missing cooling processes?

**Why this matters**: √s ∝ γ, so if γ_p is 10× lower, production rates drop by factor of 10^4 (rate ∝ s^2 ∝ γ^4).

---

### Q5: Is Blandford-Znajek mechanism the dominant power source?
**Context**: Paper uses P_BZ = κΩ_H^2 Φ_BH^2 / (4πc) for jet power.

**Specific sub-questions**:
- Contribution from accretion disk (Blandford-Payne mechanism) vs BH spin (BZ)?
- How does dominance vary with BH mass, accretion rate, spin?
- Are there AGN classes where BZ is NOT dominant?

**Why this matters**: If BZ is only 50% of jet power, production rates drop by factor of 2.

---

### Q6: Is η ≈ 140% for a=0.99 a typo or genuine physics?
**Context**: Section 2.1, line 67 claims efficiency can exceed 100%.

**Specific sub-questions**:
- What does η > 100% mean physically?
- Is this ratio of jet power to accretion power (not BH spin energy)?
- Can we extract more energy from BH spin than is accreted?
- Should paper clarify this definition?

**Why this matters**: If typo, credibility issue. If genuine, needs clear physical explanation.

---

### Q7: Are AGN lifetimes ~ 10^7 years accurate?
**Context**: Used in Eq. 45 to calculate cosmic abundance.

**Specific sub-questions**:
- Difference between quasar lifetimes and radio AGN lifetimes?
- Duty cycle vs total lifetime - which should be used?
- Does lifetime vary with AGN class, redshift, BH mass?

**Why this matters**: If lifetime is 10^8 years (10× longer), cosmic abundance increases by factor of 10.

---

### Q8: Is radial scaling B(r) ∝ r^-5/4 robust across all jets?
**Context**: Used in spatial integration (Eq. 17), citing McKinney+ 2007.

**Specific sub-questions**:
- Do all GRMHD simulations agree on this power law?
- Alternatives: r^-1 (monopole), r^-2 (dipole), r^-1 (conical jet)?
- Does power law hold over entire range r_min = 10 r_g to r_max = 1 pc?

**Why this matters**: Different B(r) scaling → different integrated production rates (possibly factor of 2-5).

---

## CATEGORY 2: PARTICLE PHYSICS & EFT (Questions 9-14)

### Q9: Is EFT cutoff scale Λ ~ M_Pl justified for UHDM production?
**Context**: Paper assumes Λ = 1.22 × 10^19 GeV (Planck scale).

**Specific sub-questions**:
- Could Λ be much lower? (e.g., string scale ~ 10^16 GeV, GUT scale ~ 10^16 GeV?)
- How would lower Λ affect EFT validity at √s ~ 10^18 eV?
- Should paper scan over Λ as additional parameter?
- What do specific UV completions (SUSY, extra dimensions) predict for Λ?

**Why this matters**: If Λ ~ 10^16 GeV, then √s ~ 10^18 eV = 10^9 GeV is only factor of 10^7 below Λ, not 10^9. EFT validity marginal!

---

### Q10: Are dimension-6 contact operators adequate at √s ~ 10^18 eV?
**Context**: Paper uses L_eff = L_SM + Σ (C_i / Λ^2) O_i^(6) + O(Λ^-4).

**Specific sub-questions**:
- When do dimension-8 operators become important?
- Naive estimate: dim-8 / dim-6 ~ (√s / Λ)^2. For √s/Λ ~ 10^-9, ratio is 10^-18 (negligible). But if Λ lower?
- Should paper include O(Λ^-4) corrections?

**Why this matters**: If dim-8 operators matter, cross sections change significantly.

---

### Q11: Is Wilson coefficient range C_i = 10^-3 to 1 reasonable?
**Context**: MCMC samples log₁₀(C_i) ~ U(-3, 0).

**Specific sub-questions**:
- What do specific models predict?
  - SUSY: C_i ~ α_s / (16π^2) ~ 10^-3 (loop-suppressed)
  - Extra dimensions: C_i ~ 1 (tree-level)
  - String theory: C_i ~ g_s ~ 0.1-1
- Should paper distinguish between different operators (vector, scalar, tensor)?
- Are all C_i expected to be similar, or could some be 0 and others O(1)?

**Why this matters**: If all operators have C_i ~ 10^-3 (loop-suppressed), rates drop by factor of 10^6 compared to C_i ~ 1!

---

### Q12: Is gluon-gluon fusion the dominant UHDM production channel?
**Context**: Paper emphasizes gg → XX via contact operators.

**Specific sub-questions**:
- Quark-antiquark annihilation contribution (q q̄ → XX)?
- At √s ~ 10^18 eV, which parton luminosity is larger: L_gg or L_qq̄?
- Photon-photon fusion (γγ → XX) at high energies?
- W/Z boson fusion?

**Why this matters**: If quark channels dominate, PDF extrapolation is different (valence vs sea quarks).

---

### Q13: Are CT18 NNLO PDFs reliable at √s ~ 10^18 eV?
**Context**: CT18 fitted to LHC data at √s ≤ 13 TeV. This extrapolates to 10^9 TeV!

**Specific sub-questions**:
- What are CT18 error bands at x ~ 10^-2, Q^2 ~ (10^17 eV)^2 = 10^34 GeV^2?
- Can DGLAP evolution predict PDFs at Q^2 >> LHC scales? Reliability?
- Alternative: Use Froissart bound (total cross section growth ≤ log^2 s)?
- Should paper use different PDF sets (NNPDF, MMHT, HERAPDF) for comparison?

**Why this matters**: PDF uncertainties at these scales could be factor of 10-100, not factor of 3 as claimed!

---

### Q14: Should synchrotron cooling of produced UHDM be considered?
**Context**: Paper assumes UHDM escapes jet without radiating.

**Specific sub-questions**:
- Even if weakly coupled, does UHDM have charge under U(1)_EM or SU(3)_c?
- If so, synchrotron losses in jet B-field?
- If UHDM is composite (e.g., UHDM bound state), does it have magnetic moment?

**Why this matters**: If UHDM radiates, energy loss → different kinematics and observational signatures.

---

## CATEGORY 3: COSMOLOGY & DARK MATTER (Questions 15-18)

### Q15: Is Ω_X^AGN ~ 10^-10 Ω_DM detectable or relevant?
**Context**: Paper calculates cosmic abundance is 10^-10 of dark matter.

**Specific sub-questions**:
- At what level does a subdominant DM component affect structure formation?
- Could 10^-10 Ω_DM be seen in:
  - CMB (Planck)?
  - Large-scale structure (DESI, Euclid)?
  - Galaxy clustering?
- Or is 10^-10 simply too small to ever matter?

**Why this matters**: If completely undetectable and irrelevant, why publish this result?

---

### Q16: How does AGN-produced UHDM compare to primordial gravitational production?
**Context**: Paper claims AGN is "subdominant to primordial mechanisms" but doesn't calculate primordial rate!

**Specific sub-questions**:
- Gravitational particle creation during inflation: Ω_X ~ (m_X / M_Pl)^2 × (H_I / M_Pl)^2 × N_reheating
- For m_X = 10^17 eV, H_I ~ 10^14 GeV: What is Ω_X^primordial?
- Is primordial production 10^-50 (way below AGN) or 10^-5 (way above AGN)?
- If AGN actually dominates, does that change the paper's conclusions?

**Why this matters**: CRITICAL! If AGN dominates over primordial, this is huge news. If not, need to show the numbers.

---

### Q17: Does AGN-produced UHDM have different velocity distribution than primordial?
**Context**: Paper mentions "unique kinematic signatures" (line 48).

**Specific sub-questions**:
- Primordial UHDM: Produced at rest in early universe → cold (v ~ 0)
- AGN UHDM: Produced with v ~ c → hot? Does it cluster?
- How does velocity distribution evolve over cosmic time?
- Could higher v_X affect direct detection rates (if detectable)?

**Why this matters**: Kinematic differences are key distinguisher between astrophysical and primordial UHDM.

---

### Q18: Are there other astrophysical UHDM production sites?
**Context**: Paper focuses on AGN jets exclusively.

**Specific sub-questions**:
- Supernovae: Core-collapse SNe reach ρ ~ 10^15 g/cm^3, T ~ 10 MeV → √s?
- Gamma-ray bursts: Relativistic jets with γ ~ 100-1000 → lower √s than AGN
- Neutron star mergers: Kilonova jets, magnetar formation
- Pulsar magnetospheres: B ~ 10^12-10^15 G → higher acceleration?
- Cosmological phase transitions: Electroweak, QCD

**Why this matters**: If pulsars or NS mergers dominate, AGN contribution is further subdominant.

---

## CATEGORY 4: OBSERVATIONAL TESTS (Questions 19-24)

### Q19: Are Fermi-LAT energy budget constraints accurate?
**Context**: Paper uses Ṅ_X < ε_γ P_BZ / m_X with ε_γ ~ 0.01.

**Specific sub-questions**:
- How much energy can be diverted to UHDM production without affecting observed γ-ray spectra?
- Is f_budget = 1% a conservative limit, or could it be 10% or 0.1%?
- Do different AGN classes have different f_budget?

**Why this matters**: If f_budget = 10%, rates can be 10× higher before violating Fermi limits.

---

### Q20: Can IceCube-Gen2 actually constrain these models?
**Context**: Paper predicts 10× improvement will constrain γ_p,max to ~50%.

**Specific sub-questions**:
- What is expected neutrino signal from UHDM production? (Ṅ_X particles → ν via decay?)
- Would neutrino signal be correlated with AGN positions?
- Or does paper mean IceCube constrains proton acceleration (indirectly constraining environment)?

**Why this matters**: Unclear how IceCube directly tests UHDM production vs jet physics in general.

---

### Q21: Is LISA-GW correlation signal realistic?
**Context**: Paper proposes SMBH mergers → jet formation → UHDM bursts correlated with GW events.

**Specific sub-questions**:
- Do SMBH mergers always trigger AGN jets? (Observational evidence?)
- Time delay between GW event and jet formation: Seconds? Years?
- Requires: (1) LISA detects merger, (2) jet forms, (3) UHDM is produced, (4) UHDM detector sees it, (5) time correlation is significant
- Probability of all 5 happening?

**Why this matters**: If probability is < 1%, need > 100 SMBH mergers to test. Feasible?

---

### Q22: Can CTA constrain γ_e,max to factor-of-3 as claimed?
**Context**: Section 5.4.1 claims "CTA will constrain γ_e,max to ~30%."

**Specific sub-questions**:
- CTA measures γ-ray flux vs energy → high-energy cutoff
- Cutoff depends on: γ_e,max, B, Doppler factor δ, viewing angle θ
- Degeneracies: Different (γ_e,max, B, δ) give same spectrum
- How to break degeneracies? Multi-wavelength? VLBI?

**Why this matters**: Without breaking degeneracies, CTA constrains only combinations like γ_e,max × B^1/2.

---

### Q23: What would CTA/IceCube/Auger observations tell us about UHDM production?
**Context**: Paper claims multi-messenger "falsifiability."

**Specific sub-questions**:
- Are these experiments measuring UHDM directly or just jet physics?
- If CTA sees higher γ-ray flux, does that mean more UHDM or just higher γ_e,max?
- Can any multi-messenger observation distinguish UHDM production from standard jet emission?

**Why this matters**: If experiments only constrain jet physics (not UHDM), framework is not falsifiable.

---

### Q24: What's the "smoking gun" signature for astrophysical UHDM production?
**Context**: Paper emphasizes distinguishing astrophysical from primordial UHDM.

**Specific sub-questions**:
- Spatial clustering: Around massive galaxies (AGN hosts) - detectable how?
- Kinematic signatures: Higher velocity dispersion - measurable how?
- GW correlation: LISA + UHDM detector - but no UHDM detector exists!
- Time variability: AGN jets turn on/off on ~10^6 yr timescales - relevant?

**Why this matters**: Need ONE clear, unique signature. What is it?

---

## CATEGORY 5: METHODOLOGY & STATISTICS (Questions 25-27)

### Q25: Is factor-of-10^3 uncertainty acceptable for a physics prediction?
**Context**: Abstract emphasizes "factor-of-10^3 systematic uncertainties."

**Specific sub-questions**:
- At what point does a prediction become non-falsifiable due to uncertainty?
- Comparison: Particle physics (1-10%), cosmology (factor of 2-3), astrophysics (factor of 10)
- Does spanning 10^10 s^-1 to 10^13 s^-1 (factor of 1000) constitute a prediction?
- Or is this an exploratory framework, not a quantitative prediction?

**Why this matters**: Philosophical question about what constitutes "science" vs "speculation."

---

### Q26: Are MCMC priors appropriate? Do they bias results?
**Context**: Log-uniform priors on C_i, B, σ.

**Specific sub-questions**:
- Do log-uniform priors favor small values? (Median of log-U(10^-3, 1) is 10^-1.5 ≈ 0.03)
- Should paper use uniform (not log-uniform) priors on physical parameters?
- Prior predictive check: Do priors match physical expectations?
- Posterior sensitivity: How much do results depend on prior choice?

**Why this matters**: If priors bias C_i toward 10^-2 instead of 10^0, production rates are 10^4 lower!

---

### Q27: Is spatial integration (multi-zone) significantly different from single-zone?
**Context**: Paper implements Eq. 17 (spatial integration) as "improvement."

**Specific sub-questions**:
- What is Ṅ_X(single-zone) vs Ṅ_X(multi-zone) numerically?
- Does integration change results by factor of 2? 10? 100?
- If factor of 2, is this "improvement" significant given 10^3 total uncertainty?

**Why this matters**: If multi-zone gives same answer within factor of 2, single-zone was adequate.

---

## CATEGORY 6: VALIDITY & FALSIFIABILITY (Questions 28-30)

### Q28: Is this framework truly falsifiable (Popper criterion)?
**Context**: Large uncertainties + no direct detection + indirect tests that measure jet physics.

**Specific sub-questions**:
- What observation would definitively disprove this framework?
- If future experiments are consistent with predictions (within factor of 10^3!), does that validate it?
- Or can any observation be accommodated by adjusting C_i, B, σ within prior ranges?

**Why this matters**: Falsifiability is demarcation between science and pseudoscience.

---

### Q29: What specific prediction is MOST testable with current/near-future experiments?
**Context**: Paper lists many observables (CTA, IceCube, LISA).

**Specific sub-questions**:
- Which experiment gives tightest constraint with least degeneracies?
- Rank experiments by "testability":
  1. Fermi-LAT energy budget: Already tested (predictions consistent)
  2. CTA γ-ray spectrum: Future, but degeneracies with B, δ
  3. IceCube-Gen2 neutrinos: Future, indirect constraint on jets
  4. LISA + UHDM detector: Far future, detector doesn't exist

**Why this matters**: Focus on most testable prediction for near-term falsification.

---

### Q30: How does this compare to WIMP searches?
**Context**: WIMPs: Decades of null results in direct detection, indirect detection, colliders.

**Specific sub-questions**:
- Is UHDM similar to WIMPs: Theoretically motivated but experimentally elusive?
- If no discovery in 10-20 years, will this be abandoned like WIMPs?
- What's the timeline for discovery if this is correct?
- Could this be another "SUSY problem" - theoretically beautiful but not realized in nature?

**Why this matters**: Sociology of science. Should we invest resources in UHDM searches?

---

## SUMMARY: MOST CRITICAL QUESTIONS

**TOP 5 QUESTIONS THAT MUST BE ANSWERED:**

1. **Q13 (PDF extrapolation)**: Are CT18 PDFs reliable at √s ~ 10^18 eV? This affects results by potentially orders of magnitude.

2. **Q16 (Primordial comparison)**: Does AGN UHDM actually dominate over gravitational production? Paper claims "subdominant" but doesn't show numbers!

3. **Q25 (Falsifiability)**: Is factor-of-10^3 uncertainty acceptable for a scientific prediction?

4. **Head-on collisions (not in numbered list but in RED FLAGS)**: Angle-averaged rates could be 10^8-10^10 lower! This is CRITICAL.

5. **Q9 (EFT cutoff)**: If Λ ~ 10^16 GeV (not 10^19 GeV), EFT validity is marginal. Should paper scan Λ?

---

**If these 5 questions have satisfactory answers, the framework is defensible. If not, paper needs major revision.**

---

**END QUESTIONS FOR EXPERT REVIEW**
