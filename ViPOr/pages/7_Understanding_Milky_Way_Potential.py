# A page to help the user undersatnd the potential of the Milky Way galaxy. Users can select various components of the 
# Milky Way and see how they impact the rotation curve, orbits and motion of particles in the Milky Way — both individually
# and summed together.

from galpy.util.conversion import get_physical
import numexpr
import matplotlib.pyplot as plt
from astropy import units
from galpy.util import conversion
from galpy import orbit 
from galpy.potential import plotPotentials, calcRotcurve, PowerSphericalPotentialwCutoff, MiyamotoNagaiPotential, NFWPotential, KeplerPotential
import numpy
import streamlit as st

# initialize the bulge potential, disk potential and dark matter halo potential

bp = PowerSphericalPotentialwCutoff(alpha=1.8,rc=1.9/8.,normalize=0.05)
mp = MiyamotoNagaiPotential(a=3./8.,b=0.28/8.,normalize=.6)
np = NFWPotential(a=16/8.,normalize=.35)

galaxy = []

# create a list of radii at which to evaluate the rotation curve

r_s = numpy.linspace(0.01, 10, 1000)

st.markdown("## Understanding the Milky Way Potential")
st.markdown("Now that you've had a chance to look at general potentials and understand how particles behave in them, in this module, we will look at \
	a specific case: the Milky Way.")
st.markdown("The Milky Way can be simplified and broken down into four separate components: a **:green[bulge]**, a **:green[disk]**, a **:green[halo]** and a **:green[black hole]**.")
st.markdown("Because potentials are scalar quantities, they have the property of linearity, and thus we can add them together \
	to yield the potential of a more complex system. The Milky Way potential can then be written as:")

st.latex(r'''\Phi_{\text{MW}} = \Phi_{\text{disk}} + \Phi_{\text{bulge}} + \Phi_{\text{halo}} + \Phi_{\text{black hole}}''')

st.markdown("The disk can be approximated with the Miyamoto-Nagai Potential, the bulge with a power-law spherical potential with a cutoff, and \
	the halo with the NFW potential. The black hole may be treated as a point mass, which has a Keplerian potential.")
st.markdown("Check the boxes below to see how the rotation curves and the orbit changes as components are added or removed.")

# create checkboxes so the user can add or take away various components of the Milky Way

bulge = st.checkbox("Add bulge?")
disk = st.checkbox("Add disk?")
darkmatter = st.checkbox("Add dark matter?")
blackhole = st.checkbox("Add black hole?")

fig, ax = plt.subplots()

# for each MW component, calculate the rotation curve of the individual component, append the potential to the list and plot the separate rotation curve

if bulge == True:
	rc_bp = calcRotcurve(bp, r_s)
	galaxy.append(bp)
	ax.plot(r_s, rc_bp, label = "Bulge Potential")

if disk == True:
	rc_mp = calcRotcurve(mp, r_s)
	ax.plot(r_s, rc_mp, label = "Disk Potential")
	galaxy.append(mp)

if darkmatter == True:
	rc_np = calcRotcurve(np, r_s)
	ax.plot(r_s, rc_np, label = "Dark Matter, NFW Potential")
	galaxy.append(np)

if blackhole == True:
	milkyway_bh = KeplerPotential(amp=4*10**6./conversion.mass_in_msol(220.,8.))
	rc_bh = calcRotcurve(milkyway_bh, r_s)
	ax.plot(r_s, rc_bh, label = "Black Hole Potential")
	galaxy.append(milkyway_bh)

# if there are no galaxy components checked off and put into the list, do nothing at all

if len(galaxy) == 0:

	pass

else:  

	# set title, labels and legend for the rotation curve plot

	ax.set_title("Rotation Curves of Components of the Milky Way Galaxy")
	ax.set_xlabel(r"$R/R_0$")
	ax.set_ylabel(r"$v_c(R)/v_c(R_0)$")
	ax.legend()

	# calculate the total rotation curve
	rot_curve = calcRotcurve(galaxy, r_s)

	st.markdown("Here are the rotation curves for each individual component of the Milky Way:")

	# plot the figure with the individual components
	st.pyplot(fig)

	fig_total, ax_total = plt.subplots()

	# plot the total rotation curve, also set the titles and axis labels for the total rotation curve plot
	ax_total.plot(r_s, rot_curve)
	ax_total.set_xlabel(r"$R/R_0$")
	ax_total.set_ylabel(r"$v_c(R)/v_c(R_0)$")
	ax_total.set_title(r"Total Rotation Curve of the Milky Way Galaxy")

	st.markdown("Here is the rotation curve for the sum of the components of the Milky Way:")

	# show the total rotation curve plot
	st.pyplot(fig_total)

	# initialize and integrate the orbit over the age of the Milky Way
	times = numpy.linspace(0.,13.6, 3001)*units.Gyr
	orbits = orbit.Orbit(**get_physical(galaxy))
	orbits.integrate(times, galaxy)

	st.markdown("Below is a plot of the potential for the Milky Way with the components selected, over each value of R and \
		z. The darker regions are areas where the magnitude of the potential is higher — so we can see that the potential \
		increases as the object gets closer to the center.")

	# plot the potential at each value of R and z
	density = plotPotentials(galaxy)
	st.pyplot(density.get_figure())

	# take the raw html of the 2D animated orbit and plot it
	st.markdown("See how the movement of the particle changes depending on the components we include. In two dimensions...")
	raw_html = orbits.animate()._repr_html_()
	st.components.v1.html(raw_html, height = 500)

	# take the raw html of the 3D animated orbit and plot it
	st.markdown("And in three dimensions...")
	raw_html_3d = orbits.animate3d(mw_plane_bg = True)._repr_html_()
	st.components.v1.html(raw_html_3d, height = 800)
