import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='genpasswd',
    packages=setuptools.find_packages(),
    version='1.1.2',
    license='MIT',
    description='To generate random and strong passwords.',
    author='Gowthaman',
    author_email='rgngowthaman1@gmail.com',
    url='https://github.com/Gowthaman1401/GenPasswd',
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
