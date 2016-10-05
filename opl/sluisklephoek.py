#!/usr/bin/python
# coding: utf-8
# Dit werk is gelicenseerd onder de licentie Creative Commons Naamsvermelding-GelijkDelen 4.0 Internationaal. Ga naar http://creativecommons.org/licenses/by-sa/4.0/ om een kopie van de licentie te kunnen lezen.
import numpy as np

# Gegevens
g = 9.81                # m/s2
rho = 1000.         	# kg/m3
H = 4.         	        # m
B = 4.        	        # m
R = 6.        	        # m
F = 100e3               # N


# Oplossing
# Het moment van de externe kracht moet gelijk zijn aan het moment uitgeoefend door de water druk:
# $F R = Fp \frac{1}{3} R^*$
# De grootte van de kracht uitgeoefend door de druk kunnen we bepalen als:
# $Fp = \frac{1}{2} R^* \rho g H B$
# Met alpha de hoek die de klep maakt met de horizontale wordt:
# $R^* \sin(\alpha) = H$
# Invullen geeft:
# $F R = \frac{1}{2} \frac{H}{\sin(\alpha)} \rho g H B \frac{1}{3} \frac{H}{\sin(\alpha)}$
# Oplossen naar $\alpha$:
# \sin^2(\alpha) = \frac{1}{6} \frac{ \rho g B H^3 }{F R}


# Uitwerking
sin2alpha = 1./6*(rho*g*B*H**3)/(F*R)
alpha = np.arcsin( sin2alpha**0.5 )

# controle
Rs = H/np.sin(alpha)
Fp = 1./2*Rs*rho*g*H*B

print('R* = {:.2f} m'.format(Rs) )
print('Mf = {:.2f} kNm'.format(F*R/1000) )
print('Mp = {:.2f} kNm'.format(Fp*Rs/3/1000) )

print('De hoek tussen de klep en de horizontale is:')
print('alpha = {:.2f} deg'.format(alpha*180/np.pi) )

