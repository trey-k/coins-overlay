from setuptools import setup

setup(
    name = "coinsprogram",
    version = "0.1.0",
    author = "Trey Kuchinsky",
    author_email = "treykuchinsky@gmail.com",
    packages = ['coinsprogram'],
    entry_points = {
        "console_scripts": [
            "coinsprogram = coinsprogram.__main__:main"
        ]
    },
)