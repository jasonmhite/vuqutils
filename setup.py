#from distutils.core import setup
from setuptools import setup

setup(
    name='vuqutils',
    version='0.0.2',
    author='Jason M. Hite',
    author_email='jasonmhite@gmail.com',
    packages=['vuqutils'],
    license='LICENSE.txt',
    description='Useful stuff for VUQ warriors.',
    long_description=open('README.txt').read(),
    install_requires=[
        "seaborn",
        "tables"
    ],
    scripts=[
        'bin/sdf2hdf5',
    ]
)
