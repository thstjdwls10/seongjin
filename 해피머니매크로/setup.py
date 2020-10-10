import io
from setuptools import find_packages, setup


# Read in the README for the long description on PyPI
def long_description():
    with io.open('README.rst', 'r', encoding='utf-8') as f:
        readme = f.read()
    return readme

setup(name='algorithms',
      version='0.1',
      description='practice python with solving algorithms',
      long_description=long_description(),
      url='https://github.com/thstjdwls10/seongjin',
      author='seongjin',
      author_email='thstjdwls10@naver.com',
      license='MIT',
      packages=find_packages(),
      classifiers=[
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          ],
      zip_safe=False)