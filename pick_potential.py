from astropy import units
from galpy.orbit import Orbit
from galpy.util.conversion import get_physical
from galpy.potential import plotPotentials, TwoPowerSphericalPotential, PowerSphericalPotential, HomogeneousSpherePotential, SphericalShellPotential, PlummerPotential
import numexpr
import matplotlib.pyplot as plt
import numpy
import streamlit as st

#@st.cache_data
def pick_potential(pot_fxn, index):

	mod_params = [r"$\alpha$, the power law exponent", r"$\alpha$ and $\beta$, the power law exponents", r"$a$, the radius of the shell", r"$R$, the radius of the sphere", r"$b$, the scale parameter"]
	eqns = [r'''\rho(r)= \frac{\text{amp}}{r^{3}} \left(\frac{r_1}{r}\right)^\alpha''', r'''\rho(r)= \frac{\text{amp}}{4\pi a^3} \frac{1}{r^{\alpha} (1 + r/a)^{\beta-\alpha}}''',\
	r'''\rho(r)= \frac{\text{amp}}{4\pi a^2} \delta(r-a)''', r'''\rho(r)= \rho_0''', r''' ''']

	pot_name_string = "You've selected the **"+pot_fxn+"**."

	parameters = mod_params[index]
	equation = eqns[index]

	if pot_fxn != "Plummer Potential":
		density_string = "The equation for the density of this distribution is:"
		latex = equation

	else:
		density_string = "This potential is characterized by the equation:"
		latex = r'''\Phi(R,z) = - \frac{\text{amp}}{\sqrt{R^2 + z^2 + b^2}}'''

	# if pot_fxn == "Two Power Spherical Potential":
	# 	param1 = st.slider("Power Law Exponent, " + r"$\alpha$", min_value = 0.0, max_value = 6.0, step = 0.25)
	# 	param2 = st.slider("Power Law Exponent, " + r"$\beta$", min_value = 0.0, max_value = 6.0, step = 0.25)

	# 	pot_fxn_set = TwoPowerSphericalPotential(alpha = param1, beta = param2)

	if pot_fxn == "Power Spherical Potential":
		param1 = "Power Law Exponent, " + r"$\alpha$"
		min_value = 0.0
		max_value = 6.0
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

#@st.cache_data
def set_potential(pot_fxn, param):

	if pot_fxn == "Power Spherical Potential":
		pot_fxn_set = PowerSphericalPotential(alpha = param)

	elif pot_fxn == "Homogeneous Sphere Potential":
		pot_fxn_set = HomogeneousSpherePotential(R = param*units.kpc)

	elif pot_fxn == "Spherical Shell Potential":
		pot_fxn_set = SphericalShellPotential(a = param*units.kpc)

	else:
		pot_fxn_set = PlummerPotential(b = param)

	return pot_fxn_set


