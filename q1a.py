# import scipy
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from scipy.stats import expon
mean = (0+1+3)/10
values_icdf = []
# uniform = np.random.rand(10000)
# values_icdf
num_of_samples = 10000
for i in range(num_of_samples):
    inverse = (-np.log(1-np.random.rand()))*mean
    # print(inverse)
    values_icdf.append(inverse)

# exponential_dist = expon(scale=mean)
# values_inbuilt = exponential_dist.rvs(size=10000)
xx = np.linspace(0, 10, 1000)
pdf_valuesx = expon.pdf(xx, scale=mean)
cdf_valuesx = expon.cdf(xx, scale=mean)

# values_icdf.sort()
# xx = np.linspace(0, 10, 100000)
# pdf_valuesx = (np.exp( -xx/mean))/mean
# print(values_icdf)
# cdf_valuesx = 1 - np.exp(-xx/mean) 

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(xx, pdf_valuesx, label='Exponential Inbuilt PDF')
sns.distplot(values_icdf,hist=False,label='Exponential Generated PDF')
# sns.distplot(values_icdf, hist=False, kde_kws={'bw_method': 0.1, 'kernel': 'gau'}, label='Exponential Generated PDF')
# plt.show()
# plt.subplot(1, 2, 1)

# plt.hist(values_icdf,bins=50, label='Exponential Generated PDF')
plt.title('PDF of Exponent Random Variable') 
plt.legend() 
plt.xlabel('Exponential Variable (X)')
plt.ylabel('PDF')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(xx, cdf_valuesx, label='Exponential Inbuilt CDF')
# plt.hist(values_icdf,bins=50,cumulative=True,label='Exponential Generated CDF')
sns.distplot(values_icdf,hist=False,kde_kws={"cumulative": True},label='Exponential Generated CDF')
plt.title('CDF of Exponent Random Variable')
plt.legend() 
plt.xlabel('Exponential Variable (X)')
plt.ylabel('CDF')
plt.grid(True)
plt.show()