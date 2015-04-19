# coding: utf-8
from setuptools import setup
import os


README = os.path.join(os.path.dirname(__file__), 'README.rst')

setup(name='domplus',
      version='0.1.3',
      description='domplus is a python package with common functions for commercial applications.',
      long_description=open(README).read(),
      author="Eduardo Basílio", author_email="eduardoafonsobasilio@gmail.com",
      url='http://github.com/eabps/domplus/',
      # license="Common Public License",
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Common Public License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries',
      ],
      packages=[
        'domplus',
        'domplus.govplus',
        'domplus.financeplus',
      ],
)
