# Home page of the website
# This is the first page the user sees, which gives a brief introduction to what ViPOr is as well as a description of the 
# pages it includes. It also presents an overview of what gravitational potentials are, how they're affected by mass distributions, 
# and how they relate to the motion and orbits of particles in galaxies

import streamlit as st

st.set_page_config(
    page_title="Welcome to ViPOr!",
    page_icon="🐍",
)

# some introductory text with basic information about gravitational potentials, forces and orbits

st.markdown("# Welcome to :green[ViPOr] :green[Vi]sualizing :green[P]otentials and :green[Or]bits with Python!")

st.markdown("### A teaching tool to understand how particles move in different galaxy potentials.")

# overview of ViPOr's features
st.markdown("### Some useful features:")
st.markdown("- Examining the :green[**rotation curves**] produced by different spherically symmetric, axisymmetric and triaxial potentials")
st.markdown("- Visualizing the primary :green[**spherically symmetric**] potentials in two and three dimensions")
st.markdown("- Plotting the general :green[**axisymmetric**] and :green[**triaxial**] potentials in two and three dimensions")
st.markdown("- Understanding the components of the :green[**Milky Way potential**]")

st.markdown("Below is some general information about gravitational potentials and the resulting orbits within galaxies")

# overview of potentials
st.markdown("### Basic Information About Potentials")

st.markdown("Potential is the work per unit mass required to move an object from one point to another. In a gravitational field, this is the amount \
	of work done by gravity to move an object from infinity to a specific reference point.")

st.markdown("The force on a particle within a given mass distribution is related to the potential by the equation:")

st.latex(r'''
	\bar{F}(\bar{x}) = -\bar{\nabla} \Phi
	''')
st.markdown(r"where $\Phi(\bar{x})$ is defined as")

st.latex(r'''
	\Phi(\bar{x}) = -G \int \frac{1}{|\bar{x}' - \bar{x}|} \rho (\bar{x'}) d^3 x'
	''')

st.markdown("A useful equation that relates force to density and potential is the **Poisson equation**, given by:")

st.latex(r'''
	\nabla \cdot \bar{F} = - \nabla^2 \Phi = -4 \pi G \rho(\bar{x})
	''')

st.markdown("In practice, it's often much easier to compute and visualize the graviational potential than it is the force; therefore, we can \
	start by computing the mass distribution, determining the potential and then taking the gradient to yield the force on a particle.")

st.markdown("Galaxy systems can be organized into three distinct categories, depending on their symmetries: :green[**spherically symmetric**], :green[**axisymmetric**] and :green[**triaxial**].")

# overview of spherically symmetric potentials
st.markdown("#### Spherically Symmetric Systems")

st.markdown("Spherically symmetric systems are exactly what they sound like: distributions that are symmetrical around any axis. These are simple to deal with \
	because of Newton's theorems. These state that an observer standing outside the distribution may treat the entire system as if the mass is concentrated at \
	the center of the sphere, effectively reducing the system to a point mass. The other states that an observer inside the sphere experiences no net force from \
	the shell of material beyond their position — however, this material does affect the gravitational potential.")

st.markdown("The Poisson equation for spherical systems, which we use to relate the density of the distribution and the potential, is:")

st.latex(r"\nabla^2 \Phi (\bar{x}) = 4 \pi G \rho(\bar{x})")

st.markdown("Or, in spherical coordinates,")

st.latex(r"\frac{1}{r^2} \frac{\partial}{\partial r} (r^2 \frac{\partial \Phi}{\partial r}) = 4 \pi G \rho(r)")

# overview of axisymmetric potentials
st.markdown("#### Axisymmetric Systems")

st.markdown("Axisymmetric systems represent galaxy disks, and are only symmetrical about their rotational axis. They can \
	either take the shape of oblate spheroids (which look like hamburgers) or prolate spheroids (which look like pickles). \
	Axisymmetric distributions are dealt with most easily using cylindrical coordinates. In this case, the Poisson equation becomes:")

st.latex(r"\nabla^2 \Phi (r, z) = \frac{1}{r^2} \frac{\partial}{\partial r} (r^2 \frac{\partial \Phi}{\partial r}) + \frac{\partial^2 \Phi}{\partial z^2} = 4 \pi G \rho(r)")

# overview of triaxial potentials
st.markdown("#### Triaxial Systems")

st.markdown("Triaxial systems are found in elliptical galaxies. In general, they represent the most complicated systems, as they are not always \
	symmetrical in any of the three directions. Visually, triaxial distributions look like asymmetrical footballs.")

st.markdown("Solving and characterizing these systems analytically requires multipole expansions and Bessel functions; therefore, these will be too complex \
	to describe here with equations. However, we include a page that allows the user to manipulate and experiment with this galaxy geometry.")

st.markdown("Finally, we can determine orbits from potentials by employing Newton's 3rd Law.")


