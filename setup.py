# -*- coding: utf-8 -*-

from twipy import version
from setuptools import setup

setup(name='twipy',
      version=version,
      description='Another Twitter client using Python 2.7',
      author='Victor Martin',
      author_email='vitomarti@gmail.com',
      url='http://github.com/ervitis/twipy',
      keywords='twitter client console',
      zip_safe=True,
      entry_points={
          'console_scripts': ['twipy = twipy.main:main']
      },
      download_url='://github.com/ervitis/twipy/tarball/' + version,
      license='MIT',
      classifiers=[])
