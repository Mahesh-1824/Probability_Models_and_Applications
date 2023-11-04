# import scipy
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches 
from scipy.stats import expon
mean = (0+1+3)/10
values_icdf = []
num_of_samples = 10000
for i in range(num_of_samples):
    inverse = (-np.log(1-np.random.rand()))*mean
    values_icdf.append(inverse)

exponential_dist = expon(scale=mean)
values_inbuilt = exponential_dist.rvs(size=10000)
x = np.linspace(0, max(values_inbuilt), 1000)
pdf_values = expon.pdf(x, scale=mean)
cdf_values = exponential_dist.cdf(x)

values_icdf.sort()
xx = np.linspace(0, max(values_icdf), 1000)
pdf_valuesx = (np.exp( -xx/mean))/mean
cdf_valuesx = 1 - np.exp(-xx/mean)
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(x, pdf_values, label='PDF1',color='red')
plt.plot(xx, pdf_valuesx, label='PDF2',color='blue')
plt.title('PDF of Exponent Random Variable')
pop_a = mpatches.Patch(color='red', label='Inbuilt PDF') 
pop_b = mpatches.Patch(color='blue', label='Generated PDF') 
plt.legend(handles=[pop_a,pop_b]) 
plt.xlabel('Exponential Variable (X)')
plt.ylabel('PDF')
plt.grid(True)

# Plot the CDF
plt.subplot(1, 2, 2)
plt.plot(x, cdf_values, label='CDF1',color='red')
plt.plot(xx, cdf_valuesx, label='CDF2',color='blue')
plt.title('CDF of Exponent Random Variable')
pop_a = mpatches.Patch(color='red', label='Inbuilt CDF') 
pop_b = mpatches.Patch(color='blue', label='Generated CDF') 
plt.legend(handles=[pop_a,pop_b]) 
plt.xlabel('Exponential Variable (X)')
plt.ylabel('CDF')
plt.grid(True)
plt.show()