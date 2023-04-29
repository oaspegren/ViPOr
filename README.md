# ViPOr: Visualizing and Plotting Potentials and Orbits (with Python)

ViPOr is a teaching tool to help understand the orbits of particles in different potentials. The package is a web application launched using streamlit. 

ViPOr makes use of galpy, a Python package that includes features for initializing potentials, integrating orbits and displaying the paths of particles through multidimensional plots and animations. 

The application is composed of several pages:
  - **Homepage**: the introduction to the web app, where the user can navigate to different modules
  - **A Closer Look at Rotation Curves**: where the user can examine the rotation curves of different potentials
  - **Spherically Symmetric Potentials in 2D**: allows the user to initialize different spherically symmetric potentials and then plot and animate them
  - **Spherically Symmetric Potentials in 3D**: same thing as the two-dimensional version, just in three dimensions
  - **A Generic Axisymmetric Example**: plots and animations of the most basic axisymmetric potential
  - **A Generic Triaxial Example**: plots and animations of the most basic triaxial potential
  - **Understanding the Milky Way Potential**: allows the user to add components of the Milky Way potential together and see how each separate piece impacts the potential and particle orbits

# DEPENDENCIES

galpy, numpy, matplotlib, numexpr, astropy, streamlit

# LINK TO STREAMLIT PAGE

https://oaspegren-vipor-1-vipor-homepage-nmt112.streamlit.app/

![XKCD comic about orbital mechanics](https://imgs.xkcd.com/comics/orbital_mechanics.png)
