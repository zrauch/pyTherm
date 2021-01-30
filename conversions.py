# Import libraries
import numpy as np # NumPy: contains basic numerical routines
import scipy # SciPy: contains additional numerical routines to numpy
import scipy.sparse as scysparse
import scipy.sparse.linalg
import re
import itertools # for permutations
import os
import matplotlib.pyplot as plt
import math
from math import pi as PI
from scipy.optimize import fsolve
from matplotlib.font_manager import FontProperties
from sympy import symbols, solve
import os
import CoolProp
import CoolProp.CoolProp as CP
from CoolProp.CoolProp import PropsSI as prop

## define standard constant variables
p_ref = 101325
T_ref = 298.15


def KtoC(temp):
	temp-=273.15
	return temp

def CtoK(temp):
	temp+=273.15
	return temp

def BarToPa(pres):
	pres*=100000
	return pres