#!/usr/bin/python
# coding: utf-8
# Dit werk is gelicenseerd onder de licentie Creative Commons Naamsvermelding-GelijkDelen 4.0 Internationaal. Ga naar http://creativecommons.org/licenses/by-sa/4.0/ om een kopie van de licentie te kunnen lezen.
import numpy as np
import _lib.frictionfactor

# Gegevens
g = 9.81				# m/s2
rho = 1000.				# kg/m3
nu = 1e-6				# m2/s
D_A = 0.200      		# m
L_A = 2000.				# m
D_B = 0.150      		# m
L_B = 3000.				# m
D_C = 0.100      		# m
L_C = 2000.				# m
D_D = 0.180      		# m
L_D = 1000.				# m
e = 0.5e-3				# m
V_flow_A = 200./3600.	# m3/s



# Oplossing
# \frac{p_1}{\rho g} + 8 \frac{\dot{V}_\mathrm{A}^2}{g \pi^2 D_\mathrm{A}^4} + z_1 - h_mathrm{L,A} - h_mathrm{L,BC} - h_mathrm{L,D} = \frac{p_2}{\rho g} + 8 \frac{\dot{V}_\mathrm{D}^2}{g \pi^2 D_\mathrm{A}^4} + z_2
# p_1-p_2 = 8 \rho \frac{\dot{V}_\mathrm{A}^2}{\pi^2} ( \frac{1}{D_\mathrm{A}^4}-\frac{1}{D_\mathrm{D}^4} ) + \rho g ( h_mathrm{L,A} + h_mathrm{L,BC} + h_mathrm{L,D} )

# h_mathrm{L,A} = 8 f_\mathrm{A} \frac{\dot{V}_\mathrm{A}^2}{g \pi^2} \frac{L_\mathrm{A}}{D_\mathrm{A}^5}
# h_mathrm{L,BC} = h_mathrm{L,B} = 8 f_\mathrm{B} \frac{\dot{V}_\mathrm{B}^2}{g \pi^2} \frac{L_\mathrm{B}}{D_\mathrm{B}^5}
# h_mathrm{L,BC} = h_mathrm{L,C} = 8 f_\mathrm{C} \frac{\dot{V}_\mathrm{B}^2}{g \pi^2} \frac{L_\mathrm{C}}{D_\mathrm{C}^5}
# h_mathrm{L,D} = 8 f_\mathrm{D} \frac{\dot{V}_\mathrm{D}^2}{g \pi^2} \frac{L_\mathrm{D}}{D_\mathrm{D}^5}

# \dot{V}_\mathrm{B} = x \dot{V}_\mathrm{A}
# \dot{V}_\mathrm{C} = (1-x) \dot{V}_\mathrm{A}
# \dot{V}_\mathrm{D} = \dot{V}_\mathrm{A}

# f_\mathrm{B} x^2 \frac{L_\mathrm{B}}{D_\mathrm{B}^5} = f_\mathrm{C} (1-x)^2 \frac{L_\mathrm{C}}{D_\mathrm{C}^5}

# \mathrm{Re}_\mathrm{A} = \frac{4\dot{V}_\mathrm{A}}{\pi D_\mathrm{A} \nu}
# \mathrm{Re}_\mathrm{B} = \frac{4\dot{V}_\mathrm{B}}{\pi D_\mathrm{B} \nu}
# \mathrm{Re}_\mathrm{C} = \frac{4\dot{V}_\mathrm{C}}{\pi D_\mathrm{C} \nu}
# \mathrm{Re}_\mathrm{D} = \frac{4\dot{V}_\mathrm{D}}{\pi D_\mathrm{D} \nu}


# Stel $x = 0.5$
# Bereken  $\dot{V}_\mathrm{A-D}$
# Bereken  $f_\mathrm{A-D}$
# bereken een nieuwe $x$
# itereer

# Uitwerking
x = 0.5
niter = 3
for i in range(niter):
	# bereken debieten
	V_flow_B = x*V_flow_A
	V_flow_C = (1-x)*V_flow_A
	V_flow_D = V_flow_A

	Re_A = (4*V_flow_A)/(np.pi*D_A*nu)
	Re_B = (4*V_flow_B)/(np.pi*D_B*nu)
	Re_C = (4*V_flow_C)/(np.pi*D_C*nu)
	Re_D = (4*V_flow_D)/(np.pi*D_D*nu)
	
	# bereken wrijvingsfactoren
	f_A = _lib.frictionfactor.turbulent(Re_A,e/D_A)
	f_B = _lib.frictionfactor.turbulent(Re_B,e/D_B)
	f_C = _lib.frictionfactor.turbulent(Re_C,e/D_C)
	f_D = _lib.frictionfactor.turbulent(Re_D,e/D_D)
	
	# bereken $x$ uit $A x^2 + B x + C = 0$
	A = f_B*L_B/D_B**5 - f_C*L_C/D_C**5
	B = 2*f_C*L_C/D_C**5
	C = -f_C*L_C/D_C**5
	
	x1 = (-B + (B**2-4*A*C)**0.5)/(2*A)
	x2 = (-B - (B**2-4*A*C)**0.5)/(2*A)
	if x1 >= 0 and x1 <= 1:
		x = x1
	elif x2 >= 0 and x2 <= 1:
		x = x2
	else:
		raise ValueError( 'Both solutions are invalid x1: {}, x2: {}'.format(x1,x2) )
	
	print(x)
	

h_LA = 8*f_A*V_flow_A**2/(np.pi**2*g)*L_A/D_A**5
h_LB = 8*f_B*V_flow_B**2/(np.pi**2*g)*L_B/D_B**5
h_LC = 8*f_C*V_flow_C**2/(np.pi**2*g)*L_C/D_C**5
h_LD = 8*f_D*V_flow_D**2/(np.pi**2*g)*L_D/D_D**5

h_LBC = h_LB

dp = 8*rho*V_flow_A**2/np.pi**2 * ( 1/D_A**4-1/D_D**4 ) + rho*g*( h_LA + h_LBC + h_LD )

print('')
print('De debieten zijn:')
print('V_flow_A: {:.2f} m3/h'.format(V_flow_A*3600) )
print('V_flow_B: {:.2f} m3/h'.format(V_flow_B*3600) )
print('V_flow_C: {:.2f} m3/h'.format(V_flow_C*3600) )
print('V_flow_D: {:.2f} m3/h'.format(V_flow_D*3600) )

print('')
print('De wrijvingsfactoren zijn:')
print('f_A: {:.3f}'.format(f_A) )
print('f_B: {:.3f}'.format(f_B) )
print('f_C: {:.3f}'.format(f_C) )
print('f_D: {:.3f}'.format(f_D) )

print('')
print('De ladingsverliezen zijn:')
print('h_LA: {:.2f} m'.format(h_LA) )
print('h_LB: {:.2f} m'.format(h_LB) )
print('h_LC: {:.2f} m'.format(h_LC) )
print('h_LD: {:.2f} m'.format(h_LD) )

print('')
print('Het drukverlies is:')
print('dp = {:.0f} kPa'.format(dp/1000) )
