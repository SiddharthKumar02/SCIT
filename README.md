# SCIT
This is the repository for all SCIT tasks
## Task 1
We are required to plot the histograms of Poisson and normal distributions for set of 1000 samples 3 times making use of the ``numpy.random.poisson()`` and the ``numpy.random.normal()`` functions to generate the samples and then, using the same parameters, select **100 data points** at random and plot the histogram of the average of them.

*Pre-requisites: python, matplotlib, numpy*
### Sub-Task 1: Plotting Poisson Distribution
A set of 1000 samples is selected randomly using the ``numpy.random.poisson()`` function. It takes the parameters *lam* and *size* which are the expectation of interval and the number of samples to be generated respectively and returns an array containing the samples from the poisson distribution. **The size _determines the_ output shape**.

The graph is plotted using the ``pyplot.hist()`` function

![alt Poisson Distribution with *lam*=10](https://github.com/SiddharthKumar02/SCIT/blob/master/Task_1/Graphs/Poisson/Poisson0.png "Poisson Distribution with lam=10") | ![alt iteration 2](https://github.com/SiddharthKumar02/SCIT/blob/master/Task_1/Graphs/Poisson/Poisson1.png "Iteration 2") | ![alt iteration 3](https://github.com/SiddharthKumar02/SCIT/blob/master/Task_1/Graphs/Poisson/Poisson2.png "Iteration 3")

**Inference:** The ``numpy.random.poisson()`` function generates samples that follow the poisson distribution with highest frequencies around the mean value hence creating the same curve as a poisson distribution.

### Sub-Task 2: Plotting Normal Distribution
A set of 1000 samples is selected randomly using the ``numpy.random.normal()`` function. It takes the parameters *mean*,*standard deviation* and *size*.

*Mean*: Expectation value of the distribution

*Standard deviation*: Spread or width of the distribution

 *Size*: Determines the shape of the output

 ``pyplot.hist()`` function is used to spawn the following graphs.

 ![alt Normal Distribution with *Mean*=0](https://github.com/SiddharthKumar02/SCIT/blob/master/Task_1/Graphs/Normal/Normal0.png "Normal Distribution with Mean=0") | ![alt iteration 2](https://github.com/SiddharthKumar02/SCIT/blob/master/Task_1/Graphs/Normal/Normal1.png "Iteration 2") | ![alt iteration 3](https://github.com/SiddharthKumar02/SCIT/blob/master/Task_1/Graphs/Normal/Normal2.png "Iteration 3")

 **Inference:** The ``numpy.random.normal()`` function generates samples that follow the normal distribution with highest frequencies around the mean value hence creating the bell curve.


 ### Sub-Task 3: Plotting the Average of Poisson and Normal Distributions
 A set of 100 data points are selected randomly from both of the above two distributions using the ``numpy.random.poisson()`` and the ``numpy.random.normal()`` function. A histogram is plotted for the new data set generated taking the average of their respective datapoints from both the distributions.

 ``pyplot.hist()`` function is used for the generation of the histogram.

 _Mean_=100

 ![alt Histogram for the average of Normal and Poisson distributions 1st iteration](https://github.com/SiddharthKumar02/SCIT/blob/master/Task_1/Graphs/Average/Average0.png "Histogram for the average of Normal and Poisson distributions 1st iteration")| ![alt 100th iteration](https://github.com/SiddharthKumar02/SCIT/blob/master/Task_1/Graphs/Average/Average15.png "Iteration 15" ) | ![](https://github.com/SiddharthKumar02/SCIT/blob/master/Task_1/Graphs/Average/Average99.png "Iteration 100")

 **Inference:** The mean of the average graph is very close to the mean of both the normal and poisson distributions, Which implies that the mean of the average histograph of both normal and poisson distribution still gives the same mean as the respective distributions itself.
