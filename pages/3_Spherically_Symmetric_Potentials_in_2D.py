# This page allows the user to select a spherically symmetric potential, modify its key parameters (power law exponent, scale length, etc.),
# and then examine different plots that describe its motion in three-dimensions. At the end, there's an animation that shows the motion
# of the particle in its orbit.

from astropy import units
from galpy.orbit import Orbit
from galpy.util.conversion import get_physical
from galpy.potential import plotPotentials, TwoPowerSphericalPotential, PowerSphericalPotential, HomogeneousSpherePotential, SphericalShellPotential, PlummerPotential
import numexpr
import matplotlib.pyplot as plt
import numpy
import streamlit as st

from PlotPotentialandOrbit2D import plot_orbit_2D
from pick_potential import pick_potential, set_potential

st.markdown("## Experimenting with Spherically Symmetric Orbits in Two Dimensions")

pot_names = ["Power Spherical Potential", "Two Power Spherical Potential", "Spherical Shell Potential", "Homogeneous Sphere Potential", "Plummer Potential"]
pot_fxn = st.selectbox('Select a potential function:', pot_names)
# mod_params = [r"$\alpha$, the power law exponent", r"$\alpha$ and $\beta$, the power law exponents", r"$a$, the radius of the shell", r"$R$, the radius of the sphere", r"$b$, the scale parameter"]
pot_name_string = "You've selected the **"+pot_fxn+"**."
st.markdown(pot_name_string)

parameters, equation, param1, density_string, latex, min_value, max_value, step = pick_potential(pot_fxn, pot_names.index(pot_fxn))

st.markdown(density_string)
st.latex(latex)

param_string = "The parameter(s) you can modify are: **"+parameters+"**."

st.markdown(param_string)

st.markdown(
	'''
	Use the sliders to change this value and see what happens to the potential and orbit!
	''')

param = st.slider(param1, min_value = min_value, max_value = max_value, step = step)

pot_fxn_set = set_potential(pot_fxn, param)


# pot_name_string = "You've selected the **"+pot_fxn+"**."
# eqns = [r'''\rho(r)= \frac{\text{amp}}{r^{3}} \left(\frac{r_1}{r}\right)^\alpha''', r'''\rho(r)= \frac{\text{amp}}{4\pi a^3} \frac{1}{r^{\alpha} (1 + r/a)^{\beta-\alpha}}''',\
# 	r'''\rho(r)= \frac{\text{amp}}{4\pi a^2} \delta(r-a)''', r'''\rho(r)= \rho_0''', r''' ''']

# if pot_fxn != "Plummer Potential":
# 	st.markdown("The equation for the density of this distribution is:")
# 	st.latex(eqns[pot_names.index(pot_fxn)])

# if pot_fxn == "Plummer Potential":
# 	st.markdown("This potential is characterized by the equation:")
# 	st.latex(r'''\Phi(R,z) = - \frac{\text{amp}}{\sqrt{R^2 + z^2 + b^2}}''')

# param_string = "The parameter(s) you can modify are: **"+mod_params[pot_names.index(pot_fxn)]+"**."

# st.markdown(pot_name_string)
# st.markdown(param_string)

# st.markdown(
# 	'''
# 	Use the sliders to change this value and see what happens to the potential and orbit!
# 	''')

years = st.slider("Time (Gyr):", min_value = 0, max_value = 14)
radius = st.slider("Set the initial distance from the galactic center:", min_value = 0.0, max_value = 50.0, step = 1.0)

# if pot_fxn == "Two Power Spherical Potential":
# 	param1 = st.slider("Power Law Exponent, " + r"$\alpha$", min_value = 0.0, max_value = 6.0, step = 0.25)
# 	param2 = st.slider("Power Law Exponent, " + r"$\beta$", min_value = 0.0, max_value = 6.0, step = 0.25)

# 	pot_fxn_set = TwoPowerSphericalPotential(alpha = param1, beta = param2)

# elif pot_fxn == "Power Spherical Potential":
# 	param1 = st.slider("Power Law Exponent, " + r"$\alpha$", min_value = 0.0, max_value = 6.0, step = 0.25)
# 	pot_fxn_set = PowerSphericalPotential(alpha = param1)

# elif pot_fxn == "Homogeneous Sphere Potential":
# 	param1 = st.slider("Sphere Radius, " + r"$R$", min_value = 1, max_value = 50)*units.kpc
# 	pot_fxn_set = HomogeneousSpherePotential(R = param1)

# elif pot_fxn == "Spherical Shell Potential":
# 	param1 = st.slider("Shell Radius, " + r"$a$", min_value = 1, max_value = 50)*units.kpc
# 	pot_fxn_set = SphericalShellPotential(a = param1)

