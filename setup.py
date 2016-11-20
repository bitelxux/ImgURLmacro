#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from setuptools import setup

setup(
    name='ImgURLMacro',
    version='0.21',
    packages=['imgurl'],
    author="Bitelxux",
    maintainer="Bitelxux",
    maintainer_email="bitelxux@gmail.com",
    description="Inline an image from an URL",
    long_description="""Inline an image from an URL
                     """,
    license="GPL",
    keywords="trac plugin image url",
    url="",
    entry_points={
        'trac.plugins': [
            'imgurl.macro = imgurl.macro'
        ]
    },
)
