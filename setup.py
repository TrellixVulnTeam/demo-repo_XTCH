import setuptools
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="plexflo",
    version="0.0.1",
    author="Plexflo",
    author_email="hello@plexflo.com",
    description="Python wrapper around Plexflo's apps, APIs, and algorithms that help energy companies build "
                "intelligence, apps, and dashboards to accelerate clean-tech adoption across all communities.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Plexflo/PyPlexflo",
    project_urls={
        "Bug Tracker": "https://github.com/Plexflo/PyPlexflo/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'attrs==21.2.0',
        'build==0.7.0',
        'certifi==2021.10.8',
        'click==8.0.3',
        'click-plugins==1.1.1',
        'cligj==0.7.2',
        'colorama==0.4.4',
        'GDAL @ https://github.com/Plexflo/Binaries/raw/main/GDAL-3.3.2-cp37-cp37m-win_amd64.whl'.format(os.getcwd()),
        'Fiona @ https://github.com/Plexflo/Binaries/raw/main/Fiona-1.8.20-cp37-cp37m-win_amd64.whl'.format(os.getcwd()),
        'geopandas @ https://github.com/Plexflo/Binaries/raw/main/geopandas-0.10.0-py2.py3-none-any.whl'.format(os.getcwd()),
        'pyproj @ https://github.com/Plexflo/Binaries/raw/main/pyproj-3.1.0-cp37-cp37m-win_amd64.whl'.format(os.getcwd()),
        'Shapely @ https://github.com/Plexflo/Binaries/raw/main/Shapely-1.7.1-cp37-cp37m-win_amd64.whl'.format(os.getcwd()),
        'geographiclib==1.52',
        'geopy==2.2.0',
        'importlib-metadata==4.8.1',
        'kiwisolver==1.3.2',
        'matplotlib==3.4.3',
        'munch==2.5.0',
        'numpy==1.21.3',
        'packaging==21.0',
        'pandas==1.3.4',
        'pep517==0.12.0',
        'pyparsing==3.0.0',
        'pyproj',
        'python-dateutil==2.8.2',
        'pytz==2021.3',
        'Shapely==1.7.1',
        'six==1.16.0',
        'tomli==1.2.1',
        'typing-extensions==3.10.0.2',
        'zipp==3.6.0',
        'colorlog==6.5.0',
        'easydev==0.12.0',
        'fitter==1.4.0',
        'pexpect==4.8.0',
        'ptyprocess==0.7.0',
        'scipy==1.7.1'
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)

