# This page allows the user to select a spherically symmetric potential, modify its key parameters (power law exponent, scale length, etc.),
# and then examine different plots that describe its motion in three-dimensions. At the end, there's an animation that shows the motion
# of the particle in its orbit.

from astropy import units
from galpy.orbit import Orbit
from galpy.potential import plotPotentials, TwoPowerSphericalPotential, PowerSphericalPotential, HomogeneousSpherePotential, SphericalShellPotential, PlummerPotential
from galpy.util.conversion import get_physical
import numexpr
import matplotlib.pyplot as plt
import numpy

import streamlit as st

from PlotPotentialandOrbit3D import plot_orbit_3D
from pick_potential import pick_potential, set_potential

st.markdown("## Experimenting with Spherically Symmetric Orbits in Three Dimensions")

st.markdown("In this module, you can visualize various spherically symmetric potentials and their corresponding orbits in three \
	dimension by selecting various potential forms, manipulating their key parameters and experimenting with different initial conditions. \
	The page below will generate plots that show certain characteristics of their motion in a variety of coordinate systems.")

st.markdown("Select a potential form below to get started.")

# list of potential names and the drop down menu for the options the user has to pick their potential
pot_names = ["Power Spherical Potential", "Spherical Shell Potential", "Homogeneous Sphere Potential", "Plummer Potential"]
pot_fxn = st.selectbox('Select a potential function:', pot_names)

# print out the name of the potential the user has picked
pot_name_string = "You've selected the **"+pot_fxn+"**."
st.markdown(pot_name_string)

# given the chosen potential, get the equation, parameter of interest, latex string of the equation, as well as the minimum,
# maximum and step values for the parameter's slider
parameters, equation, param1, density_string, latex, min_value, max_value, step = pick_potential(pot_fxn, pot_names.index(pot_fxn))

st.markdown(density_string)
st.latex(latex)

param_string = "The parameter(s) you can modify are: **"+parameters+"**."

st.markdown(param_string)

st.markdown(
	'''
	Use the sliders to change this value and see what happens to the potential and orbit!
	''')

st.markdown("NOTE: This may take a few moments to run and generate plots. If the application throws an error, that's because the parameters are not \
	allowed — please select new ones.")

param = st.slider(param1, min_value = min_value, max_value = max_value, step = step)

# set the potential with the chosen parameter
pot_fxn_set = set_potential(pot_fxn, param)

years = st.slider("Time (Gyr):", min_value = 0, max_value = 14)
radius = st.slider("Set the initial distance from the galactic center:", min_value = 0.0, max_value = 50.0, step = 1.0)
height = st.slider("Set the initial height from the galactic plane:", min_value = 0.0, max_value = 50.0, step = 1.0)

# call plot_orbit_3D, which obtains the three plots and the animation for the given potential and initial conditions

try:
	fig0, fig1, fig2, raw_html, density = plot_orbit_3D(pot_fxn_set, years, radius, height)

except ValueError:
	
	st.markdown("Please select other initial conditions!")

st.markdown("Below is a plot of the potential over each value of R and \
		z. The darker regions are areas where the magnitude of the potential is higher — so we can see that the potential \
		increases as the object gets closer to the center.")

# plot the potential

st.pyplot(density.get_figure())

st.markdown("This first plot shows the orbit in **x, y and z coordinates**. With this we can see how the particle will move \
	in three-dimensional space.")

# plot the orbit in Cartesian coordinates
st.pyplot(fig0, bbox_inches = "tight", pad_inches = 0.5)

st.markdown("This next plot shows the relationship between the **orbital radius, radial velocity and height from the disk plane**. \
	This shows how the radial velocity of the particle changes with its position inside the distribution.")

# plot the orbit with r vs. v_R vs. z
st.pyplot(fig1, bbox_inches = "tight", pad_inches = 0.5)

st.markdown("The last plot shows the relationship between the particle's **orbital radius, radial velocity and vertical velocity**. \
	This plot shows how fast the particle is moving radially and vertically, depending on its distance from the center of the galaxy.")

# plot the orbit with r vs. v_r vs. v_z.
st.pyplot(fig2, bbox_inches = "tight", pad_inches = 0.5)

# show the animated orbit in 3D
st.markdown("And now we display the 3D animation of the orbit.")
st.components.v1.html(raw_html, height = 800)

