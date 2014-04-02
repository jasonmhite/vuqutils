from distutils.core import setup
#from setuptools import setup

setup(
    name='vuqutils',
    version='0.0.2',
    author='Jason M. Hite',
    author_email='jasonmhite@gmail.com',
    packages=['vuqutils',
        'vuqutils.files',
        'vuqutils.math',
        'vuqutils.plot',
        ],
    license='LICENSE.txt',
    description='Useful stuff for VUQ warriors.',
    long_description=open('README.txt').read(),
    install_requires=[
        "seaborn",
        "numexpr >= 2.0.0", # for pytables
        "cython",
        "tables",
    ],
    scripts=[
        'bin/sdf2hdf5',
    ]
)
