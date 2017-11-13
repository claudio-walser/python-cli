#!/usr/bin/env python3

from setuptools import setup, find_packages

def read(fpath):
    with open(fpath, 'r') as f:
        return f.read()


def version(fpath):
    return read(fpath).strip()


setup(
    name='simplecli',
    version=version('version.txt'),
    description='Helper for Python CLI Scripts',
    author='Claudio Walser',
    author_email='claudio.walser@srf.ch',
    url='https://github.com/claudio-walser/python-simplecli',
    packages=find_packages(),
    license='Apache License',
    keywords=['cli'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities'
    ]
)

