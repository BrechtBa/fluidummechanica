#!/usr/bin/python
# coding: utf-8
# Dit werk is gelicenseerd onder de licentie Creative Commons Naamsvermelding-GelijkDelen 4.0 Internationaal. Ga naar http://creativecommons.org/licenses/by-sa/4.0/ om een kopie van de licentie te kunnen lezen.
import numpy as np

# Gegevens
rho_p = 830.			# kg/m3
mu_p = 0.5				# Pa s
D_p = 1.0        		# m
V_flow_p = 1800./3600.	# m3/s
rho_m = 1000.			# kg/m3
nu_m = 1e-6				# m2/s
D_m = 0.074   			# m


# Oplossing
# \mathrm{Re}_p = \mathrm{Re}_m
# \frac{v_p D_p}{\nu_p} = \frac{v_m D_m}{\nu_m}
# v_m = v_p \frac{\nu_m}{\nu_p} \frac{D_p}{D_m}

# Uitwerking
v_p = 4.*V_flow_p/np.pi/D_p**2
nu_p = mu_p/rho_p

v_m = v_p*nu_m/nu_p*D_p/D_m

print('De snelheid voor het model is:')
print('v_m = {:.4f} m/s'.format(v_m) )
