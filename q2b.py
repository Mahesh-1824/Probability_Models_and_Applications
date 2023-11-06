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
