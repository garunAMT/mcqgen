# we use setup.py files for installing the local package in our virtual environment

from setuptools import setup, find_packages

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Anurag Mani Tripathi',
    author_email="anuragmani000@gmail.com",
    install_requires=["openai", "langchain", "streamlit", "python-dotenv", "PyPDF2"],
    packages=find_packages() # responsible for finding all the local packages in the directory
)