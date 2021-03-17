# Import libraries
import sys,os
sys.path.append('~/phd-work/graduate-coursework/pyTherm/')
import conversions

import numpy as np # NumPy: contains basic numerical routines
import scipy # SciPy: contains additional numerical routines to numpy
import matplotlib.pyplot as plt
import CoolProp.CoolProp as cp
from CoolProp.CoolProp import PropsSI as prop


## define standard constant variables
p_ref = 101325 # Pa
T_ref = 298.15 # K
R_air = 287 # J/kg-K
Cp_air = 1005 # J/kg-K
R_u = 8314 # J/mol-K

cp.set_reference_state('Air',"DEF")

def airProperties(propertyNames, propertyValues, printOutput): ## ALL INPUTS IN SI UNITS FOR GASES
	if propertyNames[0]=='P' and propertyNames[1]=='T': # P must be in Pa, T must be in K
		u = prop('U',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],'Air')
		h = prop('H',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],'Air')
		s = prop('S',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],'Air')
		rho = prop('D',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],'Air')

	elif propertyNames[0]=='T' and propertyNames[1]=='P': # P must be in Pa, T must be in K
		u = prop('U',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],'Air')
		h = prop('H',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],'Air')
		s = prop('S',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],'Air')
		rho = prop('D',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],'Air')

	elif propertyNames[0]=='P' and propertyNames[1]=='D': # P must be in Pa, D must be in kg/m3
		u = prop('U',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],'Air')
		h = prop('H',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],'Air')
		s = prop('S',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],'Air')
		rho = prop('D',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],'Air')

	elif propertyNames[0]=='H' and propertyNames[1]=='D':
		u = prop('U',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],'Air')
		s = prop('S',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],'Air')
		h = propertyValues[0]
		rho = propertyValues[1]

	elif propertyNames[0]=='D' and propertyNames[1]=='H':
		u = prop('U',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],'Air')
		s = prop('S',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],'Air')
		h = propertyValues[0]
		rho = propertyValues[1]	

	if printOutput:
		print("Air Properties (SI UNITS)")
		print("===========================================")
		print("Interal Energy [J/kg] =",u)
		print("Enthalpy [J/kg] =",h)
		print("Entropy [J/kg-K] =",s)
		print("Density [kg/m3] =",rho)
		print("\n")

	return [u,h,s,rho]

def gasProperties(propertyNames, propertyValues, gas ,printOutput): ## ALL INPUTS IN SI UNITS
	if propertyNames[0]=='P' and propertyNames[1]=='T': # P must be in Pa, T must be in K
		u = prop('U',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],gas)
		h = prop('H',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],gas)
		s = prop('S',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],gas)
		rho = prop('D',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],gas)

	elif propertyNames[0]=='P' and propertyNames[1]=='H': # P must be in Pa, T must be in K
		u = prop('U',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],gas)
		h = propertyValues[1]
		s = prop('S',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],gas)
		rho = prop('D',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],gas)

	elif propertyNames[0]=='P' and propertyNames[1]=='S': # P must be in Pa, T must be in K
		u = prop('U',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],gas)
		h = prop('H',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],gas)
		s = propertyValues[1]
		rho = prop('D',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],gas)

	elif propertyNames[0]=='T' and propertyNames[1]=='P': # P must be in Pa, T must be in K
		u = prop('U',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],gas)
		h = prop('H',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],gas)
		s = prop('S',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],gas)
		rho = prop('D',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],gas)

	elif propertyNames[0]=='P' and propertyNames[1]=='D': # P must be in Pa, D must be in kg/m3
		u = prop('U',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],gas)
		h = prop('H',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],gas)
		s = prop('S',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],gas)
		rho = prop('D',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],gas)

	elif propertyNames[0]=='H' and propertyNames[1]=='D':
		u = prop('U',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],gas)
		s = prop('S',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],gas)
		h = propertyValues[0]
		rho = propertyValues[1]

	elif propertyNames[0]=='D' and propertyNames[1]=='H':
		u = prop('U',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],gas)
		s = prop('S',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],gas)
		h = propertyValues[0]
		rho = propertyValues[1]	

	if printOutput:
		print(gas,"Properties (SI UNITS)")
		print("===========================================")
		print("Interal Energy [J/kg] =",u)
		print("Enthalpy [J/kg] =",h)
		print("Entropy [J/kg-K] =",s)
		print("Density [kg/m3] =",rho)
		print("\n")

	return [u,h,s,rho]

