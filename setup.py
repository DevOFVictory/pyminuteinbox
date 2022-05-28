from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Minuteinbox API Wrapper'
LONG_DESCRIPTION = 'A simple python API Wrapper for the temp mail service https://www.minuteinbox.com'

# Setting up
setup(
    name="pyminuteinbox",
    version=VERSION,
    author="DevOFVictory",
    author_email="<devofvictory@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    package_dir={'': 'src'},
    keywords=['python', 'api', 'tempmail', 'trashmail', '10minutemail'],
    classifiers=[
        "Development Status :: 1 - Development",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ]
)