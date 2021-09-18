from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='testing-pypi-autorelease',
    version='0.0.2',
    description='For testing',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Pedro Torcatt',
    author_email='pedrotorcattsoto@gmail.com',
    url='https://github.com/dvl/python-internet-sabotage',
    classifiers=[
        'Development Status :: 4 - Beta',
    ],
    keywords='test pypi',
    packages=find_packages(),
)
