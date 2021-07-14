import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pamit",
    version="0.1.2",
    author="Feng Liang",
    author_email="feng.liang@kaust.edu.sa",
    description="Taichi Map Utils",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ifsheldon/pamit",
    project_urls={
        "Bug Tracker": "https://github.com/ifsheldon/pamit/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "pamit"},
    packages=setuptools.find_packages(where="pamit"),
    python_requires=">=3.6",
)
