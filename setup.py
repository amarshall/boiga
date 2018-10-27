#!/usr/bin/env python
from glob import glob
from os.path import basename, splitext

from setuptools import find_packages
from setuptools import setup


setup(
    name='boiga',
    version='0.1.0',
    license='MIT',
    description='Type-safe functional programming',
    author='Andrew Marshall',
    url='https://github.com/amarshall/boiga',
    packages=find_packages('src'),  # type: ignore
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Utilities',
        ],
    keywords=[],
    python_requires='>= 3.6',
    install_requires=[
        'typing_extensions >=3.6.6,<4.0',
        ],
    extras_require={},
    )
