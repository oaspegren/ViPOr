from astropy import units
import galpy
import galpy.potential
from galpy.util.conversion import get_physical
import numexpr
import matplotlib.pyplot as plt
import numpy

import streamlit as st

from PlotPotentialandOrbit3D import plot_orbit_3D

pot_list = [galpy.potential.PowerSphericalPotential, galpy.potential.TwoPowerSphericalPotential, galpy.potential.SphericalShellPotential, galpy.potential.HomogeneousSpherePotential, galpy.potential.NFWPotential, galpy.potential.PlummerPotential]
pot_names = ["Power Spherical Potential", "Two Power Spherical Potential", "Spherical Shell Potential", "Homogeneous Sphere Potential", "NFW Potential", "Plummer Potential"]
pot_fxn = st.selectbox('Select a potential function:', pot_names)
mod_params = [r"$\alpha$, the power law exponent", r"$\alpha$ and $\beta$, the power law exponents", r"$a$, the radius of the shell", r"$R$, the radius of the sphere", r"$a$, the scale radius", r"$b$, the scale parameter"]

pot_name_string = "You've selected the **"+pot_fxn+"**."

param_string = "The parameter(s) you can modify are: **"+mod_params[pot_names.index(pot_fxn)]+"**."

st.markdown(pot_name_string)
st.markdown(param_string)

st.markdown(
	'''
	Use the sliders to change this value and see what happens to the potential and orbit!
	''')

years = st.slider("Time (Gyr):", min_value = 0, max_value = 14)

if pot_fxn == "Two Power Spherical Potential":
	param1 = st.slider("Power Law Exponent, " + r"$\alpha$", min_value = 0.0, max_value = 6.0)
	param2 = st.slider("Power Law Exponent, " + r"$\beta$", min_value = 0.0, max_value = 6.0)

	pot_fxn_set = galpy.potential.TwoPowerSphericalPotential(alpha = param1, beta = param2)

elif pot_fxn == "Power Spherical Potential":
	param1 = st.slider("Power Law Exponent, " + r"$\alpha$", min_value = 0.0, max_value = 6.0)
	pot_fxn_set = galpy.potential.PowerSphericalPotential(alpha = param1)

elif pot_fxn == "Homogeneous Sphere Potential":
	param1 = st.slider("Sphere Radius, " + r"$R$", min_value = 1, max_value = 100)
	pot_fxn_set = galpy.potential.HomogenerousSpherePotential(R = param1)

elif pot_fxn == "Spherical Shell Potential":
	param1 = st.slider("Shell Radius, " + r"$a$", min_value = 1, max_value = 100)
	pot_fxn_set = galpy.potential.SphericalShellPotential(a = param1)

elif pot_fxn == "NFW Potential":
	param1 = st.slider("Scale Radius, " + r"$a$", min_value = 1, max_value = 100)
	pot_fxn_set = galpy.potential.NFWPotential(a = param1)

else:
	param = st.slider("Scale Parameter" + r"$b$", min_value = 0, max_value = 8)

	pot_fxn_set = galpy.potential.PlummerPotential(b = param)

plot_orbit_3D(pot_fxn_set, years)

#animate_orbit_2D()

#sample_distribution_2D()