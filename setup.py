import os
from setuptools import setup, find_packages


here = os.path.dirname(__file__)
README = open(os.path.join(here, "README.rst")).read()
CHANGES = open(os.path.join(here, "CHANGES.txt")).read()

points = {
    "paste.app_factory": [
        "main=weiwei:main",
    ],
}


setup(
    name='weiwei',
    version='0.0',
    license='GNU GPL v2',
    packages=find_packages(),
    url='https://github.com/hirokiky/weiwei/',
    author='hirokiky',
    author_email='hirokiky@gmail.com',
    description='A reader-friendly Wiki engine.',
    long_description=README + '\n' + CHANGES,
    install_requires=[
        'matcha==0.2',
        'gearbox==0.0.2',
        'webob==1.2.3',
        'sqlalchemy==0.8.2',
        'deform==2.0a1',
        'zope.sqlalchemy==0.7.3'
    ],
    entry_points=points,
)
