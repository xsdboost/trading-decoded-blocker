from setuptools import setup, find_packages

setup(
    name="bantools",
    version="1.0.0",
    packages=find_packages(include=["bantools", "bantools.*"]),
    install_requires=["pyYAML>=6.0", "discord>=1.7.3"],
)
