from galpy.util.conversion import get_physical
import numexpr
import matplotlib.pyplot as plt
from astropy import units
from galpy.util import conversion
import galpy
import numpy
import streamlit as st

r_s = numpy.linspace(0.01, 10, 1000)

lp = galpy.potential.LogarithmicHaloPotential()
psp = galpy.potential.PowerSphericalPotential()
pspc = galpy.potential.PowerSphericalPotentialwCutoff()
ssp = galpy.potential.SphericalShellPotential()
dedp = galpy.potential.DoubleExponentialDiskPotential()
tptp = galpy.potential.TwoPowerTriaxialPotential()
    
    #R_value = st.slider('Input an initial distance from the galactic center:')
    
    #z_value = st.slider("Input an initial distance from the disk plane:")
    
    #vx_value = st.slider("Input an initial x-velocity:")
    
    #vz_value = st.slider("Input an initial z-velocity:")
    
    #phi_value = st.slider("Input an initial azimuthal angle:")
    
#init_conds = [R_value, z_value, vx_value, vz_value, phi_value]

fig, ax = plt.subplots()

rc_lp = galpy.potential.calcRotcurve(lp, r_s)
ax.plot(r_s, rc_lp, label = "Log Halo")

rc_psp = galpy.potential.calcRotcurve(psp, r_s)
ax.plot(r_s, rc_psp, label = "Power Spherical")

rc_pspc = galpy.potential.calcRotcurve(pspc, r_s)
ax.plot(r_s, rc_pspc, label = "Power Spherical, with Cutoff")

rc_ssp = galpy.potential.calcRotcurve(ssp, r_s)
ax.plot(r_s, rc_ssp, label = "Spherical Shell")

rc_dedp = galpy.potential.calcRotcurve(dedp, r_s)
ax.plot(r_s, rc_dedp, label = "Double Exponential Disk")

rc_tptp = galpy.potential.calcRotcurve(tptp, r_s)
ax.plot(r_s, rc_tptp, label = "Two Power Triaxial")

ax.legend()

st.pyplot(fig)
