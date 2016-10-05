#!/usr/bin/python
# coding: utf-8
# Dit werk is gelicenseerd onder de licentie Creative Commons Naamsvermelding-GelijkDelen 4.0 Internationaal. Ga naar http://creativecommons.org/licenses/by-sa/4.0/ om een kopie van de licentie te kunnen lezen.
import numpy as np

# Gegevens
g = 9.81                # m/s2
rho = 1000.         	# kg/m3
R = 6.         	        # m
Hl = 3.        	        # m
Hr = 1.        	        # m



# Oplossing
# De horizontale kracht per eenheid breedte kan berekend worden als de kracht op een verticaal recht oppervlak
# Dit wordt dus:
# f_\mathrm{x,l} = \frac{1}{2} \rho g H_\mathrm{l} H_\mathrm{l}
# f_\mathrm{x,r} = \frac{1}{2} \rho g H_\mathrm{r} H_\mathrm{r}
# f_\mathrm{x,r} = f_\mathrm{x,l}-f_\mathrm{x,r}
#
# Voor de verticale kracht moet de integraal uitgewerkt worden:
# \int_A -p (\mathbf{r} \circ \mathbf{n}) \mathrm{d} A
# De projectie van de druk in de verticale richting aan de linkerzijde kan geschreven worden als:
# -p (\mathbf{r} \circ \mathbf{n}) = -p \sin \alpha
# aan de rechterzijde wordt dit:
# -p (\mathbf{r} \circ \mathbf{n}) = p \sin \alpha
# Verder kan de druk aan de linker zijde uitgewerkt worden als:
# p_\mathrm{l} = \rho g (H_\mathrm{l} - H_\mathrm{r} - R \sin \alpha)
# en aan de rechterzijde als:
# p_\mathrm{r} = \rho g (- R \sin \alpha)
# Het infenitesimaal oppervlak kan geschreven worden als:
# \mathrm{d} A = R \mathrm{d} \alpha
#
# De krachten worden dan:
# f_\mathrm{x,l} = \int_{\alpha_1}^{\alpha_2} -\rho g (H_\mathrm{l} - H_\mathrm{r} - R \sin \alpha) \sin \alpha R \mathrm{d} \alpha
# f_\mathrm{x,r} = \int_{\alpha_1}^{0} \rho g ( - R \sin \alpha) \sin \alpha R \mathrm{d} \alpha
# f_\mathrm{x,r} = f_\mathrm{x,l} + f_\mathrm{x,r}
#
# de integratie grenzen worden:
# \alpha_1 = -\arcsin(\frac{H_\mathrm{r}}{R})
# \alpha_2 = -\arcsin(\frac{H_\mathrm{l}-H_\mathrm{r}}{R})


# Uitwerking
f_xl = 0.5*rho*g*Hl*Hl
f_xr = 0.5*rho*g*Hr*Hr
f_x = f_xl - f_xr

print('f_xl = {:.3f} kN/m'.format(f_xl/1000))
print('f_xr = {:.3f} kN/m'.format(f_xr/1000))
print('')


alpha1 = -np.arcsin(Hr/R)
alpha2 = np.arcsin( (Hl-Hr)/R )

print('alpha1 = {:.3f} rad'.format(alpha1))
print('alpha2 = {:.3f} rad'.format(alpha2))
print('')

alpha_l = np.linspace(alpha1,alpha2,100)
p_l = rho*g*(Hl-Hr-R*np.sin(alpha_l))
integrandum_l = -p_l*np.sin(alpha_l)*R
f_yl = np.trapz(integrandum_l,alpha_l)


alpha_r = np.linspace(alpha1,0.,100)
p_r = rho*g*(-R*np.sin(alpha_r))
integrandum_r = p_r*np.sin(alpha_r)*R
f_yr = np.trapz(integrandum_r,alpha_r)

f_y = f_yl + f_yr

print('f_yl = {:.3f} kN/m'.format(f_yl/1000))
print('f_yr = {:.3f} kN/m'.format(f_yr/1000))
print('')


print('De totale horizontale kracht is:')
print('f_x = {:.2f} kN/m'.format(f_x/1000) )

print('De totale verticale kracht is:')
print('f_y = {:.2f} kN/m'.format(f_y/1000) )

