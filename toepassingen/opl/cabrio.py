#!/usr/bin/python
# coding: utf-8
# Dit werk is gelicenseerd onder de licentie Creative Commons Naamsvermelding-GelijkDelen 4.0 Internationaal. Ga naar http://creativecommons.org/licenses/by-sa/4.0/ om een kopie van de licentie te kunnen lezen.
import numpy as np

# Gegevens
C_d_open = 0.45			# -
C_d_dicht = 0.35		# -
v_dicht = 100./3.6		# m/s



# Oplossing
# P_\mathrm{open} = P_\mathrm{dicht}
# F_\mathrm{open} v_\mathrm{open} = P_\mathrm{dicht} v_\mathrm{dicht}
# C_\mathrm{d,open} 1/2 \rho v_\mathrm{open}^2 A v_\mathrm{open} = C_\mathrm{d,dicht} 1/2 \rho v_\mathrm{dicht}^2 A v_\mathrm{dicht}
# v_\mathrm{open} = v_\mathrm{dicht} \left(\frac{C_\mathrm{d,dicht}}{C_\mathrm{d,open}} \right)^{1/3}

# Uitwerking
v_open = v_dicht*(C_d_dicht/C_d_open)**(1./3.)



print('De snelheid voor de cabrio met open dak is:')
print('v_open = {:.1f} km/h'.format(v_open*3.6) )
