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

def plot_orbit_3D(pot_fxn, years):
	'''
	Plot the orbit of your selected potential, integrating over a variable number of times and allowing
	the user to change the number of spiral arms present, and the effects of dynamical friction.

	Inputs: potential function, selected from the dropdown menu

	Outputs: 2-dimensional plot of the orbit.
	'''	
	R = numpy.random.uniform(0., 100., 10)*units.kpc
	z = 0.0*units.kpc
	
	#phi = st.slider("Set Initial Azimuth", min_value = 0.0, max_value = numpy.pi)
		
	#vR = st.slider("Set Initial Radial Velocity", min_value = 0.0, max_value = 50.0)*units.km/units.s
	#vT = st.slider("Set Initial Tangential Velocity", min_value = 0.0, max_value = 50.0)*units.km/units.s
	#vz = st.slider("Set Initial Vertical Velocity", min_value = 0.0, max_value = 50.0)*units.km/units.s

	vR = 0.0*units.km/units.s
	vT = 0.0*units.km/units.s
	vz = 0.0*units.km/units.s
	
	#init_cond = [[R[i], vR, vT, z, vz] for i in range(len(R))]
	init_cond = [50.0, 0.0, 0.0, 0.0, 0.0]*units.kpc

	'''
	if st.checkbox('Arms?'):
	    number = st.slider("How many arms?", min_value = 1, max_value = 8)
	    pot_fxn = pot_fxn + galpy.potential.SpiralArmsPotential(N = number)
	'''
	    
	orbit = Orbit(**get_physical(pot_fxn))

	times = numpy.linspace(0.,years,3001)*units.Gyr
	orbit.integrate(times, pot_fxn)

	reg = orbit.plot3d(lw=0.6)[0].get_data_3d()

	fig0, ax0 = plt.subplots(subplot_kw=dict(projection='3d'))
	ax0.plot(reg[0], reg[1], reg[2])
	st.pyplot(fig0)
	#st.components.v1.html(raw_plot, height = 500)

	plt.xlim(-100.,100.)
	plt.ylim(-100.,100)
	
	#plt.gca().set_zlim3d(-100., 100.)
	r_vr = orbit.plot3d(d1 = 'R',d2 = 'vR', d3 = 'z')[0].get_data_3d()
	ra_dec = orbit.plot3d(d1 = 'R',d2 = 'vR', d3 = 'vT')[0].get_data_3d()

	fig1, ax1 = plt.subplots(subplot_kw=dict(projection='3d'))
	ax1.plot(ra_dec[0], ra_dec[1], ra_dec[2])

	fig2, ax2 = plt.subplots(subplot_kw=dict(projection='3d'))
	ax2.plot(r_vr[0], r_vr[1], r_vr[2])

	st.pyplot(fig1)
	st.pyplot(fig2)

	