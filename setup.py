from setuptools import setup, find_packages

setup(
    name="logosign",
    version="0.1.0",
    author="Amirhosein Vali",
    author_email="amirhosein.vali@yahoo.com",
    description="Auto command line ASCII logo creator for Python projects",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'logosign': ['default.ascii'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "django>=2.2",
        "Pillow>=8.0.0"
    ],
)