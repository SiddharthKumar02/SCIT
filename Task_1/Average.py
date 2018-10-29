import matplotlib.pyplot as plt
import numpy as np
import random
mu,sigma= 100,1

for i in range(100):
    n = np.random.normal(mu,sigma,1000)
    np.savetxt("Data/Average/Normal/Dataset"+str(i)+".csv",n,delimiter=',')
    p = np.random.poisson(mu,1000)
    np.savetxt("Data/Average/Poisson/Dataset"+str(i)+".csv",p,delimiter=',')
    Data= []
    for j in range(100):
        rand = random.randint(0,1000)
        avg = (n[rand-1] + p[rand-1])/float(2)
        Data.append(avg)
    with open("Data/Average/avg/Dataset"+str(i)+".csv","w") as f:
        for item in Data:
            f.write("%s\n" % item)
    bins=plt.hist(Data,30,density=True)
    plt.ylabel('Probability')
    plt.xlabel('Data')
    plt.title('Histogram for Average of Normal & Poisson Distribution')
    plt.savefig('Graphs/Average/Average'+str(i)+'.png')
