#!/usr/bin/python
# coding: utf-8
# Dit werk is gelicenseerd onder de licentie Creative Commons Naamsvermelding-GelijkDelen 4.0 Internationaal. Ga naar http://creativecommons.org/licenses/by-sa/4.0/ om een kopie van de licentie te kunnen lezen.
import numpy as np
import matplotlib.pyplot as plt
import _lib.frictionfactor

# Gegevens
g = 9.81				# m/s2
rho = 990				# kg/m3
nu = 1e-6				# m2/s

L_h = 0.500				# m
L_v = 0.040				# m
D_h = 0.014       		# m
D_v = 0.018				# m
e = 0.10e-3				# m
V_flow = 5./60000		# m3/s
n = 10					# - , het aantal horizontale verbindingen

# Oplossing
# \dot{V}_{\mathrm{h},i}, D_\mathrm{h}, e \rightarrow f_{\mathrm{h},i}
# \dot{V}_{\mathrm{v},i}, D_\mathrm{v}, e \rightarrow f_{\mathrm{v},i}

# R_{\mathrm{h},i} = \frac{8*f_{\mathrm{h},i}}{g \pi^2} \frac{L_\mathrm{h}}{D_\mathrm{h}^5}
# R_{\mathrm{v},i} = \frac{8*f_{\mathrm{v},i}}{g \pi^2} \frac{L_\mathrm{v}}{D_\mathrm{v}^5}

# R_{1\rightarrow 2} = \left( \frac{1}{\sqrt{R_{\mathrm{h},1}}} + \frac{1}{\sqrt{2R_{\mathrm{v},1}+R_{\mathrm{h},1}}} \right)^{-2}
# R_{1\rightarrow i} = \left( \frac{1}{\sqrt{R_{\mathrm{h},i-1}}} + \frac{1}{\sqrt{2R_{\mathrm{v},i-1}+R_{1\rightarrow i-1}}} + \right)^{-2}

# h_{\mathrm{L},1\rightarrow i} = h_{\mathrm{L,h},i}
# h_{\mathrm{L},1\rightarrow i} = 2 h_{\mathrm{L,v},i-1} + h_{\mathrm{L},1\rightarrow i-1}
# R_{1\rightarrow i} \dot{V}_{\mathrm{v},i} = R_{\mathrm{h},i} \dot{V}_{\mathrm{h},i}^2
# R_{1\rightarrow i} \dot{V}_{\mathrm{v},i} =  2 R_{\mathrm{v},i-1} \dot{V}_{\mathrm{v},i-1}^2 + R_{1\rightarrow i-1} \dot{V}_{\mathrm{v},i-1}^2

# Oplossingsmethode:
# schat \dot{V}_{\mathrm{v},i}, \dot{V}_{\mathrm{h},i}
# bereken Re_{\mathrm{v},i}, Re_{\mathrm{h},i}
# bereken f_{\mathrm{v},i}, f_{\mathrm{h},i}
# bereken R_{1\rightarrow 2},..., R_{1\rightarrow n}
# bereken \dot{V}_{\mathrm{v},i}, \dot{V}_{\mathrm{h},i}
# itereer


# Uitwerking
niter = 10

# initialisatie
V_flow_h = V_flow/n*np.ones(n)
V_flow_v = np.cumsum(V_flow_h)
V_flow_v[n-1] = V_flow

f_h = np.zeros_like(V_flow_h)
f_v = np.zeros_like(V_flow_h)

R_h = np.zeros_like(V_flow_h)
R_v = np.zeros_like(V_flow_h)
R = np.zeros_like(V_flow_h)
h_L = np.zeros_like(V_flow_h)
h_Lh = np.zeros_like(V_flow_h)
h_Lv = np.zeros_like(V_flow_h)

for k in range(niter):

	print( 'iteration {}, V_flow_h[0] = {:.2f} l/min'.format(k,V_flow_h[0]*60000) )
	
	# bereken Re
	Re_v = 4.0*V_flow_v/(nu*np.pi*D_v)
	Re_h = 4.0*V_flow_h/(nu*np.pi*D_h)

	# bereken f
	damping = 0.5
	for i in range(n):
		if Re_v[i] > 2300:
			f_v[i] = damping*f_v[i] + (1-damping)*_lib.frictionfactor.turbulent(Re_v[i],e/D_v)
		else:
			f_v[i] = damping*f_v[i] + (1-damping)*_lib.frictionfactor.laminar(Re_v[i])
			
		if Re_h[i] > 2300:
			f_h[i] = damping*f_h[i] + (1-damping)*_lib.frictionfactor.turbulent(Re_h[i],e/D_h)
		else:
			f_h[i] = damping*f_h[i] + (1-damping)*_lib.frictionfactor.laminar(Re_h[i])
	
	# bereken R_h en R_v
	for i in range(n):
		R_h[i] = (8.*f_h[i])/(g*np.pi**2)*L_h/D_h**5
		R_v[i] = (8.*f_v[i])/(g*np.pi**2)*L_v/D_v**5
	
	# bereken R
	R[0] = R_h[0]
	for i in range(1,n):
		R[i] = ( 1.0/R_h[i]**0.5 + 1.0/(2.0*R_v[i-1]+R[i-1])**0.5 )**-2

	# bereken V_flow_h en V_flow _v
	for i in range(n-1, 0, -1):
		V_flow_h[i]   = (R[i]/R_h[i])**0.5 * V_flow_v[i]
		V_flow_v[i-1] = ( R[i]/(2.0*R_v[i-1] + R[i-1]) )**0.5 * V_flow_v[i]

	V_flow_h[0] = V_flow_v[0]
	
	# itereer
	
	
	
# totaal ladingsverlies
h_L = R[n-1]*V_flow_v[n-1]**2

print('')
print('het ladingsverlies is:')
print('h_l = {:.3f} m'.format(h_L) )


# equivalente lengte
Re_eq = 4.0*V_flow/(nu*np.pi*D_v)
if Re_eq > 2300:
	f_eq = _lib.frictionfactor.turbulent(Re_eq,e/D_v)
else:
	f_eq = _lib.frictionfactor.laminar(Re_eq)
	
L_eq = h_L*np.pi**2*g*D_v**5/8.0/f_eq/V_flow



	
# plot stijl instellen
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.rc('figure', autolayout=True)
	
# plotten
plt.figure()
width = 0.5
plt.bar(np.arange(n)+1-0.5*width, V_flow_v*60000, width, color='r', label=r'verticaal')
plt.bar(np.arange(n)+1-0.5*width+0.5*width, V_flow_h*60000, width, color='b', label=r'horizontaal')
plt.legend(loc=2)
plt.xlabel(r'$i$ (-)')
plt.ylabel(r'$\dot{V}$ (l/min)')
plt.gca().set_xlim([0.5,n+1])
plt.gca().set_ylim([0.0,1.1*V_flow*60000])
plt.gca().set_xticks(np.arange(n)+1)
plt.show()
