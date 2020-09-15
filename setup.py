import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rlyehian",
    version="0.2",
    author="Jimmy Le (JLDevOps)",
    author_email="jldevops@gmail.com",
    description="Translate to the language of the \"old ones\" with the serpent's tong in the digital world.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JLDevOps/Rlyehian",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)