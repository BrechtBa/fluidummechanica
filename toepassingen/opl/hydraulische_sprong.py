#!/usr/bin/python
# coding: utf-8
# Dit werk is gelicenseerd onder de licentie Creative Commons Naamsvermelding-GelijkDelen 4.0 Internationaal. Ga naar http://creativecommons.org/licenses/by-sa/4.0/ om een kopie van de licentie te kunnen lezen.
import numpy as np
import matplotlib.pyplot as plt

# Gegevens
g = 9.81				# m/s2
rho = 1000   			# kg/m3
z_1 = 0.20 				# m
v_1 = 5.				# m/2

# Oplossing
# Behoud van impuls voor een controlevolume met één instroom en één uitstroom in de richting van de stroming tussen het lage en het hoge gedeelte:
# F = \dot{m} (v_2-v_1)
#
# De krachten kunnen geëvalueerd worden als hydrostatische krachten en het massadebiet kan bepaald worden met de snelheid:
# \frac{1}{2} \rho g z_1^2 B -  \frac{1}{2} \rho g z_2^2 B = \rho v_1 z_1 B (v_2-v_1)
#
# Behoud van massa:
# \rho v_1 z_1 B = \rho v_2 z_2 B
#
# Omvormen naar $v_2$ en invullen geeft:
# \frac{1}{2} \rho g z_1^2 -  \frac{1}{2} \rho g z_2^2 = \rho v_1 z_1 (v_1\frac{z_1}{z_2}-v_1)
#
# Alles vermenigvuldigen met $z_2$ en delen door $\rho$ geeft een 3e graadsvergelijking:
# \frac{1}{2} g z_1^2 z_2 -  \frac{1}{2} g z_2^3 + z_1 v_1^2 (z_2-z_1) = 0

# Deze vergelijking kan numeriek opgelost worden en heeft 2 positieve oplossingen waarvan één de oorspronkelijke hoogte is 


# Uitwerking
niter = 20

z_2 = 1.0
for i in range(niter):
    z_2_old = z_2
    
    f = 0.5*g*z_1**2*z_2 - 0.5*g*z_2**3 + z_1*v_1**2*(z_2-z_1)
    dfdz = 0.5*g*z_1**2 - 3*0.5*g*z_2**2 + 2*z_1*v_1*(z_2-z_1)

    dz = f/dfdz
    z_2 = z_2 - dz
    
    print(z_2)
    
    if abs(z_2_old-z_2) < 1e-4:
        break
        
print('')
print('De hoogte na de hydraulische sprong is:')
print('z_2 = {:.2f} m'.format(z_2) )


plt.plot(z_1,0,'rs')
plt.plot(z_2,f,'ro')

z_2 = np.linspace(0.0,1.0,20)
f = 0.5*g*z_1**2*z_2 - 0.5*g*z_2**3 + z_1*v_1**2*(z_2-z_1)

plt.plot(z_2,f)
plt.plot(z_2,np.zeros_like(z_2),'k--')

plt.show()
