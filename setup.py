#!/usr/bin/env python

from setuptools import setup

setup(
    name='propertycrawler',
    version='0.1.0',
    description='Property Crawler',
    author='Tyler Ryu',
    author_email='tylerk.ryu@gmail.com',
    url='https://github.com/tylerstuff/Property-Crawler',
    packages=['propertycrawler'],
    install_requires=[
        'requests>=2.22.0,<3',
        'beautifulsoup4>=4.8.2,<5',
        'pytest>=5.3.2,<6',
        'mock>=3.0.5,<4',
        'randproxy>=0.1.0,<2'
    ],
    dependency_links=[
        'git+https://github.com/tylerstuff/randproxy.git#egg=randproxy-0.1.0'
    ]
)