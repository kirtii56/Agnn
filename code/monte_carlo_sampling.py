"""
Monte Carlo Sampling Module
============================

MCMC parameter space exploration using emcee (affine-invariant ensemble sampler).

Samples parameter space:
- UHDM mass M_X
- Coupling g_eff
- Magnetization σ
- Jet opening angle θ_jet

Performs Bayesian inference with observational constraints.
"""

import numpy as np
import matplotlib.pyplot as plt
import corner
import emcee
import h5py
from multiprocessing import Pool

# Import other modules
import sys
sys.path.append('.')
from eft_cross_sections import eft_contact_operator_xsec, eft_validity_cutoff
from grmhd_acceleration import max_lorentz_factor_reconnection


def log_prior(theta):
    """
    Log prior probability for parameters.

    Parameters:
    -----------
    theta : array-like
        [log10(M_X), log10(g_eff), log10(sigma), theta_jet]

    Returns:
    --------
    log_prior : float
        Log prior probability
    """
    log_M_X, log_g_eff, log_sigma, theta_jet = theta

    # Uniform priors in log space
    if not (2 < log_M_X < 5):  # 100 GeV to 100 TeV
        return -np.inf
    if not (-2 < log_g_eff < 1):  # 0.01 to 10
        return -np.inf
    if not (-1 < log_sigma < 2):  # 0.1 to 100
        return -np.inf
    if not (0.01 < theta_jet < 0.5):  # 0.01 to 0.5 radians
        return -np.inf

    return 0.0  # Flat prior


def log_likelihood(theta, data_constraints):
    """
    Log likelihood function comparing model to observations.

    Parameters:
    -----------
    theta : array-like
        Parameter vector
    data_constraints : dict
        Dictionary of observational constraints

    Returns:
    --------
    log_like : float
        Log likelihood
    """
    log_M_X, log_g_eff, log_sigma, theta_jet = theta

    M_X = 10**log_M_X
    g_eff = 10**log_g_eff
    sigma = 10**log_sigma

    # Calculate model predictions
    s_collision = (1e8)**2  # AGN jet collision energy (GeV)^2, ~10^17-10^18 eV
    Lambda = eft_validity_cutoff(M_X, g_eff)
    xsec = eft_contact_operator_xsec(s_collision, M_X, Lambda, g_eff)

    if np.isnan(xsec):
        return -np.inf  # EFT invalid

    # Production rate in AGN jet
    L_jet = 1e45  # erg/s (typical blazar jet luminosity)
    n_collisions = L_jet / (M_X * 1.783e-27)  # Number of collisions per second
    N_production = xsec * 1e-36 * n_collisions  # Production rate (per second)

    # Compare to observational upper limits
    # Fermi-LAT gamma-ray flux limit
    F_gamma_limit = data_constraints.get('fermi_flux_limit', 1e-11)  # erg/cm²/s
    F_gamma_predicted = N_production * M_X * 1.6e-3 / (4*np.pi*(100*3.086e24)**2)

    # IceCube neutrino limit
    F_nu_limit = data_constraints.get('icecube_flux_limit', 1e-12)  # erg/cm²/s
    F_nu_predicted = F_gamma_predicted * 0.1  # Assume 10% to neutrinos

    # Log likelihood (Gaussian approximation)
    chi2 = 0.0

    # Gamma-ray constraint
    if F_gamma_predicted > F_gamma_limit:
        chi2 += ((np.log10(F_gamma_predicted) - np.log10(F_gamma_limit))/0.3)**2

    # Neutrino constraint
    if F_nu_predicted > F_nu_limit:
        chi2 += ((np.log10(F_nu_predicted) - np.log10(F_nu_limit))/0.3)**2

    log_like = -0.5 * chi2

    return log_like


def log_probability(theta, data_constraints):
    """
    Log posterior probability = log prior + log likelihood.
    """
    lp = log_prior(theta)
    if not np.isfinite(lp):
        return -np.inf
    return lp + log_likelihood(theta, data_constraints)


