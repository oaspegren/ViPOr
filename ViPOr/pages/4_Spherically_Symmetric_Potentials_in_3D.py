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

pot_names = ["Power Spherical Potential", "Two Power Spherical Potential", "Spherical Shell Potential", "Homogeneous Sphere Potential", "Plummer Potential"]
pot_fxn = st.selectbox('Select a potential function:', pot_names)
mod_params = [r"$\alpha$, the power law exponent", r"$\alpha$ and $\beta$, the power law exponents", r"$a$, the radius of the shell", r"$R$, the radius of the sphere", r"$b$, the scale parameter"]

pot_name_string = "You've selected the **"+pot_fxn+"**."
st.markdown(pot_name_string)

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

pot_fxn_set = set_potential(pot_fxn, param)

years = st.slider("Time (Gyr):", min_value = 0, max_value = 14)
radius = st.slider("Set the initial distance from the galactic center:", min_value = 0.0, max_value = 50.0, step = 1.0)
height = st.slider("Set the initial height from the galactic plane:", min_value = 0.0, max_value = 50.0, step = 1.0)

fig0, fig1, fig2, raw_html, density = plot_orbit_3D(pot_fxn_set, years, radius, height)

st.markdown("This is what a density plot of the potential looks like.")

st.pyplot(density.get_figure())

st.markdown("This first plot shows the orbit in **x, y and z coordinates**. With this we can see how the particle will move \
	in three-dimensional space.")

st.pyplot(fig0, bbox_inches = "tight", pad_inches = 0.5)

st.markdown("This next plot shows the relationship between the **orbital radius, radial velocity and height from the disk plane**. \
	This shows how the radial velocity of the particle changes with its position inside the distribution.")

st.pyplot(fig1, bbox_inches = "tight", pad_inches = 0.5)

st.markdown("The last plot shows the relationship between the particle's **orbital radius, radial velocity and vertical velocity**. \
	This plot shows how fast the particle is moving radially and vertically, depending on its distance from the center of the galaxy.")

st.pyplot(fig2, bbox_inches = "tight", pad_inches = 0.5)

st.markdown("And now we display the 3D animation of the orbit.")
st.components.v1.html(raw_html, height = 800)

