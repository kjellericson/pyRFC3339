import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

setup(
    name = "pyRFC3339",
    version = "0.1",

    author = "Kurt Raschke",
    author_email = "kurt@kurtraschke.com",
    description = "Generate and parse RFC 3339 timestamps",
    keywords = "rfc 3339 timestamp",
    license = "MIT",

    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Internet"
        ],

    packages = find_packages(),

    install_requires = ['pytz'],
    setup_requires=['nose>=0.11', 'coverage>=3.0.1'],
    test_suite = 'nose.collector',
    tests_require = ['nose']
    )
