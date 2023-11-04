import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches 
from scipy.stats import rayleigh
mean = 2*(0+1+3)/10
sigma = (np.sqrt(2/np.pi))*mean
values_icdf = []
num_of_samples = 10000
for i in range(num_of_samples):
    inverse = np.sqrt(2 * (sigma ** 2) * -np.log(1-np.random.rand()))
    values_icdf.append(inverse)

values_icdf.sort()
x1 = np.linspace(0, max(values_icdf), 1000)
pdf_values_inbuilt = rayleigh.pdf(x1,scale=sigma)
cdf_values_inbuilt = rayleigh.cdf(x1,scale=sigma)
x = np.linspace(0, max(values_icdf), 1000)
pdf_values = (x/sigma ** 2)*(np.exp(- (x ** 2)/(2 * (sigma ** 2))))
cdf_values = 1 - np.exp(-x**2 / (2 * sigma**2))
plt.figure(figsize=(12, 6))
plt.subplot(1,2,1)
plt.plot(x1, pdf_values_inbuilt, label="Rayleigh Inbuilt PDF")
plt.plot(x, pdf_values, label="Rayleigh Generated PDF ")
plt.xlabel("Rayleigh Variable (x)")
plt.ylabel("PDF")
plt.legend()
plt.title("PDF of Rayleigh Random Variable ")

plt.subplot(1,2,2)
plt.plot(x1, cdf_values_inbuilt, label="Rayleigh Inbuilt CDF")
plt.plot(x, cdf_values, label="Rayleigh Generated CDF ")
plt.xlabel("Rayleigh Variable (x)")
plt.ylabel("CDF")
plt.legend()
plt.title("CDF of Rayleigh Random Variable ")
plt.show()