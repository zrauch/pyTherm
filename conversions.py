# Import libraries
import numpy as np
import scipy
import os

def KtoC(temp):
	temp-=273.15
	return temp

def CtoK(temp):
	temp+=273.15
	return temp

def BarToPa(pres):
	pres*=100000
	return pres

def cm3Tom3(vol):
	vol*=1e-6
	return vol