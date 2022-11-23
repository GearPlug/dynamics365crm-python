import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="dynamics365crm-python",
    version="1.0.0",
    description="API wrapper for Dynamics365CRM written in Python",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/GearPlug/dynamics365crm-python",
    author="Yordy Gelvez",
    author_email="yordy.gelvez@gmail.com",
    license="GPL",
    packages=[
        "dynamics365crm",
    ],
    install_requires=["requests", "msal"],
    zip_safe=False,
)
