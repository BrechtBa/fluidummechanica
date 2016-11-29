#!/usr/bin/python
# coding: utf-8
# Dit werk is gelicenseerd onder de licentie Creative Commons Naamsvermelding-GelijkDelen 4.0 Internationaal. Ga naar http://creativecommons.org/licenses/by-sa/4.0/ om een kopie van de licentie te kunnen lezen.
import numpy as np

# Gegevens
g = 9.81				# m/s2
rho_l = 1.22   			# kg/m3
rho_o = 800   			# kg/m3
dz_1 = 0.2				# m
dz_2 = 0.6				# m

# Oplossing
# p_s = \rho_o g dz_2
# p_d = \rho_o g dz_1
# p_d = 1/2 \rho_l v^2
# v = \sqrt{2 \frac{p_d}{\rho_l}}

# Uitwerking
p_s = rho_o*g*dz_2
p_d = rho_o*g*dz_1
v = (2*p_d/rho_l)**0.5


print('De statische overdruk is:')
print('p_s = {:.0f} Pa'.format(p_s) )
print('De dynamische overdruk is:')
print('p_d = {:.0f} Pa'.format(p_d) )
print('De snelheid in de buis is:')
print('v = {:.1f} m/s'.format(v) )
