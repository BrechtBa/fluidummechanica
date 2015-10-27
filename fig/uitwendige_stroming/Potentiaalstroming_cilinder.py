#!/usr/bin/python
# coding: utf-8
# Dit werk is gelicenseerd onder de licentie Creative Commons Naamsvermelding-GelijkDelen 4.0 Internationaal. Ga naar http://creativecommons.org/licenses/by-sa/4.0/ om een kopie van de licentie te kunnen lezen.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

extent = 5
num = 10
grdsize = 200


R = 1.        		# m
v0 = 1.       		# m/s


rho = 1000.      	# kg/m³
nu = 1.e-6       	# m²/s
p0  = 100000.   	# N/m²

Re = v0*2.*R/nu

K = v0*R**2;

theta = np.linspace(0.01,np.pi-0.01,100)
psi = np.linspace(0,v0*R*extent,num)

psi,theta = np.meshgrid(psi,theta)
r =(psi+(psi**2+4.*v0**2*np.sin(theta)**2*R**2)**0.5)/2./v0/np.sin(theta)

# streamlines in cathesians coordinates
x = r*np.cos(theta)
y = r*np.sin(theta)

# Calculate velocity and pressure on a regular grid
xx,yy = np.meshgrid(np.linspace(-extent*R,extent*R,grdsize),np.linspace(-extent*R,extent*R,grdsize))
rr = (xx**2+yy**2)**0.5
tt = np.arctan2(yy,xx)

# remove values inside the circle
rr[np.where(rr<R)] = np.nan
tt[np.where(rr<R)] = np.nan


v_theta = -v0*np.sin(tt)-v0*R**2*np.sin(tt)/rr**2;
v_r     = v0*np.cos(tt)-v0*R**2*np.cos(tt)/rr**2;
v = (v_theta**2+v_r**2)**0.5

v_x = -v_theta*np.sin(tt)+v_r*np.cos(tt);
v_y =  v_theta*np.cos(tt)+v_r*np.sin(tt);

# calculate pressure according to Bernoulli
p = p0 + 0.5*rho*(v0**2-v**2)



################################################################################
# plotting
################################################################################
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.rc('figure', autolayout=True)

# velocity
plt.figure(figsize=(15/2.54,10/2.54))
plt.pcolormesh(xx, yy, v/v0, vmin=0, vmax=2*v0)
plt.colorbar().set_label(r'$v/v_{\infty}$ (-)')

# streamlines
plt.plot([-extent*R,-R,np.nan,R,extent*R],[0,0,np.nan,0,0],'k')
for xi,yi in zip(x.T,y.T):
	plt.plot(xi,yi,'k')
	plt.plot(xi,-yi,'k')
	
ax = plt.gca()
ax.set_xlim([-extent*R,extent*R])
ax.set_ylim([-extent*R,extent*R])
ax.set_aspect('equal')
ax.set_xlabel(r'$x/R$ (-)')
ax.set_ylabel(r'$x/R$ (-)')

# add the cylinder
verts = list(zip(R*np.cos(np.linspace(0,2.*np.pi,100)), R*np.sin(np.linspace(0,2.*np.pi,100))))
poly = Polygon(verts, facecolor='w', edgecolor=None)
ax.add_patch(poly)

plt.savefig('Potentiaalstroming_cilinder_snelheid.pdf')




# pressure
plt.figure(figsize=(15/2.54,10/2.54))
plt.pcolormesh(xx, yy, (p-p0)/(0.5*rho*v0**2), vmin=-3, vmax=1)
plt.colorbar().set_label(r'$\Delta p/\frac{1}{2} \rho v_{\infty}^2$ (-)')

# streamlines
plt.plot([-extent*R,-R,np.nan,R,extent*R],[0,0,np.nan,0,0],'k')
for xi,yi in zip(x.T,y.T):
	plt.plot(xi,yi,'k')
	plt.plot(xi,-yi,'k')
	
ax = plt.gca()
ax.set_xlim([-extent*R,extent*R])
ax.set_ylim([-extent*R,extent*R])
ax.set_aspect('equal')
ax.set_xlabel(r'$x/R$ (-)')
ax.set_ylabel(r'$x/R$ (-)')

# add the cylinder
verts = list(zip(R*np.cos(np.linspace(0,2.*np.pi,100)), R*np.sin(np.linspace(0,2.*np.pi,100))))
poly = Polygon(verts, facecolor='w', edgecolor=None)
ax.add_patch(poly)

plt.savefig('Potentiaalstroming_cilinder_druk.pdf')



plt.show()

