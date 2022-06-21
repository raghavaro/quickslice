from setuptools import setup, find_packages

setup(
    name="quickslice",
    version="1.3.1",
    author="Raghav Arora",
    author_email="agu94.raghav@gmail.com",
    url="http://github.com/raghavaro/quickslice",
    description="Extract slices from compressed volumetric data",
    license="MIT",
    packages=find_packages(),
    scripts=["qslice"],
    install_requires=[
        "Pillow==6.2.0",
        "numpy==1.22.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)
