import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

exec(open('logger_loco/__version__.py').read())

setuptools.setup(
    name="logger-loco",
    version=__version__,
    author="Sergey Lushkovsky",
    author_email="s.lushkovsky@gmail.com",
    description="Comment-driven python loggin package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=['logging', 'logger', 'log', 'comments'],
    url="https://github.com/lushkovsky-s/logger-loco",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
