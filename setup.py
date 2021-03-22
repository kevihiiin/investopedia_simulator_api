#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'certifi==2019.3.9',
    'chardet==3.0.4',
    'idna==2.8',
    'lxml==4.6.2',
    'ratelimit==2.2.1',
    'requests==2.21.0',
    'titlecase==0.12.0',
    'urllib3==1.24.2',
]

setup_requirements = []

test_requirements = []

setup(
    author="Kevin Yuan",
    author_email='kevihiiin@users.noreply.github.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Python Boilerplate contains all the boilerplate you need to create a Python package.",
    entry_points={
        'console_scripts': [
            'investopedia_api=investopedia_api.cli:main',
        ],
    },
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='investopedia_api',
    name='investopedia_api',
    packages=find_packages(include=['investopedia_api', 'investopedia_api.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/kevihiiin/investopedia_simulator_api',
    version='0.1.0',
    zip_safe=False,
)
