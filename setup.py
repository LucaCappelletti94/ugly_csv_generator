"""Setup for the ugly-csv-generator python package."""
import os
import re
from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the relevant file
with open(os.path.join(here, 'README.md'), encoding='utf8') as f:
    long_description = f.read()


def read(*parts):
    with open(os.path.join(here, *parts), 'r', encoding='utf8') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


__version__ = find_version("ugly_csv_generator", "__version__.py")

test_deps =[
    "pytest",
    "pytest-cov",
    "validate_version_code",
    "random_csv_generator>=1.0.2"
]

extras = {
    'test': test_deps,
}

setup(
    name='ugly_csv_generator',
    version=__version__,
    description="Python package to generate ugly real-looking csvs.",
    long_description=long_description,
    url="https://github.com/LucaCappelletti94/ugly_csv_generator",
    author="LucaCappelletti94",
    author_email="cappelletti.luca94@gmail.com",
    # Choose your license
    license='MIT',
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    tests_require=test_deps,
    # Add here the package dependencies
    install_requires=[
        "pandas",
        "numpy",
        "tqdm"
    ],
    extras_require=extras,
)