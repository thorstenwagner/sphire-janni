from setuptools import setup
import os
import re
import codecs

# Create new package with python setup.py sdist

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with codecs.open(os.path.join(here, *parts), "r") as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name="janni",
    version=find_version("janni", "__init__.py"),
    python_requires=">=3.9, <3.12",
    packages=["janni"],
    url="https://github.com/MPI-Dortmund/sphire-janni",
    license="MIT",
    author="Thorsten Wagner",
    setup_requires=["Cython"],
    extras_require={
        "gpu": ["tensorflow[and-cuda] >= 2.0.0, < 2.16.0"],
        "cpu": ["tensorflow-cpu >= 2.0.0, < 2.16.0"],
    },
    install_requires=[
        "mrcfile >=1.3.0",
        "Keras",
        "numpy >= 1.16.0, <= 1.26.4",
        "h5py >= 2.5.0",
        "Pillow >= 6.0.0",
        "Cython",
        "tifffile == 2020.9.3",
        "Gooey",
        "wxPython >= 4.2.1",
        "scikit-image >= 0.15.0",
        "protobuf == 4.25.3",
    ],
    author_email="thorsten.wagner@mpi-dortmund.mpg.de",
    description="noise 2 noise for cryo em data",
    entry_points={"console_scripts": ["janni_denoise.py = janni.jmain:_main_"]},
)
