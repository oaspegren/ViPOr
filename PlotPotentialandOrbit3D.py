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

def plot_orbit_3D(pot_fxn, years, R):
	'''
	Plot the orbit of your selected potential, integrating over a variable number of times and allowing
	the user to change the number of spiral arms present, and the effects of dynamical friction.

	Inputs: potential function, selected from the dropdown menu

	Outputs: 2-dimensional plot of the orbit.
	'''	

	# define all the initial conditions
	R = R*units.kpc
	z = 0.0*units.kpc
	
	vR = 0.0*units.km/units.s
	vT = 0.0*units.km/units.s
	vz = 0.0*units.km/units.s
	phi = 0.0*units.radian

	init_cond = [R, vR, vT, z, vz, phi]

	# initialize the orbit, and integrate it over the input duration of time
	orbit = Orbit(init_cond, **get_physical(pot_fxn))

	times = numpy.linspace(0.,years,3001)*units.Gyr
	orbit.integrate(times, pot_fxn)

	# get all the quantities so we can plot them in matplotlib
	reg = orbit.plot3d(lw=0.6)[0].get_data_3d()

	fig0, ax0 = plt.subplots(figsize = (10, 9),subplot_kw=dict(projection='3d'))
	ax0.plot(reg[0], reg[1], reg[2])
	ax0.set_xlabel(r"$x$")
	ax0.set_ylabel(r"$y$")
	ax0.set_zlabel(r"$z$")
	ax0.set_title("Orbit in X, Y and Z Coordinates")

	plt.xlim(-100.,100.)
	plt.ylim(-100.,100)
	
	r_vr = orbit.plot3d(d1 = 'R',d2 = 'vR', d3 = 'z')[0].get_data_3d()
	ra_dec = orbit.plot3d(d1 = 'R',d2 = 'vR', d3 = 'vT')[0].get_data_3d()

	fig1, ax1 = plt.subplots(figsize = (10, 9), subplot_kw=dict(projection='3d'))
	ax1.plot(ra_dec[0], ra_dec[1], ra_dec[2])
	ax1.set_xlabel(r"$R$")
	ax1.set_ylabel(r"$v_R$")
	ax1.set_zlabel(r"$z$")
	ax1.set_title("Orbital Radius vs. Radial Velocity and Height from the Plane of the Disk")

	fig2, ax2 = plt.subplots(figsize = (10, 9), subplot_kw=dict(projection='3d'))
	ax2.plot(r_vr[0], r_vr[1], r_vr[2])
	ax2.set_xlabel(r"$R$")
	ax2.set_ylabel(r"$v_R$")
	ax2.set_zlabel(r"$v_z$")
	ax2.set_title("Orbital Radius vs. Radial and Vertical Velocities")

	# st.pyplot(fig0, bbox_inches = "tight", pad_inches = 0.5)
	# st.pyplot(fig1, bbox_inches = "tight", pad_inches = 0.5)
	# st.pyplot(fig2, bbox_inches = "tight", pad_inches = 0.5)

	st.markdown("And the 3D animation of the orbit:")
	raw_html = orbit.animate3d()._repr_html_()
	#st.components.v1.html(raw_html, height = 800)


	return fig0, fig1, fig2, raw_html

	