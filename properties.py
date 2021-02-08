# Import libraries
import sys,os
sys.path.append('~/phd-work/graduate-coursework/pyTherm/')
import conversions

import numpy as np # NumPy: contains basic numerical routines
import scipy # SciPy: contains additional numerical routines to numpy
import matplotlib.pyplot as plt
import CoolProp
from CoolProp.CoolProp import PropsSI as prop


## define standard constant variables
p_ref = 101325 # Pa
T_ref = 298.15 # K
R_air = 287 # J/kg-K


def airProperties(propertyNames, propertyValues, printOutput):
	if propertyNames[0]=='P' and propertyNames[1]=='T':
		u = prop('U',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],'Air')
		h = prop('H',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],'Air')
		s = prop('S',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],'Air')
		rho = prop('D',propertyNames[0],propertyValues[0],propertyNames[1],propertyValues[1],'Air')

	if printOutput:
		print("Air Properties (SI UNITS)")
		print("===========================================")
		print("Interal Energy [J/kg] =",u)
		print("Enthalpy [J/kg] =",h)
		print("Entropy [J/kg-K] =",s)
		print("Density [kg/m3] =",rho)
		print("\n")

	return [u,h,s]



### Fluid Property Calculations Based on State Conditions
def waterProperties(propertyNames, propertyValues, printOutput):
	if propertyNames[0]=='P' and propertyNames[1]=='Q':
		rho = prop('D',propertyNames[0],conversions.BarToPa(propertyValues[0]),propertyNames[1],propertyValues[1],'Water') # kg/m3
		v = 1/rho # m3/kg
		temp = prop('T',propertyNames[0],conversions.BarToPa(propertyValues[0]),propertyNames[1],propertyValues[1],'Water') # K
		intEnergy = prop('U',propertyNames[0],conversions.BarToPa(propertyValues[0]),propertyNames[1],propertyValues[1],'Water') # J/kg
		enthalpy = prop('H',propertyNames[0],conversions.BarToPa(propertyValues[0]),propertyNames[1],propertyValues[1],'Water') # J/kg
		entropy = prop('S',propertyNames[0],conversions.BarToPa(propertyValues[0]),propertyNames[1],propertyValues[1],'Water') # J/kg-K

	elif propertyNames[0]=='P' and propertyNames[1]=='D':
		rho = propertyValues[1]
		v = 1/rho # m3/kg
		temp = prop('T',propertyNames[0],conversions.BarToPa(propertyValues[0]),propertyNames[1],rho,'Water') # K
		intEnergy = prop('U',propertyNames[0],conversions.BarToPa(propertyValues[0]),propertyNames[1],rho,'Water') # J/kg
		enthalpy = prop('H',propertyNames[0],conversions.BarToPa(propertyValues[0]),propertyNames[1],rho,'Water') # J/kg
		entropy = prop('S',propertyNames[0],conversions.BarToPa(propertyValues[0]),propertyNames[1],rho,'Water') # J/kg-K

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