import numpy as np
from src.nn import Linear, ReLU

def test_shapes():
 l=Linear(3,2); x=np.ones((4,3)); y=l.forward(x); assert y.shape==(4,2); assert l.backward(np.ones_like(y)).shape==(4,3)
def test_relu():
 r=ReLU(); assert np.array_equal(r.forward(np.array([[-1,2]])),np.array([[0,2]]))
