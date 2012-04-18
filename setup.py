from setuptools import setup, find_packages
import os

version = '1.0.1'

long_description = (
    open('README.rst').read()
    + '\n\n' +
    open('CONTRIBUTORS.rst').read()
    + '\n\n' +
    open('CHANGES.rst').read()
    + '\n\n' +
    open(os.path.join('docs', 'LICENSE.rst')).read())

setup(name='collective.tinymceplugins.embedly',
      version=version,
      description="Integration of the Embedly TinyMCE plugin with Plone",
      long_description=long_description,
      classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python",
        "Topic :: Text Processing :: Markup :: HTML"
        ],
      keywords='',
      author='Netsight Internet Solutions Limited',
      author_email='info@netsight.co.uk',
      url='http://github.com/collective/collective.tinymceplugins.embedly',
      license='GPL v2',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['collective', 'collective.tinymceplugins'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.TinyMCE>=1.3dev', # embedly plugin doesn't work < TinyMCE 3.4.5
          'collective.embedly'
      ],
      extras_require={'test': ['plone.app.testing']},
      entry_points="""
      # -*- Entry points: -*-
  	  [z3c.autoinclude.plugin]
  	  target = plone
      """,
      )
