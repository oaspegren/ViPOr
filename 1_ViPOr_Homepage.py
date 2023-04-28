# Main Website interface

import streamlit as st

st.set_page_config(
    page_title="Welcome to ViPOr!",
    page_icon="🐍",
)

st.markdown("# Welcome to :green[ViPOr]: :green[Vi]sualizing :green[P]otentials and :green[Or]bits with Python!")

st.markdown("### A teaching tool to understand how particles move in different galaxy potentials.")

st.markdown("### Some useful features:")
st.markdown("- Examining the **rotation curves** produced by different spherically symmetric, axisymmetric and triaxial potentials")
st.markdown("- Visualizing the primary **spherically symmetric** potentials in two and three dimensions")
st.markdown("- Understanding the components of the **Milky Way potential**")
st.markdown("- Plotting the general **axisymmetric** and **triaxial** potentials in multiple dimensions")

st.markdown("### Basic Information About Potentials")

st.markdown("The force on a particle within a given mass distribution is related to the potential by the equation:")

st.latex(r'''
	\bar{F}(\bar{x}) = -\bar{\nabla} \Phi
	''')
st.markdown(r"where $\Phi(\bar{x})$ is defined as")

st.latex(r'''
	\Phi(\bar{x}) = -G \int \frac{1}{|\bar{x}' - \bar{x}|} \rho (\bar{x'}) d^3 x'
	''')

st.markdown("In practice, it's often much easier to compute and visualize the graviational potential than it is the force; therefore, we can \
	start by computing the potential of a given mass distribution and use that to derive the force on an object in that potential.")

st.markdown("A useful equation that relates force to density and potential is the **Poisson equation**, given by:")

st.latex(r'''
	\nabla \cdot \bar{F} = - \nabla^2 \Phi = -4 \pi G \rho(\bar{x})
	''')

st.markdown("Galaxy systems can be organized into three distinct categories, depending on their symmetries: spherically symmetric, axisymmetric and triaxial.")

st.markdown("#### Spherically Symmetric Systems")

st.markdown("Spherically symmetric systems are exactly what they sound like: distributions that are symmetrical in all three coordinates.")

st.markdown("The Poisson equation for spherical systems, which we use to relate the density of the distribution and the potential, is,")

st.latex(r"\nabla^2 \Phi (\bar{x}) = 4 \pi G \rho(\bar{x})")

st.markdown("Or, in spherical coordinates,")

st.latex(r"\frac{1}{r^2} \frac{\partial}{\partial r} (r^2 \frac{\partial \Phi}{\partial r}) = 4 \pi G \rho(r)")

st.markdown("#### Axisymmetric Systems")

st.markdown("Axisymmetric systems represent galaxy disks, and are only symmetrical in two directions. We often deal with axisymmetric systems \
	using cylindrical coordinates. In this case, the Poisson equation becomes:")

st.latex(r"\nabla^2 \Phi (r, z) = \frac{1}{r^2} \frac{\partial}{\partial r} (r^2 \frac{\partial \Phi}{\partial r}) + \frac{\partial^2 \Phi}{\partial z^2} = 4 \pi G \rho(r)")

st.markdown("#### Triaxial Systems")

st.markdown("Triaxial systems are found in elliptical galaxies. In general, they represent the most complicated systems, as they are not always \
	symmetrical in any of the three directions. Visually, triaxial distributions look like footballs.")

st.markdown("Solving and characterizing these systems analytically requires multipole expansions and Bessel functions; therefore, these will be too complex \
	to describe here. However, we include a page that allows the user to manipulate and experiment with this galaxy geometry.")

