# EXPERT REVIEW PACKAGE
**Ultra-Heavy Dark Matter Production in AGN Jets**
**Complete Package for Physics Expert Review**
**Generated: 2025-11-02**

---

## Purpose

This package contains all information extracted from the UHDM AGN paper for **independent physics verification** by domain experts. All claims, equations, assumptions, and numerical results have been systematically extracted and organized for review.

---

## Package Contents

### **00_OVERVIEW.md**
**Executive summary of the entire paper**
- 30-second summary
- Key numbers at a glance
- Novel contributions
- Methodology overview
- Main results
- Critical assumptions
- Potential red flags (brief)
- Questions requiring expert input (summary)
- Bottom line recommendation

**USE THIS FIRST** - Get oriented before diving into details.

---

### **01_all_claims.csv**
**Every quantitative claim in the paper (30 claims total)**

Format:
- Claim number
- Claim statement (exact quote)
- Location in paper (section, equation, line number)
- Supporting code/calculation
- Value/range
- Uncertainty

**USE THIS** to verify each claim independently. Check literature, do order-of-magnitude calculations, compare to other work.

---

### **02_key_equations.md** [See 07_physics_claims_for_review.md Section 2]
**All important equations with full context**

For each equation:
- LaTeX source (copy-pasteable)
- Equation number in paper
- Purpose (what it calculates)
- Input parameters (with values used)
- Output values obtained
- Literature source (if cited)
- Code location (if applicable)

Includes:
- Blandford-Znajek power (Eq. 1)
- Maximum Lorentz factors (Eqs. 6-7)
- Center-of-mass energies (Eq. 9)
- EFT validity (Eq. 11)
- EFT cross sections (Eq. 14)
- Spatial integration (Eq. 17)
- Parton luminosity (Eq. 19)
- Cosmic abundance (Eq. 45)
- UHDM escape (Eq. 47)
- And more...

**USE THIS** to check dimensional analysis, verify algebra, assess physical reasonableness.

---

### **03_numerical_results.csv**
**All numerical values extracted from paper in machine-readable format**

Categories:
- Lorentz factors
- Collision energies
- Production rates
- Cosmic abundance
- Magnetic fields
- EFT parameters
- MCMC diagnostics
- Observational limits
- Future projections

**USE THIS** to:
- Import into analysis tools (Python, Mathematica, etc.)
- Cross-check internal consistency
- Compare to your own calculations
- Verify error propagation

---

### **04_code_analysis.txt** [See manuscript code/ directory]
**Analysis of Python implementation**

Modules:
- `grmhd_acceleration.py` - Lorentz factor calculations
- `eft_cross_sections.py` - EFT production cross sections
- `pdf_integration.py` - Parton luminosity integration
- `monte_carlo_sampling.py` - MCMC parameter scan
- `observational_constraints.py` - Multi-messenger limits

**Key findings**:
- Functions used for each calculation
- Input parameters and their ranges
- Output values generated
- Random seeds for reproducibility
- NOTE: Code requires numpy/scipy (not installed in audit environment)

**USE THIS** to verify computational methodology, check for bugs, assess reproducibility.

---

### **05_assumptions_approximations.md** [See 07_physics_claims_for_review.md Section 6]
**Every assumption made in the paper (15 major assumptions)**

For each assumption:
- Statement (exact quote)
- Location in paper
- Justification provided
- Is it standard in the field?
- What would change if assumption is wrong?

Examples:
- "AGN jets are magnetically dominated (σ >> 1)"
- "Contact interaction operators are adequate for EFT"
- "Parton-level processes dominate UHDM production"
- "Jets are optically thin to UHDM"
- And 11 more...

**USE THIS** to identify weak points, challenge unjustified assumptions, suggest improvements.

---

### **06_red_flags.md**
**Suspicious items flagged for critical scrutiny (12 red flags)**

Categories:
1. Mathematical/physical inconsistencies (e.g., efficiency >100%)
2. Extrapolation beyond data (e.g., PDFs at 10^18 eV)
3. Uncertainty & falsifiability (e.g., factor-of-10^3 uncertainties)
4. Missing comparisons (e.g., no primordial UHDM calculation)
5. Prior/methodological biases (e.g., MCMC log priors)
6. Observational claims (e.g., CTA precision overstated)

For each red flag:
- Location in paper
- Issue description
- Analysis of problem
- Verdict (severity: low/medium/high/critical)
- Action for reviewer

**CRITICAL RED FLAGS:**
- Head-on collision assumption (may overestimate by 10^8-10^10!)
- PDF extrapolation (14 orders beyond LHC data)
- Primordial UHDM comparison missing
- Falsifiability with 10^3 uncertainties

**USE THIS** to focus your review on the most problematic claims.

---

### **07_questions_for_expert.md**
**30 specific questions requiring physics expertise**

Categories:
1. Astrophysics & jet physics (Q1-Q8)
2. Particle physics & EFT (Q9-Q14)
3. Cosmology & dark matter (Q15-Q18)
4. Observational tests (Q19-Q24)
5. Methodology & statistics (Q25-Q27)
6. Validity & falsifiability (Q28-Q30)

**TOP 5 MOST CRITICAL:**
1. Q13: Are CT18 PDFs reliable at √s ~ 10^18 eV?
2. Q16: Does AGN UHDM dominate over primordial production?
3. Q25: Is factor-of-10^3 uncertainty scientifically acceptable?
4. Q4: Are Lorentz factors γ_e ~ 10^6, γ_p ~ 10^9 realistic?
5. Q9: Is EFT cutoff Λ ~ M_Pl justified?

**USE THIS** as a checklist. Answer as many as possible. If TOP 5 don't have good answers, paper needs major revision.

---

## How to Use This Package

