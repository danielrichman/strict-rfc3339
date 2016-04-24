import os.path
from distutils.core import setup

readme_file = os.path.join(os.path.dirname(__file__), 'README.md')
readme = open(readme_file).read()

setup(
    name='strict-rfc3339',
    version='0.7',
    author='Daniel Richman, Adam Greig',
    author_email='main@danielrichman.co.uk',
    url='http://www.danielrichman.co.uk/libraries/strict-rfc3339.html',
    py_modules=['strict_rfc3339'],
    description="Strict, simple, lightweight RFC3339 functions",
    long_description=readme,
    license="GNU General Public License Version 3",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3"
    ]
)
