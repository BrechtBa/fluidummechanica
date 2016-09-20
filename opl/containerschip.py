#!/usr/bin/python
# coding: utf-8
# Dit werk is gelicenseerd onder de licentie Creative Commons Naamsvermelding-GelijkDelen 4.0 Internationaal. Ga naar http://creativecommons.org/licenses/by-sa/4.0/ om een kopie van de licentie te kunnen lezen.
import numpy as np

# Gegevens
g = 9.81                # m/s2
rho = 1045.         	# kg/m3
L = 300.         	    # m
B = 60.        	        # m
H = 20.        	        # m
m = 150000e3            # kg
H_z = 30.  	            # m
alpha = 10.*np.pi/180	# rad

# Oplossing
# Zoek eerst de diepgang van de boot.
# Het ondergedompeld volume kan daarvoor worden opgesplitst in een rechthoek en een driehoek
#
# m g = F_o = V_o \rho g
# V_o = L ( A_\mathrm{rechthoek} + A_\mathrm{driehoek} )
# m = L ( B H_o + \frac{1}{2} B B \tan(\alpha) ) \rho 
# H_o = \frac{m}{\rho L B} - \frac{1}{2} B \tan(\alpha)
#
# Nu kan het aangrijpingspunt van de opwaartse kracht bepaald worden als het
# zwaartepunt van het ondergedomperld volume
# Kies een oorsprong in het midden van de kiel van het schip
#
# x_a = \frac{ x_\mathrm{rechthoek} A_\mathrm{rechthoek} + x_\mathrm{driehoek} A_\mathrm{driehoek} }{A_\mathrm{rechthoek} + A_\mathrm{driehoek}}
# x_\mathrm{rechthoek} = 1/2 H_o \sin(\alpha)
# x_\mathrm{driehoek} = H_o \sin(\alpha) + 1/6 B \cos(\alpha) + 1/3 B \tan(\alpha) \sin(\alpha)
#
# x_z = H_z \sin(\alpha)
#
# als $\Delta x = x_a-x_z < 0$ dan zal het schip kapseizen

# Uitwerking

H_o = m/(rho*L*B) - 0.5*B*np.tan(alpha)

x_rechthoek = 1./2*H_o*np.sin(alpha)
x_driehoek = H_o*np.sin(alpha) + 1./6*B*np.cos(alpha) + 1./3*B*np.tan(alpha)*np.sin(alpha)

A_rechthoek = B*H_o
A_driehoek = 0.5*B*B*np.tan(alpha)

x_a = ( x_rechthoek*A_rechthoek + x_driehoek*A_driehoek )/(A_rechthoek + A_driehoek)
x_z = H_z*np.sin(alpha)

dx = x_a - x_z

print('H_o = {:.2f} m'.format(H_o) )

print('Het verschil tussen aangrijpingspunt en zwaartepunt in de horizontale richting x_a - x_z is:')
print('dx = {:.2f} m'.format(dx) )

if dx > 0:
    print('Oef, de boot zal niet kapseizen.')
else:
    print('Verlaat het schip! De boot zal kapseizen.')