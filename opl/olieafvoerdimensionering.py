#!/usr/bin/python
# coding: utf-8
# Dit werk is gelicenseerd onder de licentie Creative Commons Naamsvermelding-GelijkDelen 4.0 Internationaal. Ga naar http://creativecommons.org/licenses/by-sa/4.0/ om een kopie van de licentie te kunnen lezen.
import numpy as np
import _lib.frictionfactor

# Gegevens
g = 9.81                # m/s2
rho = 830.              # kg/m3
nu = 240.e-6            # Pa s
L = 1.0                 # m
z_1 = 0.5               # m
z_2 = 0.0               # m
V_flow = 80./60000      # l/min
K_bocht_45 = 0.21*0.55  # -  Tabel B.1, r/D = 1, glad  en Tabel B.2
K_bocht_90 = 0.21       # -  Tabel B.1, r/D = 1, glad

# Oplossing
# De energievergelijking tussen het reservoir en de uitstroom wordt:
# H_2 = H_1 - h_\mathrm{L} - 2 h_\mathrm{L,bocht,45^\circ} - h_\mathrm{L,bocht,90^\circ}
# z_2 + 8 \frac{\dot{V}^2}{\pi^2 g D^4} = z_1 - 8 f \frac{\dot{V}^2}{\pi^2 g}\frac{L}{D^5} - 2 8 K_\mathrm{bocht,45^\circ} \frac{\dot{V}^2}{\pi^2 g D^4} - 8 K_\mathrm{bocht,90^\circ} \frac{\dot{V}^2}{\pi^2 g D^4}
# Indien de stroming turbulent is, is er een iteratieve oplossingsprocedure nodig, maar aangezien het om smeerolie gaat is de stroming waarschijnlijk laminair
# We kunnen in elk geval de vergelijking oplossen naar $D$ indien we één $D$ in het ladingsverlies als gekend veronderstellen:
# D^4 = \frac{ 8 \frac{\dot{V}^2}{\pi^2 g} + 8 f \frac{\dot{V}^2}{\pi^2 g}\frac{L}{D} +  2 8 K_\mathrm{bocht,45^\circ} \frac{\dot{V}^2}{\pi^2 g} + 8 K_\mathrm{bocht,90^\circ} \frac{\dot{V}^2}{\pi^2 g} }{z_1-z_2}
# Indien de stroming laminair is, kan de wrijvingsfactor uitgewerkt worden:
# f = \frac{64}{\mathrm{Re}} = \frac{16 \pi \nu D}{\dot{V}}
# Dit invullen geeft:
# D^4 = \frac{ 8 \frac{\dot{V}^2}{\pi^2 g} + 8 16 \nu \frac{\dot{V}}{\pi g} L +  2 8 K_\mathrm{bocht,45^\circ} \frac{\dot{V}^2}{\pi^2 g} + 8 K_\mathrm{bocht,90^\circ} \frac{\dot{V}^2}{\pi^2 g} }{z_1-z_2}

# Indien de stroming niet laminair is, is er een iteratieve procedure nodig
# Stel $D = 0.020$
# Bereken $\mathrm{Re}$
# Bereken $f$
# Bereken  $D$
# itereer

# Uitwerking
D4 = ( 8.*(V_flow**2)/(np.pi**2*g) + 8.*16.*nu*(V_flow)/(np.pi*g)*L +  2.*8.*K_bocht_45*(V_flow**2)/(np.pi**2*g) + 8.*K_bocht_90*(V_flow**2)/(np.pi**2*g) )/(z_1-z_2)
D = D4**(1./4.)

# het reynoldsgetal controleren
Re = 4*V_flow/(np.pi*nu*D)

print('')
print('Het Reynoldsgetal is:')
print('Re: {:.0f}'.format(Re) )

print('')
print('Het minimum diameter is:')
print('D: {:.1f} mm'.format(D*1000) )



# iteratief:
# Indien de stroming laminair is geeft ook dit meteen de exacte oplossing voor eenderwelke veronderstelling $D>0$
print('')
D = 0.020
niter = 5
for i in range(niter):
    D_old = D
    
    Re = 4*V_flow/(np.pi*nu*D)
    
    if Re > 2300:
        f = _lib.frictionfactor.turbulent(Re,0./D)
    else:
        f = _lib.frictionfactor.laminar(Re)
    
    D4 = ( 8.*(V_flow**2)/(np.pi**2*g) + 8*f*(V_flow**2)/(np.pi**2*g)*L/D_old +  2.*8.*K_bocht_45*(V_flow**2)/(np.pi**2*g) + 8.*K_bocht_90*(V_flow**2)/(np.pi**2*g) )/(z_1-z_2)
    D = D4**(1./4.)

    print('{:.1f}'.format(D*1000))
        
    if abs(D_old-D)/D <= 0.01:
        break
    