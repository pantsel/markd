"""
Project setup
"""
import os
import re
import setuptools

def envstring(var):
    """
    Get environment variable
    """
    return os.environ.get(var) or ""

# read the contents of your README file
CWD = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(CWD, 'README.md'), "r") as f:
    LONG_DESCRIPTION = f.read()

# read the variables file
if os.path.isfile("variables"):
    try:
        with open("variables", "r") as fh:
            VARIABLES = fh.read().strip().split("\n")
        for v in VARIABLES:
            key, value = v.split("=")
            os.environ[key] = re.sub("['\"]", "", value)
    except FileNotFoundError:
        pass



setuptools.setup(
    name=envstring("NAME"),
    version=envstring("VERSION"),
    author=envstring("AUTHOR"),
    author_email=envstring("AUTHOR_EMAIL"),
    description=envstring("DESCRIPTION"),
    url=envstring("URL"),
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=[envstring("NAME")],
    license=envstring("LICENCE"),
    classifiers=[
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Natural Language :: English',
        'Topic :: Software Development :: Libraries',
        'Environment :: Plugins',
    ],
)