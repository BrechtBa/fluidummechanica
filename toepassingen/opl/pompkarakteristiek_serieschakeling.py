#!/usr/bin/python
# coding: utf-8
# Dit werk is gelicenseerd onder de licentie Creative Commons Naamsvermelding-GelijkDelen 4.0 Internationaal. Ga naar http://creativecommons.org/licenses/by-sa/4.0/ om een kopie van de licentie te kunnen lezen.

"""

De energievergelijking tussen de twee reservoirs wordt:

\begin{equation}
    H_2 = H_1 - h_\mathrm{L} + h_\mathrm{P}
\end{equation}

\noindent
Dit wordt uitgewerkt tot:

\begin{align}
    z_2 &= z_1 \\
        &- 8 f_A \frac{\dot{V}^2}{\pi^2 g}\frac{L_A}{D_A^5} \nonumber \\
        &- 8 f_B \frac{\dot{V}^2}{\pi^2 g}\frac{L_B}{D_B^5} \nonumber \\
        &- 8 K_i \frac{\dot{V}^2}{\pi^2 g}\frac{1}{D_A^4} \nonumber \\
        &- 8 K_v \frac{\dot{V}^2}{\pi^2 g}\frac{1}{D_A^4} \nonumber \\
        &- 8 K_b \frac{\dot{V}^2}{\pi^2 g}\frac{1}{D_B^4} \nonumber \\
        &- 8 K_u \frac{\dot{V}^2}{\pi^2 g}\frac{1}{D_B^4} \nonumber \\
        &+ h_\mathrm{P} \nonumber
\end{align}

\noindent
Oplossen naar \dot{V} geeft:

\begin{equation}
    \dot{V} = \left(  \frac{h_\mathrm{P} + z_1-z_2}{ \frac{8 f_A}{\pi^2 g}\frac{L_A}{D_A^5} + \frac{8 f_B}{\pi^2 g}\frac{L_B}{D_B^5} + \frac{8 K_i}{\pi^2 g}\frac{1}{D_A^4} + \frac{8 K_v}{\pi^2 g}\frac{1}{D_A^4} + \frac{8 K_b}{\pi^2 g}\frac{1}{D_B^4} + \frac{8 K_u}{\pi^2 g}\frac{1}{D_B^4} }  \right)^{1/2}
\end{equation}

\noindent
Deze vergelijking kan met behulp van een iteratieve strategie opgelost worden:

\begin{enumerate}
    \item Stel $f_A = 0.02$, $f_B = 0.02$
    \item Bereken $\dot{V}$
    \item Bereken $\mathrm{Re}_A$, $\mathrm{Re}_B$
    \item Bereken $f_A$, $f_B$
    \item ga naar stap 2
\end{enumerate}

"""

import numpy as np
import scipy.interpolate
import _lib.frictionfactor

# Gegevens
g = 9.81                # m/s2
rho = 1000.             # kg/m3
nu = 1.e-6              # Pa s
D_A = 0.200             # m
L_A = 20.               # m
e_A = 0.5e-3            # m
D_B = 0.120             # m
L_B = 16.               # m
e_B = 0.5e-3            # m
K_i = 0.50              # - 
K_v = 0.84*0.32         # - 
K_b = 0.51              # - 
K_u = 1.00              # - 
z_1 = 0.0               # m
z_2 = 15.0              # m

V_pomp = np.array([ 0., 80., 120., 170., 190.])/3600.       # m3/s
H_pomp = np.array([40., 37.,  30.,  12.,   0.])             # m


# interpolatie van h_P
h_P_ifv_V = scipy.interpolate.interp1d(V_pomp,H_pomp,'quadratic')


# Uitwerking methode 1
f_A = 0.03
f_B = 0.03
h_P = 18

# interpolatie

niter = 20
V_flow = -1