def run_mcmc(n_walkers=32, n_steps=10000, output_file='../data/mc_posterior_samples.h5'):
    """
    Run MCMC parameter scan using emcee.

    Parameters:
    -----------
    n_walkers : int
        Number of MCMC walkers
    n_steps : int
        Number of steps per walker
    output_file : str
        HDF5 output file for samples
    """
    print("Running MCMC Parameter Scan")
    print("=" * 50)

    # Parameter dimension
    ndim = 4

    # Initial positions (random ball around initial guess)
    initial = np.array([3.5, -0.5, 0.5, 0.1])  # [log M_X, log g, log σ, θ]
    pos = initial + 1e-2 * np.random.randn(n_walkers, ndim)

    # Observational constraints
    data_constraints = {
        'fermi_flux_limit': 1e-11,  # erg/cm²/s
        'icecube_flux_limit': 1e-12,  # erg/cm²/s
    }

    # Set up backend to save progress
    backend = emcee.backends.HDFBackend(output_file)
    backend.reset(n_walkers, ndim)

    # Run MCMC
    print(f"Initializing {n_walkers} walkers...")
    print(f"Running {n_steps} steps...")

    with Pool() as pool:
        sampler = emcee.EnsembleSampler(
            n_walkers, ndim, log_probability,
            args=(data_constraints,),
            pool=pool,
            backend=backend
        )

        # Run with progress bar
        for i, result in enumerate(sampler.sample(pos, iterations=n_steps)):
            if (i+1) % 100 == 0:
                print(f"  Step {i+1}/{n_steps} ({100*(i+1)/n_steps:.1f}%)")

    print(f"\nMCMC complete!")
    print(f"Samples saved to: {output_file}")
    print(f"Acceptance fraction: {np.mean(sampler.acceptance_fraction):.3f}")

    return sampler


def plot_mcmc_diagnostics(sampler, output_file='../figures/figS1_mcmc_diagnostics.pdf'):
    """
    Generate Figure S1: MCMC diagnostics.

    Parameters:
    -----------
    sampler : emcee.EnsembleSampler
        MCMC sampler object
    output_file : str
        Output filename
    """
    print("\nGenerating MCMC diagnostics...")

    # Extract samples
    samples = sampler.get_chain()
    flat_samples = sampler.get_chain(discard=1000, thin=10, flat=True)

    # Parameter names
    labels = [r'$\log_{10}(M_X/{\rm GeV})$',
              r'$\log_{10}(g_{\rm eff})$',
              r'$\log_{10}(\sigma)$',
              r'$\theta_{\rm jet}$ [rad]']

    # Create corner plot
    fig = corner.corner(flat_samples, labels=labels,
                       quantiles=[0.16, 0.5, 0.84],
                       show_titles=True, title_fmt='.3f',
                       smooth=1.0)

    fig.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Diagnostics saved: {output_file}")
    plt.close(fig)

    # Trace plots
    fig, axes = plt.subplots(4, 1, figsize=(10, 10))
    for i in range(4):
        axes[i].plot(samples[:, :, i], 'k', alpha=0.3, lw=0.5)
        axes[i].set_ylabel(labels[i])
        axes[i].grid(alpha=0.3)
    axes[-1].set_xlabel('Step')
    plt.tight_layout()
    trace_file = output_file.replace('.pdf', '_traces.pdf')
    plt.savefig(trace_file, dpi=300, bbox_inches='tight')
    print(f"Trace plots saved: {trace_file}")
    plt.close(fig)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='MCMC parameter space exploration for UHDM production in AGN jets'
    )
    parser.add_argument('--nsamples', type=int, default=1000000,
                       help='Total number of samples (default: 1000000)')
    parser.add_argument('--nchains', type=int, default=5,
                       help='Number of chains/walkers (default: 5)')
    parser.add_argument('--output', type=str, default='../data/mc_posterior_samples.h5',
                       help='Output HDF5 file (default: ../data/mc_posterior_samples.h5)')
    parser.add_argument('--seed', type=int, default=42,
                       help='Random seed for reproducibility (default: 42)')
    args = parser.parse_args()

    # Set random seed
    np.random.seed(args.seed)

    print("Monte Carlo Sampling Module")
    print("=" * 50)
    print(f"Configuration:")
    print(f"  Total samples: {args.nsamples:,}")
    print(f"  Number of chains: {args.nchains}")
    print(f"  Steps per chain: {args.nsamples // args.nchains:,}")
    print(f"  Random seed: {args.seed}")
    print(f"  Output file: {args.output}")
    print("=" * 50)

    # Calculate n_walkers and n_steps from nsamples and nchains
    n_walkers = args.nchains
    n_steps = args.nsamples // args.nchains

    sampler = run_mcmc(n_walkers=n_walkers, n_steps=n_steps, output_file=args.output)

    # Generate diagnostics
    plot_mcmc_diagnostics(sampler)

    print("\n" + "=" * 50)
    print("Analysis complete!")
