#!/usr/bin/python
# coding: utf-8
# Dit werk is gelicenseerd onder de licentie Creative Commons Naamsvermelding-GelijkDelen 4.0 Internationaal. Ga naar http://creativecommons.org/licenses/by-sa/4.0/ om een kopie van de licentie te kunnen lezen.

"""

De energievergelijking tussen de twee reservoirs wordt:

\begin{equation}
    H_2 = H_1 - h_\mathrm{L} + h_\mathrm{P}
\end{equation}

\noindent
Met de pompkarakteristiek als $H = A - B \dot{V}^2$ wordt dit uitgewerkt tot:

\begin{equation}
    z_2 = z_1 - 8 f \frac{\dot{V}^2}{\pi^2 g}\frac{L}{D^5} + A_\mathrm{pomp} - B_\mathrm{pomp} \dot{V}^2
\end{equation}

\noindent
Oplossen naar \dot{V} geeft:

\begin{equation}
    \dot{V} = \left( \frac{A_\mathrm{pomp} + z_1-z_2}{ \frac{8 f}{\pi^2 g}\frac{L}{D^5} + B_\mathrm{pomp} }  \right)^{1/2}
\end{equation}

\noindent
Deze vergelijking kan met behulp van een iteratieve strategie opgelost worden:

\begin{enumerate}
    \item Stel $f = 0.02$
    \item Bereken $\dot{V}$
    \item Bereken $\mathrm{Re}$
    \item Bereken $f$
    \item ga naar stap 2
\end{enumerate}

"""

import numpy as np
import _lib.frictionfactor

# Gegevens
g = 9.81                # m/s2
rho = 1000.             # kg/m3
nu = 1.e-6              # Pa s
D = 0.024               # m
L = 10.                 # m
e = 0.002e-3            # m
z_1 = 0.0               # m
z_2 = 3.0               # m

# de pompkarakteristiek kan geschreven worden als H = A - B \dot{V}^2
# met $H$ in \unit{m} en $\dot{V}$ in \unit{m^3/2}
A_pomp = 5.             # m
B_pomp = 2.*3600**2     # m/(m^6/s^2)


# Uitwerking
f = 0.03
niter = 5
V_flow = -1
for i in range(niter):
    V_flow_old = V_flow
    
    # bereken debieten
    V_flow = ( (A_pomp + z_1-z_2)/(  (8.*f)/(np.pi**2*g)*L/D**5 + B_pomp  ) )**0.5
    
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
print('De pomp opvoerhoogte is:')
print('H: {:.3f}'.format(A_pomp - B_pomp*V_flow**2) )

print('')
print('Het debiet is:')
print('V_flow: {:.2f} m3/h'.format(V_flow*3600) )

