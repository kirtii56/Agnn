"""
EFT Cross Section Module
=========================

Calculates effective field theory production cross sections for
ultra-high-density matter (UHDM) at parton level.

Implements contact interaction operators and validates EFT cutoff scales.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.special import kn  # Modified Bessel function

# Physical constants
alpha_s = 0.118  # Strong coupling at M_Z
GeV = 1.0  # Energy units
pb = 1.0  # Cross section units (picobarn)
GeV2_to_pb = 3.894e8  # Conversion factor


def eft_contact_operator_xsec(s, M_X, Lambda_cutoff, g_eff=1.0):
    """
    Calculate EFT contact operator cross section.

    For operator: (1/Λ²) (q̄q)(X̄X)

    σ ~ (g_eff² / Λ⁴) * s

    Parameters:
    -----------
    s : float
        Center-of-mass energy squared (GeV²)
    M_X : float
        UHDM particle mass (GeV)
    Lambda_cutoff : float
        EFT cutoff scale (GeV)
    g_eff : float
        Effective coupling (default 1.0)

    Returns:
    --------
    xsec : float
        Cross section in pb
    """
    if s < 4 * M_X**2:
        return 0.0  # Below threshold

    # EFT validity check
    if np.sqrt(s) > Lambda_cutoff:
        # EFT breaks down, return NaN or apply form factor
        return np.nan

    # Phase space factor
    beta = np.sqrt(1 - 4*M_X**2/s)

    # Contact operator cross section
    xsec = (g_eff**2 / Lambda_cutoff**4) * s * beta * GeV2_to_pb

    return xsec


def s_channel_resonance_xsec(s, M_X, M_mediator, Gamma_mediator, g_q=1.0, g_X=1.0):
    """
    Calculate s-channel resonance production cross section.

    pp → Z' → XX

    Parameters:
    -----------
    s : float
        Center-of-mass energy squared (GeV²)
    M_X : float
        UHDM particle mass (GeV)
    M_mediator : float
        Mediator mass (GeV)
    Gamma_mediator : float
        Mediator width (GeV)
    g_q : float
        Quark coupling
    g_X : float
        UHDM coupling

    Returns:
    --------
    xsec : float
        Cross section in pb
    """
    if s < 4 * M_X**2:
        return 0.0

    beta = np.sqrt(1 - 4*M_X**2/s)

    # Breit-Wigner propagator
    BW = (s * Gamma_mediator**2) / ((s - M_mediator**2)**2 +
                                     M_mediator**2 * Gamma_mediator**2)

    xsec = (np.pi * g_q**2 * g_X**2 / s) * BW * beta * GeV2_to_pb

    return xsec


def eft_validity_cutoff(M_X, coupling=1.0, relative_correction=0.1):
    """
    Estimate EFT validity cutoff scale.

    Λ ~ M_X / sqrt(g * relative_correction)

    EFT valid when Q² << Λ²

    Parameters:
    -----------
    M_X : float
        UHDM mass (GeV)
    coupling : float
        Coupling strength
    relative_correction : float
        Acceptable relative correction (default 10%)

    Returns:
    --------
    Lambda : float
        Cutoff scale (GeV)
    """
    Lambda = M_X / np.sqrt(coupling * relative_correction)
    return Lambda


def plot_eft_validity(output_file='../figures/fig1_eft_validity_corrected.pdf'):
    """
    Generate Figure 1: EFT validity regions (corrected).
    """
    M_X_array = np.logspace(2, 5, 100)  # 100 GeV to 100 TeV

    # Different coupling scenarios
    couplings = [0.1, 1.0, 4*np.pi]  # Weak, O(1), Strong
    labels = [r'$g = 0.1$', r'$g = 1$', r'$g = 4\pi$']
    colors = ['blue', 'green', 'red']

    plt.figure(figsize=(10, 7))

    for coupling, label, color in zip(couplings, labels, colors):
        Lambda_array = np.array([eft_validity_cutoff(M_X, coupling)
                                 for M_X in M_X_array])
        plt.loglog(M_X_array, Lambda_array, lw=2.5, label=label, color=color)

    # LHC reach
    plt.axhline(y=13000, color='orange', linestyle='--', lw=2,
                label='LHC (13 TeV)', alpha=0.7)

    # Planck scale
    plt.axhline(y=1.22e19, color='gray', linestyle=':', lw=2,
                label='Planck Scale', alpha=0.5)

    # EFT validity region (shaded)
    plt.fill_between(M_X_array, M_X_array, 1e20, alpha=0.1, color='gray',
                     label='EFT Valid Region')

    plt.xlabel(r'UHDM Mass $M_X$ [GeV]', fontsize=16)
    plt.ylabel(r'EFT Cutoff $\Lambda$ [GeV]', fontsize=16)
    plt.title('EFT Validity Analysis (Corrected)', fontsize=18)
    plt.legend(fontsize=12, loc='upper left')
    plt.grid(True, alpha=0.3, which='both')
    plt.xlim(1e2, 1e5)
    plt.ylim(1e2, 1e20)
    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Figure saved: {output_file}")
    plt.close()


def plot_production_rate(M_X_array, xsec_array,
                         output_file='../figures/fig3_production_rate.pdf'):
    """
    Generate Figure 3: Production rate vs mass.

    Parameters:
    -----------
    M_X_array : ndarray
        Array of masses (GeV)
    xsec_array : ndarray
        Array of cross sections (pb)
    output_file : str
        Output filename
    """
    plt.figure(figsize=(10, 7))
    plt.loglog(M_X_array, xsec_array, 'b-', lw=2.5)
    plt.xlabel(r'UHDM Mass $M_X$ [GeV]', fontsize=16)
    plt.ylabel(r'Production Cross Section [pb]', fontsize=16)
    plt.title('UHDM Production Rate vs Mass', fontsize=18)
    plt.grid(True, alpha=0.3, which='both')
    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Figure saved: {output_file}")
    plt.close()


if __name__ == '__main__':
    print("EFT Cross Section Module")
    print("=" * 50)

    # Example calculation
    s = (14000)**2  # LHC energy (GeV²)
    M_X = 1000  # GeV
    Lambda = 5000  # GeV

    xsec_contact = eft_contact_operator_xsec(s, M_X, Lambda)
    Lambda_cutoff = eft_validity_cutoff(M_X)

    print(f"\nExample Parameters:")
    print(f"  √s = {np.sqrt(s):.0f} GeV")
    print(f"  M_X = {M_X} GeV")
    print(f"  Λ = {Lambda} GeV")
    print(f"\nResults:")
    print(f"  σ (contact) = {xsec_contact:.2e} pb")
    print(f"  Λ_cutoff (10% accuracy) = {Lambda_cutoff:.2e} GeV")

    # Generate figures
    print(f"\nGenerating Figure 1...")
    plot_eft_validity()

    # Example production rate plot
    M_array = np.logspace(2, 4, 50)
    xsec_array = np.array([eft_contact_operator_xsec((1e4)**2, M, 1e4)
                           for M in M_array])
    print(f"\nGenerating Figure 3...")
    plot_production_rate(M_array, xsec_array)
