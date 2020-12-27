from distutils.core import setup
import setuptools

def readme():
    with open(r'README.md') as f:
        README = f.read()
    return README

setup(
    name = 'pypasswdgen',
    packages = setuptools.find_packages(),
    version = '1.0.0',
    license='MIT',
    description = 'pypasswdgen is a package to generate random passwords.',
    author = 'Gowthaman',
    author_email = 'rgngowthaman1@gmail.com',
    url = 'https://github.com/Gowthaman1401/PyPassGen',
    download_url = 'https://github.com/Gowthaman1401/PyPassGen/archive/1.0.tar.gz',
    include_package_data=True,
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)