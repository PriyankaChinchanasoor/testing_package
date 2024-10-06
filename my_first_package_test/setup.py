from setuptools import setup, find_packages
from os import path
working_directory=path.abspath(path.dirname(__file__))

with open(path.join(working_directory,'README.md'),encoding='utf-8') as f:
    long_description=f.read()

setup(
    name='testing_package',
    version='0.01',
    #url=https://github.com/PriyankaChinchanasoor/testing_package
    author='Priyanka',
    author_email='priyankabcc1999@gmail.com',
    description='Simple test Package',
    long_description=long_description,
    long_description_content_type='test/markdown',
    packages=find_packages(),
    install_requires=[]


)