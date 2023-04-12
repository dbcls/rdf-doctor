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
            "rdf-doctor = doctor:doctor"
        ]
    },
    name = 'rdf-doctor',
    version = '0.1',
    description = 'Validate RDF data, report problems, and support creation of more accurate data',
    author = 'DBCLS',
    url = 'https://github.com/dbcls/rdf-doctor',
    packages=find_packages("rdf-doctor"),
    include_package_data=True,
    data_files=[
        ("",["LICENSE"]),
        ("reference",glob("rdf-doctor/reference/*")),
    ],
    package_dir={"": "rdf-doctor"},
    py_modules=[splitext(basename(path))[0] for path in glob('rdf-doctor/*.py')],
    long_description = read('README.md'),
    long_description_content_type='text/markdown',
)