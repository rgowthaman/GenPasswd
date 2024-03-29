import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='genpasswd',
    packages=setuptools.find_packages(),
    version='1.3.4',
    license='MIT',
    description='To generate random and strong passwords.',
    author='Gowthaman',
    url='https://github.com/rgowthaman/GenPasswd',
    download_url='https://github.com/rgowthaman/GenPasswd/releases',
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
    entry_points={'console_scripts': ['genpasswd=genpasswd.__main__:main']
                  },
    python_requires='>=3.6',
)
