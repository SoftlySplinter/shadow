#!/usr/bin/env python

import sys

from setuptools import setup, find_packages

setup(
    name             = 'shadow',
    version          = '0.1.1',
    license          = 'Apache Software License 2.0',
    url              = 'https://github.com/SoftlySplinter/shadow',

    maintainer       = 'Alexander Brown',
    maintainer_email = 'alex@alexanderdbrown.com.com',

    description      = 'A stealth-based rougelike game',
    long_description = open('README.rst').read(),

    classifiers      = [
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
    ],

    # Package
    
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,

    entry_points={
        'console_scripts': [
            'shadow-game = shadow:run',
        ]
    },

    # Requirements

    install_requires=[
        'pygame'
    ],
)
