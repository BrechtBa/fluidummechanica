#!/usr/bin/python
# coding: utf-8
# Dit werk is gelicenseerd onder de licentie Creative Commons Naamsvermelding-GelijkDelen 4.0 Internationaal. Ga naar http://creativecommons.org/licenses/by-sa/4.0/ om een kopie van de licentie te kunnen lezen.

"""
Oplossing:

Het drukverlies kan bepaald worden als:
\begin{equation}
    \Delta p = f \frac{1}{2} \rho v^2 \frac{L}{D}
\end{equation}

Bij het systeem met $n$ buizen zal het debiet opgesplitst worden.
Indien door elke buis evenveel debiet loopt kan de gemiddelde snelheid voor beide systemen bepaald worden als:
\begin{align}
    v_\mathrm{kanaal} &= \frac{\dot{V}}{B H}
    v_\mathrm{buis} &= \frac{4 \dot{V}}{n \pi D^2}
\end{align}

Voor het rechhoekig kanaal moet de hydraulische diameter gebruikt worden voor de berekening van het drukverlies.
Deze wordt bepaald worden als:
\begin{equation}
    D_h = \frac{4 A}{P} = \frac{4 B H}{2 B + 2 H}
\end{equation}

Reynolds getallen worden dan:
\begin{align}
    \mathrm{Re}_\mathrm{kanaal} &= \frac{v_\mathrm{kanaal} D_h}{\nu}
    \mathrm{Re}_\mathrm{buis} &= \frac{v_\mathrm{buis} D}{\nu}
\end{align}

Indien we een bepaald aantal kanalen veronderstellen kan de wrijvingsfactor uit het moody diagram gehaald worden en kan de drukval voor 1 m leiding bepaald worden.
Of er kan een iteratieve procedure gebruikt worden:

\begin{enumerate}
    \item Veronderstel $n$
    \item Bepaal $\mathrm{Re}_\mathrm{kanaal}$ en $\mathrm{Re}_\mathrm{buis}$
    \item Bepaal $f_\mathrm{kanaal}$ en $f_\mathrm{buis}$
    \item Bepaal $n$ uit $f_\mathrm{kanaal} \frac{1}{2} \rho v_\mathrm{kanaal}^2 \frac{1}{D_h} = f_\mathrm{buis} 8 \rho \frac{\dot{V}^2}{n^2 \pi^2} \frac{1}{D^5}$
\end{enumerate}


"""

import numpy as np
import _lib.frictionfactor

# Gegevens
g = 9.81                 # m/s2
rho = 1.22               # kg/m3
nu = 15e-6               # m2/s
H = 0.060                # m
B = 0.200                # m
D = 0.060                # m
e = 0.02e-3              # m
V_flow = 80./3600.       # m3/s


# Uitwerking

# voor het kanaal kan alles vooraf berekend worden
# bereken snelheid
v_kanaal = V_flow/(B*H)

# bereken de hydraulische diameter
D_h = (4*B*H)/(2*B+2*H)

# bereken Reynolds
Re_kanaal = v_kanaal*D_h/nu

# bereken wrijvingsfactor
f_kanaal = _lib.frictionfactor.turbulent(Re_kanaal,e/D_h)

niter = 10
n = 2
for i in range(niter):
    n_old = n
    
    # bereken snelheid
    v_buis = 4*V_flow/(n*np.pi*D**2)

    # bereken Reynolds
    Re_buis = v_buis*D/nu
    
    # bereken wrijvingsfactor
    f_buis = _lib.frictionfactor.turbulent(Re_buis,e/D)
    
    # bereken n
    n2 = (f_buis*8*rho*V_flow**2/np.pi**2*1./D**5)/(f_kanaal*0.5*rho*v_kanaal**2*1./D_h)
    n = np.ceil( n2**0.5 )
    
    print(n)
    
    if n == n_old:
        # controle
        dp_kanaal = f_kanaal*0.5*rho*v_kanaal**2*1./D_h
        dp_buis = f_buis*0.5*rho*v_buis**2*1./D

        break
    

    
print('')
print('De snelheden zijn:')
print('v_kanaal: {:.3f} m/s'.format(v_kanaal) )
print('v_buis: {:.3f} m/s'.format(v_buis) )
    
print('')
print('De hydraulische diameter van de buis is:')
print('D_h: {:.0f} mm'.format(D_h*1000) )
    
print('')
print('De Reynoldsgetallen zijn:')
print('Re_kanaal: {:.0f}'.format(Re_kanaal) )
print('Re_buis: {:.0f}'.format(Re_buis) )

print('')
print('De wrijvingsfactoren zijn:')
print('f_kanaal: {:.3f}'.format(f_kanaal) )
print('f_buis: {:.3f}'.format(f_buis) )

print('')
print('De drukvallen zijn:')
print('dp_kanaal: {:.3f} Pa/m'.format(dp_kanaal) )
print('dp_buis: {:.3f} Pa/m'.format(dp_buis) )

print('')
print('Het aantal nodige buizen is:')
print('n: {:.0f}'.format(n) )

