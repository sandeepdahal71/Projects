import numpy as np

class Linear:
    def __init__(self, in_features, out_features, seed=42):
        rng=np.random.default_rng(seed); self.W=rng.normal(0, np.sqrt(2/in_features),(in_features,out_features)); self.b=np.zeros((1,out_features))
    def forward(self,x): self.x=x; return x@self.W+self.b
    def backward(self,grad):
        self.dW=self.x.T@grad/len(self.x); self.db=grad.mean(axis=0,keepdims=True); return grad@self.W.T
    def step(self,lr): self.W-=lr*self.dW; self.b-=lr*self.db
class ReLU:
    def forward(self,x): self.mask=x>0; return np.maximum(x,0)
    def backward(self,g): return g*self.mask
class Sigmoid:
    def forward(self,x): self.y=1/(1+np.exp(-np.clip(x,-50,50))); return self.y
    def backward(self,g): return g*self.y*(1-self.y)
class MSE:
    def forward(self,p,y): self.p,self.y=p,y; return np.mean((p-y)**2)
    def backward(self): return 2*(self.p-self.y)/self.p.size
class Sequential:
    def __init__(self,*layers): self.layers=list(layers)
    def forward(self,x):
        for l in self.layers:x=l.forward(x)
        return x
    def backward(self,g):
        for l in reversed(self.layers):g=l.backward(g)
    def step(self,lr):
        for l in self.layers:
            if hasattr(l,'step'):l.step(lr)
