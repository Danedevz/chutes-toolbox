from setuptools import setup, find_packages  # ty:ignore[unresolved-import]

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="chutes-edit",
    version="1.0",
    packages=find_packages(),
    install_requires=requirements,
)