"""
PDF Integration Module
=======================

Integrates parton distribution functions (PDFs) using CT18 NNLO.

Calculates parton-level luminosities for pp collisions at AGN jet energies.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad, dblquad

# Note: For actual use, install lhapdf: pip install lhapdf
# This is a simplified implementation

class SimplePDF:
    """
    Simplified parton distribution function model.

    For production use, replace with LHAPDF CT18NNLO.
    """

    def __init__(self, pdf_set='CT18NNLO'):
        self.pdf_set = pdf_set
        print(f"Initialized PDF: {pdf_set}")
        print("Note: Using simplified model. Install LHAPDF for full CT18NNLO.")

    def xf(self, x, Q2, flavor):
        """
        x * f(x, Q²) - parton distribution

        Parameters:
        -----------
        x : float
            Momentum fraction (0 < x < 1)
        Q2 : float
            Factorization scale squared (GeV²)
        flavor : int
            Parton flavor (1=d, 2=u, -1=dbar, -2=ubar, 21=g)

        Returns:
        --------
        xf : float
            x times the PDF value
        """
        if x <= 0 or x >= 1:
            return 0.0

        # Simplified valence + sea + gluon model
        Q0 = 1.0  # GeV
        alpha_s = 0.118

        # Valence quarks (uv, dv)
        if flavor in [1, 2]:
            valence = 3.0 * x**0.5 * (1-x)**3
            sea = 0.2 * (1-x)**7 / x**0.5
            return valence + sea

        # Anti-quarks (sea)
        elif flavor in [-1, -2]:
            sea = 0.2 * (1-x)**7 / x**0.5
            return sea

        # Gluons
        elif flavor == 21:
            gluon = 3.0 * (1-x)**5 / x**0.3
            return gluon

        else:
            return 0.0


def parton_luminosity(pdf, s, M_X, flavors=(2, -2)):
    """
    Calculate parton luminosity: dL/d(tau) where tau = M_X²/s

    L = (1/s) ∫ dx₁ dx₂ f₁(x₁) f₂(x₂) δ(x₁x₂ - tau)

    Parameters:
    -----------
    pdf : SimplePDF
        PDF object
    s : float
        pp center-of-mass energy squared (GeV²)
    M_X : float
        Invariant mass (GeV)
    flavors : tuple
        (flavor1, flavor2) for incoming partons

    Returns:
    --------
    luminosity : float
        Parton luminosity
    """
    tau = M_X**2 / s
    Q2 = M_X**2  # Factorization scale

    if tau >= 1:
        return 0.0

    def integrand(x1):
        x2 = tau / x1
        if x2 >= 1:
            return 0.0
        f1 = pdf.xf(x1, Q2, flavors[0]) / x1
        f2 = pdf.xf(x2, Q2, flavors[1]) / x2
        return f1 * f2 / x1

    result, error = quad(integrand, tau, 1.0, limit=100)
    return result / s


def convolve_with_pdfs(cross_section_hat, pdf, s, M_X_array):
    """
    Convolve partonic cross section with PDFs to get hadronic cross section.

    σ(pp → XX) = Σ_ij ∫ dx₁ dx₂ fᵢ(x₁) fⱼ(x₂) σ̂ᵢⱼ(x₁x₂s)

    Parameters:
    -----------
    cross_section_hat : function
        Partonic cross section σ̂(ŝ)
    pdf : SimplePDF
        PDF object
    s : float
        pp collision energy squared (GeV²)
    M_X_array : ndarray
        Array of UHDM masses (GeV)

    Returns:
    --------
    sigma_array : ndarray
        Hadronic cross sections (pb)
    """
    sigma_array = np.zeros_like(M_X_array)

    # Parton pairs to sum over
    quark_flavors = [(2, -2), (1, -1)]  # u-ubar, d-dbar

    for i, M_X in enumerate(M_X_array):
        sigma_tot = 0.0

        for flavors in quark_flavors:
            # Partonic cross section at threshold
            s_hat = M_X**2
            sigma_hat = cross_section_hat(s_hat, M_X)

            # Parton luminosity
            lumi = parton_luminosity(pdf, s, M_X, flavors)

            # Contribution to total cross section
            sigma_tot += sigma_hat * lumi

        sigma_array[i] = sigma_tot

    return sigma_array


def plot_parton_luminosities(output_file='../figures/parton_luminosities.pdf'):
    """
    Plot parton luminosities vs invariant mass.
    """
    pdf = SimplePDF('CT18NNLO')

    s = (14000)**2  # LHC 14 TeV
    M_array = np.logspace(2, 4, 50)  # 100 GeV to 10 TeV

    # Calculate luminosities for different parton combinations
    lumi_uu = np.array([parton_luminosity(pdf, s, M, (2, -2)) for M in M_array])
    lumi_dd = np.array([parton_luminosity(pdf, s, M, (1, -1)) for M in M_array])
    lumi_gg = np.array([parton_luminosity(pdf, s, M, (21, 21)) for M in M_array])

    plt.figure(figsize=(10, 7))
    plt.loglog(M_array, lumi_uu, 'b-', lw=2, label=r'$u\bar{u}$')
    plt.loglog(M_array, lumi_dd, 'r-', lw=2, label=r'$d\bar{d}$')
    plt.loglog(M_array, lumi_gg, 'g-', lw=2, label=r'$gg$')

    plt.xlabel(r'Invariant Mass $M$ [GeV]', fontsize=14)
    plt.ylabel(r'Parton Luminosity [GeV$^{-2}$]', fontsize=14)
    plt.title('CT18 NNLO Parton Luminosities', fontsize=16)
    plt.legend(fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Figure saved: {output_file}")
    plt.close()


if __name__ == '__main__':
    print("PDF Integration Module")
    print("=" * 50)

    # Initialize PDF
    pdf = SimplePDF('CT18NNLO')

    # Example calculation
    s = (14000)**2  # GeV²
    M_X = 1000  # GeV

    lumi_uu = parton_luminosity(pdf, s, M_X, (2, -2))
    lumi_gg = parton_luminosity(pdf, s, M_X, (21, 21))

    print(f"\nExample: √s = {np.sqrt(s):.0f} GeV, M_X = {M_X} GeV")
    print(f"  L(u-ubar) = {lumi_uu:.2e} GeV^-2")
    print(f"  L(g-g) = {lumi_gg:.2e} GeV^-2")

    # Generate plot
    print(f"\nGenerating parton luminosity plot...")
    plot_parton_luminosities()
