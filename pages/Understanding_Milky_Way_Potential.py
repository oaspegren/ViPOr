# File to investigate the effects of different galaxy components on the rotation curves and 
# circular velocities of particles in the galaxy

from galpy.util.conversion import get_physical
import numexpr
import matplotlib.pyplot as plt
from astropy import units
from galpy.util import conversion
import galpy
import numpy
import streamlit as st

bp = galpy.potential.PowerSphericalPotentialwCutoff(alpha=1.8,rc=1.9/8.,normalize=0.05)
mp = galpy.potential.MiyamotoNagaiPotential(a=3./8.,b=0.28/8.,normalize=.6)
np = galpy.potential.NFWPotential(a=16/8.,normalize=.35)

galaxy = []

r_s = numpy.linspace(0.01, 10, 1000)

bulge = st.checkbox("Add bulge?")
disk = st.checkbox("Add disk?")
darkmatter = st.checkbox("Add dark matter?")
blackhole = st.checkbox("Add black hole?")

fig, ax = plt.subplots()

if bulge == True:
	rc_bp = galpy.potential.calcRotcurve(bp, r_s)
	galaxy.append(bp)
	ax.plot(r_s, rc_bp)

if disk == True:
	rc_mp = galpy.potential.calcRotcurve(mp, r_s)
	ax.plot(r_s, rc_mp)
	galaxy.append(mp)

if darkmatter == True:
	rc_np = galpy.potential.calcRotcurve(np, r_s)
	ax.plot(r_s, rc_np)
	galaxy.append(np)

if blackhole == True:
	milkyway_bh = galpy.potential.KeplerPotential(amp=4*10**6./conversion.mass_in_msol(220.,8.))
	rc_bh = galpy.potential.calcRotcurve(milkyway_bh, r_s)
	ax.plot(r_s, rc_bh)
	galaxy.append(milkyway_bh)

if len(galaxy) == 0:

	pass

else:  

	rot_curve = galpy.potential.calcRotcurve(galaxy, r_s)

	st.pyplot(fig)

	fig_total, ax_total = plt.subplots()

	ax_total.plot(r_s, rot_curve)

	st.pyplot(fig_total)


	times = numpy.linspace(0.,13.6, 3001)*units.Gyr

	orbits = galpy.orbit.Orbit(**get_physical(galaxy))
	orbits.integrate(times, galaxy)

	raw_html = orbits.animate()._repr_html_()
	st.components.v1.html(raw_html, height = 500)

	raw_html_3d = orbits.animate3d(mw_plane_bg = True)._repr_html_()
	st.components.v1.html(raw_html_3d, height = 800)

	#st.write(orbits.animate())
	#st.write(orbits.animate3d())


