#!/usr/bin/env python

from setuptools import setup
from setuptools.command.test import test as TestCommand
import sys


class Tox(TestCommand):
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]
    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        import shlex
        args = self.tox_args
        if args:
            args = shlex.split(self.tox_args)
        errno = tox.cmdline(args=args)
        sys.exit(errno)


def linelist(text):
    """
    Returns each non-blank line in text enclosed in a list.
    """
    return [l.strip() for l in text.strip().splitlines() if l.split()]


setup(
    name='namedentities',
    version='1.6.6',
    author='Jonathan Eunice',
    author_email='jonathan.eunice@gmail.com',
    description='Named (and numeric) HTML entities to/from each other or Unicode',
    long_description=open('README.rst').read(),
    url='http://bitbucket.org/jeunice/namedentities',
    license='Apache License 2.0',
    packages=['namedentities'],
    install_requires=[],
    tests_require=['tox', 'pytest', 'six>=1.9'],
    test_suite="test",
    cmdclass = {'test': Tox},
    zip_safe=False,
    keywords='HTML entities Unicode named numeric decimal hex hexadecimal glyph character set charset',
    classifiers=linelist("""
		Development Status :: 5 - Production/Stable
		Operating System :: OS Independent
		License :: OSI Approved :: Apache Software License
		Intended Audience :: Developers
		Environment :: Web Environment
		Programming Language :: Python
		Programming Language :: Python :: 2
		Programming Language :: Python :: 2.6
		Programming Language :: Python :: 2.7
		Programming Language :: Python :: 3
		Programming Language :: Python :: 3.2
		Programming Language :: Python :: 3.3
		Programming Language :: Python :: 3.4
		Programming Language :: Python :: 3.5
		Programming Language :: Python :: Implementation :: CPython
		Programming Language :: Python :: Implementation :: PyPy
		Topic :: Text Processing :: Filters
		Topic :: Text Processing :: Markup :: HTML
        Topic :: Software Development :: Libraries :: Python Modules
    """)
)
