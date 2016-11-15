#!/usr/bin/python
# coding: utf-8
# Dit werk is gelicenseerd onder de licentie Creative Commons Naamsvermelding-GelijkDelen 4.0 Internationaal. Ga naar http://creativecommons.org/licenses/by-sa/4.0/ om een kopie van de licentie te kunnen lezen.
import numpy as np

# Gegevens
g = 9.81				# m/s2
rho = 1.22   			# kg/m3
V_flow = 0.03           # m3/s
alpha = 45*np.pi/180    # rad
H_1 = 0.030 			# m
D_1 = 0.080				# m
D_2 = 0.050				# m
p_1 = 0                 # Pa overdruk

# Oplossing
# Behoud van impuls voor een controlevolume met één instroom en één uitstroom in horizontal (rechts positief) en verticale richting (boven positief):
# F_{\mathrm{reactie},x} - p_2 A_2 \cos \alpha = \dot{m} (v_2 \cos \alpha - 0)
# F_{\mathrm{reactie},y} - p_2 A_2 \sin \alpha = \dot{m} (v_2 \sin \alpha - 0)
#
# De ingaande snelheid is in beide richtingen gelijk aan 0 aangezien deze volledig radiaal is.
#
# De druk in punt 2 kan bepaald worden met behulp van Bernoulli, na verwaarlozing van hoogteverschillen wordt dit:
# p_1 + \frac{1}{2} \rho v_1^2 = p_2 + \frac{1}{2} \rho v_2^2 
# 
# Hier mag $v_1$ niet gelijk aan nul genomen worden. Als je een stroomlijn volgt kom je in één punt op de omtrek uit.
# De snelheden heffen elkaar dus niet op zoals hierboven.
# De gemiddelde snelheid aan de inlaat en de uitlaat zijn:
# v_1 = \frac{\dot{V}}{\pi D_1 H_1}
# v_2 = \frac{4 \dot{V}}{\pi D_1^2}
#
# Invullen in Bernoulli leidt tot een formule voor $p_2$
# Deze infullen in behoud van impuls leidt tot de gevraagde krachten

# Uitwerking
v_1 = V_flow/(np.pi*D_1*H_1)
v_2 = 4*V_flow/(np.pi*D_2**2)

p_2  = p_1 + 0.5*rho*(v_1**2 - v_2**2) 

F_reactie_x = rho*V_flow*(v_2*np.cos(alpha) - 0) + p_2*np.pi*D_2**2/4*np.cos(alpha)
F_reactie_y = rho*V_flow*(v_2*np.sin(alpha) - 0) + p_2*np.pi*D_2**2/4*np.sin(alpha)

print('v_1 = {:.2f} m/2'.format(v_1) )
print('v_2 = {:.2f} m/2'.format(v_2) )
print('p_2 = {:.0f} Pa'.format(p_2) )

print('')
print('kracht die door de stroming op de zuigmond wordt uitgeoefend is:')
print('F_x = {:.2f} N'.format(-F_reactie_x) )
print('F_y = {:.2f} N'.format(-F_reactie_y) )