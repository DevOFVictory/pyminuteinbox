from setuptools import setup, find_packages

VERSION = '0.9'
DESCRIPTION = 'Minuteinbox API Wrapper'
with open('README.md', 'r') as f:
    LONG_DESCRIPTION = f.read()

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
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ]
)