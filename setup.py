import os
from setuptools import setup, find_packages


here = os.path.dirname(__file__)
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()


setup(name='weiwei',
      version='0.0',
      description='weiwei',
      long_description=README + '\n\n' + CHANGES,
      author='',
      author_email='',
      keywords='web wsgi uiro',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      entry_points={
          'paste.app_factory': [
              'main = uiro:main'
          ],
      },
      install_requires=[
          'uiro',
          'deform==2.0a2',
          'docutils==0.11',
      ],
      dependency_links=[
          'https://github.com/hirokiky/uiro/tarball/master#egg=uiro-0.2',
      ]
      )
