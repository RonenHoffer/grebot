from setuptools import setup

VERSION = '0.1dev'

setup(
    name='grebot',
    version=VERSION,
    packages=['grebot'],
    license='MIT',
    long_description=open('README.txt').read(),
    scripts=['grebot/grebot.py'],
)
