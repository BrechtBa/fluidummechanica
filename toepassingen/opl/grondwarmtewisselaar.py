#!/usr/bin/python
# coding: utf-8
# Dit werk is gelicenseerd onder de licentie Creative Commons Naamsvermelding-GelijkDelen 4.0 Internationaal. Ga naar http://creativecommons.org/licenses/by-sa/4.0/ om een kopie van de licentie te kunnen lezen.
import numpy as np
import _lib.frictionfactor

# Gegevens
g = 9.81				# m/s2
rho = 1130.				# kg/m3
mu = 1.4363e-3			# Pa s
D = 0.037      			# m
L_A = 160.				# m
L_B = 160.+120.			# m
e = 0.015e-3			# m
V_flow = 50./60000.		# m3/s



# Oplossing

# h_mathrm{L,A} = h_mathrm{L,B} 
# \dot{V}_\mathrm{A} = x \dot{V}
# \dot{V}_\mathrm{B} = (1-x) \dot{V}
# 8 f_\mathrm{A} \frac{x^2 \dot{V}^2}{g \pi^2} \frac{L_\mathrm{A}}{D^5} = 8 f_\mathrm{B} \frac{(1-x)^2 \dot{V}^2}{g \pi^2} \frac{L_\mathrm{B}}{D^5}
# f_\mathrm{A} x^2 L_\mathrm{A} = f_\mathrm{B} (1-x)^2 L_\mathrm{B}

# Stel $x = 0.5$
# Bereken  $\dot{V}_\mathrm{A-D}$
# Bereken  $f_\mathrm{A-D}$
# bereken een nieuwe $x$
# itereer

# Uitwerking
x = 0.5
niter = 5
for i in range(niter):
	# bereken debieten
	V_flow_A = x*V_flow
	V_flow_B = (1-x)*V_flow

	Re_A = (4*rho*V_flow_A)/(np.pi*D*mu)
	Re_B = (4*rho*V_flow_B)/(np.pi*D*mu)
	
	# bereken wrijvingsfactoren
	f_A = _lib.frictionfactor.turbulent(Re_A,e/D)
	f_B = _lib.frictionfactor.turbulent(Re_B,e/D)
	
	# bereken $x$ uit $A x^2 + B x + C = 0$
	A = f_A*L_A - f_B*L_B
	B = 2*f_B*L_B
	C = -f_B*L_B
	
	x1 = (-B + (B**2-4*A*C)**0.5)/(2*A)
	x2 = (-B - (B**2-4*A*C)**0.5)/(2*A)
	if x1 >= 0 and x1 <= 1:
		x = x1
	elif x2 >= 0 and x2 <= 1:
		x = x2
	else:
		raise ValueError( 'Both solutions are invalid x1: {}, x2: {}'.format(x1,x2) )
	
	print(x)
	
	
print('')
print('De Reynoldsgetallen zijn:')
print('Re_A: {:.3f}'.format(Re_A) )
print('Re_B: {:.3f}'.format(Re_B) )

print('')
print('De wrijvingsfactoren zijn:')
print('f_A: {:.3f}'.format(f_A) )
print('f_B: {:.3f}'.format(f_B) )

print('')
print('De debieten zijn:')
print('V_flow_A: {:.1f} l/min'.format(V_flow_A*60000) )
print('V_flow_B: {:.1f} l/min'.format(V_flow_B*60000) )

