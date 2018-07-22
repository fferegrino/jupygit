from setuptools import setup, find_packages

try:
    long_desc = open('README.md').read()
except:
    long_desc = ''

setup(
    name="jupygit",
    url="https://github.com/fferegrino/jupygit",
    author="Antonio Feregrino",
    author_email="antonio.feregrino@gmail.com",
    version="0.0.26",
    packages=find_packages(),
    install_requires=[
        "jupyter==1"
    ],
    include_package_data=True,
    description="Prepare your Notebooks to be pushed to GitHub",
    long_description=long_desc,
)