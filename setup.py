import codecs
import os.path
from setuptools import setup
from setuptools import find_packages
from doctor.consts import VERSION_FILE


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def _requires_from_file(rel_path):
    return open(rel_path).read().splitlines()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

setup(
    install_requires=_requires_from_file('requirements.txt'),
    entry_points={
        "console_scripts":[
            "rdf-doctor = doctor.doctor:doctor"
        ]
    },
    name='rdf-doctor',
    version=get_version("doctor/" + VERSION_FILE),
    description='Validate RDF data, report problems, and support creation of more accurate data',
    author='DBCLS',
    license='MIT',
    url='https://github.com/dbcls/rdf-doctor',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    classifiers=[
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
    ],
)
