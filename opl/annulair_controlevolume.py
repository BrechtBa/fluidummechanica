#!/usr/bin/python
# coding: utf-8
# Dit werk is gelicenseerd onder de licentie Creative Commons Naamsvermelding-GelijkDelen 4.0 Internationaal. Ga naar http://creativecommons.org/licenses/by-sa/4.0/ om een kopie van de licentie te kunnen lezen.
import numpy as np

# Gegevens
g = 9.81				# m/s2
rho = 1.22   			# kg/m3
r = 20.   				# m
dr = 1.					# m
v_1a = 10.				# m/s
omega_1 = 1.26			# rad/s
omega_2 = 1.29			# rad/s

# Oplossing
# Behoud van impuls voor een controlevolume met één instroom en één uitstroom in de axiale richting
# F_a = \dot{m} (v_{2a}-v_{1a})
# 
# Behoud van massa
# \rho v_{1a} A = \rho v_{2a} A 
# v_{2a} = v_{1a}
#
# Krachten die inwerken op het controlevolume in axiale richting:
# F is de kracht die het voorwerp uitoefent op de lucht in het controlevolume
# F_a = F + p_1 A - p_2 A = 0
# F = (p_2 - p_1) 2 \pi r dr
#
# Bernoulli:
# 1/2 \rho v_1^2 + p_1 = 1/2 \rho v_2^2 + p_2
# p_2-p_1 = 1/2 \rho (v_1^2-v_2^2)
#
# v_1^2 = v_{1a}^2 + \omega_1^2 r^2
# v_2^2 = v_{2a}^2 + \omega_2^2 r^2


# Uitwerking
v_2a = v_1a
v_1 = (v_1a**2 + omega_1**2*r**2)**0.5
v_2 = (v_2a**2 + omega_2**2*r**2)**0.5
# dp = p_2-p_1
dp = 1./2.*rho*(v_1**2-v_2**2)
F = dp*2.*np.pi*r*dr

print('De kracht die wordt uitgeoefend op het voorwerp in het controlevolume is:')
print('F = {:.2f} kN in de richting van de stroming'.format(-F/1000) )
