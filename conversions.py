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

def PaToBar(pres):
	pres*=1e-5
	return pres

def cm2Tom2(area):
	area*=1e-4
	return area

def cm3Tom3(vol):
	vol*=1e-6
	return vol

def JtokJ(energy):
	energy*=1e-3
	return energy

def kJtoJ(energy):
	energy*=1e3
	return energy