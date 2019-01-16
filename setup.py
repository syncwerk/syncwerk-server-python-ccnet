from setuptools import setup, find_packages
setup(
    name='syncwerk-server-python-ccnet',
    version='20181227',
    author='Syncwerk GmbH',
    author_email='support@syncwerk.com',
    packages=find_packages(exclude=["Makefile.am", "*.tests", "*.tests.*", "tests.*", "tests"]),
    url='https://www.syncwerk.com',
    license='Apache 2.0',
    description='Syncwerk Authentication Server bindings',
    long_description='A Python module to communicate with the Syncwerk Authentication Server',
    platforms=['any'],
    include_package_data=True,
)
