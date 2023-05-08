# This file contrains functions for plotting figures that describe the orbit of a particle in two dimensions. This function is called in the
# spherically symmetric, axisymmetric and triaxial mass distribution pages. 

from galpy.orbit import Orbit
from astropy import units
import galpy.potential
from galpy.util.conversion import get_physical
import numexpr
import matplotlib.pyplot as plt
import numpy
import streamlit as st

def plot_orbit_2D(_pot_fxn, _years, _R, _z):
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
	fig0: a two dimensional plot of the orbit in R vs. z coordinates
	fig1: a two dimensional plot of the orbit in right ascension vs. declination coordinates
	fig2: a two dimensional plot of the orbit in R vs. radial velocity coordinates
	fig3: a two dimensional plot of the orbit in Cartesian coordinates
	raw_html: the raw html for the animation, which can be plotted by streamlit
	density: a contour plot of the potential
	'''	

	# define all the initial conditions — some of these are input by the user and others are set automatically
	
	R = _R*units.kpc
	z = _z*units.kpc
	
	vR = 0.0*units.km/units.s
	vT = 0.0*units.km/units.s
	vz = 0.0*units.km/units.s
	phi = 0.0*units.radian

	init_cond = [R, vR, vT, z, vz, phi]

	# initialize the orbit and integrate
	orbit = Orbit(init_cond, **get_physical(_pot_fxn))
	times = numpy.linspace(0.,_years,3001)*units.Gyr
	orbit.integrate(times, _pot_fxn)

	fig, ax = plt.subplots()

	# get the data from the plot of the orbit in R vs. z coordinates
	reg = orbit.plot(lw=0.6)[0].get_data()

	# plot the orbit, setting axis labels and titles
	fig0, ax0 = plt.subplots()
	plt.plot(reg[0], reg[1])
	ax0.set_xlabel(r"$R$ (kpc)")
	ax0.set_ylabel(r"$z$ (kpc)")
	ax0.set_title("Orbit, in R vs. z")
	
	# get the data for the orbit in right ascension vs. declination coordinates
	ra_dec = orbit.plot(d1='ra',d2='dec')[0].get_data()

	# plot the orbit, setting axis labels and titles
	fig1, ax1 = plt.subplots()
	ax1.scatter(ra_dec[0], ra_dec[1])
	ax1.set_xlabel(r"$\alpha$, Right Ascension (deg)")
	ax1.set_ylabel(r"$\delta$, Declination (deg)")
	ax1.set_title("Orbit, in RA and Dec Coordinates")

	# get the data for the orbit in R vs. radial velocity coordinates
	r_vr = orbit.plot(d1='R',d2='vR')[0].get_data()

	# plot the orbit, setting axis labels and titles
	fig2, ax2 = plt.subplots()
	ax2.plot(r_vr[0], r_vr[1])
	ax2.set_xlabel(r"$R$ (kpc)")
	ax2.set_ylabel(r"$v_R$ (km/s)")
	ax2.set_title("Radius vs. Radial Velocity")

	# get the data for the orbit in Cartesian coordinates
	x_y = orbit.plot(d1='x',d2='y')[0].get_data()

	# plot the orbit, setting axis labels and titles
	fig3, ax3 = plt.subplots()
	ax3.scatter(x_y[0], x_y[1])
	ax3.set_xlabel(r"$x$ (kpc)")
	ax3.set_ylabel(r"$y$ (kpc)")
	ax3.set_title("Orbit, Projected Onto X-Y Plane")

	# get the raw html data for the two-dimensional orbit in Cartesian and R vs. z coordinates
	raw_html = orbit.animate(d1=['x','R'],d2=['y','z'])._repr_html_()

	# get the plot of the potential
	density = galpy.potential.plotPotentials(_pot_fxn)

	return fig0, fig1, fig2, fig3, raw_html, density


