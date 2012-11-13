from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='kk.cs',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='neue werkstaetten',
      author='Kreativkombinat GbR',
      author_email='sd@kreativkombinat.de',
      url='https://github.com/kreativkombinat/cs',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['kk'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.theming',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
