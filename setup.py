from setuptools import setup, find_packages


setup(
    name="flashcards",
    version="0.1",
    packages=find_packages(),
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
        # And include any *.msg files found in the 'hello' package, too:
        'db': ['*.sql'],
    }
)
