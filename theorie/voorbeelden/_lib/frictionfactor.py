#!/usr/bin/python
# coding: utf-8
# Dit werk is gelicenseerd onder de licentie Creative Commons Naamsvermelding-GelijkDelen 4.0 Internationaal. Ga naar http://creativecommons.org/licenses/by-sa/4.0/ om een kopie van de licentie te kunnen lezen.
import numpy as np



def laminar(Re):
	"""
	Calculates the friction factor for laminar flow
	
	Arguments:
	Re:		float, Reynolds number
	"""
	if Re > 10000:
		print('Warning: the Reynolds number is larger than 10000 so the flow is probably turbulent');
	
	return 64./Re
	
	
def turbulent(Re,eD):
	"""
	Calculates the friction factor for turbulent flow according to the Colebrook formula
	
	Arguments:
	Re:		float, Reynolds number
	eD:		float, relative roughness, roughness divided by diameter
	"""
	
	if Re < 2300:
		print('Warning: the Reynolds number is less than 2300 so the flow is probably laminar');
	
	# initial guess
	f = 0.03
	
	for i in range(10):
		f_old = f
		f = 1/( -2*np.log10( eD/3.71 + 2.51/Re/np.sqrt(f_old) ) )**2
		if np.abs(f-f_old)< 1e-3:
			break
			
	return f