import numpy as np
from src.nn import Linear, ReLU, Sigmoid, MSE, Sequential
X=np.array([[0.,0.],[0.,1.],[1.,0.],[1.,1.]])
y=np.array([[0.],[1.],[1.],[0.]])
net=Sequential(Linear(2,8,1),ReLU(),Linear(8,1,2),Sigmoid()); loss=MSE()
for epoch in range(10000):
 p=net.forward(X); v=loss.forward(p,y); net.backward(loss.backward()); net.step(.5)
 if epoch%1000==0: print(epoch, round(v,6))
print(np.c_[p,(p>.5).astype(int)])
