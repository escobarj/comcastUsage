from setuptools import setup
from comcastUsage import __version__

setup(name='comcast-usage',
      version=__version__,
      description='A script to check your Comcast data usage',
      author='Jorge Escobar',
      author_email='escobarj@gmail.com',
      license='MIT',
      url='https://github.com/escobarj/comcastUsage',
      packages=['comcastUsage'],
      install_requires=[
          'future==0.15.2',
          'requests==2.8.1',
      ],
      entry_points = {
        'console_scripts': ['comcast-usage = comcastUsage.command_line:main']
      },
)