import codecs
import os
import re

from setuptools import setup

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
    packages=['furiosa'],
    package_dir={'furiosa': 'furiosa'},
    setup_requires=setup_requires,
    install_requires=install_requires
)