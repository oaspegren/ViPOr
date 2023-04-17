# File to create and plot different potentials

from galpy.orbit import Orbit
from astropy import units
import galpy
import galpy.potential
from galpy.util.conversion import get_physical
import numexpr
import matplotlib.pyplot as plt
import numpy

def plot_orbit_2D(pot_fxn):
	'''
	Plot the orbit of your selected potential, integrating over a variable number of times and allowing
	the user to change the number of spiral arms present, and the effects of dynamical friction.

	Inputs: potential function, selected from the dropdown menu

	Outputs: 2-dimensional plot of the orbit.
	'''
    
    R = numpy.random.uniform(0., 100., 10)*units.kpc
	z = st.slider()*units.kpc
	phi = st.slider(0, numpy.pi)

	vR = st.slider()*units.km/units.s
	vT = st.slider()*units.km/units.s
	vz = st.slider()*units.km/units.s

	init_cond = [[R[i], vR, vT, z, vz, phi] for i in range(len(R))]

    if st.checkbox('Arms?'):
    	number = input("How many arms?")
        pot_fxn = pot_fxn + galpy.potential.SpiralArmsPotential(N = number)
        
    if st.checkbox('Friction?'):
        pot_fxn = pot_fxn + galpy.potential.ChandrasekharDynamicalFriction() # inputs for friction?
    
    years = st.slider("Time:")
        
    orbit = Orbit(**get_physical(pot_fxn))
    times = numpy.linspace(0.,int(years),3001)*units.Gyr
    orbit.integrate(times, pot_fxn)
    orbit.plot(lw=0.6)
    orbit_w_arms.plot(lw=0.6)
	plt.xlim(-100.,100.)
	plt.ylim(-100.,100)

	#plt.gca().set_zlim3d(-100., 100.)
	orbit_w_arms.plot(d1='ra',d2='dec')
	orbit_w_arms.plot(d1='R',d2='vR')
	orbit_w_arms.plot(d1='x',d2='y')
	orbit_w_arms.plot('k.',d1='ll',d2='bb')

	