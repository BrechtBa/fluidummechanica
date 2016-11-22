#!/usr/bin/python
# coding: utf-8
# Dit werk is gelicenseerd onder de licentie Creative Commons Naamsvermelding-GelijkDelen 4.0 Internationaal. Ga naar http://creativecommons.org/licenses/by-sa/4.0/ om een kopie van de licentie te kunnen lezen.
import numpy as np
import matplotlib.pyplot as plt

# Gegevens
B = 50.					# m
H = 300.				# m
C_d = 2.2       		# -
p = 0.40				# -
rho = 1.22				# kg/m3
v_0 = 30.				# m/s
z_0 = 10.				# m

# Oplossing
# v_0 = C z_0^p
# C = \frac{v_0}{z_0^p}

# F = C_d 1/2 \rho v^2 A
# dF = C_d 1/2 \rho v^2 B dz
# F = C_d 1/2 \rho B C^2 \int_0^H z^{2p} dz
# f = C_d 1/2 \rho B C^2 z^{2p}

# Uitwerking
C = v_0/z_0**p

C_f = C_d*0.5*rho*B*C**2 
p_f = 2*p
F = C_d*0.5*rho*B*C**2*( 1./(2*p+1)*H**(2*p+1) )

print('De totale kracht op het gebouw is:')
print('F = {:.1f} kN'.format(F/1000) )
print('f = {:.0f} z^{} N/m'.format(C_f,p_f) )

z = np.linspace(0,H,100)
v = C*z**p
f = C_d*0.5*rho*B*v**2

plt.plot(f,z)
plt.xlabel('$f$ (N/m)')
plt.ylabel('$z$ (m)')
plt.show()