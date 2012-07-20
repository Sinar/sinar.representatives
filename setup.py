from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='sinar.representatives',
      version=version,
      description='Dexterity Content Types for Malaysian Representatives',
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      license='GPL',
      packages=find_packages('src',exclude=['ez_setup']),
      namespace_packages=['sinar'],
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
	  'Plone',
	  'plone.app.dexterity',
      'plone.app.versioningbehavior',
      'plone.app.referenceablebehavior',
      'collective.cmfeditionsdexteritycompat',
      'collective.z3cform.datagridfield',
      'plone.namedfile[blobs]',
      'plone.formwidget.namedfile',
      'collective.dexteritytextindexer',
      'collective.dexteritydiff',
      'collective.z3cform.widgets',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
