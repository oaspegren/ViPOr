# This page allows the user to select a spherically symmetric potential, modify its key parameters (power law exponent, scale length, etc.),
# and then examine different plots that describe its motion in three-dimensions. At the end, there's an animation that shows the motion
# of the particle in its orbit.

from astropy import units
from galpy.orbit import Orbit
from galpy.potential import plotPotentials, TwoPowerSphericalPotential, PowerSphericalPotential, HomogeneousSpherePotential, SphericalShellPotential, PlummerPotential
from galpy.util.conversion import get_physical
import numexpr
import matplotlib.pyplot as plt
import numpy

import streamlit as st

from PlotPotentialandOrbit3D import plot_orbit_3D
from pick_potential import pick_potential, set_potential

st.markdown("## Experimenting with Spherically Symmetric Orbits in Three Dimensions")

pot_names = ["Power Spherical Potential", "Two Power Spherical Potential", "Spherical Shell Potential", "Homogeneous Sphere Potential", "Plummer Potential"]
pot_fxn = st.selectbox('Select a potential function:', pot_names)
mod_params = [r"$\alpha$, the power law exponent", r"$\alpha$ and $\beta$, the power law exponents", r"$a$, the radius of the shell", r"$R$, the radius of the sphere", r"$b$, the scale parameter"]

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
height = st.slider("Set the initial height from the galactic plane:", min_value = 0.0, max_value = 50.0, step = 1.0)

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

fig0, fig1, fig2, raw_html = plot_orbit_3D(pot_fxn_set, years, radius, height)

st.markdown("This first plot shows the orbit in **x, y and z coordinates**. With this we can see how the particle will move \
	in three-dimensional space.")

st.pyplot(fig0, bbox_inches = "tight", pad_inches = 0.5)

st.markdown("This next plot shows the relationship between the **orbital radius, radial velocity and height from the disk plane**. \
	This shows how the radial velocity of the particle changes with its position inside the distribution.")

st.pyplot(fig1, bbox_inches = "tight", pad_inches = 0.5)

st.markdown("The last plot shows the relationship between the particle's **orbital radius, radial velocity and vertical velocity**. \
	This plot shows how fast the particle is moving radially and vertically, depending on its distance from the center of the galaxy.")

st.pyplot(fig2, bbox_inches = "tight", pad_inches = 0.5)

st.markdown("And now we display the 3D animation of the orbit.")
st.components.v1.html(raw_html, height = 800)


#plotPotentials(pot_fxn_set)

# R = radius*units.kpc
# z = 0.0*units.kpc

# vR = 0.0*units.km/units.s
# vT = 0.0*units.km/units.s
# vz = 0.0*units.km/units.s
# phi = 0.0*units.radian

# init_cond = [R, vR, vT, z, vz, phi]

# # initialize the orbit, and integrate it over the input duration of time
# orbit = Orbit(init_cond, **get_physical(pot_fxn_set))

# times = numpy.linspace(0.,years,3001)*units.Gyr
# orbit.integrate(times, pot_fxn_set)

# # get all the quantities so we can plot them in matplotlib
# reg = orbit.plot3d(lw=0.6)[0].get_data_3d()

# fig0, ax0 = plt.subplots(subplot_kw=dict(projection='3d'))
# ax0.plot(reg[0], reg[1], reg[2])
# ax0.set_xlabel(r"$x$")
# ax0.set_ylabel(r"$y$")
# ax0.set_zlabel(r"$z$")

# plt.xlim(-100.,100.)
# plt.ylim(-100.,100)

# r_vr = orbit.plot3d(d1 = 'R',d2 = 'vR', d3 = 'z')[0].get_data_3d()
# ra_dec = orbit.plot3d(d1 = 'R',d2 = 'vR', d3 = 'vT')[0].get_data_3d()

# fig1, ax1 = plt.subplots(subplot_kw=dict(projection='3d'))
# ax1.plot(ra_dec[0], ra_dec[1], ra_dec[2])
# ax1.set_xlabel(r"$R$")
# ax1.set_ylabel(r"$v_R$")
# ax1.set_zlabel(r"$z$")

# fig2, ax2 = plt.subplots(subplot_kw=dict(projection='3d'))
# ax2.plot(r_vr[0], r_vr[1], r_vr[2])
# ax2.set_xlabel(r"$R$")
# ax2.set_ylabel(r"$v_R$")
# ax2.set_zlabel(r"$v_T$")

# st.pyplot(fig0)
# st.pyplot(fig1)
# st.pyplot(fig2)

# st.markdown("And the 3D animation of the orbit:")
# raw_html = orbit.animate3d()._repr_html_()
# st.components.v1.html(raw_html, height = 800)


#animate_orbit_2D()

#sample_distribution_2D()