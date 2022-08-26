import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="IP2WHOIS",
    version="2.2.3",
    author="IP2WHOIS",
    author_email="support@ip2whois.com",
    description="IP2WHOIS Python SDK to help user to check WHOIS information for a particular domain.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ip2whois/ip2whois-python",
    license='MIT',
    keywords='WHOIS',
    project_urls={
        'Official Website': 'https://www.ip2location.com',
    },
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    # packages=setuptools.find_packages(),
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    tests_require=['pytest>=3.0.6'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        'Programming Language :: Python :: 2.7',
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)