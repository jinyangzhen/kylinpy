# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import codecs
import os.path
import re

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    return codecs.open(os.path.join(here, *parts), 'r').read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


setup(
    name='kylinpython',
    version=find_version('kylinpy', '__init__.py'),
    author='Yongjie Zhao',
    author_email='yangzhen.jin@gmail.com',
    maintainer='Yangzhen Jin',
    maintainer_email='yangzhen.jin@gmail.com',
    packages=find_packages(),
    url='https://github.com/jinyangzhen/kylinpy',
    license='MIT License',
    description='Apache Kylin Python Client Library with minor fixes',
    long_description=open('README.rst').read(),
    long_description_content_type='text/x-rst',
    install_requires=[],
    extras_require={
        'sqlalchemy': ['sqlalchemy>=1.1.0'],
    },
    keywords=['apache kylin', 'kylin', 'kap', 'kyligence',
              'kyligence enterprise', 'cli', 'sqlalchemy dialect'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'sqlalchemy.dialects': ['kylin=kylinpy.sqla_dialect:KylinDialect'],
    },
)
