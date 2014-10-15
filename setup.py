# -*- coding: utf-8 -*-

from setuptools import setup
import twipy

setup(name='twipy',
      version=twipy.version,
      packages=['twipy'],
      description='Another Twitter client using Python 2.7',
      author='Victor Martin',
      author_email='vitomarti@gmail.com',
      url='https://github.com/ervitis/twipy',
      keywords='twitter client console',
      zip_safe=True,
      entry_points={
          'console_scripts': ['twipy = twipy.main:main']
      },
      download_url='https://github.com/ervitis/twipy/tarball/' + twipy.version,
      license='MIT',
      classifiers=[])
