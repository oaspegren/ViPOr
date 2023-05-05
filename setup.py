import setuptools

setuptools.setup(
     name="ViPOr",
     version="0.1",
     author="Olivia Aspegren",
     author_email="olivia.aspegren@yale.edu",
     description="A teaching tool for understanding galaxy potentials and orbits",
     packages=["ViPOr","ViPOr/pages"]
)

python_requires='>=3'

install_requires=["streamlit", "numpy", "galpy", "matplotlib", "astropy", "numexpr"]