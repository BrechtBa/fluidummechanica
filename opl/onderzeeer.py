#!/usr/bin/python
# coding: utf-8
# Dit werk is gelicenseerd onder de licentie Creative Commons Naamsvermelding-GelijkDelen 4.0 Internationaal. Ga naar http://creativecommons.org/licenses/by-sa/4.0/ om een kopie van de licentie te kunnen lezen.
import numpy as np

# Gegevens
rho_p = 1028.			# kg/m3
nu_p = 1.83e-6			# m2/s
D_p = 20.       		# -
v_p = 10.*0.5144		# m/s
rho_m = 998.			# kg/m3
nu_m = 1.e-6			# m2/s
D_m = 1. 	  			# m
F_m = 200.e3			# N

# Oplossing
# \mathrm{Re}_p = \mathrm{Re}_m
# \frac{v_p D_p}{\nu_p} = \frac{v_m D_m}{\nu_m}
# v_m = v_p \frac{\nu_m}{\nu_p} \frac{D_p}{D_m}
# 
# P_p = F_p v_p
# F_p = F_m \frac{\rho_p}{\rho_m}\frac{v_p^2}{v_m^2}\frac{D_p^2}{D_m^2}

# Uitwerking
v_m = v_p*(nu_m/nu_p)*(D_p/D_m)
F_p = F_m*(rho_p/rho_m)*(v_p**2/v_m**2)*(D_p**2/D_m**2)
P_p = F_p*v_p

print('De snelheid voor het model is:')
print('v_m = {:.1f} m/s'.format(v_m) )
print('Het vermogen van het prototype is:')
print('P_p = {:.0f} kW'.format(P_p/1000) )
