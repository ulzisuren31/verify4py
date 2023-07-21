import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="verify4py",
    version="1.0.1",
    author="Surenbayar Doloonjin",
    author_email="surenbayar@corex.mn",
    description="Issue certificates using blockchain and smart contract",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/teo-mn/verify4py",
    project_urls={
        "Bug Tracker": "https://github.com/teo-mn/verify4py/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6,<3.11",
    install_requires=['web3==6.6.1', 'merkletools==1.0.3', 'pdfrw==0.3']
)
