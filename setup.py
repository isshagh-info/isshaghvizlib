from setuptools import setup, find_packages

setup(
    name="isshaghvizlib",
    version="0.1.0",
    description="Visualization library for election and geospatial data in Mauritania",
    author="Isshagh",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pandas>=1.5",
        "numpy",
        "matplotlib",
        "geopandas>=0.14",
        "shapely",
        "pyproj",
        "fiona",
        "pyogrio",
        "bokeh>=3.0"
    ],
    python_requires=">=3.9",
)
