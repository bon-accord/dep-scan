import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="appthreat-depscan",
    version="1.0.0",
    author="Team AppThreat",
    author_email="cloud@appthreat.com",
    description="Fully open-source security audit for project dependencies based on known vulnerabilities and advisories.",
    entry_points={"console_scripts": ["scan=depscan.cli:main"]},
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/appthreat/dep-scan",
    packages=setuptools.find_packages(),
    install_requires=["appthreat-vulndb", "defusedxml", "tabulate"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Topic :: Utilities",
        "Topic :: Security",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">= 3",
)
