"""
DDD package installation
"""
from setuptools import setup, find_packages

setup(
    name='domain-driven-design',
    version='0.0.2',
    license='MIT',
    description='A module to develop easily in Domain Driven Design in python project.',
    url='https://github.com/pidevops/py-domain-driven-design.git',
    author='Etienne de Longeaux',
    author_email='etienne.delongeaux@gmail.fr',
    packages=['ddd'],
    install_requires=[
        "jinja2==2.10.*",
        "zope.interface==4.5.*"
    ],
    extras_require={
        'ci': ['flake8', 'coverage'],
        'ci': ['mock', 'pyinspector'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ]
)