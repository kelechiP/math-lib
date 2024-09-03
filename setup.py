from setuptools import setup, find_packages

setup(
    name="math_lib",  # Replace with your package name
    version="0.1.0",
    description="A simple Python library for basic mathematical operations",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Kelechi Uradu",
    author_email="kelechiuradu@yahoo.com",
    url="https://github.com/kelechiP/math-lib",
    license="MIT",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=["pytest==7.0.0"],  # List your dependencies here
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