### **For Quick Review (30 minutes):**
1. Read `00_OVERVIEW.md` (10 min)
2. Skim `06_red_flags.md` - focus on CRITICAL flags (10 min)
3. Review `07_questions_for_expert.md` - TOP 5 questions (10 min)
4. **Decision**: Major concerns? → Full review. Minor concerns? → Accept with revisions.

---

### **For Thorough Review (2-4 hours):**
1. **Overview** (15 min): Read `00_OVERVIEW.md`
2. **Claims** (30 min): Go through `01_all_claims.csv` - pick 10 random claims, verify independently
3. **Equations** (45 min): Check `02_key_equations.md` [Section 2 of 07_physics_claims] - dimensional analysis, order-of-magnitude checks
4. **Red Flags** (45 min): Work through `06_red_flags.md` - assess severity, check if valid concerns
5. **Questions** (45 min): Answer as many of `07_questions_for_expert.md` as possible
6. **Final Synthesis** (30 min): Write review report based on findings

---

### **For Deep Dive (1-2 days):**
1. All of above
2. **Code Review**: Read Python modules (code/ directory in main repo)
3. **Literature Check**: Verify all citations, compare to similar work
4. **Independent Calculation**: Reproduce key results (γ_max, production rates, cosmic abundance)
5. **Alternative Models**: Test sensitivity to assumptions (non-MAD jets, different PDFs, etc.)
6. **Write Detailed Review**: With quantitative critiques and suggested improvements

---

## Key Files for Different Expertise

### **If you're an ASTROPHYSICIST:**
- Focus on: Lorentz factors (γ_max), jet physics (B, σ, η), GRMHD assumptions
- Read: Questions Q1-Q8, Red Flags #1, #4, #8
- Check: Sections 2.1-2.2 of paper

### **If you're a PARTICLE PHYSICIST:**
- Focus on: EFT framework, cross sections, PDF extrapolation, Wilson coefficients
- Read: Questions Q9-Q14, Red Flags #3, #10
- Check: Sections 3.1-3.3 of paper

### **If you're a COSMOLOGIST:**
- Focus on: Cosmic abundance, primordial production, DM signatures
- Read: Questions Q15-Q18, Red Flag #8
- Check: Section 5.2 of paper

### **If you're an EXPERIMENTALIST:**
- Focus on: Observational tests, falsifiability, multi-messenger constraints
- Read: Questions Q19-Q24, Red Flags #11, #12
- Check: Sections 4, 5.4 of paper

### **If you're a STATISTICIAN:**
- Focus on: MCMC methodology, uncertainty quantification, prior choices
- Read: Questions Q25-Q27, Red Flag #10
- Check: Section 3.4, monte_carlo_sampling.py

---

## Decision Tree for Reviewers

```
START
  |
  ├─ Read 00_OVERVIEW.md
  |
  ├─ Are there CRITICAL red flags that invalidate results?
  |    ├─ YES → Recommend REJECTION or MAJOR REVISION
  |    └─ NO → Continue
  |
  ├─ Can TOP 5 questions be satisfactorily answered?
  |    ├─ NO → Recommend MAJOR REVISION
  |    └─ YES → Continue
  |
  ├─ Are systematic uncertainties (factor of 10^3) acceptable?
  |    ├─ NO → Recommend MAJOR REVISION with uncertainty reduction
  |    └─ YES (exploratory framework) → Continue
  |
  ├─ Are assumptions reasonable and well-justified?
  |    ├─ NO → Recommend REVISION with better justification
  |    └─ YES → Continue
  |
  ├─ Is the framework falsifiable with current/near-future experiments?
  |    ├─ NO → Recommend REVISION with clearer testability
  |    └─ YES → Continue
  |
  └─ ACCEPT (with minor revisions for clarity)
```

---

## Contact for This Audit

**Audit performed by**: Claude Code Systematic Framework
**Date**: 2025-11-02
**Purpose**: Extract all physics claims for independent expert verification

**Note**: This audit is DESCRIPTIVE (extracting claims) not EVALUATIVE (judging validity). Physics judgment is left to domain experts.

---

## Repository Structure

```
expert_review_package/
├── 00_OVERVIEW.md                 # Start here
├── 01_all_claims.csv              # All 30 claims
├── 03_numerical_results.csv       # All numbers
├── 06_red_flags.md                # Suspicious items
├── 07_questions_for_expert.md     # 30 questions
└── README.md                      # This file

../audit_report/
└── 07_physics_claims_for_review.md  # Complete extraction (includes sections 2, 5, 6 referenced above)

../manuscript/
└── manuscript_final.tex           # Original paper LaTeX source

../code/
├── grmhd_acceleration.py          # Lorentz factor calculations
├── eft_cross_sections.py          # EFT production cross sections
├── pdf_integration.py             # Parton luminosity
├── monte_carlo_sampling.py        # MCMC parameter scan
└── observational_constraints.py   # Multi-messenger limits
```

---

## Bottom Line

**This paper proposes a novel framework for UHDM production in AGN jets with factor-of-10^3 systematic uncertainties. The methodology is transparent and reproducible. However, CRITICAL questions remain:**

1. **PDF extrapolation**: 14 orders beyond LHC data - reliable?
2. **Head-on collisions**: Angle-averaged rates may be 10^8 lower
3. **Primordial comparison**: AGN vs gravitational production not quantified
4. **Falsifiability**: With 10^3 uncertainties, is this testable?

**Your expert judgment on these 4 issues will determine if this paper represents:**
- (A) A valuable exploratory framework for a new UHDM channel, OR
- (B) A non-falsifiable speculation with uncertainties too large to be meaningful

**Please focus your review on resolving this question.**

---

**Thank you for your expert review!**

**Prepared by**: Claude Code Systematic Audit Framework
**Generated**: 2025-11-02
