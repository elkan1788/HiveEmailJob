# coding: utf-8
# __author = 'elkan1788@gmail.com'

from setuptools import setup, find_packages
from pip.req import parse_requirements

INSTALL_REQ = parse_requirements('requirements.txt', session='hack')
REQUIRES = [str(ir.req) for ir in INSTALL_REQ]

"""
Email Job setup requires 
"""
setup(
    name='email_job',
    version='2.0.4',
    description='Use Python implements get data from Hive then send attachments to user.',
    author='elkan1788',
    author_email='elkan1788@gmail.com',
    license='Apache License V2.0',
    install_requires=REQUIRES,
    packages=find_packages()
)
