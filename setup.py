#!/usr/bin/python
# File Name: setup.py
# Created:   23-02-2011

import sys
import os
from skeleton.config import settings
from skeleton.blabla import Blabla

def main(argv):
    try:
      from setuptools import setup
    except ImportError:
      from distutils.core import setup

    print(settings["token"])

    Blabla("buuuu", "aaaaaa")

    #config = {
      #'description': 'Project Name',
      #'author': 'My Name',
      #'url': 'Homepage url',
      #'download_url': 'Download url',
      #'author_email': 'my email',
      #'version': '0.1',
      #'install_requires': ['nose'],
      #'packages': ['NAME'],
      #'scripts': [],
      #'name': 'projectname'
    #}
    #setup(**config)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
