# Import libraries
import numpy as np
import scipy
import os

## define standard constant variables
p_ref = 101325 # Pa
T_ref = 298.15 # K
R_air = 287 # J/kg-K


def KtoC(temp):
	temp-=273.15
	return temp

def CtoK(temp):
	temp+=273.15
	return temp

def BarToPa(pres):
	pres*=100000
	return pres