### Fluid Property Calculations Based on State Conditions
def waterProperties(propertyNames, propertyValues, printOutput):
	if propertyNames[0]=='P' and propertyNames[1]=='Q':
		rho = prop('D',propertyNames[0],conversions.BarToPa(propertyValues[0]),propertyNames[1],propertyValues[1],'Water') # kg/m3
		v = 1/rho # m3/kg
		temp = prop('T',propertyNames[0],conversions.BarToPa(propertyValues[0]),propertyNames[1],propertyValues[1],'Water') # K
		intEnergy = prop('U',propertyNames[0],conversions.BarToPa(propertyValues[0]),propertyNames[1],propertyValues[1],'Water') # J/kg
		enthalpy = prop('H',propertyNames[0],conversions.BarToPa(propertyValues[0]),propertyNames[1],propertyValues[1],'Water') # J/kg
		entropy = prop('S',propertyNames[0],conversions.BarToPa(propertyValues[0]),propertyNames[1],propertyValues[1],'Water') # J/kg-K
	
	elif propertyNames[0]=='D' and propertyNames[1]=='Q':
		rho = propertyValues[0]#prop('D',propertyNames[0],conversions.BarToPa(propertyValues[0]),propertyNames[1],propertyValues[1],'Water') # kg/m3
		v = 1/rho # m3/kg
		temp = prop('T',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],'Water') # K
		intEnergy = prop('U',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],'Water') # J/kg
		enthalpy = prop('H',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],'Water') # J/kg
		entropy = prop('S',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],'Water') # J/kg-K

	elif propertyNames[0]=='P' and propertyNames[1]=='D':
		rho = propertyValues[1]
		v = 1/rho # m3/kg
		temp = prop('T',propertyNames[0],conversions.BarToPa(propertyValues[0]),propertyNames[1],rho,'Water') # K
		intEnergy = prop('U',propertyNames[0],conversions.BarToPa(propertyValues[0]),propertyNames[1],rho,'Water') # J/kg
		enthalpy = prop('H',propertyNames[0],conversions.BarToPa(propertyValues[0]),propertyNames[1],rho,'Water') # J/kg
		entropy = prop('S',propertyNames[0],conversions.BarToPa(propertyValues[0]),propertyNames[1],rho,'Water') # J/kg-K

	elif propertyNames[0]=='P' and propertyNames[1]=='S': # pressure input must be in Bar, entropy input must be in J/kg-K
		rho = propertyValues[1]
		v = 1/rho # m3/kg
		temp = prop('T',propertyNames[0],conversions.BarToPa(propertyValues[0]),propertyNames[1],propertyValues[1],'Water') # K
		intEnergy = prop('U',propertyNames[0],conversions.BarToPa(propertyValues[0]),propertyNames[1],propertyValues[1],'Water') # J/kg
		enthalpy = prop('H',propertyNames[0],conversions.BarToPa(propertyValues[0]),propertyNames[1],propertyValues[1],'Water') # J/kg
		entropy = prop('S',propertyNames[0],conversions.BarToPa(propertyValues[0]),propertyNames[1],propertyValues[1],'Water') # J/kg-K

	elif propertyNames[0]=='T' and propertyNames[1]=='Q': # T input must be in C
		rho = prop('D',propertyNames[0],conversions.CtoK(propertyValues[0]),propertyNames[1],propertyValues[1],'Water') # kg/m3
		v = 1/rho # m3/kg
		temp = conversions.CtoK(propertyValues[0])
		intEnergy = prop('U',propertyNames[0],conversions.CtoK(propertyValues[0]),propertyNames[1],propertyValues[1],'Water') # J/kg
		enthalpy = prop('H',propertyNames[0],conversions.CtoK(propertyValues[0]),propertyNames[1],propertyValues[1],'Water') # J/kg
		entropy = prop('S',propertyNames[0],conversions.CtoK(propertyValues[0]),propertyNames[1],propertyValues[1],'Water') # J/kg-K
		pressure = prop('P',propertyNames[0],conversions.CtoK(propertyValues[0]),propertyNames[1],propertyValues[1],'Water')

	elif propertyNames[0]=='P' and propertyNames[1]=='T': # T input must be in C
		rho = prop('D',propertyNames[0],conversions.BarToPa(propertyValues[0]),propertyNames[1],conversions.CtoK(propertyValues[1]),'Water') # kg/m3
		v = 1/rho # m3/kg
		temp = prop('T',propertyNames[0],conversions.BarToPa(propertyValues[0]),propertyNames[1],conversions.CtoK(propertyValues[1]),'Water') # K
		intEnergy = prop('U',propertyNames[0],conversions.BarToPa(propertyValues[0]),propertyNames[1],conversions.CtoK(propertyValues[1]),'Water') # J/kg
		enthalpy = prop('H',propertyNames[0],conversions.BarToPa(propertyValues[0]),propertyNames[1],conversions.CtoK(propertyValues[1]),'Water') # J/kg
		entropy = prop('S',propertyNames[0],conversions.BarToPa(propertyValues[0]),propertyNames[1],conversions.CtoK(propertyValues[1]),'Water') # J/kg-K

	elif propertyNames[0]=='P' and propertyNames[1]=='H': # P must be in Bar, H must be in J/kg
		enthalpy = propertyValues[1]
		rho = prop('D',propertyNames[0],conversions.BarToPa(propertyValues[0]),propertyNames[1],propertyValues[1],'Water') # kg/m3
		v = 1/rho # m3/kg
		temp = prop('T',propertyNames[0],conversions.BarToPa(propertyValues[0]),propertyNames[1],propertyValues[1],'Water') # K
		intEnergy = prop('U',propertyNames[0],conversions.BarToPa(propertyValues[0]),propertyNames[1],propertyValues[1],'Water') # J/kg
		#enthalpy = prop('H',propertyNames[0],conversions.BarToPa(propertyValues[0]),propertyNames[1],propertyValues[1],'Water') # J/kg
		entropy = prop('S',propertyNames[0],conversions.BarToPa(propertyValues[0]),propertyNames[1],propertyValues[1],'Water') # J/kg-K

	elif propertyNames[0]=='P' and propertyNames[1]=='U': # P input must be in Bar, U input must be in J/kg
		intEnergy = propertyValues[1] # J/kg
		rho = prop('D',propertyNames[0],conversions.BarToPa(propertyValues[0]),propertyNames[1],propertyValues[1],'Water') # kg/m3
		v = 1/rho # m3/kg
		temp = prop('T',propertyNames[0],conversions.BarToPa(propertyValues[0]),propertyNames[1],propertyValues[1],'Water') # K
		enthalpy = prop('H',propertyNames[0],conversions.BarToPa(propertyValues[0]),propertyNames[1],propertyValues[1],'Water') # J/kg
		entropy = prop('S',propertyNames[0],conversions.BarToPa(propertyValues[0]),propertyNames[1],propertyValues[1],'Water') # J/kg-K
	

	if printOutput:
		print("Water Vapor Properties (SI UNITS)")
		print("===========================================")
		print("Density [rho] =\t\t",rho,"kg/m3")
		print("Specific Volume [v] =\t",v,"m3/kg")
		print("Temperature [T] =\t",temp,"K")
		print("Internal Energy [u] =\t",intEnergy,"J/kg")
		print("Enthalpy [h] =\t\t",enthalpy,"J/kg")
		print("Entropy [s] =\t\t",entropy,"J/kg-K\n")

	return [rho,v,temp,intEnergy,enthalpy,entropy]