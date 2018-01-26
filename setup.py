from setuptools import setup

setup(name='dynamics365crm-python',
      version='0.1',
      description='API wrapper for Dynamics365CRM written in Python',
      url='https://github.com/GearPlug/dynamics365crm-python',
      author='Yordy Gelvez',
      author_email='yordy.gelvez@gmail.com',
      license='GPL',
      packages=['dynamics365crm', ],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
