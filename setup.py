import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='django_audit',  
    version='0.0.1',
    author="Tairu Oluwafemi Emmanuel",
    author_email="developer.emmarex@gmail.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Emmarex/django-audit",
    download_url="",
    keywords= ['Django Audit'],
    packages=setuptools.find_packages(),
    classifiers=[ 
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: Apache Software License",
        "Development Status :: 6 - Mature",
        "Intended Audience :: Developers",
        "Framework :: Django"
    ],
 )