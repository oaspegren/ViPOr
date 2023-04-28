# File to create and plot different potentials

from galpy.orbit import Orbit
from astropy import units
import galpy
import galpy.potential
from galpy.util.conversion import get_physical
import numexpr
import matplotlib.pyplot as plt
import numpy
import streamlit as st

def plot_orbit_2D(_pot_fxn, _years, _R):
	'''
	Plot the orbit of your selected potential, integrating over a variable number of times and allowing
	the user to change the number of spiral arms present, and the effects of dynamical friction.

	Inputs: potential function, selected from the dropdown menu

	Outputs: 2-dimensional plot of the orbit.
    '''
	
	R = _R*units.kpc
	z = 5.0*units.kpc
	
	vR = 0.0*units.km/units.s
	vT = 0.0*units.km/units.s
	vz = 0.0*units.km/units.s
	phi = 0.0*units.radian

	init_cond = [R, vR, vT, z, vz, phi]

	orbit = Orbit(init_cond, **get_physical(_pot_fxn))
	times = numpy.linspace(0.,_years,3001)*units.Gyr
	orbit.integrate(times, _pot_fxn)

	fig, ax = plt.subplots()

	reg = orbit.plot(lw=0.6)[0].get_data()

	fig0, ax0 = plt.subplots()
	plt.plot(reg[0], reg[1])
	ax0.set_xlabel(r"$R$ (kpc)")
	ax0.set_ylabel(r"$z$ (kpc)")
	ax0.set_title("Orbit, in R vs. z")
	#st.components.v1.html(raw_plot, height = 500)
	
	#plt.gca().set_zlim3d(-100., 100.)
	ra_dec = orbit.plot(d1='ra',d2='dec')[0].get_data()
	r_vr = orbit.plot(d1='R',d2='vR')[0].get_data()
	x_y = orbit.plot(d1='x',d2='y')[0].get_data()

	fig1, ax1 = plt.subplots()
	ax1.scatter(ra_dec[0], ra_dec[1])
	ax1.set_xlabel(r"$\alpha$, Right Ascension (deg)")
	ax1.set_ylabel(r"$\delta$, Declination (deg)")
	ax1.set_title("Orbit, in RA and Dec Coordinates")

	fig2, ax2 = plt.subplots()
	ax2.plot(r_vr[0], r_vr[1])
	ax2.set_xlabel(r"$R$ (kpc)")
	ax2.set_ylabel(r"$v_R$ (km/s)")
	ax2.set_title("Radius vs. Radial Velocity")

	fig3, ax3 = plt.subplots()
	ax3.scatter(x_y[0], x_y[1])
	ax3.set_xlabel(r"$x$ (kpc)")
	ax3.set_ylabel(r"$y$ (kpc)")
	ax3.set_title("Orbit, Projected Onto X-Y Plane")

	# st.pyplot(fig0, bbox_inches = "tight", pad_inches = 0.5)
	# st.pyplot(fig1, bbox_inches = "tight", pad_inches = 0.5)
	# st.pyplot(fig2, bbox_inches = "tight", pad_inches = 0.5)
	# st.pyplot(fig3, bbox_inches = "tight", pad_inches = 0.5)

	raw_html = orbit.animate()._repr_html_()
	# st.components.v1.html(raw_html, height = 800)

	return fig0, fig1, fig2, fig3, raw_html



