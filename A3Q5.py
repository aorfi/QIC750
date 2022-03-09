import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import linalg

def ham(N,Eq,Ej,ng):
    H = np.zeros([N,N])
    for i in range(N):
        n = i-int(N/2)
        H[i,i] = 4*Eq*(n-ng)**2
        
        if i == N-1:
            break
        H[i,i+1] = -Ej*0.5
        H[i+1,i] = -Ej*0.5
    return H

delta = 0.01
ng = np.arange(-1,1+delta,delta)

Ej = 5.25*10**(-25)
Eq = 5*Ej
N = 3
H = ham(N,Eq,Ej,0.5)
print(H)
e_all = []
for i in ng:
    H = ham(N,Eq,Ej,i)
    e, v = scipy.linalg.eig(H)
    e.sort()
    e_all.append(e)
plt.plot(ng,e_all)
plt.grid()
plt.xlabel(r"$n_g$", size = 14)
plt.ylabel("E", size = 14)
plt.title("Energy Bands CPB $E_Q/E_J = 1$")
plt.show()