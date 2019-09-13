from setuptools import setup
from pycdek import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pycdek3',
    url='https://github.com/kpodranyuk/pycdek',
    version=__version__,
    description='Python3 client for CDEK API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Ekaterina Podranyuk',
    author_email='katherineswork44@gmail.com',
    license='MIT',
    packages=['pycdek'],
    package_data={'pycdek': [
        'pycdek/*.py',
    ]},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.4',
)