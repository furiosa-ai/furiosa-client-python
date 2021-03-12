import codecs
import os
import re

from setuptools import setup, find_packages

setup_requires = ["setuptools"]
install_requires = [
    "python-dotenv",
    "pyyaml",
    "urllib3",
    "dateutils"
]

here = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    return codecs.open(os.path.join(here, *parts), 'r').read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='furiosa-client',
    version=find_version("furiosa", "__init__.py"),
    description='FuriosaAI API Python Client',
    author='Hyunsik Choi (Furiosa AI SW Team)',
    author_email='hyunsik@furiosa.ai',
    maintainer='Hyunsik Choi (Furiosa AI SW Team)',
    maintainer_email='hyunsik@furiosa.ai',
    url='https://furiosa.ai',
    platforms=['Linux', 'Mac OS X', 'Windows'],
    license=['Apache License 2.0'],
    packages=find_packages(),
    setup_requires=setup_requires,
    install_requires=install_requires
)