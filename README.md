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

This application relies on **galpy**, a package that assists in calculating potentials, plotting orbits, and performing other actions related to galaxy dynamics. Galpy uses numpy, matplotlib, numexpr (used for characterizing and plotting orbits), and astropy (in this application, for manipulating and converting units). 

If the user would like to run the application directly from this Github repository with the link below, they will not need to perform any installations — the required dependencies are listed and installed with the *requirements.txt* file above. 

# RUNNING VIPOR

The user has two options to run ViPOr. 

The first option is to download the entire code from this repository, unzipping the compressed file, navigating to the top-level directory and installing the package by running:

`pip install .`

Then, while still in the top-level directory, run: 

`streamlit run ./ViPOr/1_ViPOr_Homepage.py`

Alternatively, the user may click the link below and be redirected to the website, where they can run the application directly online. 

[https://oaspegren-vipor-1-vipor-homepage-nmt112.streamlit.app/](https://oaspegren-vipor-vipor1-vipor-homepage-zx0uzt.streamlit.app/)
