import setuptools

with open("README.md", "r") as fh:
   long_description = fh.read()

setuptools.setup(
    name="possible_words_siramkalyan", # Replace with your own username
    version="0.0.1",
    author="siramkalyan",
    author_email="siramkalyan@gmail.com",
    description="this packages helps to extract possible english words from group of alphabets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/siramkalyan",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
