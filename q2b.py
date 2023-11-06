import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
# import seaborn as sns
mean = (0+1+3)/10
variance = 3*mean
std_deviation = np.sqrt(variance)
values_clt = []
num_of_samples = 10000
# samples = 400
for i in range(num_of_samples):
    uniform1 = np.random.rand()
    uniform2 = np.random.rand()
    inverse = np.sqrt(-2 * np.log(uniform1)) * np.cos(2 * np.pi * uniform1)
    values_clt.append(inverse*std_deviation + mean)

x1 = np.linspace(-5, 5, 1000)
# pdf_values_inbuilt = (1 / (std_deviation * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x1 - mean) / std_deviation) ** 2)
pdf_values_inbuilt = norm.pdf(x1, loc=mean, scale=std_deviation)
cdf_values_inbuilt = norm.cdf(x1, loc=mean, scale=std_deviation)
# x = np.linspace(0, max(values_clt), 1000)
# pdf_values = (x/sigma ** 2)*(np.exp(- (x ** 2)/(2 * (sigma ** 2))))
# cdf_values = 1 - np.exp(-x**2 / (2 * sigma**2))
plt.figure(figsize=(12, 6))
plt.subplot(1,2,1)
plt.plot(x1, pdf_values_inbuilt, label="Gaussian Inbuilt PDF")
plt.hist(values_clt,bins=100,density=True, label='Gaussian Generated PDF')
# sns.distplot(values_clt,hist=False, label="Rayleigh Generated PDF ")
plt.xlabel("Gaussian Variable (x)")
plt.ylabel("PDF")
plt.legend()
plt.title("PDF of Gaussian Random Variable ")

plt.subplot(1,2,2)
plt.plot(x1, cdf_values_inbuilt, label="Gaussian Inbuilt CDF")
plt.hist(values_clt,bins=100,cumulative=True,density=True,label='Gaussian Generated CDF')
# sns.distplot(values_clt,hist=False,kde_kws={"cumulative": True}, label="Rayleigh Generated CDF ")
plt.xlabel("Gaussian Variable (x)")
plt.ylabel("CDF")
plt.legend()
plt.title("CDF of Gaussian Random Variable ")
plt.show()





# # import numpy as np
# # import matplotlib.pyplot as plt

# # mean = (0+1+3)/10
# # variance = 3*mean

# # import numpy as np
# # import matplotlib.pyplot as plt

# # # Parameters
# # mean = 0.1
# # variance = 0.3  # 3 * mean

# # # a. Central Limit Theorem
# # sample_size = 10000
# # num_samples = 10000
# # clt_samples = []

# # for j in range(num_samples):
# #     random_uniform_samples = np.random.uniform(0, 1, sample_size)
# #     clt_sample = np.sum(random_uniform_samples) - sample_size / 2
# #     clt_sample = clt_sample * np.sqrt(12 * variance / sample_size) + mean
# #     clt_samples.append(clt_sample)
# # print(np.mean(clt_samples))
# # print(np.var(clt_samples))
# # # b. Box-Muller Method
# # bm_samples = []

# # for i in range(num_samples):
# #     u1, u2 = np.random.uniform(0, 1, 2)
# #     z1 = np.sqrt(-2 * np.log(u1)) * np.cos(2 * np.pi * u2)
# #     bm_sample = z1 * np.sqrt(variance) + mean
# #     bm_samples.append(bm_sample)
# # print(np.mean(bm_samples))
# # print(np.var(bm_samples))
# # # Plot the CDF and PDF of the generated samples
# # plt.figure(figsize=(12, 6))
# # plt.subplot(1, 2, 1)
# # plt.hist(clt_samples, bins=100, density=True, alpha=0.5, label='Central Limit Theorem')
# # plt.hist(bm_samples, bins=100, density=True, alpha=0.5, label='Box-Muller Method')
# # plt.xlabel('Value')
# # plt.ylabel('PDF')
# # plt.legend()

# # plt.subplot(1, 2, 2)
# # sorted_samples = np.sort(clt_samples)
# # y = np.arange(1, len(sorted_samples) + 1) / len(sorted_samples)
# # plt.plot(sorted_samples, y, label='Central Limit Theorem')
# # sorted_samples = np.sort(bm_samples)
# # y = np.arange(1, len(sorted_samples) + 1) / len(sorted_samples)
# # plt.plot(sorted_samples, y, label='Box-Muller Method')
# # plt.xlabel('Value')
# # plt.ylabel('CDF')
# # plt.legend()

# # plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# num_samples = 1000

# # Generate two sets of uniform random variables between 0 and 1
# u1 = np.random.rand(num_samples)
# u2 = np.random.rand(num_samples)

# # Apply the Box-Muller transform to generate standard Gaussian random variables
# z1 = np.sqrt(-2 * np.log(u1)) * np.cos(2 * np.pi * u2)
# z2 = np.sqrt(-2 * np.log(u1)) * np.sin(2 * np.pi * u2)

# # Plot the generated Gaussian random variables
# plt.hist(z1, bins=30, density=True, alpha=0.6, color='g')
# plt.hist(z2, bins=30, density=True, alpha=0.6, color='b')

# # Plot the standard Gaussian PDF for comparison
# x = np.linspace(-3, 3, 100)
# pdf = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)
# plt.plot(x, pdf, 'r-', lw=2)

# plt.title("Box-Muller: Generated Gaussian Random Variables vs. Standard Gaussian")
# plt.xlabel("Value")
# plt.ylabel("Probability Density")
# plt.show()
