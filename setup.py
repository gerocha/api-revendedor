import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    version="1.0",
    name="api",
    packages=setuptools.find_packages(),
    python_requires=">=3.9",
)
