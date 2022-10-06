import setuptools

with open("README.md") as file:
    read_me_description = file.read()

setuptools.setup(
    name="your-package-username",
    version="0.1",
    author="Your Name",
    author_email="your_email",
    description="This is a test package.",
    long_description=read_me_description,
    long_description_content_type="text/markdown",
    url="package_bitbucket_page",
    packages=['your_package'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
