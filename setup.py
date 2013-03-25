import os.path
from distutils.core import setup

readme_file = os.path.join(os.path.dirname(__file__), 'README.md')
readme = open(readme_file).read()

setup(
    name='strict_rfc3339',
    version='0.1',
    author='Daniel Richman, Adam Greig',
    author_email='main@danielrichman.co.uk',
    packages=['strict_rfc3339'],
    description="Strict RFC3339 Validation, Parsing and Generation",
    long_description=readme,
    license="GNU General Public License Version 3"
)
