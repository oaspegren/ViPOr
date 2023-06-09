# This page allows the user to select a spherically symmetric potential, modify its key parameters (power law exponent, scale length, etc.),
# and then examine different plots that describe its motion in three-dimensions. At the end, there's an animation that shows the motion
# of the particle in its orbit.

from astropy import units
from galpy.orbit import Orbit
from galpy.util.conversion import get_physical
from galpy.potential import plotPotentials, TwoPowerSphericalPotential, PowerSphericalPotential, HomogeneousSpherePotential, SphericalShellPotential, PlummerPotential
import numexpr
import matplotlib.pyplot as plt
import numpy
import streamlit as st

from PlotPotentialandOrbit2D import plot_orbit_2D
from pick_potential import pick_potential, set_potential

# title and description of the page

st.markdown("## Experimenting with Spherically Symmetric Orbits in Two Dimensions")

st.markdown("In this module, you can visualize various spherically symmetric potentials and their corresponding orbits in two \
	dimensions by selecting various potential forms, manipulating their key parameters and experimenting with different initial conditions. \
	The page below will generate plots that show certain characteristics of their motion in a variety of coordinate systems.")

st.markdown("Select a potential form below to get started.")

# list of possible potentials and initialization of the dropdown menu

pot_names = ["Power Spherical Potential", "Spherical Shell Potential", "Homogeneous Sphere Potential", "Plummer Potential"]
pot_fxn = st.selectbox('Select a potential function:', pot_names)

# print out the name of the potential
pot_name_string = "You've selected the **"+pot_fxn+"**."
st.markdown(pot_name_string)

# given the chosen potential, get the equation, parameter of interest, latex string of the equation, as well as the minimum,
# maximum and step values for the parameter's slider
parameters, equation, param1, density_string, latex, min_value, max_value, step = pick_potential(pot_fxn, pot_names.index(pot_fxn))

# print the form of the mass distribution density
st.markdown(density_string)
st.latex(latex)

# list the parameter that can be modified
param_string = "The parameter you can modify is: **"+parameters+"**."

st.markdown(param_string)

st.markdown(
	'''
	Use the sliders to change this value and see what happens to the potential and orbit!
	''')

st.markdown("**NOTE: This may take a few moments to run and generate plots. If the application stops running and throws an error, that's because the parameters are not \
	allowed — please select new ones.**")

# initialize slider for the parameter of interest
param = st.slider(param1, min_value = min_value, max_value = max_value, step = step)
pot_fxn_set = set_potential(pot_fxn, param)

# initialize sliders for the integration time, initial radius and initial height from the galactic plane
years = st.slider("Time (Gyr):", min_value = 0, max_value = 14)
radius = st.slider("Set the initial distance from the galactic center (kpc):", min_value = 0.0, max_value = 50.0, step = 1.0)
height = st.slider("Set the initial height from the galactic plane (kpc):", min_value = 0.0, max_value = 50.0, step = 1.0)

# get two dimensional plots for the selected potential and orbit
fig0, fig1, fig2, fig3, raw_html, raw_html_2, density = plot_orbit_2D(pot_fxn_set, years, radius, height)

st.markdown("Below is a plot of the potential over each value of R and \
		z. The darker regions are areas where the magnitude of the potential is higher — so we can see that the potential \
		increases as we get closer to the center.")

# plot the potential over R and z
st.pyplot(density.get_figure())

st.markdown("We can examine three plots to understand how particles will move in this potential.")
st.markdown("The first is an **R vs. z** plot, which displays the path of the orbit in the meridional plane. With this one, we can see how far the particle is from the \
	galactic plane — its vertical distance — at each radius from the galactic center. We can see if orbits are bound or unbound, depending on the appearance of this plot.")

# plot the orbit in R vs. z coordinates
st.pyplot(fig0, bbox_inches = "tight", pad_inches = 0.5)

st.markdown("The second is an **radius vs. radial velocity** plot, which displays the radial velocity of the particle at each radius — how fast the particle moves based on its distance \
	from the galactic center. We can track where the velocity is positive and where it is negative, which indicates the direction the particle orbits. Bound orbits will \
	fluctuate between positive and negative, while unbound orbits will increase in radial velocity off into infinity.")

# plot the orbit in R vs. vR coordinates
st.pyplot(fig2, bbox_inches = "tight", pad_inches = 0.5)

st.markdown("The next is an **RA vs. Dec** plot, which displays the path of the orbit in celestial coordinates. This is the path the particle takes within the sky.")

# plot the orbit in RA vs. Dec coordinates
st.pyplot(fig1, bbox_inches = "tight", pad_inches = 0.5)

st.markdown("Lastly, we show **the projection of the orbit into the x-y plane**, which shows the position and movement of the particle through the galactic plane.")

# plot the orbit in Cartesian coordinates
st.pyplot(fig3, bbox_inches = "tight", pad_inches = 0.5)

st.markdown("Finally, there are two animations that displays the movement of the particle perpendicular to the galactic plane — its vertical height from the galactic plane \
	at each radius — as well as the motion of the particle in the galactic plane.")

# show the animations
st.components.v1.html(raw_html, height = 600)
st.components.v1.html(raw_html_2, height = 600)

