# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 19:37:16 2020

@author: seongjin.son
"""

from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="happy macro", # 이 패키지를 설치/삭제할 때 사용할 이름을 의미한다. 이 이름과 import할 때 쓰이는 이름은 다르다.
    version="0.0.1",
    author="seongjin",
    author_email="seongjin@naver.com",
    description="happy money macro ver.1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thstjdwls10/seongjin",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=requirements,
)