#!/usr/bin/python
# coding: utf-8
# Dit werk is gelicenseerd onder de licentie Creative Commons Naamsvermelding-GelijkDelen 4.0 Internationaal. Ga naar http://creativecommons.org/licenses/by-sa/4.0/ om een kopie van de licentie te kunnen lezen.
import numpy as np

# Gegevens
g = 9.81                # m/s2
rho = 1000.             # kg/m3
D = 0.024               # m
z_0 = 1.5               # m
z_1 = 1.8               # m
z_2 = 0.0               # m


# Oplossing
# De vergelijking van bernoulli tussen punt 0 aan het oppervlak en punt 2 aan de uitstroom wordt:
# \rho g z_2 + \frac{1}{2} \rho v_2^2 = \rho g z_0
# Oplossen naar v_2 geeft:
# v_2 = \left( 2 g ( z_0-z_2 ) \right)^{1/2}

# Uitwerking
v_2 = ( 2*g*(z_0-z_2 ) )**0.5
V_flow =  v_2*np.pi*D**2/4
v_1 = v_2
    
print('')
print('V_flow: {:.1f} l/min'.format(V_flow*60000) )

print('')
print('De gemiddelde snelheid is:')
print('v_1: {:.2f} m/s'.format(v_1) )