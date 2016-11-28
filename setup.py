from setuptools import setup, find_packages
setup(
    name="CalCalc",
    version="0.1",
    install_requires=['pytest','wolframalpha','argparse'],
    packages=find_packages(),
)
