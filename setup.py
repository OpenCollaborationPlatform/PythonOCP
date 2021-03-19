from setuptools import setup

DISTNAME = "ocp"
DESCRIPTION = "Open Collaboration Platform meta package"
AUTHOR = "Stefan Tröger"
AUTHOR_EMAIL = "stefantroeger@gmx.net"
URL = "https://github.com/OpenCollaborationPlatform"
LICENSE = "LGPL2.1+"
DOWNLOAD_URL = "https://github.com/OpenCollaborationPlatform"
VERSION = '0.1.3'

# dependencies
with open('requirements.txt') as f:
    required = f.read().splitlines()

# setup
setup(name=DISTNAME,
      description=DESCRIPTION,
      maintainer=AUTHOR,
      maintainer_email=AUTHOR_EMAIL,
      author=AUTHOR,
      author_email= AUTHOR_EMAIL,
      url=URL,
      license=LICENSE,
      download_url=DOWNLOAD_URL,
      version=VERSION,
      platforms='any',
      install_requires=required)

