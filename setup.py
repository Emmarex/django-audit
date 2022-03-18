import os
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [
        (dirpath.replace(package + os.sep, "", 1), filenames)
        for dirpath, _, filenames in os.walk(package)
        if not os.path.exists(os.path.join(dirpath, "__init__.py"))
    ]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                         for filename in filenames])
    return {package: filepaths}


setup(
    name='dj_audit',
    version='0.1.3',
    author="Tairu Oluwafemi Emmanuel",
    author_email="tairuoluwafemi09@gmail.com",
    description="Django Audit is a simple Django app that tracks and logs requests to your application.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Emmarex/django-audit",
    download_url="",
    keywords=['Django Audit', 'Audit', 'audit trail'],
    include_package_data=True,
    packages=find_packages(),
    package_data=get_package_data("dj_audit"),
    python_requires='~=3.6',
    install_requires=["Django", "psycopg2-binary"],
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: Apache Software License",
        "Development Status :: 6 - Mature",
        "Intended Audience :: Developers",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0"
    ],
)
