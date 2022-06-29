## MP-NOT
import numpy as np
def McNot(x,w,t):
    #Using Sigmoidal Activation
    net = np.dot(x,w);
    out = 1/(1+np.exp(-0.1*net));
    if out>t:
        output = 1
    else:
        output = 0
    return output

#inputs and weights
x0 = np.array([0,1])
x1 = np.array([1,1])
w = np.array([-1,1])


t = 0.5 #threshold

#verifying the output
ans1 = McNot(x0,w,t)
print (x0, "value", ans1)
ans2 = McNot(x1,w,t)
print (x1, "value", ans2)
