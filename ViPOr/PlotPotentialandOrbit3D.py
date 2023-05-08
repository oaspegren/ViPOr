# This file contrains functions for plotting figures that describe the orbit of a particle in three dimensions. This function is called in the
# spherically symmetric, axisymmetric and triaxial mass distribution pages. 

from galpy.orbit import Orbit
from astropy import units
import galpy
import galpy.potential
from galpy.util.conversion import get_physical
import numexpr
import matplotlib.pyplot as plt
import numpy

import streamlit as st

def plot_orbit_3D(pot_fxn, years, R, z):
	'''
	Plot the orbit of your selected potential in three dimensions, integrating over a variable number of times and allowing
	the user to change the number of spiral arms present, and the effects of dynamical friction.

	Inputs
	--------
	pot_fxn: the potential function, either set by default or chosen by the user
	years: integration time of the orbit, either set by default or chosen by the user with a slider
	R: the initial radius from the galactic center, picked by the user 
	z: the initial height from the galactic plane, set by the user

	Outputs: 
	-------
	fig0: a three dimensional plot of the orbit in Cartesian coordinates
	fig1: a three dimensional plot of the orbit in R vs. radial velocity vs. vertical height from the disk plane
	fig2: a three dimensional plot of the orbit in R vs. radial velocity vs. vertical velocity
	raw_html: the raw html for the animation, which can be plotted by streamlit
	density: a contour plot of the potential
	'''	

	# define all the initial conditions — some of these are input by the user and others are set automatically

	R = R*units.kpc
	z = z*units.kpc
	
	vR = 0.0*units.km/units.s
	vT = 0.0*units.km/units.s
	vz = 0.0*units.km/units.s
	phi = 0.0*units.radian

	init_cond = [R, vR, vT, z, vz, phi]

	# initialize the orbit, and integrate it over the input duration of time
	orbit = Orbit(init_cond, **get_physical(pot_fxn))
	times = numpy.linspace(0.,years,3001)*units.Gyr
	orbit.integrate(times, pot_fxn)

	# get the data from the plot of the orbit in Cartesian coordinates
	reg = orbit.plot3d(lw=0.6)[0].get_data_3d()

	# plot the orbit, setting axis labels and titles
	fig0, ax0 = plt.subplots(figsize = (10, 9),subplot_kw=dict(projection='3d'))
	ax0.plot(reg[0], reg[1], reg[2])
	ax0.set_xlabel(r"$x$")
	ax0.set_ylabel(r"$y$")
	ax0.set_zlabel(r"$z$")
	ax0.set_title("Orbit in X, Y and Z Coordinates")

	plt.xlim(-100.,100.)
	plt.ylim(-100.,100)
	
	# get the data for the other two three-dimensional orbit plots
	r_vr = orbit.plot3d(d1 = 'R',d2 = 'vR', d3 = 'z')[0].get_data_3d()
	ra_dec = orbit.plot3d(d1 = 'R',d2 = 'vR', d3 = 'vT')[0].get_data_3d()

	# plot R vs. vR vs. z, configure axis labels and titles
	fig1, ax1 = plt.subplots(figsize = (10, 9), subplot_kw=dict(projection='3d'))
	ax1.plot(ra_dec[0], ra_dec[1], ra_dec[2])
	ax1.set_xlabel(r"$R$")
	ax1.set_ylabel(r"$v_R$")
	ax1.set_zlabel(r"$z$")
	ax1.set_title("Orbital Radius vs. Radial Velocity and Height from the Plane of the Disk")

	# plot R vs. vR vs. vz, configure axis labels and titles
	fig2, ax2 = plt.subplots(figsize = (10, 9), subplot_kw=dict(projection='3d'))
	ax2.plot(r_vr[0], r_vr[1], r_vr[2])
	ax2.set_xlabel(r"$R$")
	ax2.set_ylabel(r"$v_R$")
	ax2.set_zlabel(r"$v_z$")
	ax2.set_title("Orbital Radius vs. Radial and Vertical Velocities")

	# get the raw html for the animation and the contour plot of the potential, so these can be plotted with streamlit
	raw_html = orbit.animate3d()._repr_html_()
	density = galpy.potential.plotPotentials(pot_fxn, phi = 0.0*units.radian)

	return fig0, fig1, fig2, raw_html, density

	
