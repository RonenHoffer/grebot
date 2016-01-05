from setuptools import setup
from platform import system

SYSTEM = system()
VERSION = '0.1dev'

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
)