for i in range(niter):
    V_flow_old = V_flow
    
    # bereken debieten
    V_flow = ( (h_P + z_1-z_2)/(  (8.*f_A)/(np.pi**2*g)*L_A/D_A**5  +  (8.*f_B)/(np.pi**2*g)*L_B/D_B**5  +  (8.*K_i)/(np.pi**2*g)*1./D_A**4  +  (8.*K_v)/(np.pi**2*g)*1./D_A**4  +  (8.*K_b)/(np.pi**2*g)*1./D_B**4  +  (8.*K_u)/(np.pi**2*g)*1./D_B**4  ) )**0.5
    
    print('{:.1f}'.format(V_flow*3600))
        
    if abs(V_flow_old-V_flow)/V_flow <= 0.001:
        break
    
    # demping
    if V_flow_old > 0:
        d = 0.8
        V_flow = (1-d)*V_flow + d*V_flow_old
    
    # bereken de opvoerhoogte
    h_P = h_P_ifv_V(V_flow).item()
    
    # Bereken Reynolds
    Re_A = (4*V_flow)/(np.pi*D_A*nu)
    Re_B = (4*V_flow)/(np.pi*D_B*nu)
    
    # bereken wrijvingsfactoren
    f_A = _lib.frictionfactor.turbulent(Re_A,e_A/D_A)
    f_B = _lib.frictionfactor.turbulent(Re_B,e_B/D_B)
    

   
print('')
print('De Reynoldsgetallen zijn:')
print('Re_A: {:.0f}'.format(Re_A) )
print('Re_B: {:.0f}'.format(Re_B) )

print('')
print('De wrijvingsfactorren zijn:')
print('f_A: {:.3f}'.format(f_A) )
print('f_B: {:.3f}'.format(f_B) )

print('')
print('De pomp opvoerhoogte is:')
print('h_P: {:.3f}'.format(h_P) )

print('')
print('Het debiet is:')
print('V_flow: {:.1f} m3/h'.format(V_flow*3600) )



# Uitwerking methode 2
print('\n\n')
print('*'*80)
print('Methode 2\n')
# Een ruwe benadering voor h_P is kwadratisch:
# $h_\mathrm{P} = A + B \dot{V}^2$
# $30 = A + B (120/3600)^2$
# $12 = A + B (170/3600)^2$
#
# A = 30. - B*(120/3600)^2
# B = \frac{12-30}{(170/3600)^2-(120/3600)^2}

B =(12.-30.)/((170./3600.)**2-(120./3600.)**2)
A = 30. - B*(120./3600.)**2


f_A = 0.03
f_B = 0.03
h_P = 18

# interpolatie

niter = 20
V_flow = -1

for i in range(niter):
    V_flow_old = V_flow
    
    # bereken debieten
    V_flow = ( (A + z_1-z_2)/(  (8.*f_A)/(np.pi**2*g)*L_A/D_A**5  +  (8.*f_B)/(np.pi**2*g)*L_B/D_B**5  +  (8.*K_i)/(np.pi**2*g)*1./D_A**4  +  (8.*K_v)/(np.pi**2*g)*1./D_A**4  +  (8.*K_b)/(np.pi**2*g)*1./D_B**4  +  (8.*K_u)/(np.pi**2*g)*1./D_B**4  -  B  ) )**0.5
    
    print('{:.1f}'.format(V_flow*3600))
        
    if abs(V_flow_old-V_flow)/V_flow <= 0.001:
        break
    
    # bereken de opvoerhoogte
    h_P = h_P_ifv_V(V_flow).item()
    
    # Bereken Reynolds
    Re_A = (4*V_flow)/(np.pi*D_A*nu)
    Re_B = (4*V_flow)/(np.pi*D_B*nu)
    
    # bereken wrijvingsfactoren
    f_A = _lib.frictionfactor.turbulent(Re_A,e_A/D_A)
    f_B = _lib.frictionfactor.turbulent(Re_B,e_B/D_B)
    

print('')
print('De Reynoldsgetallen zijn:')
print('Re_A: {:.0f}'.format(Re_A) )
print('Re_B: {:.0f}'.format(Re_B) )

print('')
print('De wrijvingsfactorren zijn:')
print('f_A: {:.3f}'.format(f_A) )
print('f_B: {:.3f}'.format(f_B) )

print('')
print('De pomp opvoerhoogte is:')
print('h_P: {:.3f}'.format(h_P) )

print('')
print('Het debiet is:')
print('V_flow: {:.1f} m3/h'.format(V_flow*3600) )


