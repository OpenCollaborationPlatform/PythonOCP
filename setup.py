from setuptools import setup
from setuptools.dist import Distribution

DISTNAME = "ocp"
DESCRIPTION = "Open Collaboration Platform"
MAINTAINER = "Stefan Troeger"
MAINTAINER_EMAIL = "stefantroeger@gmx.net"
URL = "https://github.com/OpenCollaborationPlatform"
LICENSE = "LGPL2.1+"
DOWNLOAD_URL = "https://github.com/OpenCollaborationPlatform"
VERSION = '0.1.1'

setup(name=DISTNAME,
      description=DESCRIPTION,
      maintainer=MAINTAINER,
      maintainer_email=MAINTAINER_EMAIL,
      url=URL,
      license=LICENSE,
      download_url=DOWNLOAD_URL,
      version=VERSION,
      packages=['ocp'])

