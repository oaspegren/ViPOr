from galpy.util.conversion import get_physical
import numexpr
import matplotlib.pyplot as plt
from astropy import units
from galpy.util import conversion
from galpy.potential import DoubleExponentialDiskPotential, plotPotentials
import numpy
import streamlit as st

from PlotPotentialandOrbit2D import plot_orbit_2D
from PlotPotentialandOrbit3D import plot_orbit_3D


st.markdown("## Looking at Orbits in a Double Exponential Disk Potential")
st.markdown("We now look at a general example of an axisymmetric potential. These are orbits created \
	by disks, rings, and other distributions that are symmetric in the radial direction.")

st.markdown("The density of this distribution is given by the expression:")

st.latex(r"\rho (R, z) = \text{amp} \text{exp}( -R/h_R - |z|/h_z)")

param_string = r"For this potential, you can modify the disk scale-length, $h_r$, and scale-height, $h_z$."

st.markdown(param_string)

st.markdown(
	'''
	Use the sliders to change this value and see what happens to the potential and orbit!
	''')

years = st.slider("Time (Gyr):", min_value = 0, max_value = 14)
radius = st.slider("Set the initial distance from the galactic center:", min_value = 0.0, max_value = 50.0, step = 1.0)
height = st.slider("Set the initial height from the galactic plane:", min_value = 0.0, max_value = 50.0, step = 1.0)

scalelength = st.slider("Scale Length, " + r"$h_r$", min_value = 1, max_value = 100)
scaleheight = st.slider("Scale Height, " + r"$h_z$", min_value = 1, max_value = 20)

pot_fxn_set = DoubleExponentialDiskPotential(hr = scalelength*units.kpc, hz = scaleheight*units.kpc)

#plotPotentials(pot_fxn_set)

fig0, fig1, fig2, fig3, raw_html, density = plot_orbit_2D(pot_fxn_set, years, radius, height)

st.markdown("This is what a density plot of the potential looks like.")

st.pyplot(density.get_figure())

st.markdown("We can examine three plots to understand how particles will move in this potential.")
st.markdown("The first is an **R vs. z** plot, which displays the path of the orbit in the meridional plane. With this one, we can see how far the particle is from the \
	galactic plane — its vertical distance — at each radius from the galactic center. We can see if orbits are bound or unbound, depending on the appearance of this plot.")

st.pyplot(fig0, bbox_inches = "tight", pad_inches = 0.5)

st.markdown("The second is an **Radius vs. radial velocity** plot, which displays the radial velocity of the particle at each radius — how fast the particle moves based on its distance \
	from the galactic center. We can track where the velocity is positive and where it is negative, which indicates the direction the particle orbits. Bound orbits will \
	fluctuate between positive and negative, while unbound orbits will increase in radial velocity off into infinity.")

st.pyplot(fig2, bbox_inches = "tight", pad_inches = 0.5)

st.markdown("The next is an **RA vs. Dec** plot, which displays the path of the orbit in celestial coordinates. This is the path the particle takes within the sky.")

st.pyplot(fig1, bbox_inches = "tight", pad_inches = 0.5)

st.markdown("Lastly, we show **the projection of the orbit into the x-y plane**, which shows the position and movement of the particle through the galactic plane.")

st.pyplot(fig3, bbox_inches = "tight", pad_inches = 0.5)

st.markdown("Finally, there is an animation that displays the movement of the particle in the meridional plane — once again, its vertical height from the galactic plane \
	at each radius.")

st.components.v1.html(raw_html, height = 800)

st.markdown("We can also explore this orbit in 3 dimensions... ")

fig0, fig1, fig2, raw_html, density_3d = plot_orbit_3D(pot_fxn_set, years, radius, height)

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

