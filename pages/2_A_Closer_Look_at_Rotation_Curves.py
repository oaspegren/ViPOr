!pip install astropy
!pip install galpy

import numexpr
import matplotlib.pyplot as plt
from astropy import units
from galpy import potential
import numpy
import streamlit as st

# Initializing the user interface, adding instructions and various background information

st.markdown("## A Closer Look at Rotation Curves")

st.markdown("The rotation curve of a specific galaxy gives the velocity of particles at different radii within that \
	object.")
st.markdown("The behavior of stars within a galaxy can change given the form of the potential, \
	the presence of spiral arms, the amount of dark matter, and other factors impacting the gravitational potential.")

st.markdown("#### Walk through the tutorial below to explore how different potentials and added elements affect the \
	rotation curve of a galaxy.")

st.markdown("The potentials we will investigate here are:")
st.markdown("- **Homogeneous Sphere Potential**: A sphere with a constant density.")
st.markdown("- **Power Spherical Potential**: A sphere whose density declines with a power law relation.")
st.markdown("- **Power Spherical Potential with Cutoff**: A sphere whose density declines with a power law relation and cuts off at a given radius.")
st.markdown("- **Spherical Shell Potential**: An shell with infinitesimal thickness.")
st.markdown("- **Double Exponential Disk Potential**: A distribution that is exponential in both the radius and height.")
st.markdown("- **Two Power Triaxial Potential**: A distribution with no symmetries, and no conserved component of the angular momentum.")

st.markdown("In addition, you can add **spiral arms** or **dark matter** to further alter the rotation curves:")

# initialize the list of r values

r_s = numpy.linspace(0.01, 50, 1000)*units.kpc

# initialize the potentials that we will calculate the rotation curves for
hsp = potential.HomogeneousSpherePotential()
psp = potential.PowerSphericalPotential()
pspc = potential.PowerSphericalPotentialwCutoff()
ssp = potential.SphericalShellPotential()
dedp = potential.DoubleExponentialDiskPotential()
tptp = potential.TwoPowerTriaxialPotential()
lp = potential.NFWPotential(amp = (6*10**11)*units.solMass)
   
# Create a checkbox for the user to add spiral arms, and a slider for the number of spiral arms to add
# then alter the potentials by adding the arms component

if st.checkbox("Add Spiral Arms?"):
	number = st.slider("How many arms?", min_value = 1, max_value = 5)
	hsp = hsp + potential.SpiralArmsPotential(N = number)
	psp = psp + potential.SpiralArmsPotential(N = number)
	pspc = pspc + potential.SpiralArmsPotential(N = number)
	ssp = ssp + potential.SpiralArmsPotential(N = number)
	dedp = dedp + potential.SpiralArmsPotential(N = number)
	tptp = tptp + potential.SpiralArmsPotential(N = number)

# Create a checkbox for the user to add dark matter, and a slider for the number of spiral arms to add
# then alter the potentials by adding the dark matter component

dm_cb = st.checkbox("Add Dark Matter?")

if dm_cb == True:
	hsp = hsp + potential.NFWPotential(amp = (6*10**11)*units.solMass)
	psp = psp + potential.NFWPotential(amp = (6*10**11)*units.solMass)
	pspc = pspc + potential.NFWPotential(amp = (6*10**11)*units.solMass)
	ssp = ssp + potential.NFWPotential(amp = (6*10**11)*units.solMass)
	dedp = dedp + potential.NFWPotential(amp = (6*10**11)*units.solMass)
	tptp = tptp + potential.NFWPotential(amp = (6*10**11)*units.solMass)

	st.markdown("We approximate the component of dark matter with the **NFW Potential**:")
	st.latex(r'''\rho(r)= \frac{\text{amp}}{4\pi a^3} \frac{1}{(r/a)(1 + r/a)^{2}} ''')

fig, ax = plt.subplots(figsize = (10, 6))

st.markdown("Check a box to display the rotation curve for a given potential:")

# give the users the option to display or hide different rotation curves

if st.checkbox("Homogeneous Sphere Potential"):
	rc_hsp = potential.calcRotcurve(hsp, r_s, phi = 0)
	ax.plot(r_s, rc_hsp, label = "Homogeneous Sphere Potential")

if st.checkbox("Power Spherical Potential"):
	rc_psp = potential.calcRotcurve(psp, r_s, phi = 0)
	ax.plot(r_s, rc_psp, label = "Power Spherical")

if st.checkbox("Power Spherical Potential, with Cutoff"):
	rc_pspc = potential.calcRotcurve(pspc, r_s, phi = 0)
	ax.plot(r_s, rc_pspc, label = "Power Spherical, with Cutoff")

if st.checkbox("Spherical Shell Potential"):
	rc_ssp = potential.calcRotcurve(ssp, r_s, phi = 0)
	ax.plot(r_s, rc_ssp, label = "Spherical Shell")

if st.checkbox("Double Exponential Disk Potential"):
	rc_dedp = potential.calcRotcurve(dedp, r_s, phi = 0)
	ax.plot(r_s, rc_dedp, label = "Double Exponential Disk")

if st.checkbox("Two Power Triaxial Potential"):
	rc_tptp = potential.calcRotcurve(tptp, r_s, phi = 0)
	ax.plot(r_s, rc_tptp, label = "Two Power Triaxial")

if st.checkbox("Dark Matter Halo") and dm_cb == True:
	rc_lp = potential.calcRotcurve(lp, r_s, phi = 0)
	ax.plot(r_s, rc_lp, label = "Dark Matter Halo")

# set labels and the legend for the plot
ax.set_title("Rotation Curves of Various Potentials")

ax.set_xlabel(r"$R/R_0$")

ax.set_ylabel(r"$v_c(R)/v_c(R_0)$")

ax.legend()

st.pyplot(fig)
