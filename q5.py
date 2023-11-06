import random
import numpy as np
def fair_dice_pmf(x):
    if 1 <= x <= 6:
        return 1/6
    else:
        return 0

def proposal_distribution():
    return random.randint(1, 6)

def accept_reject_sampling(target_pmf, proposal_distribution, num_samples):
    samples = []
    m=1.2
    for _ in range(num_samples):
        x = proposal_distribution()
        u = random.random()
        if u < target_pmf(x) / (m/6):
            samples.append(x)
    return samples
num_samples = 10000
samples = accept_reject_sampling(fair_dice_pmf, proposal_distribution, num_samples)
counts = [samples.count(x) for x in range(1, 7)]
estimated_probabilities = [count / num_samples for count in counts]
for i, count in enumerate(counts, start=1):
    print(f"Number of times {i} gets accepted: {count} occurrences")


