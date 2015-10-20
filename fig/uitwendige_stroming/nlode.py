import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt


pi = np.pi
sqrt = np.sqrt
cos = np.cos
sin = np.sin

def dpdt(p, t):
	x = p[0]
	y = p[1]
	return y, x-x**3

t = np.linspace(0, 10, 1000)

p0 = [(1.0,0.8),(1.0,0.7)]

p = []
for pp0 in p0:
	p.append(integrate.odeint(dpdt, pp0, t))


plt.figure()
for pp,pp0 in zip(p,p0):
	plt.plot(pp[:,0],pp[:,1],label='x_0 = {}, y_0 = {}'.format(pp0[0],pp0[1]))

plt.legend()
plt.gca().set_xlabel('x')
plt.gca().set_ylabel('y')
plt.show()