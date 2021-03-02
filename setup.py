from setuptools import setup, find_packages

def read(filename):
    """Help the packages installation from requirements"""
    return [req.strip() for req in open(filename).readlines()]

setup(
    name="factory",
    version="0.1.0",
    description="It is a studying project",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read("requirements.txt"),
    extras_require={
        "dev": read("requirements-dev.txt")
    }
)