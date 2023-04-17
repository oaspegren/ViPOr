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


def plot_orbit_2D(pot_fxn, years):
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

	fig, ax = plt.subplots()

	reg = orbit.plot(lw=0.6)[0].get_data()

	fig0, ax0 = plt.subplots()
	plt.plot(reg[0], reg[1])
	st.pyplot(fig0)
	#st.components.v1.html(raw_plot, height = 500)

	plt.xlim(-100.,100.)
	plt.ylim(-100.,100)
	
	#plt.gca().set_zlim3d(-100., 100.)
	ra_dec = orbit.plot(d1='ra',d2='dec')[0].get_data()
	r_vr = orbit.plot(d1='R',d2='vR')[0].get_data()
	x_y = orbit.plot(d1='x',d2='y')[0].get_data()
	ll_bb = orbit.plot('k.',d1='ll',d2='bb')[0].get_data()

	fig1, ax1 = plt.subplots()
	ax1.plot(ra_dec[0], ra_dec[1])

	fig2, ax2 = plt.subplots()
	ax2.plot(r_vr[0], r_vr[1])

	fig3, ax3 = plt.subplots()
	ax3.plot(x_y[0], x_y[1])

	fig4, ax4 = plt.subplots()
	ax4.plot(ll_bb[0], ll_bb[1])

	st.pyplot(fig1)
	st.pyplot(fig2)
	st.pyplot(fig3)
	st.pyplot(fig4)



