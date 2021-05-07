from setuptools import setup

setup(
    name = "coins-overlay",
    version = "0.1.0",
    author = "Trey Kuchinsky",
    author_email = "treykuchinsky@gmail.com",
    packages = ['coins-overlay'],
    entry_points = {
        "console_scripts": [
            "coins-overlay = coins-overlay.__main__:main"
        ]
    },
)