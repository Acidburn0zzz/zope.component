##############################################################################
#
# Copyright (c) 2006 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Setup for zope.component package

$Id$
"""

import os

try:
    from setuptools import setup, Extension
except ImportError, e:
    from distutils.core import setup, Extension

setup(name='zope.component',
      version='3.0.0.2',
      url='http://svn.zope.org/zope.component/tags/3.0.0',
      license='ZPL 2.1',
      description='Zope Component Architecture',
      author='Zope Corporation and Contributors',
      author_email='zope3-dev@zope.org',
      long_description="This package represents the core of the "
                  "Zope Component Architecture.  Together with the "
                  "'zope.interface' package, it provides facilities for "
                  "defining, registering and looking up components.",
      
      packages=['zope',
                'zope.component',
                'zope.component.tests',
               ],
      package_dir = {'': os.path.join(os.path.dirname(__file__), 'src')},

      namespace_packages=['zope',],
      tests_require = ['zope.testing'],
      install_requires=['zope.exceptions',
                        'zope.interface',
                       ],
      include_package_data = True,
      zip_safe = False,
      )
