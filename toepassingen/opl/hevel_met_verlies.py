#!/usr/bin/python
# coding: utf-8
# Dit werk is gelicenseerd onder de licentie Creative Commons Naamsvermelding-GelijkDelen 4.0 Internationaal. Ga naar http://creativecommons.org/licenses/by-sa/4.0/ om een kopie van de licentie te kunnen lezen.
import numpy as np
import _lib.frictionfactor

# Gegevens
g = 9.81                # m/s2
rho = 1000.             # kg/m3
nu = 1.e-6              # Pa s
D = 0.024               # m
L = 3.                  # m
e = 0.1e-3              # m
z_0 = 1.5               # m
z_1 = 1.8               # m
z_2 = 0.0               # m



# Oplossing
# De energievergelijking tussen punt 0 aan het oppervlak en punt 2 aan de uitstroom wordt:
# H_2 = H_0 - h_\mathrm{L}
# 8 \frac{\dot{V}^2}{\pi^2 g D^4} + z_2 = z_0 - 8 f \frac{\dot{V}^2}{\pi^2 g}\frac{L}{D^5}
# Oplossen naar \dot{V} geeft:
# \dot{V} = \left( \frac{z_0-z_2}{ \frac{8}{\pi^2 g D^4} + \frac{8 f}{\pi^2 g}\frac{L}{D^5} }  \right)^{1/2}

# Stel $f = 0.02$
# Bereken  $\dot{V}$
# Bereken $\mathrm{Re}$
# Bereken $f$
# itereer

# Uitwerking
f = 0.03
niter = 5
V_flow = -1
for i in range(niter):
    V_flow_old = V_flow
    
    # bereken debieten
    V_flow = ( (z_0-z_2)/( (8.)/(np.pi**2*g*D**4) + (8.*f)/(np.pi**2*g)*L/D**5 ) )**0.5
    
    print('{:.1f}'.format(V_flow*60000))
        
    if abs(V_flow_old-V_flow)/V_flow <= 0.01:
        break
    
    # Bereken Reynolds
    Re = (4*V_flow)/(np.pi*D*nu)
    
    # bereken wrijvingsfactoren
    f = _lib.frictionfactor.turbulent(Re,e/D)
    

    
print('')
print('Het Reynoldsgetal is:')
print('Re: {:.0f}'.format(Re) )

print('')
print('De wrijvingsfactor is:')
print('f: {:.3f}'.format(f) )

print('')
print('Het debiet is:')
print('V_flow: {:.1f} l/min'.format(V_flow*60000) )

