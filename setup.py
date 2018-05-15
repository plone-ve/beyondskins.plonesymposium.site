# -*- coding:utf-8 -*-

import os
from setuptools import setup, find_packages

version = '1.0'
long_description = open("README.rst").read() + "\n" + \
                   open(os.path.join("docs", "INSTALL.txt")).read() + "\n" + \
                   open(os.path.join("docs", "CREDITS.txt")).read() + "\n" + \
                   open(os.path.join("docs", "HISTORY.txt")).read()

setup(name='beyondskins.plonesymposium.site',
      version=version,
      description="Plone Symposium South America 2012 Theme for Plone/Diazo powered sites",
      long_description=long_description,
      # Get more strings from
      # https://pypi.org/pypi?:action=list_classifiers
      classifiers=[
        "Development Status :: 3 - Alpha",
        # XXX: Replace Development Status if needed:
        # "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Plone",
        # "Framework :: Plone :: $plone_version",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: Theme",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: Other/Proprietary License",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='web zope plone diazo theme beyondskins plonesymposium site cms',
      author='Simples Consultoria',
      author_email='products@simplesconsultoria.com.br',
      maintainer='Leonardo Caballero',
      maintainer_email='leonardocaballero@gmail.com',
      url='https://github.com/plonegovbr/beyondskins.plonesymposium.site',
      license='GPL',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['beyondskins',
                          'beyondskins.plonesymposium'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        'plone.app.theming',
        'plone.app.themingplugins',
        ],
      extras_require={
        'test': ['plone.app.testing'],
        },
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
