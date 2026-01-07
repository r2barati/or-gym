#!usr/bin/env python

from setuptools import setup, find_packages
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'or_gym'))


with open(os.path.join('or_gym', 'version.py')) as version_file:
    version = version_file.read().strip()

VERSION = version.split("=")[-1].replace("'", "")

setup(name='or-gym',
	version=VERSION,
	description='OR-Gym: A set of environments for developing reinforcement learning agents for OR problems.',
	author='Christian Hubbs, Hector Perez Parra, Owais Sarwar',
	license='MIT',
	url='https://github.com/hubbs5/or-gym',
	packages=find_packages(),
	install_requires=[
		'gymnasium>=0.26.0',
		'numpy>=1.16.1',
		'pandas>=1.2',
		'scipy>=1.0',
		'matplotlib>=3.1',
		'networkx>=2.3'
  ],
	zip_safe=False,
	python_requires='>=3.7',
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: 3.9',
	]
	)
