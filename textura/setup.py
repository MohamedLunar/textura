# setup.py

from setuptools import setup, find_packages

setup(
    name='textura',
    version='1.0.0',
    description='A simple Python library to add ANSI styles and colors to terminal text.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='MohamedLunar',
    author_email='contact.mohamedlunardev@gmail.com',
    url='https://github.com/MohamedLunar/textura',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)