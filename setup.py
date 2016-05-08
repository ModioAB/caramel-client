import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

README = open(os.path.join(here, "README.md")).read()
CHANGES = open(os.path.join(here, "CHANGES.txt")).read()


setup(
    name="caramel-client",
    version="1.0",
    description="caramel-client",
    packages=find_packages(),
    scripts=['caramel-client'],
    long_description=README + "\n\n" + CHANGES,
    classifiers=[
        "Programming Language :: Python",
    ],
    author="D.S. Ljungmark",
    author_email="spider@modio.se",
    url="https://github.com/MyTemp/caramel-client",
    keywords="caramel ssl tls certificates x509 ca cert",
    include_package_data=True,
    zip_safe=True,
    install_requires=['requests'],
)
