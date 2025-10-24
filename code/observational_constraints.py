"""
Observational Constraints Module
=================================

Implements multi-messenger constraints on UHDM production in AGN:
- Fermi-LAT gamma-ray observations (3FHL catalog)
- IceCube neutrino stacking analysis
- Pierre Auger UHECR spectrum

Compares model predictions to observational upper limits.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Import other modules (assuming they're in the same directory)
import sys
sys.path.append('.')


class MultiMessengerConstraints:
    """
    Multi-messenger observational constraints on UHDM.
    """

    def __init__(self):
        """Initialize constraint data."""
        self.fermi_lat_flux_limit = 1e-11  # erg/cm²/s (typical 3FHL limit)
        self.icecube_flux_limit = 1e-12  # erg/cm²/s (neutrino limit)
        self.auger_flux_limit = 1e-13  # erg/cm²/s (UHECR limit)

        # Energy ranges
        self.fermi_energy_range = (10, 2000)  # GeV
        self.icecube_energy_range = (1e3, 1e6)  # GeV
        self.auger_energy_range = (1e9, 1e11)  # GeV (10 EeV - 100 EeV)

    def fermi_lat_constraint(self, M_X, flux_predicted):
        """
        Check if model is excluded by Fermi-LAT.

        Parameters:
        -----------
        M_X : float
            UHDM mass (GeV)
        flux_predicted : float
            Predicted gamma-ray flux (erg/cm²/s)

        Returns:
        --------
        excluded : bool
            True if excluded by Fermi-LAT
        """
        if self.fermi_energy_range[0] < M_X < self.fermi_energy_range[1]:
            return flux_predicted > self.fermi_lat_flux_limit
        return False

    def icecube_constraint(self, M_X, flux_predicted):
        """
        Check if model is excluded by IceCube.
        """
        if self.icecube_energy_range[0] < M_X < self.icecube_energy_range[1]:
            return flux_predicted > self.icecube_flux_limit
        return False

    def auger_constraint(self, M_X, flux_predicted):
        """
        Check if model is excluded by Pierre Auger.
        """
        if self.auger_energy_range[0] < M_X < self.auger_energy_range[1]:
            return flux_predicted > self.auger_flux_limit
        return False

    def combined_constraint(self, M_X, flux_predicted_gamma,
                           flux_predicted_nu, flux_predicted_cr):
        """
        Apply all constraints.

        Returns:
        --------
        excluded : bool
            True if excluded by any constraint
        excluded_by : list
            List of experiments that exclude this point
        """
        excluded_by = []

        if self.fermi_lat_constraint(M_X, flux_predicted_gamma):
            excluded_by.append('Fermi-LAT')

        if self.icecube_constraint(M_X, flux_predicted_nu):
            excluded_by.append('IceCube')

        if self.auger_constraint(M_X, flux_predicted_cr):
            excluded_by.append('Auger')

        return len(excluded_by) > 0, excluded_by


def calculate_decay_fluxes(M_X, N_production_rate, distance=100):
    """
    Calculate decay product fluxes from UHDM production.

    Assumes: X → gamma + gamma (or X → hadrons → gamma/nu/CR)

    Parameters:
    -----------
    M_X : float
        UHDM mass (GeV)
    N_production_rate : float
        Production rate (particles/s)
    distance : float
        Distance to source (Mpc)

    Returns:
    --------
    fluxes : dict
        Dictionary with 'gamma', 'neutrino', 'cosmic_ray' fluxes
    """
    distance_cm = distance * 3.086e24  # Mpc to cm

    # Energy per decay
    E_per_decay = M_X * 1.602e-10  # GeV to erg (1 GeV = 1.602e-3 erg)

    # Total luminosity
    L_total = N_production_rate * E_per_decay

    # Flux at Earth
    F_total = L_total / (4 * np.pi * distance_cm**2)

    # Branching fractions (model-dependent)
    BR_gamma = 0.6  # 60% to photons
    BR_neutrino = 0.3  # 30% to neutrinos
    BR_cosmic_ray = 0.1  # 10% to cosmic rays

    fluxes = {
        'gamma': F_total * BR_gamma,
        'neutrino': F_total * BR_neutrino,
        'cosmic_ray': F_total * BR_cosmic_ray
    }

    return fluxes


def plot_constraints_summary(output_file='../figures/fig4_constraints.pdf'):
    """
    Generate Figure 4: Multi-messenger constraints summary.
    """
    constraints = MultiMessengerConstraints()

    # Mass range
    M_X_array = np.logspace(1, 11, 200)  # 10 GeV to 100 EeV

    # Example model prediction (power law)
    flux_gamma = 1e-10 * (M_X_array / 1000)**(-2)
    flux_nu = 1e-11 * (M_X_array / 1000)**(-2)
    flux_cr = 1e-12 * (M_X_array / 1000)**(-2)

    # Create figure
    fig, ax = plt.subplots(figsize=(12, 8))

    # Plot model predictions
    ax.loglog(M_X_array, flux_gamma, 'b-', lw=2.5, label='Predicted γ-ray Flux')
    ax.loglog(M_X_array, flux_nu, 'g-', lw=2.5, label='Predicted ν Flux')
    ax.loglog(M_X_array, flux_cr, 'r-', lw=2.5, label='Predicted CR Flux')

    # Plot observational limits
    # Fermi-LAT
    fermi_mask = (M_X_array > constraints.fermi_energy_range[0]) & \
                 (M_X_array < constraints.fermi_energy_range[1])
    ax.fill_between(M_X_array[fermi_mask],
                    constraints.fermi_lat_flux_limit,
                    1e-8, alpha=0.3, color='blue',
                    label='Fermi-LAT Excluded')

    # IceCube
    icecube_mask = (M_X_array > constraints.icecube_energy_range[0]) & \
                   (M_X_array < constraints.icecube_energy_range[1])
    ax.fill_between(M_X_array[icecube_mask],
                    constraints.icecube_flux_limit,
                    1e-8, alpha=0.3, color='green',
                    label='IceCube Excluded')

    # Auger
    auger_mask = (M_X_array > constraints.auger_energy_range[0]) & \
                 (M_X_array < constraints.auger_energy_range[1])
    ax.fill_between(M_X_array[auger_mask],
                    constraints.auger_flux_limit,
                    1e-8, alpha=0.3, color='red',
                    label='Auger Excluded')

    ax.set_xlabel(r'UHDM Mass $M_X$ [GeV]', fontsize=16)
    ax.set_ylabel(r'Flux [erg cm$^{-2}$ s$^{-1}$]', fontsize=16)
    ax.set_title('Multi-Messenger Constraints on UHDM Production', fontsize=18)
    ax.legend(fontsize=11, loc='upper right')
    ax.grid(True, alpha=0.3, which='both')
    ax.set_xlim(1e1, 1e11)
    ax.set_ylim(1e-15, 1e-8)

    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Figure saved: {output_file}")
    plt.close()


if __name__ == '__main__':
    print("Observational Constraints Module")
    print("=" * 50)

    # Initialize constraints
    constraints = MultiMessengerConstraints()

    # Example: Check if a model point is excluded
    M_X_test = 500  # GeV
    N_prod = 1e40  # particles/s
    distance = 100  # Mpc

    fluxes = calculate_decay_fluxes(M_X_test, N_prod, distance)

    print(f"\nExample Model Point:")
    print(f"  M_X = {M_X_test} GeV")
    print(f"  Production rate = {N_prod:.2e} particles/s")
    print(f"  Distance = {distance} Mpc")
    print(f"\nPredicted Fluxes:")
    print(f"  Gamma-ray: {fluxes['gamma']:.2e} erg/cm²/s")
    print(f"  Neutrino: {fluxes['neutrino']:.2e} erg/cm²/s")
    print(f"  Cosmic ray: {fluxes['cosmic_ray']:.2e} erg/cm²/s")

    excluded, excluded_by = constraints.combined_constraint(
        M_X_test,
        fluxes['gamma'],
        fluxes['neutrino'],
        fluxes['cosmic_ray']
    )

    if excluded:
        print(f"\nModel EXCLUDED by: {', '.join(excluded_by)}")
    else:
        print(f"\nModel ALLOWED by all constraints")

    # Generate Figure 4
    print(f"\nGenerating Figure 4...")
    plot_constraints_summary()
