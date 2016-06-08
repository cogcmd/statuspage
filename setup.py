from setuptools import setup, find_packages

setup (
    name = "statuspage",
    version = "0.1.5",
    description = "Cog commands for statuspage.io",
    author = "Kevin Smith",
    author_email = "kevin@operable.io",
    url = "http://operable.io",
    packages = find_packages(),
    install_requires = ["pycog3>=0.1.25"],
    keywords = ["cog", "statuspage", "incident", "bot", "devops", "chatops", "automation"],
    classifiers = [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: Apache Software License"
    ]
)
