from setuptools import setup, find_packages
setup(
    name="factory",
    version="0.1.0",
    description="It is a studying project",
    packages=find_packages(),
    include_package_data=True,
    install_requeres=["flask"]
)