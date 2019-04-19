from setuptools import setup

setup( name='mannyhi',
       version='0.1',
       description='This module says hi!  ',
       url='https://github.com/mannyest/mannyhi/tree/master/mannyhi',                # usually a github URL
       author='manny.est ',
       author_email='estevez.enma@gmail.com',
       license='BFD',
       packages=['mannyhi'],
       install_requires=[ ],
       zip_safe=False,
       test_suite='pytest',
       setup_requires=['pytest-runner'],
       tests_require=['pytest'] )

