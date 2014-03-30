#from distutils.core import setup
from setuptools import setup

setup(
    name='vuqutils',
    version='0.0.1',
    author='Jason M. Hite',
    author_email='jasonmhite@gmail.com',
    packages=['vuqutils'],
    #url='http://pypi.python.org/pypi/TowelStuff/',
    license='LICENSE.txt',
    description='Useful stuff for VUQ warriors.',
    long_description=open('README.txt').read(),
    install_requires=[
        "seaborn"
    ],
    #classifiers=[
        #'Intended Audience :: Science/Research',
        #'License :: OSI Approvied :: BSD License',
    #],
)
