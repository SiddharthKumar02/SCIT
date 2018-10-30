import numpy as np
import matplotlib.pyplot as plt
for i in range(3):
    mu=10
    s = np.random.poisson(mu,1000)
    np.savetxt("Data/Poisson/Dataset"+str(i)+".csv",s,delimiter=",")
    count,bins,ignored=plt.hist(s,14,density=True)
    plt.ylabel('Probability')
    plt.xlabel('Data')
    plt.title('Histogram for Random Poisson Distribution')
    plt.savefig('Graphs/Poisson/Poisson'+str(i)+'.png')
    plt.show()
