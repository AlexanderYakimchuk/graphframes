from setuptools import setup

setup(name='graphframes',
      version='0.8.0',
      packages=['graphframes', 'graphframes.lib', 'graphframes.examples'],
      install_requires=[
          'nose==1.3.3',
          'numpy>=1.7'
      ],
      )
