from setuptools import setup, find_packages

setup(
    name="bantools",
    version="1.0.0",
    packages=find_packages(include=["bantools", "bantools.*"]),
    package_data={"bantools": ["resources/config.yaml"]},
    install_requires=["pyYAML>=6.0", "discord>=1.7.3"],
    python_requires=">=3.8.13",
)
