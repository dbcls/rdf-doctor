from setuptools import setup
from setuptools import find_packages
from glob import glob
from os.path import basename
from os.path import splitext

def read(file_path):
	with open(file_path, "r") as f:
		return f.read()

def _requires_from_file(file_name):
    return open(file_name).read().splitlines()

setup(
    install_requires=_requires_from_file('requirements.txt'),
    entry_points={
        "console_scripts":[
            "rdf-doctor = doctor.doctor:doctor"
        ]
    },
    name = 'rdf-doctor',
    version = '0.1.17',
    description = 'Validate RDF data, report problems, and support creation of more accurate data',
    author = 'DBCLS',
    url = 'https://github.com/dbcls/rdf-doctor',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'reference': ['reference/*'],
    },
    long_description = read('README.md'),
    long_description_content_type='text/markdown',
    classifiers=[
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
    ],
)