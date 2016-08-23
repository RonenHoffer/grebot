from setuptools import setup
from platform import system

SYSTEM = system()
VERSION = '1.0.2'

if SYSTEM == 'Windows':
    scripts = ['grebot/grebot.bat']
else:
    scripts = ['grebot/grebot.sh']

setup(
    name='grebot',
    version=VERSION,
    packages=['grebot'],
    license='MIT',
    long_description=open('README.txt').read(),
    scripts=scripts,
    install_requires=['colorama']
)
