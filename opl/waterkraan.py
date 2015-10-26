#!/usr/bin/python
# coding: utf-8
# Dit werk is gelicenseerd onder de licentie Creative Commons Naamsvermelding-GelijkDelen 4.0 Internationaal. Ga naar http://creativecommons.org/licenses/by-sa/4.0/ om een kopie van de licentie te kunnen lezen.
import numpy as np

# Gegevens
g = 9.81				# m/s2
V_flow = 5./60000.   	# m3/s
D_1 = 0.018        		# m
z_1 = 0.2				# m
z_2 = 0.0				# m

# Oplossing
# v_1 = \frac{\dot{V}}{\pi D_1^2/4}
# 1/2 \rho v_1^2 + \rho g z_1 = 1/2 \rho v_2^2 + \rho g z_2
# A_2 = \frac{\dot{V}}{v_2}

# Uitwerking
v_1 = V_flow/(np.pi*D_1**2/4)
v_2 = (2*(1/2*v_1**2 + g*(z_1 - z_2)))**0.5
A_2 = V_flow/v_2
D_2 = (4*A_2/np.pi)**0.5

print('De diameter is:')
print('D = {:.1f} mm'.format(D_2*1000) )
