from setuptools import setup

setup(name = 'Monte Carlo Simulation',
    version = '1.0.0',
    packages = ['montecarlo'],
    author = "Eric Tang",
    author_email = 'ezt4q@virginia.edu',
    description = 'A Monte Carlo Simulation with three classes: die, game, and analyzer. In addition, there are unit tests, a scenario script, and documentation for the code. Created for DS5100 as a final project.',
    url = 'https://github.com/EZ-Tang/Monte-Carlo-Simulator',
    license = 'MIT',
    install_requires = ['numpy', 'pandas']
)