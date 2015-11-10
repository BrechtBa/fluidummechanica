#!/usr/bin/python
# coding: utf-8
# Dit werk is gelicenseerd onder de licentie Creative Commons Naamsvermelding-GelijkDelen 4.0 Internationaal. Ga naar http://creativecommons.org/licenses/by-sa/4.0/ om een kopie van de licentie te kunnen lezen.
import numpy as np

# Gegevens
rho = 1000.				# kg/m3
v_in = 4.0        		# m/s
p_in = 150.e3   		# Pa
A_in = 0.2	        	# m2
A_uit = 0.4				# m2

# Oplossing
# Behoud van impult in de x-richting voor een stationair controlevolume met 1 instroom en 1 uitstroom wordt:
# -F_r + p_\mathrm{in} A_\mathrm{in} + p_\mathrm{uit} A_\mathrm{uit} = \dot{m} \left(-v_\mathrm{uit}-v_\mathrm{in}\right)
# de drukken hierin zijn relatief ten opzichte van atmosfeerdruk
#
# Behoud van massa geeft:
# \dot{V} = A_\mathrm{in} v_\mathrm{in}
# v_\mathrm{uit} = \dot{V} / A_\mathrm{uit}
#
# De stroming is stationair, niet-viskeus en niet-samendrukbaar dus Bernoulli langs een stroomlijn van in- tot uitlaat wordt:
# p_\mathrm{in} + \frac{1}{2} \rho v_\mathrm{in}^2 = p_\mathrm{uit} + \frac{1}{2} \rho v_\mathrm{uit}^2 
#
# p_\mathrm{uit} = p_\mathrm{in} + \frac{1}{2} \rho \left( v_\mathrm{in}^2 - v_\mathrm{uit}^2 \right)
# 
# De reactiekracht van de buis op het water wordt dan:
# F_r = p_\mathrm{in} A_\mathrm{in} + p_\mathrm{uit} A_\mathrm{uit} - \rho \dot{V} \left(-v_\mathrm{uit}-v_\mathrm{in}\right)



# Uitwerking
V_flow = v_in*A_in
v_uit = V_flow/A_uit
p_uit = p_in + 0.5*rho*( v_in**2 -v_uit**2)

F_r =  p_in*A_in + p_uit*A_uit - rho*V_flow*(-v_uit-v_in)

print('De reactie kracht van de buis op het water is :')
print('F_r = {:.1f} kN in de richting van de uitlaatstroming'.format(F_r/1000) )
