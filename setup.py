import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="dynamics365crm-python",
    version="0.1.2",
    description="API wrapper for Dynamics365CRM written in Python",
    long_description=read("README.md"),
    url="https://github.com/GearPlug/dynamics365crm-python",
    author="Yordy Gelvez",
    author_email="yordy.gelvez@gmail.com",
    license="GPL",
    packages=[
        "dynamics365crm",
    ],
    install_requires=[
        "requests",
    ],
    zip_safe=False,
)
