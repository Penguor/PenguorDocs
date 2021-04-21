import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

entry_points = '''
[pygments.lexers]
penguor=penguorlexer.lexer:PenguorLexer
'''

setuptools.setup(
    name="penguorlexer", # Replace with your own username
    version="0.0.3",
    author_email="coozypenguin@gmail.com",
    description="Pygments lexer for the Penguor language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Penguor/PenguorDocs",
    project_urls={
        "Bug Tracker": "https://github.com/Penguor/PenguorDocs/issues",
    },
    install_requires=[
        'Pygments>=2.0.1'
    ],
    entry_points=entry_points,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
