import numpy as np
import time
import matplotlib.pyplot as plt
Lis = [[1,1,1],[1,0,1],[0,1,1],[2,2,1],[-1,-1,1],[-1,0,1],[0,-1,1],[-2,-2,1]];
X = np.array(Lis)
Label = [1,1,1,1,-1,-1,-1,-1]
Line = [1,-1,0]
W = np.array(Line)
xcor = [-2,2] 
ycor = [0,0]

#initial plot
plt.title("Intial  ") 
ycor[0] = (-1*W[2]+(-1*W[0]*xcor[0]))/W[1]
ycor[1] = (-1*W[2]+(-1*W[0]*xcor[1]))/W[1]
plt.plot(X[0:4,0],X[0:4,1],'ro')
plt.plot(X[4:,0],X[4:,1],'bo')
plt.plot(xcor,ycor)
plt.show()

for i in range(0,30) :
	Res = np.matmul(X,np.matrix.transpose(W))
	tem = Res[0:4]<0
	tem = np.matrix.transpose(np.array(1*tem))
	#print(tem.shape)
	Tes1= -1*np.matmul(tem,X[0:4,:])
	#print(Tes1.shape)
	tem = Res[4:]>0
	tem = np.matrix.transpose(np.array(1*tem))
	tem=np.array(tem)
	Tes2 = 1*np.matmul(tem,X[4:,:])
	res = Tes1+Tes2
	W = W - 0.05*res
	#print(W)
	ycor[0] = (-1*W[2]+(-1*W[0]*xcor[0]))/W[1]
	ycor[1] = (-1*W[2]+(-1*W[0]*xcor[1]))/W[1]
	#print (X[0:4,0])
	fig = plt.figure()
	plt.title("Iteration  "+str(i+1)) 
	plt.plot(X[0:4,0],X[0:4,1],'ro')
	plt.plot(X[4:,0],X[4:,1],'bo')
	plt.plot(xcor,ycor)
	plt.show()	
	plt.close(fig)