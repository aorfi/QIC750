import numpy as np
import matplotlib.pyplot as plt

delta = 0.01
x= y = np.arange(-1,1+delta,delta)

phi1 , phi2 = np.meshgrid(x, y)


phiext = 0.5
alpha = np.arange(0,1+delta,delta)
bar = []
for i in alpha:
    phi1= np.arange(-0.5,0.5+delta,delta)
    phi2 = -phi1
    potential = -np.cos(2*np.pi*phi1)-np.cos(2*np.pi*phi2) - i*np.cos(2*np.pi*phi1-2*np.pi*phi2+2*np.pi*phiext)
    potential_min = min(potential)
    phi1= phi2 = 0
    potential_zero = -np.cos(2*np.pi*phi1)-np.cos(2*np.pi*phi2) - i*np.cos(2*np.pi*phi1-2*np.pi*phi2+2*np.pi*phiext)
    bar.append(potential_zero-potential_min)



# phiext = 0.5
# alpha = 0.8
# potential = -np.cos(2*np.pi*phi1)-np.cos(2*np.pi*phi2) - alpha*np.cos(2*np.pi*phi1-2*np.pi*phi2+2*np.pi*phiext)
    

# plt.pcolor(phi1,phi2,potential)
# #plt.axis([phi2.min(), phi2.max(), phi1.min(), phi1.max()])
# plt.colorbar(label = "$\mathcal{V}/E_J$")
# plt.xlabel(r"$\frac{\phi_1}{2\pi}$", size = 14)
# plt.ylabel(r"$\frac{\phi_2}{2\pi}$", size = 14)
# plt.title("Potential of 3 JJ Circuit")
# plt.grid()
# plt.contour(phi1,phi2,potential)
# plt.show()

# phi1= np.arange(-1,1+delta,delta)
# phi2 = -phi1
# phiext = 0.5
# alpha = 0.5
# potential = -np.cos(2*np.pi*phi1)-np.cos(2*np.pi*phi2) - alpha*np.cos(2*np.pi*phi1-2*np.pi*phi2+2*np.pi*phiext)
    
# plt.plot(phi1,potential)
# plt.xlabel(r"$\frac{\phi_1}{2\pi}$", size = 14)
# plt.ylabel(r"$\frac{\phi_2}{2\pi}$", size = 14)
# plt.title("Potential of 3 JJ Circuit along $\phi_2=-\phi_1$")
# plt.grid()
# plt.show()
# 
plt.plot(alpha,bar)
plt.xlabel(r"$\alpha$", size = 14)
plt.ylabel("Barrier", size = 14)
plt.title("Potential of 3 JJ Circuit along $\phi_2=-\phi_1$")
plt.grid()
plt.show()

