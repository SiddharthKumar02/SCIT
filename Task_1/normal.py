import matplotlib.pyplot as plt
import numpy as np

for i in range(3):
    mu,sigma=0,0.1
    s = np.random.normal(mu,sigma,1000)
    np.savetxt("Data/Normal/Dataset"+str(i)+".csv",s,delimiter=",")
    count, bins, ignored = plt.hist(s,30, density=True)
    plt.plot(bins,1/(sigma * np.sqrt(2 * np.pi)) * np.exp(-(bins-mu)**2/(2* sigma **2)), linewidth=2, color='r')
    plt.ylabel('Frequency')
    plt.xlabel('Data')
    plt.title('Histogram from Random Normal Distribution')
    plt.savefig('Graphs/Normal/Normal'+str(i)+'.png')
    plt.show()
