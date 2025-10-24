"""
GRMHD Acceleration Module
=========================

Calculates maximum Lorentz factors for particles accelerated in
magnetically-dominated AGN jets using GRMHD simulation results.

Based on relativistic reconnection and shock acceleration mechanisms.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.optimize import fsolve

# Physical constants
c = 2.998e10  # Speed of light (cm/s)
m_p = 1.673e-24  # Proton mass (g)
e = 4.803e-10  # Elementary charge (esu)

def magnetization_parameter(B, n, gamma_bulk):
    """
    Calculate magnetization parameter σ = B²/(4πρc²γ²)

    Parameters:
    -----------
    B : float
        Magnetic field strength (Gauss)
    n : float
        Number density (cm^-3)
    gamma_bulk : float
        Bulk Lorentz factor of jet

    Returns:
    --------
    sigma : float
        Magnetization parameter
    """
    rho = n * m_p
    sigma = B**2 / (4 * np.pi * rho * c**2 * gamma_bulk**2)
    return sigma


def max_lorentz_factor_reconnection(B, L_acc, eta=0.1):
    """
    Maximum Lorentz factor from magnetic reconnection.

    γ_max ~ (e B L_acc) / (m_p c²)

    Parameters:
    -----------
    B : float
        Magnetic field strength (Gauss)
    L_acc : float
        Acceleration region size (cm)
    eta : float
        Acceleration efficiency (default 0.1)

    Returns:
    --------
    gamma_max : float
        Maximum Lorentz factor
    """
    gamma_max = eta * (e * B * L_acc) / (m_p * c**2)
    return gamma_max


def max_lorentz_factor_shock(gamma_shock, epsilon_B=0.01):
    """
    Maximum Lorentz factor from shock acceleration.

    Based on Fermi acceleration at relativistic shocks.

    Parameters:
    -----------
    gamma_shock : float
        Shock Lorentz factor
    epsilon_B : float
        Fraction of energy in magnetic field

    Returns:
    --------
    gamma_max : float
        Maximum Lorentz factor
    """
    # Simplified model: γ_max ~ γ_shock² for strong shocks
    gamma_max = gamma_shock**2 * np.sqrt(epsilon_B)
    return gamma_max


def calculate_gamma_distribution(gamma_min, gamma_max, N, power_law_index=-2.0):
    """
    Generate power-law distribution of Lorentz factors.

    dN/dγ ∝ γ^p

    Parameters:
    -----------
    gamma_min : float
        Minimum Lorentz factor
    gamma_max : float
        Maximum Lorentz factor
    N : int
        Number of samples
    power_law_index : float
        Spectral index (default -2.0)

    Returns:
    --------
    gamma_array : ndarray
        Array of Lorentz factors
    """
    p = power_law_index
    u = np.random.uniform(0, 1, N)

    if p != -1:
        gamma_array = ((gamma_max**(p+1) - gamma_min**(p+1)) * u +
                       gamma_min**(p+1))**(1/(p+1))
    else:
        gamma_array = gamma_min * (gamma_max/gamma_min)**u

    return gamma_array


def plot_gamma_max_vs_sigma(output_file='../figures/fig2_gamma_max.pdf'):
    """
    Generate Figure 2: Maximum Lorentz factors vs magnetization.
    """
    # Parameter ranges from GRMHD simulations
    sigma_array = np.logspace(-1, 2, 50)  # σ from 0.1 to 100
    B_array = np.logspace(3, 5, len(sigma_array))  # B from 10^3 to 10^5 Gauss
    L_acc = 1e15  # 10^15 cm ~ 0.1 pc

    gamma_max_reconnection = np.zeros_like(sigma_array)
    gamma_max_shock = np.zeros_like(sigma_array)

    for i, (sigma, B) in enumerate(zip(sigma_array, B_array)):
        gamma_max_reconnection[i] = max_lorentz_factor_reconnection(B, L_acc)
        # Estimate shock Lorentz factor from σ
        gamma_s = np.sqrt(sigma)
        gamma_max_shock[i] = max_lorentz_factor_shock(gamma_s)

    # Plotting
    plt.figure(figsize=(8, 6))
    plt.loglog(sigma_array, gamma_max_reconnection, 'b-', lw=2,
               label='Magnetic Reconnection')
    plt.loglog(sigma_array, gamma_max_shock, 'r--', lw=2,
               label='Shock Acceleration')

    plt.xlabel(r'Magnetization Parameter $\sigma$', fontsize=14)
    plt.ylabel(r'Maximum Lorentz Factor $\gamma_{\rm max}$', fontsize=14)
    plt.title('GRMHD Acceleration Mechanisms', fontsize=16)
    plt.legend(fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Figure saved: {output_file}")
    plt.close()


if __name__ == '__main__':
    print("GRMHD Acceleration Module")
    print("=" * 50)

    # Example calculation
    B = 1e4  # Gauss
    L_acc = 1e15  # cm
    n = 1e3  # cm^-3
    gamma_bulk = 10

    sigma = magnetization_parameter(B, n, gamma_bulk)
    gamma_max_rec = max_lorentz_factor_reconnection(B, L_acc)
    gamma_max_sh = max_lorentz_factor_shock(gamma_bulk)

    print(f"\nExample Parameters:")
    print(f"  B = {B:.2e} Gauss")
    print(f"  L_acc = {L_acc:.2e} cm")
    print(f"  n = {n:.2e} cm^-3")
    print(f"  γ_bulk = {gamma_bulk}")
    print(f"\nResults:")
    print(f"  σ = {sigma:.2f}")
    print(f"  γ_max (reconnection) = {gamma_max_rec:.2e}")
    print(f"  γ_max (shock) = {gamma_max_sh:.2e}")

    # Generate figure
    print(f"\nGenerating Figure 2...")
    plot_gamma_max_vs_sigma()
