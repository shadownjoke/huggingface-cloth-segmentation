from distutils.core import setup
from setuptools import find_packages
from spdk import __version__


setup(name='spdk', version=__version__, packages=find_packages())
