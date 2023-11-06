import numpy as np
import matplotlib.pyplot as plt

def true_distribution(x, actual_mean, actual_stddev):
    return (1 / (np.sqrt(2 * np.pi) * actual_stddev)) * np.exp(-0.5 * ((x - actual_mean) / actual_stddev) ** 2)

def metropolis_hastings_generator(num_samples, proposal_stddev, actual_mean, actual_stddev):
    current_sample = 1.0
    iteration = 0

    while iteration < num_samples:
        proposal = np.random.normal(current_sample, proposal_stddev)
        prob_of_accept = min(1, true_distribution(proposal, actual_mean, actual_stddev) / true_distribution(current_sample, actual_mean, actual_stddev))

        if np.random.uniform(0,1) < prob_of_accept:
            current_sample = proposal

        yield current_sample
        iteration += 1

def main():
    actual_mean = 1.0
    actual_stddev = 0.5
    num_samples = 1000000
    proposal_stddev = 2.0
    burn_in = 1000

    samples = metropolis_hastings_generator(num_samples, proposal_stddev, actual_mean, actual_stddev)

    for _ in range(burn_in):
        next(samples)

    retained_samples = [sample for sample in samples]
    empirical_mean = np.mean(retained_samples)

    x = np.linspace(-3, 5, 1000)
    plt.title("Metropolis Hastings Algorithm")
    plt.hist(retained_samples, bins=100, density=True, alpha=0.5, label='MCMC Generated Samples')
    plt.plot(x, true_distribution(x, actual_mean, actual_stddev), label='True Samples')
    plt.xlabel('X')
    plt.ylabel('Density')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
