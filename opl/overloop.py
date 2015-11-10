#!/usr/bin/python
# coding: utf-8
# Dit werk is gelicenseerd onder de licentie Creative Commons Naamsvermelding-GelijkDelen 4.0 Internationaal. Ga naar http://creativecommons.org/licenses/by-sa/4.0/ om een kopie van de licentie te kunnen lezen.
import numpy as np

# Gegevens
g = 9.81        		# m/s2
V_flow = 2000./60000.   # m3/s
h = 0.5	        		# m
b = 1.0					# m

# Oplossing
# Het debiet per eenheid breedte is:
# q = \frac{\dot{V}}{b}
#
# Ter hoogte van de overloop is de stroming kritisch
# y_c = \left(q^2/g\right)^{1/3}
#
# De specifieke energie is dan:
# E_c = y_c + \frac{q^2}{2 g y_c}
#
# Verderop in het kanaal zal de energie constant blijven
# E = h + E_c
# y + \frac{q^2}{2 g y} = h + y_c + \frac{q^2}{2 g y_c}
#
# Dit resulteert in een quadratische vergelijking:
# A y^2 + B y + C = 0
# met:
# A = 1
# B = -h - y_c - \frac{q^2}{2 g y_c}
# C = \frac{q^2}{2 g}
#
# y = \frac{-B \pm \sqrt{B^2-4 A C}}{2 A}


# Uitwerking
q = V_flow/b
y_c = (q**2/g)**(1./3.)
E_c = y_c + q**2/(2*g*y_c)

A = 1
B = -h-E_c
C = q**2/(2*g)

yp = (-B +(B**2-4*A*C)**0.5)/(2*A)
ym = (-B -(B**2-4*A*C)**0.5)/(2*A)

print('De diepte in het kanaal voor de overloop is:')
print('y = {:.3f} m'.format(yp) )
