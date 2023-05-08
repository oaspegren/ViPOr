# this page provides an example of a triaxial potential for users to manipulate, and will show various two and three dimensional plots for
# the resulting potential

from galpy.util.conversion import get_physical
import numexpr
import matplotlib.pyplot as plt
from astropy import units
from galpy.util import conversion, plot
from galpy.potential import PowerTriaxialPotential, plotPotentials
import numpy
import streamlit as st

# import functions from other files
from PlotPotentialandOrbit2D import plot_orbit_2D
from PlotPotentialandOrbit3D import plot_orbit_3D

st.markdown("## Looking at Orbits in a Power-law Triaxial Potential")
st.markdown("We now look at an example of an triaxial potential. These are orbits created by elliptical galaxies.")

# give the general equation for the axisymmetric orbit
st.markdown("The general equation for the density of a power-law triaxial distribution is:")
st.latex(r'''\rho(r)= \frac{\text{amp}}{r_1^{3}} \left(\frac{r_1}{m}\right)^\alpha''')

st.markdown(r"where $m^2$ = $x^2$ + $y^2/b^2$ + $z^2/c^2$")

param_string = r"For this potential, you can modify the power-law exponent, $\alpha$, as well as $b$, the y-to-x axis ratio, and $c$, the z-to-x axis ratio."

# print out the string above
st.markdown(param_string)

st.markdown(
	'''
	Use the sliders to change this value and see what happens to the potential and orbit!
	''')

st.markdown("**NOTE: This may take a few moments to run and generate plots. If the application throws an error, that's because the parameters are not \
	allowed — please select new ones.**")

# create sliders for the key parameter, length of time over which to integrate, radius and height above the galactic plane
param = st.slider("Power-law Exponent, " + r"$\alpha$", min_value = 0.5, max_value = 5.0, step = 0.25)
param_b = st.slider("Y-to-X Axis Ratio, " + r"$b$", min_value = 0.5, max_value = 8.0, step = 0.25)
param_c = st.slider("Z-to-X Axis Ratio, " + r"$c$", min_value = 0.5, max_value = 8.0, step = 0.25)

years = st.slider("Time (Gyr):", min_value = 0, max_value = 14)
radius = st.slider("Set the initial distance from the galactic center (kpc):", min_value = 0.0, max_value = 50.0, step = 1.0)
height = st.slider("Set the initial height from the galactic plane (kpc):", min_value = 0.0, max_value = 50.0, step = 1.0)

pot_fxn_set = PowerTriaxialPotential(alpha = param, b = param_b, c = param_c)

# get all the two-dimensional plots and data for the animations from plot_orbit_2D
fig0, fig1, fig2, fig3, raw_html, raw_html_2, density = plot_orbit_2D(pot_fxn_set, years, radius, height)

st.markdown("Below is a plot of the potential over each value of R and \
		z. The darker regions are areas where the magnitude of the potential is higher — so we can see that the potential \
		increases as the object gets closer to the center.")

st.pyplot(density.get_figure())

st.markdown("We can examine three plots to understand how particles will move in this potential.")
st.markdown("The first is an **R vs. z** plot, which displays the path of the orbit in the meridional plane. With this one, we can see how far the particle is from the \
	galactic plane — its vertical distance — at each radius from the galactic center. We can see if orbits are bound or unbound, depending on the appearance of this plot.")

st.pyplot(fig0, bbox_inches = "tight", pad_inches = 0.5)

st.markdown("The second is an **radius vs. radial velocity** plot, which displays the radial velocity of the particle at each radius — how fast the particle moves based on its distance \
	from the galactic center. We can track where the velocity is positive and where it is negative, which indicates the direction the particle orbits. Bound orbits will \
	fluctuate between positive and negative, while unbound orbits will increase in radial velocity off into infinity.")

# show the plot in R vs. vR coordinates
st.pyplot(fig2, bbox_inches = "tight", pad_inches = 0.5)

st.markdown("The next is an **RA vs. Dec** plot, which displays the path of the orbit in celestial coordinates. This is the path the particle takes within the sky.")

# show the plot in right ascension vs. declination coordinates
st.pyplot(fig1, bbox_inches = "tight", pad_inches = 0.5)

st.markdown("Lastly, we show **the projection of the orbit into the x-y plane**, which shows the position and movement of the particle through the galactic plane.")

# show the orbit in Cartesian coordinates 
st.pyplot(fig3, bbox_inches = "tight", pad_inches = 0.5)

st.markdown("Finally, there are two animations that displays the movement of the particle perpendicular to the galactic plane — its vertical height from the galactic plane \
	at each radius — as well as the motion of the particle in the galactic plane.")

# show the animation in two dimensions
st.components.v1.html(raw_html, height = 600)
st.components.v1.html(raw_html_2, height = 600)

st.markdown("We can also explore this orbit in 3 dimensions... ")

# get all of the plots of this potential from plot_orbit_3D
fig0, fig1, fig2, raw_html, density_3D = plot_orbit_3D(pot_fxn_set, years, radius, height)

st.markdown("This first plot shows the orbit in **x, y and z coordinates**. With this we can see how the particle will move \
	in three-dimensional space.")

# show the Cartesian coordinates plot
st.pyplot(fig0, bbox_inches = "tight", pad_inches = 0.5)

st.markdown("This next plot shows the relationship between the **orbital radius, radial velocity and height from the disk plane**. \
	This shows how the radial velocity of the particle changes with its position inside the distribution.")

# show the R vs. vr vs. z plot
st.pyplot(fig1, bbox_inches = "tight", pad_inches = 0.5)

st.markdown("The last plot shows the relationship between the particle's **orbital radius, radial velocity and vertical velocity**. \
	This plot shows how fast the particle is moving radially and vertically, depending on its distance from the center of the galaxy.")

# show the R vs. vR vs. vz plot
st.pyplot(fig2, bbox_inches = "tight", pad_inches = 0.5)

# show the animation
st.markdown("And now we display the 3D animation of the orbit.")
st.components.v1.html(raw_html, height = 800)
