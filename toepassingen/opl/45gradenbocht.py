#!/usr/bin/python
# coding: utf-8
# Dit werk is gelicenseerd onder de licentie Creative Commons Naamsvermelding-GelijkDelen 4.0 Internationaal. Ga naar http://creativecommons.org/licenses/by-sa/4.0/ om een kopie van de licentie te kunnen lezen.
import numpy as np

# Gegevens
rho = 1000.         	# kg/m3
V_flow = 0.250         	# m3/s
D = 0.3                	# m
alpha = 45*np.pi/180   	# rad
p = 40000				# Pa

# Oplossing
# F_x + p A – p A \cos(\alpha) = \dot{m} (v \cos(\alpha) - v)
# F_y + 0   + p A \sin(\alpha) = \dot{m} (v \sin(\alpha) - 0)

# Uitwerking
m_flow = rho*V_flow
A = np.pi*D**2/4
v = V_flow/A

F_x = m_flow*(v*np.cos(alpha)-v) - p*A + p*A*np.cos(alpha)
F_y = m_flow*(v*np.sin(alpha)-0) - 0   - p*A*np.sin(alpha)

print('De kracht die de stroming op de bocht uitoefent is:')
print('F_x = {:.2f} kN'.format(-F_x/1000) )
print('F_y = {:.2f} kN'.format(-F_y/1000) )