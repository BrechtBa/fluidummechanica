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
D_h = 0.011       		# m
D_v = 0.014				# m
e = 0.10e-3				# m
V_flow = 15./60000		# m3/s
n = 10					# - , het aantal horizontale verbindingen

# Oplossing
# H_{\mathrm{i},i} &= H_{\mathrm{i},i+1} - R'_{\mathrm{v},i} \dot{V}_{\mathrm{v},i}  i=1 \rightarrow n-1
# H_{\mathrm{u},i+1} &= H_{\mathrm{u},i} - R'_{\mathrm{v},i} \dot{V}_{\mathrm{v},i}  i=1 \rightarrow n-1
# H_{\mathrm{u},i} &= H_{\mathrm{i},i} - R'_{\mathrm{h},i} \dot{V}_{\mathrm{h},i}    i=1 \rightarrow n
# \dot{V}_{\mathrm{h},i+1} = \dot{V}_{\mathrm{v},i+1} + \dot{V}_{\mathrm{h},i}       i=1 \rightarrow n-1


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

H_i = np.zeros(n)
H_u = np.zeros(n)

f_h = np.zeros_like(V_flow_h)
f_v = np.zeros_like(V_flow_h)

R_h = np.zeros_like(V_flow_h)
R_v = np.zeros_like(V_flow_h)
R = np.zeros_like(V_flow_h)
h_L = np.zeros_like(V_flow_h)
h_Lh = np.zeros_like(V_flow_h)
h_Lv = np.zeros_like(V_flow_h)


# initialiseer het stelsel A*x = b
# variabelen zijn H_i 1->n, H_u 1->n-1, V_flow_h 1->n, V_flow_v 1->n-1
nvar = n + n-1 + n + n-1
A = np.zeros((nvar,nvar))
b = np.zeros(nvar)

for k in range(niter):

	print( 'iteration {}, V_flow_h[0] = {:.2f} l/min'.format(k,V_flow_h[0]*60000) )
	
	# bereken Re
	Re_v = 4.0*V_flow_v/(nu*np.pi*D_v)
	Re_h = 4.0*V_flow_h/(nu*np.pi*D_h)

	# bereken f
	for i in range(n):
		if Re_v[i] > 2300:
			f_v[i] = _lib.frictionfactor.turbulent(Re_v[i],e/D_v)
		else:
			f_v[i] = _lib.frictionfactor.laminar(Re_v[i])
			
		if Re_h[i] > 2300:
			f_h[i] = _lib.frictionfactor.turbulent(Re_h[i],e/D_h)
		else:
			f_h[i] = _lib.frictionfactor.laminar(Re_h[i])
	
	# bereken R_h en R_v
	for i in range(n):
		R_h[i] = (8.*f_h[i])/(g*np.pi**2)*L_h/D_h**5*V_flow_v[i]
		R_v[i] = (8.*f_v[i])/(g*np.pi**2)*L_v/D_v**5*V_flow_h[i]
	
    
	# pas de matrix aan
	A[i,j] = 

	# bereken V_flow_h, V_flow_v, H_i en H_u
	x = np.dot( np.linalg.inverse(A),b)
    
    V_flow_h = x[]
    V_flow_v = x[]
    H_i = x[]
    H_u = x[]
    
	# itereer
	
	


print('')
print('het ladingsverlies is:')
print('h_l = {:.3f} m'.format(h_L) )


	
# plot stijl instellen
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
