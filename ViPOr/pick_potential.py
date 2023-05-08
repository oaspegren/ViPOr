from astropy import units
from galpy.orbit import Orbit
from galpy.util.conversion import get_physical
from galpy.potential import plotPotentials, TwoPowerSphericalPotential, PowerSphericalPotential, HomogeneousSpherePotential, SphericalShellPotential, PlummerPotential
import numexpr
import matplotlib.pyplot as plt
import numpy
import streamlit as st

def pick_potential(pot_fxn, index):
	'''
	Outputs important information about the potential the user has chosen, which will be put into various streamlit functions.
	This is just a way to try to make streamlit a little more efficient.

	Inputs
	--------
	pot_fxn: the potential function, either set by default or chosen by the user
	index: the index of the potential function in the list of potentials

	Outputs: 
	-------
	parameters: a string with the name of the parameter that the user may alter
	equation: the equation, in latex, of either the mass distribution or the potential
	param1: a string, which will be input into the slider, of the paramter of interest
	density_string: another string, which either introduces the equation for the density or the potential
	latex: the latex form of the mass density or the potential
	min_value: the minimum value of the key parameter for the slider
	max_value: the maximum value of the key parameter for the slider
	step: the value of the steps for the slider
	'''	

	# list of the key parameters and equations in latex for each potential
	mod_params = [r"$\alpha$, the power law exponent", r"$a$, the radius of the shell", r"$R$, the radius of the sphere", r"$b$, the scale parameter"]
	eqns = [r'''\rho(r)= \frac{\text{amp}}{r^{3}} \left(\frac{r_1}{r}\right)^\alpha''', \
	r'''\rho(r)= \frac{\text{amp}}{4\pi a^2} \delta(r-a)''', r'''\rho(r)= \rho_0''', r'''\Phi(R, z) = \frac{\text{amp}}{\sqrt{R^2 + z^2 + b^2}''']

	# selecting the string with the name of the potential and the latexed equation 
	parameters = mod_params[index]
	equation = eqns[index]

	# if we're using something other than the plummer potential, then we have an equation for the mass density distribution
	if pot_fxn != "Plummer Potential":
		density_string = "The equation for the density of this distribution is:"
		latex = equation

	# if we're using the plummer potential, we only have the form of the potential, not of the mass density
	else:
		density_string = "This potential is characterized by the equation:"
		latex = r'''\Phi(R,z) = - \frac{\text{amp}}{\sqrt{R^2 + z^2 + b^2}}'''

	# for each potential, set the key parameter of interest, as well as its minimum, maximum and step values for the sliders
	if pot_fxn == "Power Spherical Potential":
		param1 = "Power Law Exponent, " + r"$\alpha$"
		min_value = 0.0
		max_value = 3.0
		step = 0.25

	elif pot_fxn == "Homogeneous Sphere Potential":
		param1 = "Sphere Radius, " + r"$R$"
		min_value = 1
		max_value = 50
		step = 1

	elif pot_fxn == "Spherical Shell Potential":
		param1 = "Shell Radius, " + r"$a$"
		min_value = 1
		max_value = 50
		step = 1

	else:
		param1 = "Scale Parameter, " + r"$b$"
		min_value = 1
		max_value = 20
		step = 1

	return parameters, equation, param1, density_string, latex, min_value, max_value, step

def set_potential(pot_fxn, param):

	'''
	Creates and sets the potential based on the user's selections for the mass distribution and the key parameters

	Inputs
	------
	pot_fxn: the potential selected by the user
	param: the key parameter for the potential

	Outputs
	-------
	pot_fxn_set: the initialized potential, with the key parameter set
	'''

	# for each potential, initialize the potential based on the value of the key parameter
	if pot_fxn == "Power Spherical Potential":
		pot_fxn_set = PowerSphericalPotential(alpha = param)

	elif pot_fxn == "Homogeneous Sphere Potential":
		pot_fxn_set = HomogeneousSpherePotential(R = param*units.kpc)

	elif pot_fxn == "Spherical Shell Potential":
		pot_fxn_set = SphericalShellPotential(a = param*units.kpc)

	elif pot_fxn == "Two Power Spherical Potential":
		pot_fxn_set = TwoPowerSphericalPotential(alpha = param[0], beta = param[1])

	else:
		pot_fxn_set = PlummerPotential(b = param)

	return pot_fxn_set

