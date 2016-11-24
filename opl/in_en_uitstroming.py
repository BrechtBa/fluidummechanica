#!/usr/bin/python
# coding: utf-8
# Dit werk is gelicenseerd onder de licentie Creative Commons Naamsvermelding-GelijkDelen 4.0 Internationaal. Ga naar http://creativecommons.org/licenses/by-sa/4.0/ om een kopie van de licentie te kunnen lezen.
import numpy as np
import _lib.frictionfactor

# Gegevens
g = 9.81                # m/s2
nu = 1e-6               # m2/s
rho = 1000.             # kg/m3
dz = 1.0                # m
L = 10.0                # m
D = 0.10                # m
e = 0.1e-3              # m

K_inlaat = 0.5          # - 
K_uitlaat = 1.0         # - 

# Oplossing
# z_1 -z_2 = h_\mathrm{L} + h_\mathrm{L,inlaat} + h_\mathrm{L,uitlaat}
# h_\mathrm{L} &= 8 f \frac{\dot{V}^2}{\pi^2 g}\frac{L}{D^5} \nonumber \\
# h_\mathrm{L,inlaat} &= 8 K_\mathrm{inlaat} \frac{\dot{V}^2}{\pi^2 g D^4} \nonumber \\
# h_\mathrm{L,uitlaat} &= 8 K_\mathrm{uitlaat} \frac{\dot{V}^2}{\pi^2 g D^4} \nonumber


# Uitwerking zonder lokale verliezen
print('zonder rekening te houden met lokale verliezen:')

f = 0.030
Re = np.nan
print('{:<10} {:<15} {:<15} {:<15}'.format('iter','Re','f','V (m3/s)'))
    
for i in range(4):
    
    V2 = dz/( 8*f*L/(np.pi**2*g*D**5) )
    V = V2**0.5
    
    print('{:<10.0f} {:<15.0f} {:<15.3f} {:<15.4f}'.format(i,Re,f,V))
    
    
    Re = 4*V/(np.pi*D*nu)
    if Re > 2300:
        f = _lib.frictionfactor.turbulent(Re,e/D)
    else:
        f = _lib.frictionfactor.laminar(Re)

print('')
        
print('Het debiet is:')
print('V = {:.3f} m3/s'.format(V) )



# Uitwerking
print('')
print('rekening houdend met lokale verliezen:')

f = 0.030
Re = np.nan

print('{:<10} {:<15} {:<15} {:<15}'.format('iter','Re','f','V (m3/s)'))
    
for i in range(4):
    
    V2 = dz/( 8*f*L/(np.pi**2*g*D**5) + 8*K_inlaat/(np.pi**2*g*D**4) + 8*K_uitlaat/(np.pi**2*g*D**4) )
    V = V2**0.5
    
    print('{:<10.0f} {:<15.0f} {:<15.3f} {:<15.4f}'.format(i,Re,f,V))
    
    
    Re = 4*V/(np.pi*D*nu)
    if Re > 2300:
        f = _lib.frictionfactor.turbulent(Re,e/D)
    else:
        f = _lib.frictionfactor.laminar(Re)

print('')
        
print('Het debiet is:')
print('V = {:.3f} m3/s'.format(V) )