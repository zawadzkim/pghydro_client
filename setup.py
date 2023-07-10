from setuptools import setup, find_packages

# Read the contents of the requirements.txt file
with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

setup(
    name='pghydro_client',
    packages=find_packages(),
    version='0.1.0',
    install_requires=requirements,
)