# else:
# 	param = st.slider("Scale Parameter, " + r"$b$", min_value = 1, max_value = 20)*units.kpc

# 	pot_fxn_set = PlummerPotential(b = param)

#plotPotentials(pot_fxn_set)

fig0, fig1, fig2, fig3, raw_html = plot_orbit_2D(pot_fxn_set, years, radius)

st.markdown("We can examine three plots to understand how particles will move in this potential.")
st.markdown("The first is an **R vs. z** plot, which displays the path of the orbit in the meridional plane. With this one, we can see how far the particle is from the \
	galactic plane — its vertical distance — at each radius from the galactic center. We can see if orbits are bound or unbound, depending on the appearance of this plot.")

st.pyplot(fig0, bbox_inches = "tight", pad_inches = 0.5)

st.markdown("The second is an **Radius vs. radial velocity** plot, which displays the radial velocity of the particle at each radius — how fast the particle moves based on its distance \
	from the galactic center. We can track where the velocity is positive and where it is negative, which indicates the direction the particle orbits. Bound orbits will \
	fluctuate between positive and negative, while unbound orbits will increase in radial velocity off into infinity.")

st.pyplot(fig2, bbox_inches = "tight", pad_inches = 0.5)

st.markdown("The next is an **RA vs. Dec** plot, which displays the path of the orbit in celestial coordinates. This is the path the particle takes within the sky.")

st.pyplot(fig1, bbox_inches = "tight", pad_inches = 0.5)

st.markdown("Lastly, we show **the projection of the orbit into the x-y plane**, which shows the position and movement of the particle through the galactic plane.")

st.pyplot(fig3, bbox_inches = "tight", pad_inches = 0.5)

st.markdown("Finally, there is an animation that displays the movement of the particle in the meridional plane — once again, its vertical height from the galactic plane \
	at each radius.")

st.components.v1.html(raw_html, height = 800)

# R = radius*units.kpc
# z = 5.0*units.kpc

# vR = 0.0*units.km/units.s
# vT = 0.0*units.km/units.s
# vz = 0.0*units.km/units.s
# phi = 0.0*units.radian

# init_cond = [R, vR, vT, z, vz, phi]

# orbit = Orbit(init_cond, **get_physical(pot_fxn_set))
# times = numpy.linspace(0.,years,3001)*units.Gyr
# orbit.integrate(times, pot_fxn_set)

# fig, ax = plt.subplots()

# reg = orbit.plot(lw=0.6)[0].get_data()

# fig0, ax0 = plt.subplots()
# plt.plot(reg[0], reg[1])
# ax0.set_xlabel(r"$R$ (kpc)")
# ax0.set_ylabel(r"$z$ (kpc)")
# ax0.set_title("Orbit, in R vs. z")
# #st.components.v1.html(raw_plot, height = 500)

# #plt.gca().set_zlim3d(-100., 100.)
# ra_dec = orbit.plot(d1='ra',d2='dec')[0].get_data()
# r_vr = orbit.plot(d1='R',d2='vR')[0].get_data()
# x_y = orbit.plot(d1='x',d2='y')[0].get_data()
# ll_bb = orbit.plot('k.',d1='ll',d2='bb')[0].get_data()

# fig1, ax1 = plt.subplots()
# ax1.plot(ra_dec[0], ra_dec[1])
# ax1.set_xlabel(r"$\alpha$, Right Ascension (deg)")
# ax1.set_ylabel(r"$\delta$, Declination (deg)")
# ax1.set_title("Orbit, in RA and Dec Coordinates")

# fig2, ax2 = plt.subplots()
# ax2.plot(r_vr[0], r_vr[1])
# ax2.set_xlabel(r"$R$ (kpc)")
# ax2.set_ylabel(r"$v_R$ (km/s)")
# ax2.set_title("Radius vs. Radial Velocity")

# fig3, ax3 = plt.subplots()
# ax3.plot(x_y[0], x_y[1])
# ax3.set_xlabel(r"$x$ (kpc)")
# ax3.set_ylabel(r"$y$ (kpc)")
# ax3.set_title("Orbit, Projected Onto X-Y Plane")

# fig4, ax4 = plt.subplots()
# ax4.plot(ll_bb[0], ll_bb[1])
# ax4.set_xlabel(r"$l$, Galactic Longitude (deg)")
# ax4.set_ylabel(r"$b$, Galactic Latitude (deg)")
# ax4.set_title("Orbit, in Galactic Longitude and Latitude Coordinates")

# st.pyplot(fig0)
# st.pyplot(fig1)
# st.pyplot(fig2)
# st.pyplot(fig3)
# st.pyplot(fig4)

# st.markdown("And the 3D animation of the orbit:")
# raw_html = orbit.animate()._repr_html_()
# st.components.v1.html(raw_html, height = 800)

