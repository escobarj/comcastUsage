from setuptools import setup

setup(name='comcast-usage',
      version="0.1.0",
      description='A script to check your Comcast data usage',
      author='Jorge Escobar',
      author_email='escobarj@gmail.com',
      license='MIT',
      url='https://github.com/escobarj/comcastUsage',
      modules=['comcastUsage'],
      install_requires=[
          'future==0.15.2',
          'requests==2.8.1',
      ],
      entry_points = {
        'console_scripts': ['comcast-usage = comcastUsage:get_usage']
      },
)