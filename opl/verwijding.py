#!/usr/bin/python
# coding: utf-8
# Dit werk is gelicenseerd onder de licentie Creative Commons Naamsvermelding-GelijkDelen 4.0 Internationaal. Ga naar http://creativecommons.org/licenses/by-sa/4.0/ om een kopie van de licentie te kunnen lezen.
import numpy as np

# Gegevens
rho = 800.         		# kg/m3
V_flow = 200./60000.   	# m3/s
D_in = 0.028        	# m
D_uit = 0.050			# m
p_in = 100000.			# Pa
p_uit = 106000.			# Pa

# Oplossing
# F + p_in A_in – p_uit A_uit  = \dot{m} (v_uit - v_in)

# Uitwerking
m_flow = rho*V_flow
A_in = np.pi*D_in**2/4
A_uit = np.pi*D_uit**2/4
v_in = V_flow/A_in
v_uit = V_flow/A_uit

F = m_flow*(v_uit-v_in) - p_in*A_in + p_uit*A_uit

print('De kracht die de stroming op de verwijding uitoefent is:')
print('F = {:.0f} N'.format(-F) )
