from setuptools import setup

setup(name="HPPL (High Performance Python Lab)-Final Project-2022",
      author="Lyubits* Flow",
      description = 
      '''
      Numerical and Physical modeling of Pressure-Driven Pipe Flow, Hagen-Poiseuille Flow
      ''',
      install_requires = [
          "numpy >= 1.21.6"
          "cupy  >= 11.0.0"
          "numba >= 0.56.4"
          "tqdm  >= 4.64.1"
          "matplotlib >= 3.2.2"
      ],

long_description = open('README.md').read()
)
