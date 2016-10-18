#!/usr/bin/python
# coding: utf-8
# Dit werk is gelicenseerd onder de licentie Creative Commons Naamsvermelding-GelijkDelen 4.0 Internationaal. Ga naar http://creativecommons.org/licenses/by-sa/4.0/ om een kopie van de licentie te kunnen lezen.

# voorbeeld van de kracht van het Buckingham Pi theorema bij het analyseren van experimenten

import numpy as np
import scipy.optimize
import matplotlib.pyplot as plt
import textablepy

# matplotlib settings
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.rc('figure', autolayout=True)

# experiment data
rho = 1000.
nu = 1e-6
N = np.array([100,200,300]*9)          			# rpm
D = np.array(([0.2]*3+[0.4]*3+[0.6]*3)*3)    	# m
v = np.array([2.5]*9+[5.0]*9+[7.5]*9)    	 	# m/s
F = np.array([1.0,1.5,1.5,4.6,4.3,2.7,9.0,3.2,0.2,1.8,3.1,4.0,8.1,11.8,11.0,19.1,19.8,14.3,2.1,3.7,5.7,10.5,17.6,22.2,23.8,41.5,34.7])   # kN
no = range(1,len(N)+1)

# create a latex table
textablepy.textable( [no,N,D,v,F],f=['{:}','{:.0f}','{:.2f}','{:.1f}','{:.1f}'] )


# plotting the raw data
plt.figure(figsize=(16/2.54,12/2.54))
p = plt.scatter(N,F,c=v, s=D*500, alpha=0.7,cmap=plt.cm.viridis)
cbar = plt.colorbar(p)
cbar.set_label('$v$ (m/s)', rotation=90)
cbar.ax.yaxis.set_label_coords(3.1, 0.5)
plt.xlabel('$N$ (rpm)')
plt.ylabel('$F$ (kN)')

xlim = plt.gca().get_xlim()
ylim = plt.gca().get_ylim()

# add a custom legend
leg = []
lab = []
for i in [0,3,6]:
	leg.append( plt.scatter(-100,-100,c=v[0], s=D[i]*500, alpha=0.7) )
	lab.append( 'D = {:.1f} m'.format(D[i]) )

plt.gca().set_xlim(xlim)
plt.gca().set_ylim(ylim)

plt.legend(leg,lab,scatterpoints=1,loc=2)
plt.savefig('Dimensieanalyse_voorbeeld_data.pdf')


# create dimensionless numbers
Re = v*D/nu
l = N*D/v
C_F = 2*F/(rho*v**2*D**2)


# plot again with one parameter (forgotten viscosity)
plt.figure(figsize=(16/2.54,12/2.54))
p = plt.scatter(l,C_F, s=100, alpha=0.7, color='k')
plt.xlabel(r'$\frac{ N D}{v}$ (-)')
plt.ylabel(r'$\frac{F}{1/2 \rho v^2 D^2}$ (-)')
plt.gca().set_xlim([0,80])
plt.gca().set_ylim([0,0.014])
plt.savefig('Dimensieanalyse_voorbeeld_data_dimensieloos_1par.pdf')


# plot again with two paramters
plt.figure(figsize=(16/2.54,12/2.54))
p = plt.scatter(l,C_F,c=Re,s=100, alpha=0.7,cmap=plt.cm.viridis)
cbar = plt.colorbar(p)
cbar.set_label('$Re$ (-)', rotation=90)
cbar.ax.yaxis.set_label_coords(4.5, 0.5)
plt.xlabel(r'$\frac{ N D}{v}$ (-)')
plt.ylabel(r'$\frac{F}{1/2 \rho v^2 D^2}$ (-)')
plt.gca().set_xlim([0,80])
plt.gca().set_ylim([0,0.014])
plt.savefig('Dimensieanalyse_voorbeeld_data_dimensieloos.pdf')

# plot trends
for re in [1e6,2e6,3e6]:
    ind = np.where( (Re>re-0.1e6) & (Re<re+0.1e6) )

    x = l[ind]
    y = C_F[ind]
    
    def f(x,p0,p1):
        return x*p0*np.exp(-p1*x)
        
    popt,pcov = scipy.optimize.curve_fit(f, x, y)
    
    x = np.linspace(min(x),max(x),20)

    plt.plot(x,f(x,*popt), linewidth=2, color=plt.cm.viridis( (re-min(Re))/(max(Re)-min(Re)) ))
plt.savefig('Dimensieanalyse_voorbeeld_data_dimensieloos_trends.pdf')

plt.show()